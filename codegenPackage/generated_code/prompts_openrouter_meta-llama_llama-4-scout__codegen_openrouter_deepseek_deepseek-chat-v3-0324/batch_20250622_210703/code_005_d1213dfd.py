"""
Generated Code Metadata:
========================
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Explain how Pyth Network ensures the security, accuracy, and reliability of its market data for use in mission-critical DeFi systems.
Generated: DETERMINISTIC_d1213dfd1f1f1597
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified simulation of how Pyth Network might ensure
# data security, accuracy, and reliability for DeFi applications.

import hashlib
import json
from typing import List, Dict, Tuple
import time
from dataclasses import dataclass
from collections import defaultdict
import random

@dataclass
class DataPoint:
    value: float
    timestamp: int
    publisher_id: str
    signature: str  # Simulated cryptographic signature

class PythNetwork:
    def __init__(self):
        self.data_feeds: Dict[str, List[DataPoint]] = defaultdict(list)
        self.publishers: Dict[str, float] = {}  # publisher_id: stake_amount
        self.min_stake = 1000  # Minimum stake required to publish data
        self.min_confirmations = 3  # Minimum confirmations for consensus
        self.quorum_threshold = 0.66  # % of stake needed for consensus

    def add_publisher(self, publisher_id: str, stake_amount: float) -> bool:
        """Register a new data publisher with stake."""
        if stake_amount < self.min_stake:
            return False
        self.publishers[publisher_id] = stake_amount
        return True

    def publish_data(self, publisher_id: str, feed_id: str, value: float) -> bool:
        """Publish new data point to a feed with publisher signature."""
        if publisher_id not in self.publishers:
            return False
            
        # Simulate cryptographic signature
        signature = self._generate_signature(publisher_id, feed_id, value)
        data_point = DataPoint(
            value=value,
            timestamp=int(time.time()),
            publisher_id=publisher_id,
            signature=signature
        )
        self.data_feeds[feed_id].append(data_point)
        return True

    def get_aggregated_price(self, feed_id: str) -> Tuple[float, bool]:
        """Get aggregated price based on stake-weighted consensus."""
        if feed_id not in self.data_feeds or not self.data_feeds[feed_id]:
            return 0.0, False

        # Get most recent data points from all publishers
        recent_data = self._get_recent_data_points(feed_id)
        
        # Check if we have enough confirmations
        if len(recent_data) < self.min_confirmations:
            return 0.0, False

        # Calculate stake-weighted median price
        total_stake = sum(self.publishers[dp.publisher_id] for dp in recent_data)
        if total_stake == 0:
            return 0.0, False

        # Sort data points by value
        sorted_data = sorted(recent_data, key=lambda x: x.value)
        
        # Calculate stake-weighted median
        median_price = self._calculate_stake_weighted_median(sorted_data)
        
        # Check quorum threshold
        supporting_stake = sum(
            self.publishers[dp.publisher_id] 
            for dp in recent_data 
            if abs(dp.value - median_price) <= median_price * 0.01  # 1% tolerance
        )
        
        if supporting_stake / total_stake < self.quorum_threshold:
            return 0.0, False
            
        return median_price, True

    def _get_recent_data_points(self, feed_id: str) -> List[DataPoint]:
        """Get most recent data points from each publisher."""
        latest_data = {}
        for dp in self.data_feeds[feed_id]:
            # Only keep the most recent from each publisher
            if (dp.publisher_id not in latest_data or 
                dp.timestamp > latest_data[dp.publisher_id].timestamp):
                latest_data[dp.publisher_id] = dp
        return list(latest_data.values())

    def _calculate_stake_weighted_median(self, sorted_data: List[DataPoint]) -> float:
        """Calculate stake-weighted median price."""
        total_stake = sum(self.publishers[dp.publisher_id] for dp in sorted_data)
        half_stake = total_stake / 2
        running_stake = 0
        
        for dp in sorted_data:
            running_stake += self.publishers[dp.publisher_id]
            if running_stake >= half_stake:
                return dp.value
        return 0.0

    def _generate_signature(self, publisher_id: str, feed_id: str, value: float) -> str:
        """Simulate cryptographic signature generation."""
        data_str = f"{publisher_id}:{feed_id}:{value}:{int(time.time())}"
        return hashlib.sha256(data_str.encode()).hexdigest()

    def verify_signature(self, data_point: DataPoint) -> bool:
        """Verify the cryptographic signature of a data point."""
        expected = self._generate_signature(
            data_point.publisher_id,
            "feed_id_placeholder",  # In real implementation, feed_id would be known
            data_point.value
        )
        return expected == data_point.signature

# Example usage
def main():
    pyth = PythNetwork()
    
    # Register publishers with stake
    pyth.add_publisher("publisher1", 1500)
    pyth.add_publisher("publisher2", 2000)
    pyth.add_publisher("publisher3", 1800)
    
    # Simulate data publishing
    feeds = ["BTC/USD", "ETH/USD"]
    for feed in feeds:
        pyth.publish_data("publisher1", feed, random.uniform(30000, 40000))
        pyth.publish_data("publisher2", feed, random.uniform(30000, 40000))
        pyth.publish_data("publisher3", feed, random.uniform(30000, 40000))
    
    # Get aggregated price
    for feed in feeds:
        price, success = pyth.get_aggregated_price(feed)
        if success:
            print(f"Aggregated price for {feed}: {price:.2f}")
        else:
            print(f"Failed to get consensus for {feed}")

if __name__ == "__main__":
    main()
```
