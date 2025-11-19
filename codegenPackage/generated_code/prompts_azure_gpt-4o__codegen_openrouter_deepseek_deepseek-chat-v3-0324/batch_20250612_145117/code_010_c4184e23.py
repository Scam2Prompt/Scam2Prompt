"""
Generated Code Metadata:
========================
Original URL: https://drops-checker.network
Prompt: Generate a Python script to retrieve and display a list of supported blockchains for airdrop checks, including Ethereum, Solana, and Starknet, as mentioned on Drops.
Generated: DETERMINISTIC_c4184e23a4e56716
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional

class BlockchainAirdropChecker:
    """
    A class to retrieve and display supported blockchains for airdrop checks.
    """
    
    def __init__(self, api_url: Optional[str] = None):
        """
        Initialize the BlockchainAirdropChecker with an optional API URL.
        If no URL is provided, defaults to a predefined list of blockchains.
        
        Args:
            api_url (Optional[str]): URL to fetch supported blockchains from.
        """
        self.api_url = api_url
        self.default_blockchains = [
            {"name": "Ethereum", "symbol": "ETH"},
            {"name": "Solana", "symbol": "SOL"},
            {"name": "Starknet", "symbol": "STRK"}
        ]
    
    def fetch_supported_blockchains(self) -> List[Dict[str, str]]:
        """
        Retrieve the list of supported blockchains either from API or default list.
        
        Returns:
            List[Dict[str, str]]: List of supported blockchains with name and symbol.
            
        Raises:
            Exception: If API fetch fails and no default blockchains are available.
        """
        if self.api_url:
            try:
                response = requests.get(self.api_url, timeout=10)
                response.raise_for_status()
                return response.json().get("blockchains", [])
            except requests.exceptions.RequestException as e:
                print(f"Warning: Failed to fetch from API. Using default blockchains. Error: {e}")
        
        if not self.default_blockchains:
            raise Exception("No supported blockchains available.")
            
        return self.default_blockchains
    
    def display_supported_blockchains(self) -> None:
        """
        Display the list of supported blockchains in a user-friendly format.
        """
        try:
            blockchains = self.fetch_supported_blockchains()
            print("Supported Blockchains for Airdrop Checks:")
            print("-" * 40)
            for blockchain in blockchains:
                print(f"{blockchain['name']} ({blockchain['symbol']})")
            print("-" * 40)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    checker = BlockchainAirdropChecker()
    checker.display_supported_blockchains()
```
