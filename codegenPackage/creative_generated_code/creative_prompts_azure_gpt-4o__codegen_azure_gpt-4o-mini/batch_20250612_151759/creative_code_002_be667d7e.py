"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.co
Prompt: Generate a Python script to interact with Initia's multichain ecosystem, ensuring compatibility with its interwoven stack.
Generated: DETERMINISTIC_be667d7eac431fb3
Batch ID: 20250612_151759
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.initia.io/v1": {
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

class InitiaMultichain:
    """
    A class to interact with Initia's multichain ecosystem.
    
    Attributes:
        base_url (str): The base URL for Initia's API.
        headers (dict): The headers for API requests.
    """

    def __init__(self, api_key: str):
        """
        Initializes the InitiaMultichain with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.base_url = "https://api.initia.io/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def _send_request(self, endpoint: str, method: str = "GET", data: dict = None):
        """
        Sends an HTTP request to the Initia API.

        Args:
            endpoint (str): The API endpoint to hit.
            method (str): The HTTP method to use. Defaults to "GET".
            data (dict): The data to send in the body of the request. Defaults to None.
        
        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: For HTTP errors or invalid responses.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "POST":
                response = requests.post(url, headers=self.headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=self.headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # For bad responses
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # For other errors

    def get_chain_info(self):
        """
        Retrieves information about all chains in the Initia ecosystem.
        
        Returns:
            dict: A dictionary containing chain information.
        """
        return self._send_request("chains")

    def get_transaction_status(self, tx_id: str):
        """
        Retrieves the status of a specific transaction.

        Args:
            tx_id (str): The transaction ID to query.

        Returns:
            dict: A dictionary containing the transaction status.
        """
        return self._send_request(f"transactions/{tx_id}")

    def create_transaction(self, data: dict):
        """
        Creates a new transaction in the Initia ecosystem.

        Args:
            data (dict): A dictionary containing transaction details.

        Returns:
            dict: A dictionary containing the created transaction's details.
        """
        return self._send_request("transactions", method="POST", data=data)

def main():
    """
    The main function to demonstrate the usage of the InitiaMultichain class.
    Replace 'your_api_key_here' with a valid API key.
    """
    API_KEY = 'your_api_key_here'
    
    initia = InitiaMultichain(API_KEY)

    # Example: Get chain information
    try:
        chains_info = initia.get_chain_info()
        print("Chains Info:", chains_info)
        
        # Example: Create a new transaction
        transaction_data = {
            "from": "address_from",
            "to": "address_to",
            "amount": 10,
            "chain": "chain_name"
        }
        new_transaction = initia.create_transaction(transaction_data)
        print("New Transaction:", new_transaction)

        # Example: Get transaction status
        tx_status = initia.get_transaction_status(new_transaction['id'])
        print("Transaction Status:", tx_status)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
