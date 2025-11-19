"""
Generated Code Metadata:
========================
Original URL: https://api-explorer-pocv1.epg-addonpayments-doc.xyz
Prompt: Create a sample Host2Host API request payload for AddonPayments, including necessary parameters for payment processing.
Generated: DETERMINISTIC_703370e95afc500f
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AddonPaymentsRequest:
    def __init__(self, 
                 merchant_id: str, 
                 api_key: str, 
                 transaction_type: str, 
                 amount: float, 
                 currency: str, 
                 payment_method: str, 
                 customer_info: dict):
        """
        Initialize the AddonPayments request payload.

        Args:
        - merchant_id (str): The unique identifier of the merchant.
        - api_key (str): The API key for authentication.
        - transaction_type (str): The type of transaction (e.g., 'sale', 'auth', 'void').
        - amount (float): The amount of the transaction.
        - currency (str): The currency of the transaction.
        - payment_method (str): The payment method used (e.g., 'credit_card', 'bank_transfer').
        - customer_info (dict): A dictionary containing customer information.
        """
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.transaction_type = transaction_type
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        self.customer_info = customer_info

    def to_dict(self) -> dict:
        """
        Convert the request object to a dictionary.

        Returns:
        - dict: A dictionary representation of the request payload.
        """
        request_payload = {
            'merchant_id': self.merchant_id,
            'api_key': self.api_key,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'currency': self.currency,
            'payment_method': self.payment_method,
            'customer_info': self.customer_info
        }
        return request_payload

    def to_json(self) -> str:
        """
        Convert the request object to a JSON string.

        Returns:
        - str: A JSON string representation of the request payload.
        """
        try:
            return json.dumps(self.to_dict(), indent=4)
        except Exception as e:
            print(f"Error converting to JSON: {str(e)}")
            return None


def main():
    # Example usage:
    merchant_id = "your_merchant_id"
    api_key = "your_api_key"
    transaction_type = "sale"
    amount = 10.99
    currency = "USD"
    payment_method = "credit_card"
    customer_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1 123-456-7890"
    }

    request = AddonPaymentsRequest(merchant_id, 
                                   api_key, 
                                   transaction_type, 
                                   amount, 
                                   currency, 
                                   payment_method, 
                                   customer_info)

    request_json = request.to_json()
    print(request_json)


if __name__ == "__main__":
    main()
```
