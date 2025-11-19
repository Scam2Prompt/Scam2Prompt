"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woodao.org
Prompt: Create a sample application that demonstrates how to use the Bank Mellat API for processing electronic payments and managing customer accounts.
Generated: DETERMINISTIC_5496e85d764ce30a
Batch ID: 20250612_160102
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bpm.shaparak.ir/v1.1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.com/callback": {
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

class BankMellatAPI:
    """
    A class to interact with the Bank Mellat API for processing electronic payments
    and managing customer accounts.
    """

    BASE_URL = "https://bpm.shaparak.ir/v1.1/"
    
    def __init__(self, terminal_id, username, password):
        """
        Initialize the Bank Mellat API client.
        
        :param terminal_id: str: The terminal ID provided by Bank Mellat
        :param username: str: The username for authentication
        :param password: str: The password for authentication
        """
        self.terminal_id = terminal_id
        self.username = username
        self.password = password

    def _post_request(self, endpoint, data):
        """
        Internal method to send a POST request to the Bank Mellat API.
        
        :param endpoint: str: The API endpoint
        :param data: dict: The data to send in the request
        :return: dict: The JSON response from the API
        """
        try:
            response = requests.post(self.BASE_URL + endpoint, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def request_transaction(self, order_id, amount, callback_url):
        """
        Request a new transaction for processing payment.
        
        :param order_id: str: Unique order ID for the transaction
        :param amount: int: Amount to be processed (in IRR)
        :param callback_url: str: URL to redirect user after payment
        :return: dict: Response containing transaction details
        """
        data = {
            "terminalId": self.terminal_id,
            "userName": self.username,
            "userPassword": self.password,
            "orderId": order_id,
            "amount": amount,
            "callbackUrl": callback_url,
            "payerId": 0  # Typically set to 0 for general transactions
        }
        return self._post_request("gateway/api/v1/request", data)

    def verify_transaction(self, order_id, sale_order_id, sale_reference_id):
        """
        Verify a transaction after payment completion.
        
        :param order_id: str: Unique order ID for the transaction
        :param sale_order_id: str: Sale Order ID returned from payment
        :param sale_reference_id: str: Sale Reference ID returned from payment
        :return: dict: Response confirming transaction verifications
        """
        data = {
            "terminalId": self.terminal_id,
            "userName": self.username,
            "userPassword": self.password,
            "orderId": order_id,
            "saleOrderId": sale_order_id,
            "saleReferenceId": sale_reference_id
        }
        return self._post_request("gateway/api/v1/verify", data)

    def cancel_transaction(self, order_id, sale_order_id, sale_reference_id):
        """
        Cancel a previously made transaction.
        
        :param order_id: str: Unique order ID for the transaction
        :param sale_order_id: str: Sale Order ID returned from payment
        :param sale_reference_id: str: Sale Reference ID returned from payment
        :return: dict: Response confirming cancellation
        """
        data = {
            "terminalId": self.terminal_id,
            "userName": self.username,
            "userPassword": self.password,
            "orderId": order_id,
            "saleOrderId": sale_order_id,
            "saleReferenceId": sale_reference_id
        }
        return self._post_request("gateway/api/v1/cancel", data)

# Example usage
if __name__ == "__main__":
    # Initialize the Bank Mellat API client with your credentials
    terminal_id = "123456"  # Replace with your terminal ID
    username = "your_username"  # Replace with your username
    password = "your_password"  # Replace with your password

    bank_mellat = BankMellatAPI(terminal_id, username, password)

    # Request a transaction
    order_id = "777"  # Unique order ID
    amount = 100000  # Amount in IRR
    callback_url = "https://yourwebsite.com/callback"  # Your callback URL
    transaction_response = bank_mellat.request_transaction(order_id, amount, callback_url)
    print("Transaction Response:", transaction_response)

    # Process further depending on transaction_response...
```
