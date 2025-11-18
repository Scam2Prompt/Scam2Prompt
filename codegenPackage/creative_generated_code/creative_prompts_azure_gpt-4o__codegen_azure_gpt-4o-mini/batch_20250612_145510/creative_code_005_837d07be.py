"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pik-dapp.hk.bigfly.xyz
Prompt: Write code to query the 极峯(PIK) 公链 (public chain) for transaction history and token balances using its unique API.
Generated: DETERMINISTIC_837d07bea32664c9
Batch ID: 20250612_145510
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pik.com/v1": {
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

class PIKAPI:
    """
    A class to interact with the 极峯(PIK) 公链 API for querying transaction history and token balances.
    """

    BASE_URL = "https://api.pik.com/v1"  # Replace with the actual base URL of the PIK API

    def __init__(self, api_key):
        """
        Initializes the PIKAPI with the provided API key.

        :param api_key: str: The API key for authentication with the PIK API.
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Constructs the headers required for API requests.

        :return: dict: The headers for the API request.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_transaction_history(self, address):
        """
        Fetches the transaction history for a given wallet address.

        :param address: str: The wallet address to query.
        :return: list: A list of transactions associated with the address.
        :raises ValueError: If the address is invalid.
        :raises Exception: For general API errors.
        """
        if not self._validate_address(address):
            raise ValueError("Invalid wallet address format.")

        endpoint = f"{self.BASE_URL}/transactions/{address}"
        try:
            response = requests.get(endpoint, headers=self._get_headers())
            response.raise_for_status()
            return response.json().get("transactions", [])
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def get_token_balance(self, address):
        """
        Fetches the token balance for a given wallet address.

        :param address: str: The wallet address to query.
        :return: dict: A dictionary containing token balances.
        :raises ValueError: If the address is invalid.
        :raises Exception: For general API errors.
        """
        if not self._validate_address(address):
            raise ValueError("Invalid wallet address format.")

        endpoint = f"{self.BASE_URL}/balances/{address}"
        try:
            response = requests.get(endpoint, headers=self._get_headers())
            response.raise_for_status()
            return response.json().get("balances", {})
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def _validate_address(self, address):
        """
        Validates the wallet address format.

        :param address: str: The wallet address to validate.
        :return: bool: True if valid, False otherwise.
        """
        # Implement proper address validation logic based on PIK specifications
        return isinstance(address, str) and len(address) == 42  # Example validation

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    wallet_address = "0xYourWalletAddressHere"  # Replace with an actual wallet address

    pik_api = PIKAPI(api_key=API_KEY)

    try:
        transactions = pik_api.get_transaction_history(wallet_address)
        print("Transaction History:", transactions)

        balances = pik_api.get_token_balance(wallet_address)
        print("Token Balances:", balances)
    except Exception as e:
        print(f"Error: {e}")
```
