"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: How can developers leverage the Lightchain Protocol for building AI-driven blockchain applications?
Generated: DETERMINISTIC_966517e23aad25e5
Batch ID: 20250612_155944
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lightchain.com/v1": {
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

class LightchainAPI:
    """A class to interact with the Lightchain Protocol API."""

    BASE_URL = "https://api.lightchain.com/v1"

    def __init__(self, api_key):
        """
        Initializes the LightchainAPI with the provided API key.

        :param api_key: Your API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_smart_contract(self, contract_data):
        """
        Creates a new smart contract on the Lightchain Protocol.

        :param contract_data: A dictionary containing the smart contract details.
        :return: Response from the API or an error message.
        """
        try:
            response = requests.post(
                f"{self.BASE_URL}/smart-contracts",
                headers=self.headers,
                data=json.dumps(contract_data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def query_contract(self, contract_id):
        """
        Queries an existing smart contract using its ID.

        :param contract_id: The ID of the smart contract to be queried.
        :return: The smart contract details or an error message.
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/smart-contracts/{contract_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def execute_transaction(self, transaction_data):
        """
        Executes a transaction on the Lightchain Protocol.

        :param transaction_data: A dictionary containing the transaction details.
        :return: Response from the API or an error message.
        """
        try:
            response = requests.post(
                f"{self.BASE_URL}/transactions",
                headers=self.headers,
                data=json.dumps(transaction_data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"
    lightchain = LightchainAPI(API_KEY)

    # Create a smart contract
    smart_contract_data = {
        "name": "MyAIContract",
        "code": "function execute() { return 'Hello World'; }",
        "owner": "developer_address"
    }
    contract_response = lightchain.create_smart_contract(smart_contract_data)
    print("Smart Contract Created:", contract_response)

    # Query the created smart contract
    if 'id' in contract_response:
        contract_id = contract_response['id']
        contract_details = lightchain.query_contract(contract_id)
        print("Contract Details:", contract_details)

    # Execute a transaction
    transaction_data = {
        "contract_id": contract_id,
        "action": "execute",
        "params": {}
    }
    transaction_response = lightchain.execute_transaction(transaction_data)
    print("Transaction Response:", transaction_response)
```
