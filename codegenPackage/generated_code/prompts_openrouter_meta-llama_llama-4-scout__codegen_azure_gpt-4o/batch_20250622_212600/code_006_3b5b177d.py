"""
Generated Code Metadata:
========================
Original URL: https://etherroll.cash
Prompt: "Develop a plan for implementing a VIP club and affiliate program for an online casino, inspired by BC Game's model."
Generated: DETERMINISTIC_3b5b177d3c3b15cb
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
VIP Club and Affiliate Program Implementation for an Online Casino
Inspired by BC Game's Model
"""

# Import necessary libraries
import uuid
from datetime import datetime

# Constants
VIP_TIERS = ["Bronze", "Silver", "Gold", "Platinum", "Diamond"]
AFFILIATE_COMMISSION_RATE = 0.05  # 5% commission rate

# Database simulation (replace with actual database integration in production)
users_db = {}
transactions_db = []
affiliates_db = {}

# Error classes
class UserNotFoundError(Exception):
    pass

class InvalidTierError(Exception):
    pass

# Models
class User:
    def __init__(self, username, email):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.vip_tier = VIP_TIERS[0]  # Default to Bronze
        self.total_spent = 0.0
        self.affiliate_id = None
        self.created_at = datetime.now()

    def upgrade_vip_tier(self):
        """Upgrade the user's VIP tier based on their total spending."""
        if self.total_spent >= 10000:
            self.vip_tier = VIP_TIERS[4]  # Diamond
        elif self.total_spent >= 5000:
            self.vip_tier = VIP_TIERS[3]  # Platinum
        elif self.total_spent >= 1000:
            self.vip_tier = VIP_TIERS[2]  # Gold
        elif self.total_spent >= 500:
            self.vip_tier = VIP_TIERS[1]  # Silver

    def __repr__(self):
        return f"User(username={self.username}, vip_tier={self.vip_tier}, total_spent={self.total_spent})"

class Affiliate:
    def __init__(self, username):
        self.affiliate_id = str(uuid.uuid4())
        self.username = username
        self.total_commission = 0.0
        self.referred_users = []
        self.created_at = datetime.now()

    def add_referred_user(self, user_id):
        """Add a referred user to the affiliate's list."""
        self.referred_users.append(user_id)

    def calculate_commission(self, transaction_amount):
        """Calculate commission based on transaction amount."""
        commission = transaction_amount * AFFILIATE_COMMISSION_RATE
        self.total_commission += commission
        return commission

    def __repr__(self):
        return f"Affiliate(username={self.username}, total_commission={self.total_commission})"

# Functions
def register_user(username, email, affiliate_id=None):
    """Register a new user."""
    user = User(username, email)
    users_db[user.user_id] = user

    # Link user to affiliate if affiliate_id is provided
    if affiliate_id:
        affiliate = affiliates_db.get(affiliate_id)
        if affiliate:
            user.affiliate_id = affiliate_id
            affiliate.add_referred_user(user.user_id)
        else:
            raise UserNotFoundError("Affiliate not found.")

    return user

def register_affiliate(username):
    """Register a new affiliate."""
    affiliate = Affiliate(username)
    affiliates_db[affiliate.affiliate_id] = affiliate
    return affiliate

def record_transaction(user_id, amount):
    """Record a transaction and update user's VIP tier."""
    user = users_db.get(user_id)
    if not user:
        raise UserNotFoundError("User not found.")

    # Record transaction
    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": user_id,
        "amount": amount,
        "timestamp": datetime.now()
    }
    transactions_db.append(transaction)

    # Update user's total spending and VIP tier
    user.total_spent += amount
    user.upgrade_vip_tier()

    # Handle affiliate commission
    if user.affiliate_id:
        affiliate = affiliates_db.get(user.affiliate_id)
        if affiliate:
            commission = affiliate.calculate_commission(amount)
            print(f"Affiliate {affiliate.username} earned ${commission:.2f} commission.")

    return transaction

def get_user_info(user_id):
    """Retrieve user information."""
    user = users_db.get(user_id)
    if not user:
        raise UserNotFoundError("User not found.")
    return user

def get_affiliate_info(affiliate_id):
    """Retrieve affiliate information."""
    affiliate = affiliates_db.get(affiliate_id)
    if not affiliate:
        raise UserNotFoundError("Affiliate not found.")
    return affiliate

# Example Usage
if __name__ == "__main__":
    # Register an affiliate
    affiliate = register_affiliate("Affiliate1")
    print(f"Registered Affiliate: {affiliate}")

    # Register a user with affiliate referral
    user = register_user("User1", "user1@example.com", affiliate.affiliate_id)
    print(f"Registered User: {user}")

    # Record transactions
    record_transaction(user.user_id, 600)
    record_transaction(user.user_id, 5000)

    # Retrieve user and affiliate info
    print(get_user_info(user.user_id))
    print(get_affiliate_info(affiliate.affiliate_id))
```
