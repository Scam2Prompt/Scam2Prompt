"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Explain how to use stAPT for lending on platforms like Meso Finance and Aries Markets, including any relevant code examples.
Generated: DETERMINISTIC_e867f3804194b198
Batch ID: 20250612_155153
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.stapt.finance": {
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

class StAPT:
    """
    A class to interact with the StAPT lending protocol on platforms like Meso Finance and Aries Markets.
    """

    def __init__(self, api_url):
        """
        Initializes the StAPT client with the provided API URL.

        :param api_url: str - The base URL for the StAPT API
        """
        self.api_url = api_url

    def get_lending_rates(self):
        """
        Fetches the current lending rates from the StAPT API.

        :return: dict - A dictionary containing lending rates
        :raises Exception: If the API request fails
        """
        try:
            response = requests.get(f"{self.api_url}/lending/rates")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching lending rates: {e}")
            raise

    def lend_tokens(self, borrower_address, token, amount):
        """
        Lends tokens to a borrower on the StAPT platform.

        :param borrower_address: str - The address of the borrower
        :param token: str - The type of token to lend
        :param amount: float - The amount of tokens to lend
        :return: dict - Response from the lending transaction
        :raises Exception: If the lending transaction fails
        """
        payload = {
            "borrower": borrower_address,
            "token": token,
            "amount": amount
        }
        try:
            response = requests.post(f"{self.api_url}/lending/execute", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error lending tokens: {e}")
            raise

    def get_active_loans(self, user_address):
        """
        Retrieves active loans for a specific user.

        :param user_address: str - The address of the user
        :return: dict - A dictionary containing active loans
        :raises Exception: If the API request fails
        """
        try:
            response = requests.get(f"{self.api_url}/loans/active/{user_address}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching active loans: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    api_url = "https://api.stapt.finance"  # Replace with actual StAPT API URL
    stapt = StAPT(api_url)

    # Fetch current lending rates
    try:
        rates = stapt.get_lending_rates()
        print("Current Lending Rates:", rates)
    except Exception as e:
        print(f"Failed to retrieve lending rates: {e}")

    # Lend tokens example
    borrower_address = "0xBorrowerAddress"  # Replace with actual address
    token = "ETH"  # Replace with actual token
    amount = 1.0  # Replace with desired amount to lend

    try:
        transaction_response = stapt.lend_tokens(borrower_address, token, amount)
        print("Lending Transaction Response:", transaction_response)
    except Exception as e:
        print(f"Failed to lend tokens: {e}")

    # Retrieve active loans example
    user_address = "0xUserAddress"  # Replace with actual user address
    try:
        active_loans = stapt.get_active_loans(user_address)
        print("Active Loans:", active_loans)
    except Exception as e:
        print(f"Failed to retrieve active loans: {e}")
```

This Python code provides a simple client for interacting with the StAPT lending protocol, including methods to get lending rates, lend tokens, and retrieve active loans. Proper error handling is included to ensure stability in case of API request failures.
