"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-stores.pages.dev
Prompt: Illustrate how to implement a rewards program using Pushd tokens, detailing the steps for user engagement and participation.
Generated: DETERMINISTIC_4f14275f2178b687
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_program.py

class User:
    def __init__(self, user_id, name):
        """
        Initialize a new user.

        :param user_id: Unique identifier for the user
        :param name: The name of the user
        """
        self.user_id = user_id
        self.name = name
        self.tokens = 0  # Initialize tokens to zero

    def earn_tokens(self, amount):
        """
        Earn tokens for a user.

        :param amount: Number of tokens to earn
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.tokens += amount
        print(f"{self.name} earned {amount} tokens. Total tokens: {self.tokens}")

    def redeem_tokens(self, amount):
        """
        Redeem tokens for a user.

        :param amount: Number of tokens to redeem
        :raises ValueError: If the amount exceeds available tokens
        """
        if amount > self.tokens:
            raise ValueError("Insufficient tokens to redeem")
        self.tokens -= amount
        print(f"{self.name} redeemed {amount} tokens. Remaining tokens: {self.tokens}")


class RewardsProgram:
    def __init__(self):
        """
        Initialize the rewards program.
        """
        self.users = {}  # Dictionary to store users by user_id

    def add_user(self, user_id, name):
        """
        Add a new user to the rewards program.

        :param user_id: Unique identifier for the user
        :param name: The name of the user
        :raises ValueError: If user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = User(user_id, name)
        print(f"User {name} added with ID {user_id}.")

    def engage_user(self, user_id, action, amount=0):
        """
        Engage a user in the rewards program through actions like earning or redeeming tokens.

        :param user_id: Unique identifier for the user
        :param action: The action to perform ('earn' or 'redeem')
        :param amount: Number of tokens to earn or redeem
        :raises KeyError: If user_id does not exist
        :raises ValueError: If action is invalid
        """
        if user_id not in self.users:
            raise KeyError(f"User ID {user_id} not found.")

        user = self.users[user_id]
        
        if action == 'earn':
            user.earn_tokens(amount)
        elif action == 'redeem':
            user.redeem_tokens(amount)
        else:
            raise ValueError("Invalid action. Use 'earn' or 'redeem'.")


# Example usage of the RewardsProgram
if __name__ == "__main__":
    rewards_program = RewardsProgram()

    try:
        # Adding users
        rewards_program.add_user(1, "Alice")
        rewards_program.add_user(2, "Bob")

        # Engaging users
        rewards_program.engage_user(1, 'earn', 50)   # Alice earns tokens
        rewards_program.engage_user(2, 'earn', 30)   # Bob earns tokens
        rewards_program.engage_user(1, 'redeem', 20)  # Alice redeems tokens

        # Attempting to redeem more tokens than available
        rewards_program.engage_user(2, 'redeem', 40)  # This will raise an error

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
