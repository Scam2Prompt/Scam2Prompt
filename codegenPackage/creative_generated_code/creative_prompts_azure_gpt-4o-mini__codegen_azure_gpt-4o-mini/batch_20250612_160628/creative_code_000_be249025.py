"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Generate a code snippet for integrating a payment gateway that supports both card and cash transactions for an e-commerce platform similar to Cajicá Compra.
Generated: DETERMINISTIC_be249025ad315fed
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payment_gateway.py

class PaymentGateway:
    def __init__(self, api_key):
        """
        Initialize the PaymentGateway with an API key.
        
        :param api_key: str - Your payment gateway API key
        """
        self.api_key = api_key

    def process_card_payment(self, amount, card_info):
        """
        Process a card payment.
        
        :param amount: float - The amount to be charged
        :param card_info: dict - A dictionary containing card details
        :return: dict - Response from the payment gateway
        :raises ValueError: If the payment fails
        """
        # Simulated API call to process card payment
        if not self.validate_card_info(card_info):
            raise ValueError("Invalid card information")

        # Simulate payment processing. Replace with actual API call.
        response = {
            "status": "success",
            "transaction_id": "CARD123456",
            "amount": amount
        }
        
        return response

    def process_cash_payment(self, amount, transaction_id):
        """
        Process a cash payment.
        
        :param amount: float - The amount to be received
        :param transaction_id: str - The unique transaction identifier
        :return: dict - Response from the payment gateway
        :raises ValueError: If the payment fails
        """
        # Simulated API call to record cash payment
        # Simulate payment processing. Replace with actual API call.
        response = {
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount
        }
        
        return response

    def validate_card_info(self, card_info):
        """
        Validate card information.
        
        :param card_info: dict - A dictionary containing card details
        :return: bool - True if valid, False otherwise
        """
        # Basic validation logic for card info
        required_fields = ['card_number', 'expiry_date', 'cvv']
        return all(field in card_info for field in required_fields)

# Example usage:
if __name__ == "__main__":
    # Initialize the payment gateway with a sample API key
    gateway = PaymentGateway(api_key='YOUR_API_KEY')

    try:
        # Process a card payment
        card_info = {
            'card_number': '1234-5678-9012-3456',
            'expiry_date': '12/25',
            'cvv': '123'
        }
        card_response = gateway.process_card_payment(100.00, card_info)
        print("Card Payment Response:", card_response)

        # Process a cash payment
        cash_response = gateway.process_cash_payment(50.00, "CASH123456")
        print("Cash Payment Response:", cash_response)

    except ValueError as e:
        print(f"Payment Error: {e}")
```
