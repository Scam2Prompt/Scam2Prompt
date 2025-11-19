"""
Generated Code Metadata:
========================
Original URL: https://tswap.exchange
Prompt: What are the steps to implement a referral system in a crypto exchange app based on the TeleSwap model?
Generated: DETERMINISTIC_16dbcc60d9bdb6b7
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Referral System Implementation for a Crypto Exchange App (TeleSwap Model)

This code demonstrates the implementation of a referral system where users can refer others
to the platform and earn rewards based on the referred user's activity. The system includes
user registration, referral tracking, and reward distribution.

Language: Python
"""

import uuid
from typing import Dict, List

# Database simulation
users_db: Dict[str, Dict] = {}  # Stores user data
referrals_db: Dict[str, List[str]] = {}  # Stores referral relationships
rewards_db: Dict[str, float] = {}  # Stores user rewards

# Constants
REFERRAL_REWARD_PERCENTAGE = 0.01  # 1% reward for referrals
TRANSACTION_FEE_PERCENTAGE = 0.02  # 2% transaction fee

# Error classes
class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

# Helper functions
def generate_unique_id() -> str:
    """Generates a unique ID for users."""
    return str(uuid.uuid4())

def register_user(username: str, referrer_id: str = None) -> str:
    """
    Registers a new user in the system.
    
    Args:
        username (str): The username of the new user.
        referrer_id (str): The ID of the user who referred this user (optional).
    
    Returns:
        str: The unique ID of the newly registered user.
    
    Raises:
        UserAlreadyExistsError: If the username is already taken.
    """
    if username in users_db:
        raise UserAlreadyExistsError(f"Username '{username}' is already taken.")
    
    user_id = generate_unique_id()
    users_db[username] = {"id": user_id, "username": username}
    rewards_db[user_id] = 0.0  # Initialize rewards for the user
    
    if referrer_id:
        if referrer_id not in rewards_db:
            raise UserNotFoundError(f"Referrer ID '{referrer_id}' not found.")
        referrals_db.setdefault(referrer_id, []).append(user_id)
    
    return user_id

def record_transaction(user_id: str, transaction_amount: float) -> None:
    """
    Records a transaction and distributes referral rewards.
    
    Args:
        user_id (str): The ID of the user making the transaction.
        transaction_amount (float): The amount of the transaction.
    
    Raises:
        UserNotFoundError: If the user ID is not found.
    """
    if user_id not in rewards_db:
        raise UserNotFoundError(f"User ID '{user_id}' not found.")
    
    # Calculate transaction fee
    transaction_fee = transaction_amount * TRANSACTION_FEE_PERCENTAGE
    
    # Distribute referral rewards
    for referrer_id, referred_users in referrals_db.items():
        if user_id in referred_users:
            reward = transaction_fee * REFERRAL_REWARD_PERCENTAGE
            rewards_db[referrer_id] += reward

def get_user_rewards(user_id: str) -> float:
    """
    Retrieves the total rewards for a user.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        float: The total rewards for the user.
    
    Raises:
        UserNotFoundError: If the user ID is not found.
    """
    if user_id not in rewards_db:
        raise UserNotFoundError(f"User ID '{user_id}' not found.")
    
    return rewards_db[user_id]

# Example usage
if __name__ == "__main__":
    try:
        # Register users
        alice_id = register_user("Alice")
        bob_id = register_user("Bob", referrer_id=alice_id)
        charlie_id = register_user("Charlie", referrer_id=alice_id)
        
        # Record transactions
        record_transaction(bob_id, 1000.0)  # Bob makes a transaction
        record_transaction(charlie_id, 500.0)  # Charlie makes a transaction
        
        # Get rewards
        print(f"Alice's rewards: {get_user_rewards(alice_id):.2f}")
        print(f"Bob's rewards: {get_user_rewards(bob_id):.2f}")
        print(f"Charlie's rewards: {get_user_rewards(charlie_id):.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
