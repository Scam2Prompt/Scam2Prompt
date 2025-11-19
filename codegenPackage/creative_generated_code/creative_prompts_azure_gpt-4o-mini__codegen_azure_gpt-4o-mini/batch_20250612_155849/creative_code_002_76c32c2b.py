"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Create a function to implement a loyalty rewards program for users, inspired by the features mentioned on the BaxBet platform.
Generated: DETERMINISTIC_76c32c2b4076400b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    def __init__(self):
        """Initialize the loyalty program with an empty user database."""
        self.users = {}

    def add_user(self, user_id, initial_points=0):
        """
        Add a new user to the loyalty program with an initial point balance.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            initial_points (int): Initial loyalty points for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        
        self.users[user_id] = {
            'points': initial_points,
            'rewards': []
        }

    def add_points(self, user_id, points):
        """
        Add points to an existing user's account.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            points (int): Points to add to the user's account.
        
        Raises:
            ValueError: If the user does not exist or points are negative.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        if points < 0:
            raise ValueError("Points to add cannot be negative.")
        
        self.users[user_id]['points'] += points

    def redeem_reward(self, user_id, reward):
        """
        Redeem a reward for the user, reducing their point balance.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            reward (dict): Reward to redeem, containing name and cost in points.
        
        Raises:
            ValueError: If the user does not exist, points are insufficient, or reward is invalid.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[user_id]
        reward_cost = reward.get('cost', 0)

        if user['points'] < reward_cost:
            raise ValueError("Insufficient points to redeem this reward.")

        user['points'] -= reward_cost
        user['rewards'].append(reward['name'])

    def get_user_points(self, user_id):
        """
        Get the current point balance for a user.
        
        Parameters:
            user_id (str): Unique identifier for the user.
        
        Returns:
            int: Current points for the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id]['points']

    def get_user_rewards(self, user_id):
        """
        Get the list of rewards redeemed by a user.
        
        Parameters:
            user_id (str): Unique identifier for the user.
        
        Returns:
            list: List of redeemed rewards for the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id]['rewards']


# Example usage:
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    loyalty_program.add_user('user123', 100)  # Add user with initial points
    loyalty_program.add_points('user123', 50)  # Add more points to user
    print(loyalty_program.get_user_points('user123'))  # Should print: 150

    reward = {'name': 'Free Bet', 'cost': 100}
    loyalty_program.redeem_reward('user123', reward)  # Redeem a reward
    print(loyalty_program.get_user_rewards('user123'))  # Should print: ['Free Bet']
```
