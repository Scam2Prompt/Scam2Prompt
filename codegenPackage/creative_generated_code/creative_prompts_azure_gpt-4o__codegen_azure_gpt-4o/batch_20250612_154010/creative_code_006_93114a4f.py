"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Write code to implement a subscription-based payment system for a time-tracking service for lawyers, inspired by BillYourTime.com's $9.99/month pricing model.
Generated: DETERMINISTIC_93114a4f8c856615
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
import stripe

# Stripe API key setup (replace with your own secret key)
stripe.api_key = "sk_test_your_api_key_here"

# Constants
SUBSCRIPTION_PRICE = 9.99  # Monthly subscription price in USD
SUBSCRIPTION_INTERVAL_DAYS = 30  # Subscription interval in days

# User class to manage user subscriptions
class User:
    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.email = email
        self.subscription_active = False  # Subscription status
        self.subscription_end_date = None  # Date the subscription expires
    
    def activate_subscription(self):
        """Activate the user's subscription."""
        self.subscription_active = True
        self.subscription_end_date = datetime.now() + timedelta(days=SUBSCRIPTION_INTERVAL_DAYS)
    
    def deactivate_subscription(self):
        """Deactivate the user's subscription."""
        self.subscription_active = False
        self.subscription_end_date = None
    
    def is_subscription_active(self):
        """Check if the user's subscription is active."""
        if self.subscription_end_date and datetime.now() > self.subscription_end_date:
            self.deactivate_subscription()
        return self.subscription_active

# Payment processing function using Stripe
def process_payment(user, payment_method_id):
    """
    Process payment for the user's subscription using Stripe.

    Args:
        user (User): The user object.
        payment_method_id (str): The payment method ID obtained from the client.
    
    Returns:
        bool: True if payment is successful, False otherwise.
    """
    try:
        # Create a customer in Stripe
        customer = stripe.Customer.create(
            email=user.email,
            name=user.name,
            payment_method=payment_method_id,
            invoice_settings={'default_payment_method': payment_method_id}
        )

        # Create a one-time payment
        stripe.PaymentIntent.create(
            amount=int(SUBSCRIPTION_PRICE * 100),  # Stripe requires amount in cents
            currency="usd",
            customer=customer.id,
            payment_method=payment_method_id,
            confirm=True,  # Confirm the payment immediately
        )

        # Activate subscription upon successful payment
        user.activate_subscription()
        print(f"Subscription activated for user {user.name}.")
        return True

    except stripe.error.CardError as e:
        # Handle card errors
        print(f"Card error: {e.user_message}")
    except stripe.error.RateLimitError:
        # Handle rate limit errors
        print("Rate limit exceeded, please try again later.")
    except stripe.error.InvalidRequestError as e:
        # Handle invalid requests
        print(f"Invalid request: {e.user_message}")
    except stripe.error.AuthenticationError:
        # Handle authentication errors
        print("Authentication error.")
    except stripe.error.APIConnectionError:
        # Handle network errors
        print("Network error.")
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        print(f"Stripe error: {e.user_message}")
    except Exception as e:
        # Handle other errors
        print(f"An unexpected error occurred: {str(e)}")
    
    return False

# Example usage
if __name__ == "__main__":
    # Create a new user
    user = User(name="Jane Doe", email="jane.doe@example.com")

    # Simulate payment method ID from client (replace with actual ID in a real scenario)
    payment_method_id = "pm_card_visa"

    # Process payment and activate subscription
    if process_payment(user, payment_method_id):
        print("Payment successful. Subscription details:")
        print(f"User: {user.name}")
        print(f"Subscription Active: {user.is_subscription_active()}")
        print(f"Subscription End Date: {user.subscription_end_date}")
    else:
        print("Payment failed. Subscription not activated.")
```
