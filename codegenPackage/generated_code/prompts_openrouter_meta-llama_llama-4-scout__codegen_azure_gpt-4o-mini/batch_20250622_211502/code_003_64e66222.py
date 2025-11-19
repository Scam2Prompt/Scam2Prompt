"""
Generated Code Metadata:
========================
Original URL: https://1xfa.club
Prompt: Design a loyalty program with rewards and cashback features, similar to BaxBet's, using a programming language of your choice.
Generated: DETERMINISTIC_64e66222184e5abf
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoyaltyProgram:
    def __init__(self):
        """Initialize the loyalty program with empty user data."""
        self.users = {}

    def add_user(self, user_id):
        """Add a new user to the loyalty program.

        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = {'points': 0, 'cashback': 0.0}

    def add_points(self, user_id, points):
        """Add loyalty points to a user's account.

        Args:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to add.

        Raises:
            ValueError: If the user does not exist or points are negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        
        self.users[user_id]['points'] += points

    def redeem_points(self, user_id, points):
        """Redeem loyalty points for rewards.

        Args:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to redeem.

        Raises:
            ValueError: If the user does not exist, points are negative, or insufficient points.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        if self.users[user_id]['points'] < points:
            raise ValueError("Insufficient points to redeem.")

        self.users[user_id]['points'] -= points
        return f"Redeemed {points} points for user {user_id}."

    def add_cashback(self, user_id, amount):
        """Add cashback to a user's account.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of cashback to add.

        Raises:
            ValueError: If the user does not exist or amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if amount < 0:
            raise ValueError("Cashback amount cannot be negative.")
        
        self.users[user_id]['cashback'] += amount

    def redeem_cashback(self, user_id, amount):
        """Redeem cashback for a user.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of cashback to redeem.

        Raises:
            ValueError: If the user does not exist, amount is negative, or insufficient cashback.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if amount < 0:
            raise ValueError("Cashback amount cannot be negative.")
        if self.users[user_id]['cashback'] < amount:
            raise ValueError("Insufficient cashback to redeem.")

        self.users[user_id]['cashback'] -= amount
        return f"Redeemed ${amount} cashback for user {user_id}."

    def get_user_info(self, user_id):
        """Retrieve the loyalty information for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: User's loyalty information.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        return self.users[user_id]

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    loyalty_program.add_user("user123")
    loyalty_program.add_points("user123", 100)
    loyalty_program.add_cashback("user123", 20.0)
    
    print(loyalty_program.get_user_info("user123"))
    print(loyalty_program.redeem_points("user123", 50))
    print(loyalty_program.redeem_cashback("user123", 10.0))
    print(loyalty_program.get_user_info("user123"))
```
