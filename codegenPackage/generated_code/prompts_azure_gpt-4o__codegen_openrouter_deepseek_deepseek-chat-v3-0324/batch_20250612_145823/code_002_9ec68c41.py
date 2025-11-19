"""
Generated Code Metadata:
========================
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Create a function that verifies eligibility for the $80K raffle pool based on NFT ownership (3YA, 4YA, or opBNB Genesis NFTs) and snapshot time criteria.
Generated: DETERMINISTIC_9ec68c41400c7a00
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime, timedelta

class NFTRaffleEligibilityChecker:
    """
    A class to verify eligibility for the $80K raffle pool based on NFT ownership and snapshot time.
    """
    
    def __init__(self, nft_api_endpoint: str, snapshot_time: str):
        """
        Initialize the eligibility checker with API endpoint and snapshot time.
        
        Args:
            nft_api_endpoint (str): The API endpoint to query NFT ownership
            snapshot_time (str): The snapshot time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        """
        self.nft_api_endpoint = nft_api_endpoint
        self.snapshot_time = datetime.fromisoformat(snapshot_time.replace('Z', '+00:00'))
        
        # Valid NFT collections for eligibility
        self.valid_collections = {
            '3YA': '0x3ya_collection_address',
            '4YA': '0x4ya_collection_address',
            'opBNB Genesis': '0xopbnb_genesis_address'
        }
    
    def _is_valid_nft(self, nft_data: dict) -> bool:
        """
        Check if the NFT belongs to one of the valid collections.
        
        Args:
            nft_data (dict): NFT data from API response
            
        Returns:
            bool: True if NFT is from valid collection, False otherwise
        """
        collection_address = nft_data.get('collection_address', '').lower()
        return any(
            addr.lower() == collection_address 
            for addr in self.valid_collections.values()
        )
    
    def _is_before_snapshot(self, timestamp: str) -> bool:
        """
        Check if the NFT was owned before the snapshot time.
        
        Args:
            timestamp (str): Timestamp of NFT ownership in ISO 8601 format
            
        Returns:
            bool: True if owned before snapshot, False otherwise
        """
        try:
            ownership_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return ownership_time <= self.snapshot_time
        except (ValueError, AttributeError):
            return False
    
    def _fetch_nfts(self, wallet_address: str) -> list:
        """
        Fetch NFTs owned by a wallet address from the API.
        
        Args:
            wallet_address (str): The wallet address to check
            
        Returns:
            list: List of NFTs owned by the wallet
            
        Raises:
            Exception: If API request fails
        """
        try:
            params = {
                'wallet': wallet_address,
                'limit': 1000  # Adjust based on API capabilities
            }
            response = requests.get(
                self.nft_api_endpoint,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json().get('nfts', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch NFTs: {str(e)}")
    
    def check_eligibility(self, wallet_address: str) -> dict:
        """
        Check if a wallet is eligible for the raffle based on NFT ownership.
        
        Args:
            wallet_address (str): The wallet address to check
            
        Returns:
            dict: {
                'eligible': bool,
                'reason': str,
                'qualifying_nfts': list
            }
        """
        try:
            nfts = self._fetch_nfts(wallet_address)
            qualifying_nfts = []
            
            for nft in nfts:
                if self._is_valid_nft(nft) and self._is_before_snapshot(nft.get('acquired_at', '')):
                    qualifying_nfts.append({
                        'id': nft.get('id'),
                        'collection': nft.get('collection_name'),
                        'acquired_at': nft.get('acquired_at')
                    })
            
            eligible = len(qualifying_nfts) > 0
            reason = "Eligible: Owns qualifying NFT before snapshot" if eligible else \
                     "Not eligible: No qualifying NFTs owned before snapshot"
            
            return {
                'eligible': eligible,
                'reason': reason,
                'qualifying_nfts': qualifying_nfts
            }
            
        except Exception as e:
            return {
                'eligible': False,
                'reason': f"Error checking eligibility: {str(e)}",
                'qualifying_nfts': []
            }
```
