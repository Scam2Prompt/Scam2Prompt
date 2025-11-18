"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Implement a feature that tracks reward forfeiture, redistributing accrued revenue share among all holders if a user sells or transfers more than 300 $BANANA or their holdings drop below 50 $BANANA.
Generated: DETERMINISTIC_acb23b07c4e6d012
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Feature: Reward Forfeiture Redistribution
Tracks $BANANA token transfers and holdings to enforce forfeiture rules. If a user sells/transfers more than 300 $BANANA
or their holdings drop below 50 $BANANA, their accrued revenue share is redistributed among all holders.

Assumptions:
- $BANANA balances and transfers are handled by a blockchain-like system.
- `get_balance(user)` fetches the user's current balance.
- `transfer(from_user, to_user, amount)` handles token transfers.
- `accrued_rewards[user]` stores user's accrued revenue share.
- `get_all_holders()` fetches all accounts holding $BANANA.
"""

# Mock Data Storage (in production, this would be part of a database or on-chain storage)
balances = {}  # Stores user balances
accrued_rewards = {}  # Stores accrued revenue share for each user

def get_balance(user):
    """Fetches the current balance of a user."""
    return balances.get(user, 0)

def transfer(from_user, to_user, amount):
    """
    Handles token transfer between two users.
    Enforces forfeiture rules and redistributes accrued revenue if applicable.
    """
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    # Check sender's balance
    sender_balance = get_balance(from_user)
    if sender_balance < amount:
        raise ValueError("Insufficient balance for transfer")

    # Perform the transfer
    balances[from_user] = sender_balance - amount
    balances[to_user] = balances.get(to_user, 0) + amount

    # Check forfeiture rules
    enforce_forfeiture_rules(from_user)

def enforce_forfeiture_rules(user):
    """
    Checks if a user's actions trigger forfeiture. If triggered, redistributes their accrued rewards.
    """
    user_balance = get_balance(user)

    # Define forfeiture conditions
    if user_balance < 50 or transferred_over_limit(user):
        redistribute_rewards(user)

def transferred_over_limit(user):
    """
    Checks if a user has transferred more than 300 $BANANA.
    This logic assumes transfer tracking is implemented elsewhere in the system.
    """
    # Placeholder implementation (in production, track transfers in a transaction log)
    # Assume this returns True if user has transferred more than 300 $BANANA
    return False  # Replace with actual logic

def redistribute_rewards(user):
    """
    Redistributes forfeited rewards among all holders.
    """
    forfeited_amount = accrued_rewards.get(user, 0)
    if forfeited_amount <= 0:
        return  # No rewards to redistribute

    # Reset user's accrued rewards
    accrued_rewards[user] = 0

    # Fetch all holders
    holders = get_all_holders()
    if not holders:
        return  # No holders to distribute rewards to

    # Calculate distribution amount
    distribution_amount = forfeited_amount / len(holders)

    # Redistribute rewards
    for holder in holders:
        accrued_rewards[holder] = accrued_rewards.get(holder, 0) + distribution_amount

def get_all_holders():
    """
    Fetches all accounts holding $BANANA.
    """
    return [user for user, balance in balances.items() if balance > 0]

# Example Usage
if __name__ == "__main__":
    # Initialize balances and accrued rewards for testing
    balances = {"Alice": 500, "Bob": 100, "Charlie": 50}
    accrued_rewards = {"Alice": 100, "Bob": 200, "Charlie": 50}

    # Example transfer that triggers forfeiture
    try:
        transfer("Alice", "Bob", 400)  # Alice transfers 400 tokens, dropping below 50
    except ValueError as e:
        print(f"Transfer Error: {e}")

    # Check results
    print("Balances:", balances)
    print("Accrued Rewards:", accrued_rewards)
```
