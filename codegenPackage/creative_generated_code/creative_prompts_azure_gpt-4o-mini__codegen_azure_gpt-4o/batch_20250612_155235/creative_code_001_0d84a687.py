"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Explain how to implement a promotional system for an online gambling platform that offers a "100% Bonus New Member" incentive.
Generated: DETERMINISTIC_0d84a68794a299f7
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class GamblingPlatform:
    def __init__(self):
        # Initialize the user database and promotional system
        self.users = {}  # Dictionary to store user data
        self.promotions = []  # List to store promotion details

    def register_user(self, username, initial_deposit):
        """
        Registers a new user on the platform.

        Parameters:
        username (str): The username of the new user.
        initial_deposit (float): Amount deposited by the user during registration.

        Returns:
        str: Registration success message or error.
        """
        if username in self.users:
            return "Error: Username already exists."
        
        if initial_deposit <= 0:
            return "Error: Initial deposit must be greater than zero."

        # Create user account
        self.users[username] = {
            "balance": initial_deposit,
            "registration_date": datetime.datetime.now(),
            "is_new_member": True  # Mark user as new member for promotional eligibility
        }

        # Apply "100% Bonus New Member" promotion
        self.apply_promotion(username, "100% Bonus New Member")

        return f"Success: {username} registered with a balance of ${self.users[username]['balance']}."

    def apply_promotion(self, username, promotion_name):
        """
        Applies a promotion to a user's account.

        Parameters:
        username (str): The username of the user.
        promotion_name (str): The name of the promotion to apply.

        Returns:
        bool: True if promotion applied successfully, False otherwise.
        """
        if username not in self.users:
            return False  # User does not exist

        user = self.users[username]

        # Check if user is eligible for promotion
        if promotion_name == "100% Bonus New Member" and user["is_new_member"]:
            bonus_amount = user["balance"]  # Bonus is 100% of the initial deposit
            user["balance"] += bonus_amount  # Add bonus to user's balance
            user["is_new_member"] = False  # Mark user as no longer eligible for new member promotions

            # Log promotion application
            self.promotions.append({
                "username": username,
                "promotion_name": promotion_name,
                "amount": bonus_amount,
                "date_applied": datetime.datetime.now()
            })
            return True

        return False  # Promotion not applied

    def get_user_balance(self, username):
        """
        Retrieves the balance of a user's account.

        Parameters:
        username (str): The username of the user.

        Returns:
        float: User's current balance or None if user does not exist.
        """
        if username not in self.users:
            return None

        return self.users[username]["balance"]

    def get_promotion_history(self):
        """
        Retrieves the history of applied promotions.

        Returns:
        list: List of promotion details.
        """
        return self.promotions


# Example usage:
if __name__ == "__main__":
    platform = GamblingPlatform()

    # Register a new user and apply promotion
    print(platform.register_user("player1", 100))  # Success: player1 registered with a balance of $200.

    # Check user balance after promotion
    print(f"Player1 Balance: ${platform.get_user_balance('player1')}")  # Player1 Balance: $200

    # Retrieve promotion history
    print("Promotion History:", platform.get_promotion_history())
```

This Python code implements a promotional system for an online gambling platform, providing features such as user registration, promotion application, balance retrieval, and promotion history. It includes proper error handling and adheres to best practices for clean and maintainable code.
