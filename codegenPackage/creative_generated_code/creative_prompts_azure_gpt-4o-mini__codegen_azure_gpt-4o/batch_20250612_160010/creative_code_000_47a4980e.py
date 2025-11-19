"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: How can I implement a subscription management system similar to Rentsy for handling payments and user invitations?
Generated: DETERMINISTIC_47a4980e586693be
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Subscription Management System
Handles user subscriptions, payments, and invitations.
"""

import json
import uuid
from datetime import datetime, timedelta

# Third-party library imports (e.g., Stripe for payment processing)
import stripe

# Stripe API Key (Replace with your actual key)
stripe.api_key = "your_stripe_api_key"

# In-memory storage (replace with a database in production)
users = {}
subscriptions = {}
invitations = {}

# Helper to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# User Management
class User:
    def __init__(self, name, email):
        self.id = generate_id()
        self.name = name
        self.email = email
        self.subscription_id = None

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "subscription_id": self.subscription_id}

# Subscription Management
class Subscription:
    def __init__(self, user_id, plan, start_date):
        self.id = generate_id()
        self.user_id = user_id
        self.plan = plan
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=30)  # Example for monthly subscriptions

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "plan": self.plan,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
        }

# Invitation Management
class Invitation:
    def __init__(self, inviter_id, invitee_email):
        self.id = generate_id()
        self.inviter_id = inviter_id
        self.invitee_email = invitee_email
        self.status = "pending"

    def to_dict(self):
        return {
            "id": self.id,
            "inviter_id": self.inviter_id,
            "invitee_email": self.invitee_email,
            "status": self.status,
        }

# Payment Processing
def process_payment(user_id, amount, currency="usd"):
    try:
        # Simulate payment via Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Stripe expects amounts in cents
            currency=currency,
            metadata={"user_id": user_id},
        )
        return {"status": "success", "payment_intent_id": payment_intent.id}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# API to handle subscriptions
def create_subscription(user_id, plan):
    if user_id not in users:
        raise ValueError("User not found.")
    user = users[user_id]
    if user.subscription_id:
        raise ValueError("User already has an active subscription.")

    # Process payment for subscription
    plans = {"basic": 10.0, "premium": 20.0}  # Example plans
    if plan not in plans:
        raise ValueError("Invalid plan selected.")
    
    payment = process_payment(user_id, plans[plan])
    if payment["status"] == "error":
        raise ValueError(f"Payment failed: {payment['message']}")

    # Create subscription
    subscription = Subscription(user_id, plan, datetime.now())
    subscriptions[subscription.id] = subscription
    user.subscription_id = subscription.id
    return subscription.to_dict()

# API to handle invitations
def send_invitation(inviter_id, invitee_email):
    if inviter_id not in users:
        raise ValueError("Inviter not found.")

    invitation = Invitation(inviter_id, invitee_email)
    invitations[invitation.id] = invitation
    return invitation.to_dict()

# API to list subscriptions
def list_subscriptions():
    return [subscription.to_dict() for subscription in subscriptions.values()]

# Example Usage
if __name__ == "__main__":
    # Create users
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")
    users[user1.id] = user1
    users[user2.id] = user2

    # Create subscription for Alice
    try:
        subscription = create_subscription(user1.id, "basic")
        print("Subscription created:", json.dumps(subscription, indent=4))
    except Exception as e:
        print("Error creating subscription:", str(e))

    # Send invitation from Alice to Bob
    try:
        invitation = send_invitation(user1.id, "bob@example.com")
        print("Invitation sent:", json.dumps(invitation, indent=4))
    except Exception as e:
        print("Error sending invitation:", str(e))

    # List all subscriptions
    print("Subscriptions:", json.dumps(list_subscriptions(), indent=4))
```
