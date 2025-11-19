"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thenaflnonce.org
Prompt: Describe the process of on-ramping from fiat to crypto using THENA's services.
Generated: DETERMINISTIC_295acac5601a0ec3
Batch ID: 20250612_161317
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thena.com": {
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
# Import necessary libraries
import requests

class ThenaOnRamp:
    """
    A class to handle the on-ramping process from fiat to cryptocurrency using THENA's services.
    """

    BASE_URL = "https://api.thena.com"  # Replace with the actual API endpoint

    def __init__(self, api_key):
        """
        Initializes the ThenaOnRamp object with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests to THENA's services.
        """
        self.api_key = api_key

    def get_conversion_rates(self, fiat_currency='USD'):
        """
        Fetches the latest conversion rates for the specified fiat currency.

        Args:
            fiat_currency (str): The fiat currency to convert from (default: 'USD').

        Returns:
            dict: A dictionary containing conversion rates for various cryptocurrencies.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/conversion-rates", params={'fiat': fiat_currency},
                                    headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching conversion rates: {e}")
            return None

    def create_transaction(self, fiat_amount, crypto_currency='BTC'):
        """
        Initiates a transaction to convert fiat to cryptocurrency.

        Args:
            fiat_amount (float): The amount of fiat currency to convert.
            crypto_currency (str): The cryptocurrency to receive (default: 'BTC').

        Returns:
            dict: A dictionary containing transaction details or an error message.
        """
        try:
            payload = {
                'amount': fiat_amount,
                'currency': crypto_currency
            }
            response = requests.post(f"{self.BASE_URL}/transactions", json=payload,
                                     headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating transaction: {e}")
            return {"error": str(e)}

    def track_transaction(self, transaction_id):
        """
        Tracks the status of a transaction using its ID.

        Args:
            transaction_id (str): The ID of the transaction to track.

        Returns:
            dict: A dictionary containing the transaction status or an error message.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/transactions/{transaction_id}",
                                    headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error tracking transaction: {e}")
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    thena_on_ramp = ThenaOnRamp(API_KEY)

    # Get conversion rates
    rates = thena_on_ramp.get_conversion_rates()
    print("Conversion Rates:", rates)

    # Create a transaction
    fiat_amount = 100.0  # Example amount in fiat currency
    transaction = thena_on_ramp.create_transaction(fiat_amount)
    print("Transaction Created:", transaction)

    # Track the transaction
    if 'id' in transaction:
        transaction_id = transaction['id']
        status = thena_on_ramp.track_transaction(transaction_id)
        print("Transaction Status:", status)
```
