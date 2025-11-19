"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aishcrypt.com
Prompt: How does Aishcrypt ensure secure transactions when exchanging Payeer to M-Pesa?
Generated: DETERMINISTIC_d8e5f6bf7b05b575
Batch ID: 20250612_155654
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://sandbox.safaricom.co.ke/mpesa/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://payeer.com/api/": {
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

class AishcryptTransaction:
    def __init__(self, payeer_api_key, mpesa_api_key):
        """
        Initializes the AishcryptTransaction with API keys for Payeer and M-Pesa.
        
        :param payeer_api_key: API key for accessing Payeer services
        :param mpesa_api_key: API key for accessing M-Pesa services
        """
        self.payeer_api_key = payeer_api_key
        self.mpesa_api_key = mpesa_api_key
        self.base_payeer_url = "https://payeer.com/api/"
        self.base_mpesa_url = "https://sandbox.safaricom.co.ke/mpesa/"

    def exchange_currency(self, amount, currency_from, currency_to):
        """
        Exchanges currency from Payeer to M-Pesa.
        
        :param amount: Amount of currency to exchange
        :param currency_from: Currency type to exchange from
        :param currency_to: Currency type to exchange to
        :return: Transaction details if successful, otherwise raises an error
        """
        try:
            # Step 1: Validate input
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            # Step 2: Get exchange rate from Payeer
            exchange_rate = self.get_exchange_rate(currency_from, currency_to)
            exchanged_amount = amount * exchange_rate

            # Step 3: Create Payeer transaction
            transaction_id = self.create_payeer_transaction(amount, currency_from)

            # Step 4: Create M-Pesa transaction
            mpesa_transaction_id = self.create_mpesa_transaction(exchanged_amount)

            return {
                "payeer_transaction_id": transaction_id,
                "mpesa_transaction_id": mpesa_transaction_id,
                "exchanged_amount": exchanged_amount,
                "exchange_rate": exchange_rate
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

    def get_exchange_rate(self, currency_from, currency_to):
        """
        Retrieves the exchange rate between two currencies from Payeer API.
        
        :param currency_from: Currency type to exchange from
        :param currency_to: Currency type to exchange to
        :return: Exchange rate
        """
        # Placeholder for API call to get exchange rate
        response = requests.get(f"{self.base_payeer_url}/exchange-rate/{currency_from}/{currency_to}")
        if response.status_code != 200:
            raise Exception("Failed to retrieve exchange rate.")
        
        data = response.json()
        return data['rate']

    def create_payeer_transaction(self, amount, currency):
        """
        Creates a transaction on Payeer.
        
        :param amount: Amount to exchange
        :param currency: Currency type
        :return: Transaction ID
        """
        response = requests.post(f"{self.base_payeer_url}/transactions", json={
            "amount": amount,
            "currency": currency,
            "api_key": self.payeer_api_key
        })

        if response.status_code != 201:
            raise Exception("Failed to create Payeer transaction.")
        
        data = response.json()
        return data['transaction_id']

    def create_mpesa_transaction(self, amount):
        """
        Creates a transaction on M-Pesa.
        
        :param amount: Amount to transfer
        :return: M-Pesa transaction ID
        """
        response = requests.post(f"{self.base_mpesa_url}/transactions", json={
            "amount": amount,
            "api_key": self.mpesa_api_key
        })

        if response.status_code != 201:
            raise Exception("Failed to create M-Pesa transaction.")
        
        data = response.json()
        return data['transaction_id']

# Example usage:
if __name__ == "__main__":
    PAYEER_API_KEY = "your_payeer_api_key"
    MPESA_API_KEY = "your_mpesa_api_key"
    
    transaction = AishcryptTransaction(PAYEER_API_KEY, MPESA_API_KEY)
    try:
        result = transaction.exchange_currency(100, "USD", "KES")
        print("Transaction successful:", result)
    except Exception as e:
        print("Transaction failed:", e)
```
