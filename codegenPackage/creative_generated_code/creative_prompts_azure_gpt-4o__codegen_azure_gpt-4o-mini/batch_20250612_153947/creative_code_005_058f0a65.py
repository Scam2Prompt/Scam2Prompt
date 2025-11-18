"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Write code to automate membership billing and renewal processes for a subscription-based crypto education platform, similar to Crypstocks' payment system.
Generated: DETERMINISTIC_058f0a65c7089bc4
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Optional
import stripe

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your secret key for stripe
stripe.api_key = 'your_stripe_secret_key'

class Subscription:
    def __init__(self, user_id: str, plan_id: str, billing_interval: str):
        self.user_id = user_id  # Unique identifier for the user
        self.plan_id = plan_id  # Identifier for the subscription plan
        self.billing_interval = billing_interval  # Monthly or yearly
        self.start_date = datetime.datetime.now()  # Start date of the subscription
        self.status = 'active'  # Subscription status

    def calculate_next_billing_date(self) -> datetime.datetime:
        if self.billing_interval == 'monthly':
            return self.start_date + datetime.timedelta(days=30)
        elif self.billing_interval == 'yearly':
            return self.start_date + datetime.timedelta(days=365)
        else:
            raise ValueError("Invalid billing interval. Must be 'monthly' or 'yearly'.")

    def renew(self) -> None:
        """Renew the subscription and charge the user."""
        try:
            next_billing_date = self.calculate_next_billing_date()
            # Charge the user using Stripe
            stripe.Charge.create(
                amount=self.get_amount(),
                currency='usd',
                customer=self.user_id,
                description='Renewal for subscription plan: ' + self.plan_id,
            )
            logging.info(f"Successfully renewed subscription for user {self.user_id}. Next billing date is {next_billing_date}.")
            self.start_date = next_billing_date  # Update start date to next billing date
        except Exception as e:
            logging.error(f"Failed to renew subscription for user {self.user_id}. Error: {str(e)}")

    def get_amount(self) -> int:
        """Get the amount to charge based on the plan."""
        # Example pricing, this would normally be fetched from a database or configuration
        prices = {
            'basic': 1000,  # $10.00 for basic plan per month
            'premium': 2000,  # $20.00 for premium plan per month
        }
        return prices.get(self.plan_id, 0)

class MembershipBillingSystem:
    def __init__(self):
        self.subscriptions: List[Subscription] = []  # List to hold active subscriptions

    def add_subscription(self, user_id: str, plan_id: str, billing_interval: str) -> Subscription:
        """Add a new subscription for a user."""
        subscription = Subscription(user_id, plan_id, billing_interval)
        self.subscriptions.append(subscription)
        logging.info(f"Added subscription for user {user_id}.")
        return subscription

    def process_renewals(self) -> None:
        """Process renewals for all active subscriptions."""
        for subscription in self.subscriptions:
            try:
                next_billing_date = subscription.calculate_next_billing_date()
                if datetime.datetime.now() >= next_billing_date:
                    subscription.renew()
            except Exception as e:
                logging.error(f"Error processing renewal for user {subscription.user_id}. Error: {str(e)}")

# Example usage:
if __name__ == "__main__":
    billing_system = MembershipBillingSystem()

    # Add a subscription for a user
    billing_system.add_subscription('user_123', 'basic', 'monthly')

    # Simulate the renewal process (this would normally be scheduled)
    billing_system.process_renewals()
```
