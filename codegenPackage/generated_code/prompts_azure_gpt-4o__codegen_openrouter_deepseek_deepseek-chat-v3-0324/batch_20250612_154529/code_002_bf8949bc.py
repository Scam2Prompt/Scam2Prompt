"""
Generated Code Metadata:
========================
Original URL: https://etherscan.in
Prompt: Generate Python code using the etherscan-python library to query Ethereum transaction details by Txhash.
Generated: DETERMINISTIC_bf8949bc5723f727
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from etherscan import Etherscan
from typing import Optional, Dict

class EthereumTransactionFetcher:
    """
    A class to fetch Ethereum transaction details using the Etherscan API.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Etherscan client.
        
        Args:
            api_key: Etherscan API key. If not provided, will try to get from ETHERSCAN_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("ETHERSCAN_API_KEY")
        if not self.api_key:
            raise ValueError("Etherscan API key is required. Provide it or set ETHERSCAN_API_KEY environment variable.")
        self.eth = Etherscan(self.api_key)
    
    def get_transaction_details(self, tx_hash: str) -> Dict:
        """
        Fetch transaction details by transaction hash.
        
        Args:
            tx_hash: The transaction hash to query.
            
        Returns:
            Dictionary containing transaction details.
            
        Raises:
            ValueError: If tx_hash is empty or invalid.
            Exception: For API errors or network issues.
        """
        if not tx_hash or not isinstance(tx_hash, str) or len(tx_hash) != 66:
            raise ValueError("Invalid transaction hash provided.")
        
        try:
            return self.eth.get_tx_by_txhash(tx_hash)
        except Exception as e:
            raise Exception(f"Failed to fetch transaction details: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with API key (or it will try to get from environment variable)
        fetcher = EthereumTransactionFetcher()
        
        # Example transaction hash (replace with actual hash)
        tx_hash = "0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060"
        
        # Get transaction details
        tx_details = fetcher.get_transaction_details(tx_hash)
        print("Transaction Details:", tx_details)
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
