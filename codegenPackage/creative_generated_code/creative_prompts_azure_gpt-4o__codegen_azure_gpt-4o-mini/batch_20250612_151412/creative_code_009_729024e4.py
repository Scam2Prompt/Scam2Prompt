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
class LoyaltyProgram:
    """
    A class to represent a loyalty program for customers to accumulate points
    and redeem rewards based on their activities.
    """

    def __init__(self):
        """
        Initialize a new Loyalty Program with an empty user database.
        """
        self.users = {}  # Store user data as a dictionary with user_id as key

    def add_user(self, user_id):
        """
        Add a new user to the loyalty program.

        Args:
            user_id (str): Unique identifier for the user. Must be unique.

        Raises:
            ValueError: If the user already exists in the program.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = {'points': 0, 'rewards': []}
        print(f"User {user_id} added successfully.")

    def accumulate_points(self, user_id, points):
        """
        Accumulate points for a user.

        Args:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to add.

        Raises:
            ValueError: If the user does not exist or if points are negative.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if points < 0:
            raise ValueError("Points to accumulate cannot be negative.")
        
        self.users[user_id]['points'] += points
        print(f"{points} points added to user {user_id}. Total points: {self.users[user_id]['points']}.")

    def redeem_reward(self, user_id, reward, cost):
        """
        Redeem a reward for a user if they have enough points.

        Args:
            user_id (str): Unique identifier for the user.
            reward (str): Description of the reward.
            cost (int): Number of points required to redeem the reward.

        Raises:
            ValueError: If the user does not exist, if points are insufficient,
                        or if the cost is negative.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if cost < 0:
            raise ValueError("Cost of reward cannot be negative.")
        if self.users[user_id]['points'] < cost:
            raise ValueError(f"User {user_id} does not have enough points to redeem {reward}.")

        self.users[user_id]['points'] -= cost
        self.users[user_id]['rewards'].append(reward)
        print(f"Reward '{reward}' redeemed for user {user_id}. Points remaining: {self.users[user_id]['points']}.")

    def get_user_info(self, user_id):
        """
        Retrieve user information including points and redeemed rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary containing the user's points and redeemed rewards.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return self.users[user_id]

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    try:
        loyalty_program.add_user("user123")
        loyalty_program.accumulate_points("user123", 100)
        loyalty_program.redeem_reward("user123", "Free Coffee", 50)
        user_info = loyalty_program.get_user_info("user123")
        print(user_info)
    except ValueError as e:
        print(f"Error: {e}")
```
