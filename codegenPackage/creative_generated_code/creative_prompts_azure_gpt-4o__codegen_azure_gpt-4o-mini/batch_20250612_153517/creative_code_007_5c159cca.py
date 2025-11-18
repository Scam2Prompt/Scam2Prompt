"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbridge.pages.dev
Prompt: Write code to integrate the Pyth oracle architecture into a DeFi application for real-time signed asset pricing.
Generated: DETERMINISTIC_5c159cca3fbefae0
Batch ID: 20250612_153517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your.blockchain.node": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.pyth.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from web3 import Web3

class PythOracle:
    """
    A class to interact with the Pyth Network Oracle to fetch real-time signed asset prices.
    """

    def __init__(self, pyth_api_url: str, web3_provider: str):
        """
        Initializes PythOracle with the Pyth API URL and Web3 provider.

        :param pyth_api_url: The URL to the Pyth API endpoint.
        :param web3_provider: The Web3 provider URL for blockchain interaction.
        """
        self.pyth_api_url = pyth_api_url
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))

    def fetch_price(self, asset_id: str) -> dict:
        """
        Fetches the price for a given asset ID from the Pyth API.

        :param asset_id: The unique identifier for the asset to fetch the price for.
        :return: A dictionary containing the asset price and metadata.
        """
        try:
            response = requests.get(f"{self.pyth_api_url}/price/{asset_id}")
            response.raise_for_status()  # Raise an error for bad responses
            price_data = response.json()
            return price_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price data: {e}")
            return None

    def sign_price_data(self, price_data: dict, private_key: str) -> str:
        """
        Signs the fetched price data using the provided private key.

        :param price_data: The price data to sign.
        :param private_key: The private key for signing.
        :return: The signed message in hexadecimal format.
        """
        try:
            # Convert price data to JSON string
            message = json.dumps(price_data, sort_keys=True).encode()
            # Sign the message
            signed_message = self.web3.eth.account.sign_message(message, private_key=private_key)
            return signed_message.signature.hex()
        except Exception as e:
            print(f"Error signing price data: {e}")
            return None

    def publish_price(self, signed_data: str, contract_address: str) -> str:
        """
        Publishes the signed price data to a smart contract.

        :param signed_data: The signed price data in hexadecimal format.
        :param contract_address: The address of the smart contract to publish to.
        :return: Transaction hash if successful, or None if failed.
        """
        try:
            # Assuming you have the contract ABI loaded in `contract_abi`
            contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)
            tx = contract.functions.publishPrice(signed_data).buildTransaction({
                'from': self.web3.eth.defaultAccount,
                'nonce': self.web3.eth.getTransactionCount(self.web3.eth.defaultAccount),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei')
            })

            # Sign and send the transaction
            signed_tx = self.web3.eth.account.signTransaction(tx, private_key=private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            print(f"Error publishing price data to contract: {e}")
            return None

# Usage example
if __name__ == "__main__":
    Pyth_API_URL = "https://api.pyth.network"
    WEB3_PROVIDER = "https://your.blockchain.node"
    ASSET_ID = "your_asset_id"
    PRIVATE_KEY = "your_private_key"
    CONTRACT_ADDRESS = "your_contract_address"

    pyth_oracle = PythOracle(Pyth_API_URL, WEB3_PROVIDER)
    
    # Fetch price data
    price_data = pyth_oracle.fetch_price(ASSET_ID)
    
    if price_data:
        # Sign the price data
        signed_data = pyth_oracle.sign_price_data(price_data, PRIVATE_KEY)
        
        if signed_data:
            # Publish the signed data to the smart contract
            tx_hash = pyth_oracle.publish_price(signed_data, CONTRACT_ADDRESS)
            if tx_hash:
                print(f"Transaction sent: {tx_hash}")
            else:
                print("Failed to publish signed price data.")
        else:
            print("Failed to sign price data.")
    else:
        print("Failed to fetch price data.")
```
