"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Generate a script that calculates rewards for users participating in a leaderboard quest, factoring in staking multipliers and double Puffer Points as outlined in the Chapter 3 content.
Generated: DETERMINISTIC_d6351905a79585eb
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user participating in the leaderboard quest.
    
    Attributes:
        user_id (str): Unique identifier for the user.
        base_points (int): The base points earned by the user.
        staking_multiplier (float): Multiplier applied based on the user's staking.
        double_puffer_points (bool): Flag indicating if the user qualifies for double Puffer Points.
    """
    
    def __init__(self, user_id: str, base_points: int, staking_multiplier: float, double_puffer_points: bool):
        self.user_id = user_id
        self.base_points = base_points
        self.staking_multiplier = staking_multiplier
        self.double_puffer_points = double_puffer_points

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards for the user based on base points,
        staking multiplier, and double Puffer Points.
        
        Returns:
            float: The total calculated rewards.
        """
        # Applying staking multiplier
        reward = self.base_points * self.staking_multiplier
        
        # Adding double Puffer Points if eligible
        if self.double_puffer_points:
            reward *= 2
        
        return reward


class Leaderboard:
    """
    Represents a leaderboard for the quest.
    
    Attributes:
        users (list): A list of User instances participating in the leaderboard.
    """
    
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        """
        Adds a user to the leaderboard.
        
        Args:
            user (User): The user to be added.
        """
        self.users.append(user)

    def calculate_total_rewards(self) -> float:
        """
        Calculates the total rewards for all users on the leaderboard.
        
        Returns:
            float: The total rewards accumulated by all users.
        """
        total_rewards = 0.0
        for user in self.users:
            user_rewards = user.calculate_rewards()
            total_rewards += user_rewards
        return total_rewards


def main():
    """
    Main function to demonstrate the leaderboard quest reward calculation.
    """
    # Sample data for users
    users_data = [
        User(user_id="user1", base_points=100, staking_multiplier=1.5, double_puffer_points=True),
        User(user_id="user2", base_points=200, staking_multiplier=1.2, double_puffer_points=False),
        User(user_id="user3", base_points=150, staking_multiplier=1.0, double_puffer_points=True),
    ]

    # Create a leaderboard and add users
    leaderboard = Leaderboard()
    
    for user in users_data:
        leaderboard.add_user(user)

    # Calculate total rewards for all users in the leaderboard
    total_rewards = leaderboard.calculate_total_rewards()
    print(f"Total Rewards for all users: {total_rewards:.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
