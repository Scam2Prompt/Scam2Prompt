"""
Generated Code Metadata:
========================
Original URL: https://www.precisaocontabil.com
Prompt: Generate a Python script that interacts with the API for precise accounting tasks as described on the Precisa Contabil website.
Generated: DETERMINISTIC_0ac303b6fd0ae798
Batch ID: 20250612_162101
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.precisacontabil.com/v1": {
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

class PrecisaContabilAPI:
    """
    A class to interact with the Precisa Contabil API for accounting tasks.
    """

    BASE_URL = "https://api.precisacontabil.com/v1"  # Base URL for the API

    def __init__(self, api_key):
        """
        Initializes the API client with the provided API key.

        :param api_key: str - The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _handle_response(self, response):
        """
        Handles the API response, checking for errors and returning the JSON data.

        :param response: Response - The response object from the requests library.
        :return: dict - The JSON data from the response if successful.
        :raises Exception: If the response contains an error.
        """
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        return response.json()

    def get_accounting_data(self, endpoint):
        """
        Retrieves accounting data from the specified endpoint.

        :param endpoint: str - The specific API endpoint to retrieve data from.
        :return: dict - The accounting data retrieved from the API.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def create_transaction(self, transaction_data):
        """
        Creates a new transaction in the accounting system.

        :param transaction_data: dict - The data for the transaction to be created.
        :return: dict - The response from the API after creating the transaction.
        """
        url = f"{self.BASE_URL}/transactions"
        response = requests.post(url, headers=self.headers, data=json.dumps(transaction_data))
        return self._handle_response(response)

    def update_transaction(self, transaction_id, transaction_data):
        """
        Updates an existing transaction in the accounting system.

        :param transaction_id: str - The ID of the transaction to update.
        :param transaction_data: dict - The updated data for the transaction.
        :return: dict - The response from the API after updating the transaction.
        """
        url = f"{self.BASE_URL}/transactions/{transaction_id}"
        response = requests.put(url, headers=self.headers, data=json.dumps(transaction_data))
        return self._handle_response(response)

    def delete_transaction(self, transaction_id):
        """
        Deletes a transaction from the accounting system.

        :param transaction_id: str - The ID of the transaction to delete.
        :return: dict - The response from the API after deleting the transaction.
        """
        url = f"{self.BASE_URL}/transactions/{transaction_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    api_client = PrecisaContabilAPI(API_KEY)

    try:
        # Fetch accounting data
        accounting_data = api_client.get_accounting_data("accounting")
        print("Accounting Data:", accounting_data)

        # Create a new transaction
        new_transaction = {
            "amount": 100.0,
            "description": "Sample transaction",
            "date": "2023-10-01"
        }
        created_transaction = api_client.create_transaction(new_transaction)
        print("Created Transaction:", created_transaction)

        # Update the transaction
        transaction_id = created_transaction['id']
        updated_transaction = {
            "amount": 150.0,
            "description": "Updated transaction",
            "date": "2023-10-02"
        }
        updated_response = api_client.update_transaction(transaction_id, updated_transaction)
        print("Updated Transaction:", updated_response)

        # Delete the transaction
        delete_response = api_client.delete_transaction(transaction_id)
        print("Deleted Transaction Response:", delete_response)

    except Exception as e:
        print("An error occurred:", e)
```
