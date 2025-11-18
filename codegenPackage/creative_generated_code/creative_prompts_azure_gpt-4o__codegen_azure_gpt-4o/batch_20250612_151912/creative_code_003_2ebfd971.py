"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Provide code examples for integrating a payment gateway to handle legal service fees for Majeli Avocat, ensuring transparency in billing for services like mediation or court representation.
Generated: DETERMINISTIC_2ebfd971f85a8e20
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payment_gateway_integration.py
import stripe

# Stripe API secret key (replace with your actual secret key)
STRIPE_API_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Initialize Stripe with the API key
stripe.api_key = STRIPE_API_SECRET_KEY

class PaymentGateway:
    """
    A class to integrate Stripe payment gateway for handling legal service fees.
    """
    def __init__(self):
        """
        Initializes the PaymentGateway instance.
        """
        pass

    def create_payment_intent(self, amount, currency, description, metadata=None):
        """
        Creates a Stripe Payment Intent to handle service fees.
        
        Args:
            amount (int): The amount to be charged in the smallest currency unit (e.g., cents for USD).
            currency (str): The currency code (e.g., 'usd', 'eur').
            description (str): A description of the payment.
            metadata (dict, optional): Additional metadata for payment tracking (e.g., service type, customer ID).

        Returns:
            dict: The response from Stripe containing payment intent details.
        """
        try:
            # Create a payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                description=description,
                metadata=metadata or {},
            )
            return payment_intent
        except stripe.error.StripeError as e:
            # Handle Stripe-related errors
            return {"error": str(e)}
        except Exception as e:
            # Handle unexpected errors
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def retrieve_payment_intent(self, payment_intent_id):
        """
        Retrieves details of a previously created payment intent.
        
        Args:
            payment_intent_id (str): The ID of the payment intent.

        Returns:
            dict: The response from Stripe containing payment intent details.
        """
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return payment_intent
        except stripe.error.StripeError as e:
            # Handle Stripe-related errors
            return {"error": str(e)}
        except Exception as e:
            # Handle unexpected errors
            return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Initialize payment gateway class
    payment_gateway = PaymentGateway()

    # Example: Create a payment intent for legal service fees
    service_fee_amount = 15000  # $150.00 represented in cents
    currency = "usd"
    service_description = "Legal Service Fees for Court Representation"
    metadata = {
        "client_name": "Majeli Avocat",
        "service_type": "Court Representation",
        "invoice_number": "INV-1001"
    }

    # Create a payment intent
    payment_intent_response = payment_gateway.create_payment_intent(
        amount=service_fee_amount,
        currency=currency,
        description=service_description,
        metadata=metadata
    )

    # Print payment intent response
    print("Payment Intent Response:", payment_intent_response)

    # Example: Retrieve the payment intent details
    if "id" in payment_intent_response:
        retrieved_payment_intent = payment_gateway.retrieve_payment_intent(payment_intent_response["id"])
        print("Retrieved Payment Intent Details:", retrieved_payment_intent)
    else:
        print("Error creating payment intent:", payment_intent_response)
```

**Note:** Replace `STRIPE_API_SECRET_KEY` with your actual Stripe secret key in production. Ensure secrets are securely stored and follow environment variable practices for security.
