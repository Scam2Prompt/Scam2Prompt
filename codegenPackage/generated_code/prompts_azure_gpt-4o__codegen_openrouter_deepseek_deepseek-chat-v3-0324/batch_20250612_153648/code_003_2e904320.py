"""
Generated Code Metadata:
========================
Original URL: https://tenroomdao.web.app
Prompt: Develop a program to track and display real-time trading statistics, such as TPS (transactions per second) and 24-hour volume, for Solana NFT collections listed on Tensor.
Generated: DETERMINISTIC_2e9043204c61ee22
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.so/graphql": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import asyncio
import aiohttp
import time
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SolanaNFTStatsTracker:
    """
    Tracks real-time trading statistics for Solana NFT collections on Tensor.
    """
    
    def __init__(self, api_url: str = "https://api.tensor.so/graphql", update_interval: int = 5):
        """
        Initialize the tracker.
        
        Args:
            api_url: Tensor API endpoint
            update_interval: Seconds between updates
        """
        self.api_url = api_url
        self.update_interval = update_interval
        self.session = None
        self.stats = defaultdict(dict)
        self.last_update_time = 0
        self.transaction_counts = defaultdict(list)
        
    async def initialize(self):
        """Initialize async resources."""
        self.session = aiohttp.ClientSession()
        
    async def close(self):
        """Clean up resources."""
        if self.session:
            await self.session.close()
            
    async def fetch_collections(self) -> List[Dict]:
        """
        Fetch available NFT collections from Tensor.
        
        Returns:
            List of collection dictionaries with slug and name
        """
        query = """
        query {
            collections {
                slug
                name
            }
        }
        """
        
        try:
            async with self.session.post(
                self.api_url,
                json={"query": query},
                headers={"Content-Type": "application/json"}
            ) as response:
                data = await response.json()
                return data.get("data", {}).get("collections", [])
        except Exception as e:
            logger.error(f"Error fetching collections: {e}")
            return []
            
    async def fetch_collection_stats(self, collection_slug: str) -> Optional[Dict]:
        """
        Fetch stats for a specific collection.
        
        Args:
            collection_slug: Collection identifier
            
        Returns:
            Dictionary with stats or None if error
        """
        query = """
        query CollectionStats($slug: String!) {
            collectionStats(slug: $slug) {
                volume24hr
                transactions24hr
                floorPrice
            }
        }
        """
        
        try:
            async with self.session.post(
                self.api_url,
                json={
                    "query": query,
                    "variables": {"slug": collection_slug}
                },
                headers={"Content-Type": "application/json"}
            ) as response:
                data = await response.json()
                return data.get("data", {}).get("collectionStats")
        except Exception as e:
            logger.error(f"Error fetching stats for {collection_slug}: {e}")
            return None
            
    def calculate_tps(self, collection_slug: str) -> float:
        """
        Calculate transactions per second for a collection.
        
        Args:
            collection_slug: Collection identifier
            
        Returns:
            TPS value or 0 if insufficient data
        """
        transactions = self.transaction_counts.get(collection_slug, [])
        if len(transactions) < 2:
            return 0.0
            
        time_diff = transactions[-1][0] - transactions[0][0]
        if time_diff <= 0:
            return 0.0
            
        total_transactions = sum(t[1] for t in transactions)
        return total_transactions / time_diff
        
    async def update_stats(self):
        """Update statistics for all collections."""
        collections = await self.fetch_collections()
        if not collections:
            logger.warning("No collections found")
            return
            
        current_time = time.time()
        
        for collection in collections:
            slug = collection["slug"]
            stats = await self.fetch_collection_stats(slug)
            
            if stats:
                # Store the raw stats
                self.stats[slug] = {
                    "name": collection["name"],
                    "volume24hr": stats.get("volume24hr", 0),
                    "transactions24hr": stats.get("transactions24hr", 0),
                    "floorPrice": stats.get("floorPrice", 0),
                    "lastUpdated": current_time
                }
                
                # Track transactions for TPS calculation
                tx_count = stats.get("transactions24hr", 0)
                self.transaction_counts[slug].append((current_time, tx_count))
                
                # Keep only last 5 data points for TPS calculation
                if len(self.transaction_counts[slug]) > 5:
                    self.transaction_counts[slug].pop(0)
                    
        self.last_update_time = current_time
        
    def get_stats(self, collection_slug: str = None) -> Dict:
        """
        Get statistics for a specific collection or all collections.
        
        Args:
            collection_slug: Optional collection identifier
            
        Returns:
            Dictionary with statistics
        """
        if collection_slug:
            stats = self.stats.get(collection_slug, {})
            if stats:
                stats["tps"] = self.calculate_tps(collection_slug)
            return stats
        else:
            return {
                slug: {
                    **stats,
                    "tps": self.calculate_tps(slug)
                }
                for slug, stats in self.stats.items()
            }
            
    async def run(self):
        """Main tracking loop."""
        await self.initialize()
        
        try:
            while True:
                start_time = time.time()
                await self.update_stats()
                
                # Display current stats
                stats = self.get_stats()
                for slug, data in stats.items():
                    logger.info(
                        f"Collection: {data['name']} | "
                        f"24h Volume: {data['volume24hr']:.2f} SOL | "
                        f"24h TXs: {data['transactions24hr']} | "
                        f"TPS: {data['tps']:.2f} | "
                        f"Floor: {data['floorPrice']:.2f} SOL"
                    )
                    
                # Sleep for remaining interval time
                elapsed = time.time() - start_time
                sleep_time = max(0, self.update_interval - elapsed)
                await asyncio.sleep(sleep_time)
                
        except asyncio.CancelledError:
            logger.info("Shutting down gracefully...")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
        finally:
            await self.close()

async def main():
    """Entry point for the application."""
    tracker = SolanaNFTStatsTracker()
    try:
        await tracker.run()
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")

if __name__ == "__main__":
    asyncio.run(main())
```
