"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1-7xq.pages.dev
Prompt: Generate a Python script that integrates the Lava Network's SDK to access data from multiple blockchain networks.
Generated: DETERMINISTIC_83aa1b1bdaee9d6d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from lava_sdk import LavaSDK  # Assuming the Lava SDK is correctly installed and imported
from lava_sdk.exceptions import LavaSDKError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BlockchainDataFetcher:
    """
    A class to interface with the Lava Network's SDK to fetch data from multiple blockchain networks.
    """

    def __init__(self, api_key):
        """
        Initializes the BlockchainDataFetcher with an API key.

        :param api_key: The API key for accessing Lava Network's services.
        """
        self.api_key = api_key
        self.sdk = self.initialize_sdk()

    def initialize_sdk(self):
        """
        Initializes the Lava Network SDK.

        :return: An instance of LavaSDK.
        """
        try:
            sdk = LavaSDK(api_key=self.api_key)
            logger.info("Lava SDK initialized successfully.")
            return sdk
        except LavaSDKError as e:
            logger.error(f"Failed to initialize Lava SDK: {e}")
            raise

    def fetch_data(self, network, query):
        """
        Fetches data from the specified blockchain network using the provided query.

        :param network: The name of the blockchain network to query.
        :param query: The query to execute on the network.
        :return: The response data from the network.
        """
        try:
            logger.info(f"Fetching data from {network} with query: {query}")
            response = self.sdk.query(network=network, query=query)
            logger.info("Data fetched successfully.")
            return response
        except LavaSDKError as e:
            logger.error(f"Error fetching data from {network}: {e}")
            raise

def main():
    """
    Main function to execute the data fetching process.
    """
    # Load API key from environment variable for security
    api_key = os.getenv("LAVA_API_KEY")
    if not api_key:
        logger.error("API key is not set. Please set the LAVA_API_KEY environment variable.")
        return

    fetcher = BlockchainDataFetcher(api_key=api_key)

    # Example usage: fetching data from different networks
    networks = ["Ethereum", "BinanceSmartChain"]
    query = "{ latestBlock { number } }"  # Sample GraphQL query

    for network in networks:
        try:
            data = fetcher.fetch_data(network, query)
            logger.info(f"Data from {network}: {data}")
        except Exception as e:
            logger.error(f"Failed to fetch data for {network}: {e}")

if __name__ == "__main__":
    main()
```
