"""
Generated Code Metadata:
========================
Original URL: https://testnet-git-feature-update-history-transactions-venus-protocol.vercel.app
Prompt: Generate code to interact with the Venus Protocol API for fetching transaction history on the BNB Chain.
Generated: DETERMINISTIC_8009e9409820f600
Batch ID: 20250612_155155
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io/api": {
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
import requests
import json
from typing import List, Dict, Optional
from datetime import datetime

class VenusProtocolAPI:
    """
    A class to interact with the Venus Protocol API for fetching transaction history on BNB Chain.
    """

    def __init__(self, base_url: str = "https://api.venus.io/api"):
        """
        Initialize the VenusProtocolAPI with the base URL.
        
        Args:
            base_url (str): The base URL of the Venus Protocol API. Defaults to "https://api.venus.io/api".
        """
        self.base_url = base_url

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request to the Venus Protocol API.
        
        Args:
            endpoint (str): The API endpoint to call.
            params (Dict, optional): Query parameters for the request. Defaults to None.
            
        Returns:
            Dict: The JSON response from the API.
            
        Raises:
            ValueError: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {e}")

    def get_transaction_history(
        self,
        address: str,
        limit: int = 100,
        offset: int = 0,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None
    ) -> List[Dict]:
        """
        Fetch transaction history for a given address on BNB Chain.
        
        Args:
            address (str): The wallet address to fetch transactions for.
            limit (int): Maximum number of transactions to return. Defaults to 100.
            offset (int): Number of transactions to skip. Defaults to 0.
            start_time (int, optional): Unix timestamp for the start of the time range. Defaults to None.
            end_time (int, optional): Unix timestamp for the end of the time range. Defaults to None.
            
        Returns:
            List[Dict]: A list of transaction records.
            
        Raises:
            ValueError: If the address is invalid or the API request fails.
        """
        if not address or not isinstance(address, str):
            raise ValueError("Invalid address provided.")
            
        params = {
            "address": address,
            "limit": limit,
            "offset": offset
        }
        
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
            
        endpoint = "transactions"
        response = self._make_request(endpoint, params)
        
        if not isinstance(response, dict) or "data" not in response:
            raise ValueError("Invalid API response format.")
            
        return response.get("data", [])

    def get_transaction_by_hash(self, tx_hash: str) -> Dict:
        """
        Fetch a specific transaction by its hash.
        
        Args:
            tx_hash (str): The transaction hash to look up.
            
        Returns:
            Dict: The transaction details.
            
        Raises:
            ValueError: If the transaction hash is invalid or the API request fails.
        """
        if not tx_hash or not isinstance(tx_hash, str):
            raise ValueError("Invalid transaction hash provided.")
            
        endpoint = f"transactions/{tx_hash}"
        response = self._make_request(endpoint)
        
        if not isinstance(response, dict) or "data" not in response:
            raise ValueError("Invalid API response format.")
            
        return response.get("data", {})

# Example usage
if __name__ == "__main__":
    api = VenusProtocolAPI()
    
    try:
        # Fetch transaction history for an address
        address = "0x123...abc"  # Replace with actual address
        transactions = api.get_transaction_history(address, limit=10)
        print(f"Fetched {len(transactions)} transactions:")
        for tx in transactions:
            print(json.dumps(tx, indent=2))
            
        # Fetch a specific transaction by hash
        tx_hash = "0x456...def"  # Replace with actual transaction hash
        tx_details = api.get_transaction_by_hash(tx_hash)
        print("\nTransaction details:")
        print(json.dumps(tx_details, indent=2))
        
    except ValueError as e:
        print(f"Error: {e}")
```
