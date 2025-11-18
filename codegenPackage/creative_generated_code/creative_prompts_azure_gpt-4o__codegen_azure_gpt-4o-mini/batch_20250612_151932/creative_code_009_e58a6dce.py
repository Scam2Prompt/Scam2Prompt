"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Demonstrate how to retrieve and display transaction history for a specific wallet address in a StarkNet dApp.
Generated: DETERMINISTIC_e58a6dceda174b38
Batch ID: 20250612_151932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io": {
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

class StarkNetAPI:
    """
    A class to interact with the StarkNet blockchain API.
    """

    def __init__(self, base_url):
        """
        Initializes the StarkNetAPI with the given base URL.

        :param base_url: The base URL for the StarkNet API.
        """
        self.base_url = base_url

    def get_transaction_history(self, wallet_address):
        """
        Retrieves the transaction history for a specific wallet address.

        :param wallet_address: The wallet address to fetch transaction history for.
        :return: List of transactions or an error message.
        """
        try:
            # Endpoint for fetching transaction history
            endpoint = f"{self.base_url}/v1/wallets/{wallet_address}/transactions"
            response = requests.get(endpoint)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()  # Return the transaction history as JSON
            else:
                raise Exception(f"Error fetching transaction history: {response.status_code} - {response.text}")

        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")


def display_transaction_history(wallet_address):
    """
    Fetches and displays the transaction history for a given wallet address.

    :param wallet_address: The wallet address whose transaction history is to be displayed.
    """
    # Base URL for the StarkNet API
    base_url = "https://api.starknet.io"
    api = StarkNetAPI(base_url)

    try:
        # Fetch transaction history
        transactions = api.get_transaction_history(wallet_address)

        # Display the transaction history
        print(f"Transaction history for wallet address {wallet_address}:")
        for transaction in transactions:
            print(f"- Hash: {transaction['hash']}, Status: {transaction['status']}, Timestamp: {transaction['timestamp']}")

    except Exception as e:
        print(f"Failed to retrieve transaction history: {str(e)}")


if __name__ == "__main__":
    # Replace with the wallet address you want to query
    wallet_address = "0xYourWalletAddressHere"
    display_transaction_history(wallet_address)
```
