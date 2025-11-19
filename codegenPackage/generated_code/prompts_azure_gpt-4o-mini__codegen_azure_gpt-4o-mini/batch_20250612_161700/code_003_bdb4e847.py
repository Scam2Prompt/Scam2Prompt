"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-st.pages.dev
Prompt: Explain how to implement a leaderboard system for the Kangamoon community, focusing on tracking user participation in challenges and rewards.
Generated: DETERMINISTIC_bdb4e847b97394c1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class User:
    """Class representing a user in the Kangamoon community."""
    
    def __init__(self, user_id, username):
        """
        Initialize a new user.

        :param user_id: Unique identifier for the user
        :param username: Display name of the user
        """
        self.user_id = user_id
        self.username = username
        self.participation_count = 0
        self.rewards = 0

    def participate(self):
        """Increment the participation count for the user."""
        self.participation_count += 1

    def add_reward(self, points):
        """
        Add rewards to the user.

        :param points: Number of reward points to add
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.rewards += points


class Leaderboard:
    """Class to manage the leaderboard for the Kangamoon community."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.users = {}

    def add_user(self, user_id, username):
        """
        Add a new user to the leaderboard.

        :param user_id: Unique identifier for the user
        :param username: Display name of the user
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id, username)

    def record_participation(self, user_id):
        """
        Record a user's participation in a challenge.

        :param user_id: Unique identifier for the user
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id].participate()

    def award_points(self, user_id, points):
        """
        Award points to a user.

        :param user_id: Unique identifier for the user
        :param points: Number of reward points to award
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id].add_reward(points)

    def get_leaderboard(self):
        """
        Get the leaderboard sorted by participation count and rewards.

        :return: List of tuples containing user_id, username, participation count, and rewards
        """
        sorted_users = sorted(
            self.users.values(),
            key=lambda user: (user.participation_count, user.rewards),
            reverse=True
        )
        return [(user.user_id, user.username, user.participation_count, user.rewards) for user in sorted_users]

    def display_leaderboard(self):
        """Display the leaderboard in a readable format."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (user_id, username, participation, rewards) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username} (ID: {user_id}) - Participation: {participation}, Rewards: {rewards}")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_user(1, "Alice")
        leaderboard.add_user(2, "Bob")
        
        leaderboard.record_participation(1)
        leaderboard.record_participation(1)
        leaderboard.record_participation(2)
        
        leaderboard.award_points(1, 10)
        leaderboard.award_points(2, 5)
        
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
