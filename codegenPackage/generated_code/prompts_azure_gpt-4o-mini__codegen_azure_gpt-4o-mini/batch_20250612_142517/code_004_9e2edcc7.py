"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: How can I develop a watch-and-earn feature for a socialfi platform that encourages environmental conservation, inspired by Everyworld?
Generated: DETERMINISTIC_9e2edcc768280e4b
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import List, Dict, Any

class User:
    """Class representing a user in the socialfi platform."""
    
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.earnings = 0.0  # User's earnings from watching content
        self.watch_history: List[Dict[str, Any]] = []  # History of watched content

    def add_earnings(self, amount: float):
        """Add earnings to the user's account."""
        if amount < 0:
            raise ValueError("Earnings amount must be non-negative.")
        self.earnings += amount

    def record_watch(self, content_id: str):
        """Record a watched content."""
        self.watch_history.append({
            'content_id': content_id,
            'timestamp': time.time()
        })

class Content:
    """Class representing content available for users to watch."""
    
    def __init__(self, content_id: str, title: str, base_reward: float):
        self.content_id = content_id
        self.title = title
        self.base_reward = base_reward  # Base reward for watching this content

    def get_reward(self) -> float:
        """Calculate the reward for watching this content."""
        # Simulate a random multiplier for the reward
        multiplier = random.uniform(1.0, 2.0)
        return self.base_reward * multiplier

class WatchAndEarnPlatform:
    """Class representing the watch-and-earn feature of the platform."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user_id
        self.contents: Dict[str, Content] = {}  # Dictionary to store contents by content_id

    def register_user(self, user_id: str, username: str):
        """Register a new user on the platform."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)

    def add_content(self, content_id: str, title: str, base_reward: float):
        """Add new content to the platform."""
        if content_id in self.contents:
            raise ValueError("Content ID already exists.")
        self.contents[content_id] = Content(content_id, title, base_reward)

    def watch_content(self, user_id: str, content_id: str):
        """Simulate a user watching content and earning rewards."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        if content_id not in self.contents:
            raise ValueError("Content not found.")

        user = self.users[user_id]
        content = self.contents[content_id]

        # Simulate watching time
        time.sleep(2)  # Simulate a 2-second watch time

        # Record the watch and calculate earnings
        user.record_watch(content_id)
        reward = content.get_reward()
        user.add_earnings(reward)

        return {
            'user_id': user.user_id,
            'content_id': content.content_id,
            'reward': reward,
            'total_earnings': user.earnings
        }

# Example usage
if __name__ == "__main__":
    platform = WatchAndEarnPlatform()
    
    # Register users
    platform.register_user("1", "Alice")
    platform.register_user("2", "Bob")

    # Add content
    platform.add_content("101", "Protecting Forests", 1.0)
    platform.add_content("102", "Ocean Cleanup", 1.5)

    # Users watch content
    try:
        result = platform.watch_content("1", "101")
        print(result)
        
        result = platform.watch_content("2", "102")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
