"""
Generated Code Metadata:
========================
Original URL: https://pythgo.com
Prompt: "Generate code to use Pyth price feed oracles for smart contract data feeds in Python."
Generated: DETERMINISTIC_f558d0732d9d9271
Batch ID: 20250622_212444
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://hermes.pyth.network/api/latest_price_feeds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://pyth.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
from web3 import Web3
from typing import Dict, Optional

# Configuration
PYTH_RPC_URL = "https://pyth.network"
PYTH_PRICE_FEED_API = "https://hermes.pyth.network/api/latest_price_feeds"
CHAIN_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
CONTRACT_ADDRESS = "0xYOUR_CONTRACT_ADDRESS"  # Replace with your contract address
ABI = [
    # Replace with your contract's ABI
    {
        "inputs": [{"internalType": "bytes32", "name": "priceId", "type": "bytes32"}],
        "name": "getPrice",
        "outputs": [{"internalType": "int64", "name": "price", "type": "int64"}],
        "stateMutability": "view",
        "type": "function"
    }
]

class PythPriceFeed:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(CHAIN_RPC_URL))
        self.contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(CONTRACT_ADDRESS),
            abi=ABI
        )

    def get_price_feed_ids(self) -> Dict[str, str]:
        """Get available price feed IDs from Pyth network"""
        try:
            response = requests.get(f"{PYTH_RPC_URL}/price_feed_ids")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch price feed IDs: {str(e)}")

    def get_latest_price_feeds(self, price_ids: Optional[list] = None) -> Dict:
        """
        Get latest price feeds from Pyth network
        :param price_ids: List of price IDs to filter (optional)
        :return: Dictionary of price feeds
        """
        params = {}
        if price_ids:
            params["ids[]"] = price_ids

        try:
            response = requests.get(PYTH_PRICE_FEED_API, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch price feeds: {str(e)}")

    def get_contract_price(self, price_id: str) -> int:
        """
        Get price from smart contract
        :param price_id: Price ID to query
        :return: Price as integer
        """
        try:
            price_id_bytes = Web3.to_bytes(hexstr=price_id)
            price = self.contract.functions.getPrice(price_id_bytes).call()
            return price
        except Exception as e:
            raise Exception(f"Failed to get price from contract: {str(e)}")

    def update_price_feed(self, price_id: str, price: int) -> str:
        """
        Update price feed in smart contract (mock function)
        In production, this would be a transaction signed and sent
        :param price_id: Price ID to update
        :param price: New price value
        :return: Transaction hash
        """
        try:
            # In a real implementation, you would:
            # 1. Build the transaction
            # 2. Sign it with a private key
            # 3. Send it to the network
            # This is just a mock implementation
            price_id_bytes = Web3.to_bytes(hexstr=price_id)
            tx_hash = "0x" + "mocktxhash".ljust(64, '0')
            return tx_hash
        except Exception as e:
            raise Exception(f"Failed to update price feed: {str(e)}")

# Example usage
if __name__ == "__main__":
    pyth = PythPriceFeed()
    
    try:
        # Get available price feed IDs
        price_feed_ids = pyth.get_price_feed_ids()
        print("Available price feed IDs:", price_feed_ids)
        
        # Get latest price feeds
        price_feeds = pyth.get_latest_price_feeds()
        print("Latest price feeds:", json.dumps(price_feeds, indent=2))
        
        # Get price from contract
        sample_price_id = list(price_feed_ids.keys())[0] if price_feed_ids else "0x0000000000000000000000000000000000000000000000000000000000000000"
        contract_price = pyth.get_contract_price(sample_price_id)
        print(f"Contract price for {sample_price_id}: {contract_price}")
        
        # Mock price update
        tx_hash = pyth.update_price_feed(sample_price_id, contract_price + 1)
        print(f"Price update transaction hash: {tx_hash}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
