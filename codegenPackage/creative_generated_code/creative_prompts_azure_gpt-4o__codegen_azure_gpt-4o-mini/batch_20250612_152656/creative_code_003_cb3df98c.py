"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nerve-network.web.app
Prompt: Write a Python script to query the NerveNetwork Explorer API for transaction details, including confirmation time and asset flow statistics.
Generated: DETERMINISTIC_cb3df98ccf5b31b9
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nerve.network/explorer/v1": {
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
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NerveNetworkExplorer:
    """A class to interact with the NerveNetwork Explorer API to fetch transaction details."""
    
    BASE_URL = "https://api.nerve.network/explorer/v1"  # Base URL for the NerveNetwork Explorer API

    def __init__(self, transaction_id):
        """
        Initialize the NerveNetworkExplorer with a specific transaction ID.

        Args:
            transaction_id (str): The ID of the transaction to query.
        """
        self.transaction_id = transaction_id

    def fetch_transaction_details(self):
        """
        Fetch the transaction details from the NerveNetwork Explorer API.

        Returns:
            dict: A dictionary containing transaction details if successful, otherwise None.
        """
        url = f"{self.BASE_URL}/transaction/{self.transaction_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")  # Log request errors
        except Exception as err:
            logging.error(f"An error occurred: {err}")  # Log any other errors
        return None

    def display_transaction_details(self):
        """
        Display the transaction details, including confirmation time and asset flow statistics.
        """
        transaction_details = self.fetch_transaction_details()
        if transaction_details:
            logging.info("Transaction Details:")
            logging.info(f"Transaction ID: {transaction_details.get('id')}")
            logging.info(f"Confirmation Time: {transaction_details.get('confirmationTime')}")
            logging.info(f"Asset Flow Statistics: {transaction_details.get('assetFlowStatistics')}")
        else:
            logging.error("Failed to retrieve transaction details.")


if __name__ == "__main__":
    # Example transaction ID to query
    transaction_id = "TX123456789"
    
    # Create an instance of the NerveNetworkExplorer class
    explorer = NerveNetworkExplorer(transaction_id)
    
    # Display the transaction details
    explorer.display_transaction_details()
```
