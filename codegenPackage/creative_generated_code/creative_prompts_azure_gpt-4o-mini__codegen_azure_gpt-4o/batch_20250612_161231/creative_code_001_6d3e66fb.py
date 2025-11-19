"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rocketpool.club
Prompt: How can I implement a referral program in my application similar to Rocket Pool's affiliate program, including commission structures for direct and indirect referrals?
Generated: DETERMINISTIC_6d3e66fb2cef7692
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation
This script demonstrates a referral program with direct and indirect commission structures.
It uses Python for simplicity and assumes a relational database-like structure for storing
users and their referral relationships.

Key Features:
1. Direct and indirect commission structures.
2. Error handling for invalid user cases.
3. Modular and extensible design.
"""

from typing import List, Dict

# Mock database structure for users and their referral relationships
users_db = {
    "user1": {"referrer": None, "balance": 0},
    "user2": {"referrer": "user1", "balance": 0},
    "user3": {"referrer": "user2", "balance": 0},
}

# Commission rate configuration
COMMISSION_RATES = {
    "direct": 0.10,  # 10% commission for direct referrals
    "indirect": 0.05,  # 5% commission for indirect referrals
}

# Error messages
class ReferralProgramError(Exception):
    pass

def validate_user(user_id: str) -> None:
    """
    Validates if a user exists in the database.
    :param user_id: User ID to validate.
    :raises ReferralProgramError: If user ID does not exist in the database.
    """
    if user_id not in users_db:
        raise ReferralProgramError(f"User '{user_id}' does not exist.")

def record_transaction(user_id: str, amount: float) -> None:
    """
    Records a transaction for a user and distributes referral commissions.
    :param user_id: The ID of the user making the transaction.
    :param amount: The transaction amount.
    """
    validate_user(user_id)
    
    # Record transaction for the user
    users_db[user_id]["balance"] += amount
    
    # Calculate commission for referrers
    distribute_commissions(user_id, amount)

def distribute_commissions(user_id: str, amount: float) -> None:
    """
    Distributes commissions to the direct and indirect referrers.
    :param user_id: The ID of the user making the transaction.
    :param amount: The transaction amount.
    """
    direct_referrer = users_db[user_id]["referrer"]
    if direct_referrer:
        validate_user(direct_referrer)
        direct_commission = amount * COMMISSION_RATES["direct"]
        users_db[direct_referrer]["balance"] += direct_commission
        
        # Check for indirect referrer (referrer's referrer)
        indirect_referrer = users_db[direct_referrer]["referrer"]
        if indirect_referrer:
            validate_user(indirect_referrer)
            indirect_commission = amount * COMMISSION_RATES["indirect"]
            users_db[indirect_referrer]["balance"] += indirect_commission

def get_user_balance(user_id: str) -> float:
    """
    Retrieves the balance of a user.
    :param user_id: The ID of the user.
    :return: The user's balance.
    """
    validate_user(user_id)
    return users_db[user_id]["balance"]

if __name__ == "__main__":
    # Example usage: Recording transactions and checking balances
    try:
        print("Initial balances:")
        for user, data in users_db.items():
            print(f"{user}: {data['balance']}")
        
        # Record a transaction for user3
        record_transaction("user3", 100)
        
        print("\nBalances after user3's transaction:")
        for user, data in users_db.items():
            print(f"{user}: {data['balance']}")
    except ReferralProgramError as e:
        print(f"Error: {e}")
```
