"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgetensor.org
Prompt: Write a code snippet that interacts with the BridgeTensor service to check the status of a bridging transaction, considering the 360-block processing time mentioned on the website.
Generated: DETERMINISTIC_b1d38093f026dc1f
Batch ID: 20250612_155852
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bridgetensor.com": {
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
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BridgeTensorClient:
    """
    A client class to interact with the BridgeTensor service.
    """

    BASE_URL = "https://api.bridgetensor.com"  # Replace with actual BridgeTensor API base URL

    def __init__(self, transaction_id):
        """
        Initializes the BridgeTensorClient with the given transaction ID.

        :param transaction_id: str, the ID of the bridging transaction to check
        """
        self.transaction_id = transaction_id

    def check_transaction_status(self):
        """
        Checks the status of the bridging transaction.

        :return: dict, the status of the transaction
        :raises Exception: if the API call fails or returns an error
        """
        url = f"{self.BASE_URL}/transactions/{self.transaction_id}/status"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            logging.info("Transaction status retrieved successfully.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to retrieve transaction status from BridgeTensor.") from http_err
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception("An unknown error occurred while checking transaction status.") from err

def main():
    transaction_id = "sample-transaction-id"  # Replace with the actual transaction ID

    client = BridgeTensorClient(transaction_id)

    # Wait for the processing time of 360 blocks (assuming 15 seconds per block for demonstration)
    processing_time_seconds = 360 * 15

    logging.info(f"Waiting for {processing_time_seconds} seconds to check the transaction status...")
    time.sleep(processing_time_seconds)

    try:
        status = client.check_transaction_status()
        logging.info(f"Transaction Status: {status}")
    except Exception as e:
        logging.error(f"Failed to check transaction status: {e}")

if __name__ == "__main__":
    main()
```
