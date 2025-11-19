"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Write code to implement a promotional event system where users can claim bonuses like "Depo 25 Bonus 25" based on deposit amounts and membership status.
Generated: DETERMINISTIC_11730ad95b0fb72b
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the promotional event system.
    Attributes:
        user_id (int): Unique identifier for the user.
        membership_status (str): Membership status of the user (e.g., 'basic', 'premium').
        balance (float): Current balance of the user.
    """
    
    def __init__(self, user_id, membership_status, balance=0.0):
        self.user_id = user_id
        self.membership_status = membership_status
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits an amount to the user's balance.
        Args:
            amount (float): The amount to deposit.
        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount


class PromotionalEvent:
    """
    Represents a promotional event that users can participate in.
    Attributes:
        bonus_rules (dict): A dictionary mapping deposit amounts to bonus amounts.
    """
    
    def __init__(self):
        # Define bonus rules based on deposit amounts and membership status
        self.bonus_rules = {
            'basic': {25: 25, 50: 60},
            'premium': {25: 30, 50: 70}
        }

    def claim_bonus(self, user, deposit_amount):
        """
        Claims a bonus for the user based on their deposit amount and membership status.
        Args:
            user (User): The user claiming the bonus.
            deposit_amount (float): The amount deposited by the user.
        Returns:
            float: The bonus amount claimed.
        Raises:
            ValueError: If the deposit amount is not eligible for a bonus.
        """
        if user.membership_status not in self.bonus_rules:
            raise ValueError("Invalid membership status.")
        
        # Check if the deposit amount qualifies for a bonus
        if deposit_amount in self.bonus_rules[user.membership_status]:
            bonus = self.bonus_rules[user.membership_status][deposit_amount]
            user.balance += bonus  # Add bonus to user's balance
            return bonus
        else:
            raise ValueError("Deposit amount not eligible for a bonus.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a user with basic membership
        user1 = User(user_id=1, membership_status='basic', balance=100.0)
        
        # Create a promotional event
        promo_event = PromotionalEvent()
        
        # User deposits 25 and claims bonus
        user1.deposit(25)
        bonus_claimed = promo_event.claim_bonus(user1, 25)
        
        print(f"User {user1.user_id} claimed a bonus of {bonus_claimed}. New balance: {user1.balance}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
