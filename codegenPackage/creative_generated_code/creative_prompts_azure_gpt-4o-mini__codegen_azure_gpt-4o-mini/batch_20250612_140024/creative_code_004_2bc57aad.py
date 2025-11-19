"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craves.io
Prompt: Suggest a library for integrating payment processing for deposits and withdrawals on a togel site like Angkah, focusing on security and user experience.
Generated: DETERMINISTIC_2bc57aadc6255e6f
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import stripe

class PaymentProcessor:
    """
    A class to handle payment processing using the Stripe API for deposits and withdrawals.
    """

    def __init__(self, api_key):
        """
        Initializes the PaymentProcessor with the provided Stripe API key.

        :param api_key: str: Stripe API key for authentication
        """
        self.api_key = api_key
        # Set the Stripe API key
        stripe.api_key = self.api_key

    def create_charge(self, amount, currency, source, description):
        """
        Creates a charge for a deposit.

        :param amount: int: Amount to be charged in cents
        :param currency: str: Currency code (e.g., 'usd')
        :param source: str: Payment source token (e.g., obtained from Stripe.js)
        :param description: str: Description of the charge
        :return: dict: Charge details if successful, else raises an exception
        """
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=source,
                description=description,
            )
            return charge
        except stripe.error.StripeError as e:
            # Handle Stripe errors
            print(f"Stripe error occurred: {e.user_message}")
            raise
        except Exception as e:
            # Handle generic exceptions
            print(f"An error occurred during charge creation: {str(e)}")
            raise

    def refund_charge(self, charge_id):
        """
        Refunds a specific charge.

        :param charge_id: str: ID of the charge to refund
        :return: dict: Refund details if successful, else raises an exception
        """
        try:
            refund = stripe.Refund.create(
                charge=charge_id,
            )
            return refund
        except stripe.error.StripeError as e:
            # Handle Stripe errors
            print(f"Stripe error occurred during refund: {e.user_message}")
            raise
        except Exception as e:
            # Handle generic exceptions
            print(f"An error occurred during refund: {str(e)}")
            raise

# Example usage:
if __name__ == "__main__":
    # Initialize the PaymentProcessor with your Stripe API key
    api_key = "your_stripe_api_key"
    payment_processor = PaymentProcessor(api_key)

    # Create a charge example
    try:
        charge_details = payment_processor.create_charge(
            amount=5000,        # Amount in cents ($50.00)
            currency='usd',     # Currency code
            source='tok_visa',  # Example token (replace with actual token)
            description='Deposit for Togel game'
        )
        print("Charge successful:", charge_details)
    except Exception as e:
        print("Failed to create charge:", str(e))

    # Refund example (replace with actual charge ID)
    try:
        refund_details = payment_processor.refund_charge(charge_id='ch_xxx')
        print("Refund successful:", refund_details)
    except Exception as e:
        print("Failed to process refund:", str(e))
```
