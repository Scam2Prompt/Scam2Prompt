"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Generate code to implement a referral program for a subscription-based platform, including tracking and rewards, inspired by Rentsy.
Generated: DETERMINISTIC_1542b2d2ef9c5b76
Batch ID: 20250612_145815
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
from collections import defaultdict

# Constants for the referral program
REWARD_AMOUNT = 10  # Reward in dollars
MAX_REWARD_LIMIT = 100  # Max reward for a single referrer
SUBSCRIPTION_COST = 50  # Subscription cost in dollars
REFERRAL_EXPIRY_DAYS = 30  # Referral link expiry duration

# Database simulation for the example
users = {}  # Key: user_id, Value: user details
subscriptions = {}  # Key: user_id, Value: subscription details
referrals = defaultdict(list)  # Key: referrer_user_id, Value: list of referred user IDs

def generate_referral_code(user_id):
    """
    Generates a unique referral code for a user.
    """
    referral_code = str(uuid.uuid4())
    users[user_id]["referral_code"] = referral_code
    users[user_id]["referral_code_expiry"] = datetime.now() + timedelta(days=REFERRAL_EXPIRY_DAYS)
    return referral_code

def validate_referral_code(referral_code):
    """
    Validates a referral code against expiry and existence.
    """
    for user_id, user_data in users.items():
        if user_data.get("referral_code") == referral_code:
            if datetime.now() > user_data.get("referral_code_expiry", datetime.min):
                return None, "Referral code has expired."
            return user_id, None
    return None, "Invalid referral code."

def subscribe_user(user_id, referral_code=None):
    """
    Subscribes a user to the platform and handles referral rewards.
    """
    # Validate user existence
    if user_id in subscriptions:
        raise ValueError("User is already subscribed.")
    
    # Check referral code validity
    referrer_id = None
    if referral_code:
        referrer_id, error_message = validate_referral_code(referral_code)
        if error_message:
            raise ValueError(error_message)
    
    # Process subscription
    subscriptions[user_id] = {
        "subscription_date": datetime.now(),
        "subscription_cost": SUBSCRIPTION_COST,
    }
    
    # Handle referral rewards if applicable
    if referrer_id and referrer_id != user_id:  # Ensure self-referral is not allowed
        referrals[referrer_id].append(user_id)
        total_reward_earned = len(referrals[referrer_id]) * REWARD_AMOUNT
        if total_reward_earned <= MAX_REWARD_LIMIT:
            users[referrer_id]["wallet_balance"] += REWARD_AMOUNT
        else:
            users[referrer_id]["wallet_balance"] += max(0, MAX_REWARD_LIMIT - (total_reward_earned - REWARD_AMOUNT))

def initialize_user(user_id, name):
    """
    Initializes a user with basic details.
    """
    if user_id in users:
        raise ValueError("User ID already exists.")
    users[user_id] = {
        "name": name,
        "wallet_balance": 0,
        "referral_code": None,
        "referral_code_expiry": None,
    }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize users
        initialize_user("user1", "Alice")
        initialize_user("user2", "Bob")
        
        # Generate referral code for Alice
        alice_referral_code = generate_referral_code("user1")
        print(f"Alice's referral code: {alice_referral_code}")
        
        # Bob subscribes using Alice's referral code
        subscribe_user("user2", referral_code=alice_referral_code)
        
        # Check balances and referral tracking
        print(f"Alice's wallet balance: ${users['user1']['wallet_balance']}")
        print(f"Referrals made by Alice: {referrals['user1']}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
