"""
Generated Code Metadata:
========================
Original URL: https://lavanetwork.pages.dev
Prompt: Design a simple blockchain-agnostic application using Lava Network's APIs and SDK, enabling users to interact with different blockchain networks.
Generated: DETERMINISTIC_e7764f91ba62341d
Batch ID: 20250622_210027
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lavanet.xyz": {
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
import os
import json
import requests
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LavaNetworkClient:
    """
    A blockchain-agnostic client for interacting with multiple blockchains via Lava Network's APIs.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.lavanet.xyz"):
        """
        Initialize the Lava Network client.
        
        Args:
            api_key: Lava Network API key
            base_url: Base URL for Lava Network API (default: production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def _make_request(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal method to make API requests.
        
        Args:
            endpoint: API endpoint
            payload: Request payload
            
        Returns:
            JSON response from API
            
        Raises:
            Exception: If request fails
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def get_blockchain_info(self, chain_id: str) -> Dict[str, Any]:
        """
        Get information about a specific blockchain.
        
        Args:
            chain_id: Chain identifier (e.g., "ETH", "SOL", "COSMOS")
            
        Returns:
            Blockchain information
        """
        endpoint = "v1/blockchain/info"
        payload = {
            "chain_id": chain_id
        }
        return self._make_request(endpoint, payload)
    
    def query_chain(self, chain_id: str, method: str, params: Optional[List[Any]] = None) -> Dict[str, Any]:
        """
        Query a blockchain using RPC methods.
        
        Args:
            chain_id: Chain identifier
            method: RPC method name
            params: Optional parameters for the RPC call
            
        Returns:
            Query result
        """
        endpoint = "v1/query/chain"
        payload = {
            "chain_id": chain_id,
            "method": method,
            "params": params or []
        }
        return self._make_request(endpoint, payload)
    
    def send_transaction(self, chain_id: str, signed_tx: str) -> Dict[str, Any]:
        """
        Send a signed transaction to the blockchain.
        
        Args:
            chain_id: Chain identifier
            signed_tx: Signed transaction in hex format
            
        Returns:
            Transaction result
        """
        endpoint = "v1/transaction/send"
        payload = {
            "chain_id": chain_id,
            "signed_tx": signed_tx
        }
        return self._make_request(endpoint, payload)
    
    def get_transaction_status(self, chain_id: str, tx_hash: str) -> Dict[str, Any]:
        """
        Get the status of a transaction.
        
        Args:
            chain_id: Chain identifier
            tx_hash: Transaction hash
            
        Returns:
            Transaction status
        """
        endpoint = "v1/transaction/status"
        payload = {
            "chain_id": chain_id,
            "tx_hash": tx_hash
        }
        return self._make_request(endpoint, payload)

# Example usage
if __name__ == "__main__":
    # Initialize client with API key from environment
    api_key = os.getenv("LAVA_API_KEY")
    if not api_key:
        raise ValueError("LAVA_API_KEY environment variable not set")
    
    client = LavaNetworkClient(api_key)
    
    try:
        # Example: Get Ethereum blockchain info
        eth_info = client.get_blockchain_info("ETH")
        print("Ethereum Info:", json.dumps(eth_info, indent=2))
        
        # Example: Query latest block
        latest_block = client.query_chain("ETH", "eth_blockNumber")
        print("Latest Block:", json.dumps(latest_block, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
