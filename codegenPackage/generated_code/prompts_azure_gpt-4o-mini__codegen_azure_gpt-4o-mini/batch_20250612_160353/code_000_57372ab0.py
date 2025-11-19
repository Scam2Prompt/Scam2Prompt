"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate a code snippet for integrating Instant Bank Transfer payments for a casino website, referencing the features of Jackpot Cow Casino's banking options.
Generated: DETERMINISTIC_57372ab062d582fe
Batch ID: 20250612_160353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jackpotcowcasino.com/banking": {
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

class InstantBankTransfer:
    """
    A class to handle Instant Bank Transfer payments for Jackpot Cow Casino.
    """

    BASE_URL = "https://api.jackpotcowcasino.com/banking"  # Base URL for the casino's banking API

    def __init__(self, api_key):
        """
        Initializes the InstantBankTransfer with the provided API key.

        :param api_key: str - The API key for authenticating requests to the casino's banking API.
        """
        self.api_key = api_key

    def initiate_payment(self, amount, account_number, routing_number):
        """
        Initiates an Instant Bank Transfer payment.

        :param amount: float - The amount to be transferred.
        :param account_number: str - The user's bank account number.
        :param routing_number: str - The user's bank routing number.
        :return: dict - Response from the payment API.
        :raises ValueError: If the amount is not positive.
        :raises Exception: For any other errors during the API call.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")

        # Prepare the payment request payload
        payload = {
            "amount": amount,
            "account_number": account_number,
            "routing_number": routing_number
        }

        # Set the headers for the request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make the API call to initiate the payment
            response = requests.post(f"{self.BASE_URL}/instant-bank-transfer", json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Return the JSON response from the API

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with the actual API key
    bank_transfer = InstantBankTransfer(api_key='your_api_key')

    try:
        # Initiate a payment of $100
        payment_response = bank_transfer.initiate_payment(100.00, '123456789', '987654321')
        print("Payment initiated successfully:", payment_response)
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Failed to initiate payment: {e}")
```
