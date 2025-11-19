"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Design a leaderboard system for the Tari Airdrop Game, tracking user scores and rewards, including gems, turtle shells, and sky hammers.
Generated: DETERMINISTIC_6c5910beecbce3d4
Batch ID: 20250622_204712
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
    Class to represent a user in the Tari Airdrop Game.
    Each user has a unique ID, a score, and rewards.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.score = 0
        self.rewards = {
            'gems': 0,
            'turtle_shells': 0,
            'sky_hammers': 0
        }

    def update_score(self, points):
        """
        Update the user's score by adding the given points.
        :param points: int - Points to add to the user's score.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points

    def add_reward(self, reward_type, amount):
        """
        Add a specified amount of a reward to the user's rewards.
        :param reward_type: str - Type of reward to add ('gems', 'turtle_shells', 'sky_hammers').
        :param amount: int - Amount of the reward to add.
        """
        if reward_type not in self.rewards:
            raise ValueError("Invalid reward type.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.rewards[reward_type] += amount


class Leaderboard:
    """
    Class to manage the leaderboard for the Tari Airdrop Game.
    It tracks users and their scores.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        """
        Add a new user to the leaderboard.
        :param user_id: str - Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def update_user_score(self, user_id, points):
        """
        Update the score of a user.
        :param user_id: str - Unique identifier for the user.
        :param points: int - Points to add to the user's score.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id].update_score(points)

    def add_user_reward(self, user_id, reward_type, amount):
        """
        Add a reward to a user's account.
        :param user_id: str - Unique identifier for the user.
        :param reward_type: str - Type of reward to add.
        :param amount: int - Amount of the reward to add.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id].add_reward(reward_type, amount)

    def get_leaderboard(self):
        """
        Get the leaderboard sorted by user scores in descending order.
        :return: list of tuples - List of (user_id, score) sorted by score.
        """
        return sorted(
            [(user_id, user.score) for user_id, user in self.users.items()],
            key=lambda x: x[1],
            reverse=True
        )

    def get_user_rewards(self, user_id):
        """
        Get the rewards of a specific user.
        :param user_id: str - Unique identifier for the user.
        :return: dict - User's rewards.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id].rewards


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding users
    leaderboard.add_user("user1")
    leaderboard.add_user("user2")

    # Updating scores
    leaderboard.update_user_score("user1", 100)
    leaderboard.update_user_score("user2", 150)

    # Adding rewards
    leaderboard.add_user_reward("user1", "gems", 10)
    leaderboard.add_user_reward("user2", "turtle_shells", 5)

    # Displaying leaderboard
    print("Leaderboard:")
    for user_id, score in leaderboard.get_leaderboard():
        print(f"User: {user_id}, Score: {score}")

    # Displaying user rewards
    print("User1 Rewards:", leaderboard.get_user_rewards("user1"))
    print("User2 Rewards:", leaderboard.get_user_rewards("user2"))
```
