"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Generate code to implement a loyalty program with point accumulation and reward redemption, similar to the nagoya168 system for frequent players.
Generated: DETERMINISTIC_729024e4b2d0602a
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import datetime

class LoyaltyProgram:
    """
    A class to implement a loyalty program for frequent players.
    """
    def __init__(self):
        """
        Initializes the loyalty program with empty user data.
        """
        self.users = {}  # Dictionary to store user data: {user_id: {"points": int, "rewards": list}}

    def register_user(self, user_id):
        """
        Register a new user in the loyalty program.

        :param user_id: str - Unique identifier for the user.
        """
        if user_id not in self.users:
            self.users[user_id] = {"points": 0, "rewards": []}
        else:
            raise ValueError("User is already registered.")

    def add_points(self, user_id, points):
        """
        Add points to a user's account.

        :param user_id: str - Unique identifier for the user.
        :param points: int - Number of points to add.
        """
        if user_id in self.users:
            if points > 0:
                self.users[user_id]["points"] += points
            else:
                raise ValueError("Points to add must be greater than zero.")
        else:
            raise ValueError("User not found.")

    def redeem_reward(self, user_id, reward_name, points_required):
        """
        Redeem a reward for a user if they have enough points.

        :param user_id: str - Unique identifier for the user.
        :param reward_name: str - Name of the reward.
        :param points_required: int - Points required to redeem the reward.
        """
        if user_id in self.users:
            user = self.users[user_id]
            if user["points"] >= points_required:
                # Deduct points and add reward to user's account
                user["points"] -= points_required
                user["rewards"].append({"reward_name": reward_name, "date_redeemed": datetime.datetime.now()})
            else:
                raise ValueError("Insufficient points to redeem the reward.")
        else:
            raise ValueError("User not found.")

    def get_user_data(self, user_id):
        """
        Retrieve the user's data including points and redeemed rewards.

        :param user_id: str - Unique identifier for the user.
        :return: dict - User data containing points and rewards.
        """
        if user_id in self.users:
            return self.users[user_id]
        else:
            raise ValueError("User not found.")

    def display_users(self):
        """
        Display all registered users and their data.

        :return: None
        """
        for user_id, data in self.users.items():
            print(f"User ID: {user_id}, Points: {data['points']}, Rewards: {data['rewards']}")


# Example Usage
if __name__ == "__main__":
    program = LoyaltyProgram()

    try:
        # Register users
        program.register_user("player1")
        program.register_user("player2")

        # Add points
        program.add_points("player1", 100)
        program.add_points("player2", 200)

        # Redeem rewards
        program.redeem_reward("player1", "Free Game", 50)
        program.redeem_reward("player2", "Discount Coupon", 150)

        # Retrieve and display user data
        print(program.get_user_data("player1"))
        print(program.get_user_data("player2"))

        # Display all users
        program.display_users()

    except ValueError as e:
        print(f"Error: {e}")
```
