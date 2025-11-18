"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Recommend APIs or libraries for implementing credit card processing in a restaurant POS system, referencing Retail Tech Solutions' expertise in this area.
Generated: DETERMINISTIC_165f89c4f60b52fc
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import stripe  # Stripe API for payment processing
import logging  # Logging for error handling and debugging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Stripe API Key (Replace with your actual secret key, keep it secure)
STRIPE_API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Initialize Stripe with the API key
stripe.api_key = STRIPE_API_KEY

def process_payment(amount, currency, card_token):
    """
    Process credit card payments using Stripe API.
    
    Args:
        amount (int): Payment amount in the smallest currency unit (e.g., cents for USD).
        currency (str): Currency code (e.g., 'usd').
        card_token (str): Token representing the customer's card details.
    
    Returns:
        dict: Payment response data from Stripe.
    
    Raises:
        Exception: Raises an exception if payment fails.
    """
    try:
        # Log the payment attempt
        logging.info(f"Processing payment of {amount} {currency} using card token {card_token}.")

        # Create a charge using Stripe API
        charge = stripe.Charge.create(
            amount=amount,  # Amount in cents
            currency=currency,  # Currency code
            source=card_token,  # Card token
            description="Restaurant POS Payment"  # Description for the transaction
        )
        
        # Log successful payment
        logging.info(f"Payment successful: {charge['id']}")
        return charge

    except stripe.error.CardError as e:
        # Handle card errors (e.g., declined cards)
        logging.error(f"Card error occurred: {e}")
        raise Exception("Payment failed due to a card error.") from e

    except stripe.error.RateLimitError as e:
        # Handle rate limit errors
        logging.error(f"Rate limit error occurred: {e}")
        raise Exception("Too many requests to the payment gateway. Please try again later.") from e

    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        logging.error(f"Invalid request to Stripe API: {e}")
        raise Exception("Invalid payment request. Please check the input parameters.") from e

    except stripe.error.AuthenticationError as e:
        # Handle authentication errors
        logging.error(f"Authentication error with Stripe API: {e}")
        raise Exception("Authentication with the payment gateway failed. Please check API keys.") from e

    except stripe.error.APIConnectionError as e:
        # Handle network communication errors
        logging.error(f"Network error with Stripe API: {e}")
        raise Exception("Network error while connecting to the payment gateway.") from e

    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        logging.error(f"Stripe error occurred: {e}")
        raise Exception("An error occurred while processing the payment. Please try again.") from e

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {e}")
        raise Exception("An unexpected error occurred. Please contact support.") from e


# Example usage of the payment processing function
if __name__ == "__main__":
    try:
        # Example payment details
        amount = 5000  # $50.00 in cents
        currency = "usd"  # Currency code
        card_token = "tok_visa"  # Replace with a valid Stripe token for testing

        # Process the payment
        payment_response = process_payment(amount, currency, card_token)
        print("Payment successful:", payment_response)

    except Exception as e:
        # Handle any errors that occur during payment processing
        print("Error:", str(e))
```

### Notes:
- The code uses the Stripe Python library (`stripe`) for credit card processing.
- Replace `STRIPE_API_KEY` with your actual Stripe secret key. Ensure this key is protected and not exposed in the codebase or public repositories.
- Use secure methods to obtain `card_token`, such as Stripe's Checkout or Payment Intent APIs.
- Always test API integrations thoroughly in a staging environment before deploying to production.
