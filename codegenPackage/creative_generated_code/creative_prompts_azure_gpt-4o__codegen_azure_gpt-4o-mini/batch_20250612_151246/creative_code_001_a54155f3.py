"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itsnottestingitstestingblockusa.pages.dev
Prompt: Generate code to implement a leaderboard system that updates every minute, displaying user rankings based on credits earned through social media engagement tasks.
Generated: DETERMINISTIC_a54155f390483bdf
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from typing import Dict, List
import random

class User:
    """Class representing a user in the leaderboard."""
    
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.credits = 0

    def earn_credits(self, amount: int):
        """Method to add credits to the user."""
        if amount < 0:
            raise ValueError("Credits earned cannot be negative.")
        self.credits += amount

    def __repr__(self):
        return f"{self.name} (ID: {self.user_id}, Credits: {self.credits})"


class Leaderboard:
    """Class to manage the leaderboard of users."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.update_interval = 60  # Update interval in seconds

    def add_user(self, user_id: str, name: str):
        """Add a new user to the leaderboard."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def update_credits(self):
        """Simulated method to update user credits."""
        for user in self.users.values():
            # Randomly assign new credits between 1 and 10
            user.earn_credits(random.randint(1, 10))

    def get_leaderboard(self) -> List[User]:
        """Return a sorted list of users based on their credits."""
        return sorted(self.users.values(), key=lambda u: u.credits, reverse=True)

    def start_updating(self):
        """Start the leaderboard update thread."""
        threading.Thread(target=self._update_loop, daemon=True).start()

    def _update_loop(self):
        """Background loop that updates credits every minute."""
        while True:
            self.update_credits()
            # Log the updated leaderboard
            print("Leaderboard Update:")
            for user in self.get_leaderboard():
                print(user)
            time.sleep(self.update_interval)


# Example usage:
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        
        # Adding users to the leaderboard
        leaderboard.add_user("1", "Alice")
        leaderboard.add_user("2", "Bob")
        leaderboard.add_user("3", "Charlie")

        # Start the updating process
        leaderboard.start_updating()

        # Keep the main thread alive to observe updates
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
```
