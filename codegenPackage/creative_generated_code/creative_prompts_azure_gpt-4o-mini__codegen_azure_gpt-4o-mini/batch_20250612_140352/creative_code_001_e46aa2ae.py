"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.now.sh
Prompt: What are the steps to connect to the Polygon-Mainnet or Mumbai-Testnet for accessing PolyMarket 1.0?
Generated: DETERMINISTIC_e46aa2ae3691c208
Batch ID: 20250612_140352
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc-mumbai.maticvigil.com": {
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
import json
import requests
from web3 import Web3

class PolyMarketConnector:
    """
    A class to connect to the Polygon-Mainnet or Mumbai-Testnet for accessing PolyMarket 1.0.

    Attributes:
        provider_url (str): The URL of the Ethereum provider (Mainnet or Testnet).
        web3 (Web3): The Web3 instance for interacting with the Ethereum blockchain.
    """

    def __init__(self, provider_url: str):
        """
        Initializes the PolyMarketConnector with a provider URL.

        Args:
            provider_url (str): The URL of the Ethereum provider.
        """
        self.provider_url = provider_url
        self.web3 = self.connect_to_provider()

    def connect_to_provider(self) -> Web3:
        """
        Connects to the Ethereum provider.

        Returns:
            Web3: An instance of Web3 connected to the specified provider.

        Raises:
            ConnectionError: If the connection to the provider fails.
        """
        try:
            web3_instance = Web3(Web3.HTTPProvider(self.provider_url))
            if not web3_instance.isConnected():
                raise ConnectionError("Failed to connect to the Ethereum provider.")
            return web3_instance
        except Exception as e:
            raise ConnectionError(f"Error connecting to provider: {str(e)}")

    def get_block_number(self) -> int:
        """
        Retrieves the latest block number from the connected network.

        Returns:
            int: The latest block number.

        Raises:
            RuntimeError: If unable to fetch the block number.
        """
        try:
            return self.web3.eth.block_number
        except Exception as e:
            raise RuntimeError(f"Error fetching block number: {str(e)}")

def main():
    """
    Main function to demonstrate connection to Polygon networks.
    """
    # You can set the provider URL to either Mainnet or Testnet
    # e.g. for Mainnet: "https://polygon-rpc.com"
    # e.g. for Mumbai Testnet: "https://rpc-mumbai.maticvigil.com"
    provider_url = "https://rpc-mumbai.maticvigil.com"  # Change as needed

    # Create a connector instance
    connector = PolyMarketConnector(provider_url)

    # Fetch and display the current block number
    try:
        block_number = connector.get_block_number()
        print(f"Connected to the network. Current block number: {block_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
