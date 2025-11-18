"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Generate code to set up a Lava SDK instance for querying transaction data on the Osmosis blockchain.
Generated: DETERMINISTIC_ebdd345ce0454a61
Batch ID: 20250612_152439
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
from lava_sdk import LavaClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OsmosisTransactionQuery:
    """
    A class to interact with the Lava SDK for querying transaction data on the Osmosis blockchain.
    """

    def __init__(self, api_key: str):
        """
        Initializes the OsmosisTransactionQuery instance.

        Args:
            api_key (str): The API key for accessing the Lava SDK.

        Raises:
            ValueError: If the API key is empty.
        """
        if not api_key:
            raise ValueError("API key must not be empty.")

        self.client = LavaClient(api_key=api_key)

    def get_transaction_data(self, tx_hash: str):
        """
        Fetches transaction data from the Osmosis blockchain.

        Args:
            tx_hash (str): The transaction hash to query.

        Returns:
            dict: The transaction data.

        Raises:
            Exception: If there is an error in fetching the transaction data.
        """
        try:
            logger.info(f"Fetching transaction data for hash: {tx_hash}")
            tx_data = self.client.get_transaction(tx_hash)
            logger.info("Transaction data fetched successfully.")
            return tx_data
        except Exception as e:
            logger.error(f"Error fetching transaction data: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the OsmosisTransactionQuery
    try:
        API_KEY = os.getenv('LAVA_API_KEY')  # Ensure you set this environment variable
        osmosis_query = OsmosisTransactionQuery(api_key=API_KEY)

        # Example transaction hash (replace with a real hash for testing)
        transaction_hash = "your_transaction_hash_here"
        transaction_data = osmosis_query.get_transaction_data(transaction_hash)
        print(transaction_data)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
