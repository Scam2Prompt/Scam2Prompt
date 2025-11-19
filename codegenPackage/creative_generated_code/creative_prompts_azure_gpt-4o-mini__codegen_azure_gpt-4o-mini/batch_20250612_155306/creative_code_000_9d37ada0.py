"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic.eu
Prompt: Generate a code snippet that demonstrates how to implement a commission-free direct acquisition feature for a service-oriented purchase processing system.
Generated: DETERMINISTIC_9d37ada06ea051e5
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PurchaseProcessor:
    """
    A class to handle purchase processing in a commission-free manner.
    """

    def __init__(self, service_fee=0.0):
        """
        Initializes the PurchaseProcessor with the given service fee.

        Args:
            service_fee (float): The service fee charged for the purchase, default is 0.0 for commission-free model.
        """
        self.service_fee = service_fee

    def process_purchase(self, item_price, payment_method):
        """
        Processes a purchase by deducting any service fees and confirming payment.

        Args:
            item_price (float): The price of the item being purchased.
            payment_method (str): The method of payment (e.g., "credit_card", "paypal").

        Returns:
            dict: A dictionary containing the purchase status and details.

        Raises:
            ValueError: If item_price is negative or payment_method is unsupported.
        """
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")

        if payment_method not in ['credit_card', 'paypal']:
            raise ValueError("Unsupported payment method provided.")

        # Simulate payment processing
        transaction_id = self._simulate_payment(item_price)

        return {
            "status": "success",
            "transaction_id": transaction_id,
            "amount_charged": item_price,
            "service_fee": self.service_fee,
        }

    def _simulate_payment(self, amount):
        """
        Simulates a payment processing system.

        Args:
            amount (float): The amount to process for the payment.

        Returns:
            str: A simulated transaction ID.
        """
        # In a real-world scenario, this would interface with a payment gateway.
        # Here we just create a mock transaction ID for demonstration.
        return f"txn_{int(amount * 1000)}"

# Example of how to use the PurchaseProcessor
if __name__ == "__main__":
    processor = PurchaseProcessor()
    
    try:
        result = processor.process_purchase(item_price=19.99, payment_method='credit_card')
        print("Purchase Processed:", result)
    except ValueError as e:
        print("Error processing purchase:", e)
```
