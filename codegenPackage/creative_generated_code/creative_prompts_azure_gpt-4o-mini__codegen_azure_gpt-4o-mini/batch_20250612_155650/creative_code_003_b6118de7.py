"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solscanai.com
Prompt: Provide an example of how to implement advanced AI analytics for exploring the Solana blockchain using Solscan AI.
Generated: DETERMINISTIC_b6118de74df21229
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solscan.io/v1/": {
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

class SolanaAnalytics:
    """
    A class to interact with the Solscan AI API to retrieve and analyze data from the Solana blockchain.
    """

    BASE_URL = "https://api.solscan.io/v1/"
    
    def __init__(self):
        """
        Initializes the SolanaAnalytics class.
        """
        pass

    def get_transaction_data(self, transaction_id):
        """
        Fetches transaction data from Solscan for a given transaction ID.

        Args:
            transaction_id (str): The ID of the transaction to retrieve.

        Returns:
            dict: The transaction data if successful, None otherwise.
        """
        endpoint = f"transaction/{transaction_id}"
        response = self._make_request(endpoint)
        return response

    def get_account_data(self, account_address):
        """
        Fetches account data from Solscan for a given account address.

        Args:
            account_address (str): The address of the account.

        Returns:
            dict: The account data if successful, None otherwise.
        """
        endpoint = f"account/{account_address}"
        response = self._make_request(endpoint)
        return response

    def _make_request(self, endpoint):
        """
        Helper method to make a GET request to the Solscan API.

        Args:
            endpoint (str): The API endpoint to call.

        Returns:
            dict: The JSON response from the API, or None if an error occurs.
        """
        url = self.BASE_URL + endpoint
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred during request: {req_err}")  # Log other request errors
        except json.JSONDecodeError as json_err:
            print(f"JSON decoding error: {json_err}")  # Log JSON decoding errors

        return None

# Example of using the SolanaAnalytics class
if __name__ == "__main__":
    analytics = SolanaAnalytics()
    
    # Replace with actual transaction ID and account address to test
    transaction_id = "your_transaction_id_here"
    account_address = "your_account_address_here"

    # Fetch and display transaction data
    transaction_data = analytics.get_transaction_data(transaction_id)
    if transaction_data:
        print("Transaction Data:", json.dumps(transaction_data, indent=4))
    
    # Fetch and display account data
    account_data = analytics.get_account_data(account_address)
    if account_data:
        print("Account Data:", json.dumps(account_data, indent=4))
```
