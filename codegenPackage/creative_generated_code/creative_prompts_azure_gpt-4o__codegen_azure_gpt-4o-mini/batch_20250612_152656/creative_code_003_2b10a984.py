"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gblastclaim.pages.dev
Prompt: Create a leaderboard system using JavaScript or Python that tracks user progress in quests and rewards, similar to the features on the GBlastClaim website.
Generated: DETERMINISTIC_2b10a984c4a4547e
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        """Initialize the leaderboard with an empty data structure."""
        self.user_data = defaultdict(lambda: {'quests_completed': 0, 'rewards_claimed': 0})

    def add_user(self, username):
        """Add a new user to the leaderboard."""
        if username in self.user_data:
            raise ValueError(f"User '{username}' already exists.")
        self.user_data[username] = {'quests_completed': 0, 'rewards_claimed': 0}

    def complete_quest(self, username):
        """Record the completion of a quest by a user."""
        if username not in self.user_data:
            raise ValueError(f"User '{username}' does not exist.")
        self.user_data[username]['quests_completed'] += 1

    def claim_reward(self, username):
        """Record the claiming of a reward by a user."""
        if username not in self.user_data:
            raise ValueError(f"User '{username}' does not exist.")
        self.user_data[username]['rewards_claimed'] += 1

    def get_leaderboard(self):
        """Return the leaderboard sorted by quests completed and rewards claimed."""
        sorted_leaderboard = sorted(
            self.user_data.items(),
            key=lambda item: (item[1]['quests_completed'], item[1]['rewards_claimed']),
            reverse=True
        )
        return sorted_leaderboard

    def to_json(self):
        """Return the leaderboard data as a JSON string."""
        return json.dumps(self.user_data, indent=4)

    def from_json(self, json_str):
        """Load leaderboard data from a JSON string."""
        try:
            self.user_data = json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data provided.") from e

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    try:
        leaderboard.add_user("Alice")
        leaderboard.add_user("Bob")
        leaderboard.complete_quest("Alice")
        leaderboard.claim_reward("Alice")
        leaderboard.complete_quest("Bob")

        print("Current Leaderboard:")
        for user, data in leaderboard.get_leaderboard():
            print(f"{user}: Quests Completed - {data['quests_completed']}, Rewards Claimed - {data['rewards_claimed']}")

        # Export to JSON
        json_data = leaderboard.to_json()
        print("\nLeaderboard JSON:")
        print(json_data)

        # Load from JSON
        leaderboard.from_json(json_data)

    except ValueError as e:
        print(f"An error occurred: {e}")
```
