"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicl6dcseudnsbfjhdpevb2qppfqdiqbalqpmd4kdifgdzpdduqykq.ipfs.dweb.link
Prompt: Create a script to interact with zkLink's Playground environment for testing cross-chain transactions using zkLink Nova's API.
Generated: DETERMINISTIC_03d8229aa0d381c7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class ZkLinkClient:
    """
    A client to interact with zkLink's Playground environment for testing cross-chain transactions.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the ZkLinkClient with the given API URL and API key.

        :param api_url: The base URL for the zkLink API.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the zkLink API.

        :param endpoint: The API endpoint to interact with.
        :param method: HTTP method to use for the request.
        :param data: The data to send with the request if applicable.
        :return: Response data from the API.
        :raises Exception: If there is an error with the request.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        url = f"{self.api_url}/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Unsupported HTTP method.")

            # Raise an exception if the response indicates an error
            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Capture HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Capture any other errors

    def get_balance(self, wallet_address):
        """
        Retrieves the balance of a specified wallet.

        :param wallet_address: The address of the wallet to check the balance for.
        :return: The balance of the wallet.
        """
        endpoint = f"balances/{wallet_address}"
        return self._make_request(endpoint)

    def send_transaction(self, transaction_data):
        """
        Sends a cross-chain transaction using zkLink.

        :param transaction_data: A dictionary containing transaction details.
        :return: Response from the transaction request.
        """
        endpoint = "transactions/send"
        return self._make_request(endpoint, method='POST', data=transaction_data)

    def get_transaction_status(self, transaction_id):
        """
        Retrieves the status of a specified transaction.

        :param transaction_id: The ID of the transaction to check.
        :return: The status of the transaction.
        """
        endpoint = f"transactions/{transaction_id}/status"
        return self._make_request(endpoint)

def main():
    """
    Main function to demonstrate zkLink API interaction.
    Replace 'YOUR_API_URL' and 'YOUR_API_KEY' with actual values to run.
    """
    api_url = 'YOUR_API_URL'
    api_key = 'YOUR_API_KEY'

    zklink_client = ZkLinkClient(api_url, api_key)

    # Example: Get wallet balance
    try:
        wallet_address = 'YOUR_WALLET_ADDRESS'
        balance = zklink_client.get_balance(wallet_address)
        print(f"Wallet Balance: {balance}")
    except Exception as e:
        print(e)

    # Example: Send a transaction
    try:
        transaction_data = {
            "from": "SOURCE_WALLET_ADDRESS",
            "to": "DESTINATION_WALLET_ADDRESS",
            "amount": 0.01,
            "token": "TOKEN_SYMBOL"
        }
        transaction_response = zklink_client.send_transaction(transaction_data)
        print(f"Transaction Response: {transaction_response}")
    except Exception as e:
        print(e)

    # Example: Check transaction status
    try:
        transaction_id = 'TRANSACTION_ID'
        status = zklink_client.get_transaction_status(transaction_id)
        print(f"Transaction Status: {status}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
