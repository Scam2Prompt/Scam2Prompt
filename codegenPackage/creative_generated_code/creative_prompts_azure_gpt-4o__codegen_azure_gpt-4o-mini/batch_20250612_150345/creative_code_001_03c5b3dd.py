"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Generate code to integrate automatic and manual payment gateways for an investment platform, referencing the gateway system described on Hyiprio.
Generated: DETERMINISTIC_03c5b3dda378b885
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payment_gateway.py

class PaymentGatewayError(Exception):
    """Custom exception for payment gateway errors."""
    pass

class PaymentGateway:
    """Class to handle both automatic and manual payment gateways for an investment platform."""

    def __init__(self, gateway_type):
        """
        Initialize the PaymentGateway with a specific type.

        Args:
            gateway_type (str): The type of payment gateway ('automatic' or 'manual').
        """
        self.gateway_type = gateway_type.lower()
        if self.gateway_type not in ['automatic', 'manual']:
            raise PaymentGatewayError("Invalid gateway type specified. Use 'automatic' or 'manual'.")

    def process_payment(self, amount, user_id):
        """
        Process a payment based on the gateway type.

        Args:
            amount (float): The amount to be processed.
            user_id (int): The ID of the user making the payment.

        Returns:
            str: Confirmation message upon successful payment.

        Raises:
            PaymentGatewayError: For any error occurring during payment processing.
        """
        if amount <= 0:
            raise PaymentGatewayError("Payment amount must be greater than zero.")

        if self.gateway_type == 'automatic':
            return self._process_automatic_payment(amount, user_id)
        elif self.gateway_type == 'manual':
            return self._process_manual_payment(amount, user_id)

    def _process_automatic_payment(self, amount, user_id):
        """
        Simulate the processing of an automatic payment.

        Args:
            amount (float): The amount to be processed.
            user_id (int): The ID of the user making the payment.

        Returns:
            str: Confirmation message upon successful automatic payment.
        """
        # Here, you would integrate with an actual payment API for automatic payments.
        # For demonstration purposes, we simulate the success.
        return f"Automatic payment of {amount} processed successfully for user ID: {user_id}."

    def _process_manual_payment(self, amount, user_id):
        """
        Simulate the processing of a manual payment.

        Args:
            amount (float): The amount to be processed.
            user_id (int): The ID of the user making the payment.

        Returns:
            str: Confirmation message upon successful manual payment.
        """
        # In a real application, this might involve sending instructions to the user.
        return (f"Manual payment of {amount} initiated for user ID: {user_id}. "
                "Please follow the instructions sent to your email.")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize an automatic payment gateway
        automatic_gateway = PaymentGateway(gateway_type='automatic')
        print(automatic_gateway.process_payment(100.00, user_id=1))

        # Initialize a manual payment gateway
        manual_gateway = PaymentGateway(gateway_type='manual')
        print(manual_gateway.process_payment(50.00, user_id=2))

    except PaymentGatewayError as e:
        print(f"Payment processing error: {e}")
```
