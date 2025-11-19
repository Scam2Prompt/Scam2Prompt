"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Write a code example for implementing a bonus system in a betting application that mimics the Parimatch bonus offerings for new users.
Generated: DETERMINISTIC_ff03cc8a30645c3c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BonusSystem:
    def __init__(self):
        # Initialize a dictionary to store user bonuses
        self.user_bonuses = {}

    def add_user(self, user_id):
        """Add a new user with a default bonus of 0."""
        if user_id in self.user_bonuses:
            raise ValueError(f"User {user_id} already exists.")
        self.user_bonuses[user_id] = 0.0

    def apply_bonus(self, user_id, bonus_amount):
        """Apply a bonus to a user's account."""
        if user_id not in self.user_bonuses:
            raise ValueError(f"User {user_id} does not exist.")
        if bonus_amount <= 0:
            raise ValueError("Bonus amount must be greater than zero.")
        
        self.user_bonuses[user_id] += bonus_amount

    def get_bonus(self, user_id):
        """Retrieve the current bonus for a user."""
        if user_id not in self.user_bonuses:
            raise ValueError(f"User {user_id} does not exist.")
        
        return self.user_bonuses[user_id]

    def reset_bonus(self, user_id):
        """Reset the bonus for a user to zero."""
        if user_id not in self.user_bonuses:
            raise ValueError(f"User {user_id} does not exist.")
        
        self.user_bonuses[user_id] = 0.0

    def display_bonuses(self):
        """Display all user bonuses."""
        for user_id, bonus in self.user_bonuses.items():
            print(f"User ID: {user_id}, Bonus: {bonus:.2f}")

# Example usage
if __name__ == "__main__":
    bonus_system = BonusSystem()
    
    # Adding users
    try:
        bonus_system.add_user("user123")
        bonus_system.add_user("user456")
        
        # Applying bonuses
        bonus_system.apply_bonus("user123", 50.0)
        bonus_system.apply_bonus("user456", 30.0)
        
        # Displaying bonuses
        bonus_system.display_bonuses()
        
        # Resetting a bonus
        bonus_system.reset_bonus("user123")
        
        # Displaying bonuses after reset
        bonus_system.display_bonuses()
        
    except ValueError as e:
        print(f"Error: {e}")
```
