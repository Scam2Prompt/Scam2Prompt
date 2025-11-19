"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: "Create a basic gamification system using IQRA Token for educational games and quizzes, and describe how to integrate it with the token's existing infrastructure."
Generated: DETERMINISTIC_ab7b4245cf8ec99f
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gamification_system.py

class IQRAToken:
    """
    A class to represent the IQRA Token for gamification.
    This class handles token balance and transactions.
    """

    def __init__(self):
        self.balances = {}

    def add_user(self, user_id):
        """Add a new user with an initial balance of 0 tokens."""
        if user_id not in self.balances:
            self.balances[user_id] = 0
        else:
            raise ValueError("User already exists.")

    def award_tokens(self, user_id, amount):
        """Award tokens to a user."""
        if user_id not in self.balances:
            raise ValueError("User does not exist.")
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.balances[user_id] += amount

    def deduct_tokens(self, user_id, amount):
        """Deduct tokens from a user."""
        if user_id not in self.balances:
            raise ValueError("User does not exist.")
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if self.balances[user_id] < amount:
            raise ValueError("Insufficient balance.")
        self.balances[user_id] -= amount

    def get_balance(self, user_id):
        """Get the current token balance of a user."""
        if user_id not in self.balances:
            raise ValueError("User does not exist.")
        return self.balances[user_id]


class GamificationSystem:
    """
    A class to represent the gamification system for educational games and quizzes.
    This class manages user interactions and token transactions.
    """

    def __init__(self):
        self.token_system = IQRAToken()

    def register_user(self, user_id):
        """Register a new user in the gamification system."""
        try:
            self.token_system.add_user(user_id)
            print(f"User {user_id} registered successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def complete_quiz(self, user_id, score):
        """Award tokens based on quiz completion and score."""
        try:
            # Example: 10 tokens for completion + 1 token for each point scored
            tokens_awarded = 10 + score
            self.token_system.award_tokens(user_id, tokens_awarded)
            print(f"Awarded {tokens_awarded} tokens to {user_id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def redeem_tokens(self, user_id, amount):
        """Redeem tokens for rewards."""
        try:
            self.token_system.deduct_tokens(user_id, amount)
            print(f"{user_id} redeemed {amount} tokens.")
        except ValueError as e:
            print(f"Error: {e}")

    def check_balance(self, user_id):
        """Check the token balance of a user."""
        try:
            balance = self.token_system.get_balance(user_id)
            print(f"{user_id} has {balance} tokens.")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    gamification = GamificationSystem()
    
    # Register users
    gamification.register_user("user1")
    gamification.register_user("user2")

    # Complete quizzes
    gamification.complete_quiz("user1", 5)  # User1 scores 5 points
    gamification.complete_quiz("user2", 3)  # User2 scores 3 points

    # Check balances
    gamification.check_balance("user1")
    gamification.check_balance("user2")

    # Redeem tokens
    gamification.redeem_tokens("user1", 12)  # User1 redeems 12 tokens
    gamification.check_balance("user1")
```
