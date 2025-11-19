"""
Generated Code Metadata:
========================
Original URL: https://gift-mantra.net
Prompt: Write Python code to create a personalized feed system that filters web content based on user preferences, similar to the functionality described in Stumble! ®.
Generated: DETERMINISTIC_3de6beff7dae762a
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class Content:
    """Class representing a piece of content."""
    
    def __init__(self, title: str, category: str, tags: List[str]):
        self.title = title
        self.category = category
        self.tags = tags

    def __repr__(self) -> str:
        return f"Content(title={self.title}, category={self.category}, tags={self.tags})"


class User:
    """Class representing a user with preferences."""
    
    def __init__(self, username: str, preferences: List[str]):
        self.username = username
        self.preferences = preferences

    def __repr__(self) -> str:
        return f"User(username={self.username}, preferences={self.preferences})"


class FeedSystem:
    """Class to manage the personalized feed system."""
    
    def __init__(self):
        self.contents: List[Content] = []
        self.users: Dict[str, User] = {}

    def add_content(self, content: Content) -> None:
        """Add new content to the system."""
        self.contents.append(content)

    def register_user(self, user: User) -> None:
        """Register a new user in the system."""
        self.users[user.username] = user

    def filter_content(self, user: User) -> List[Content]:
        """Filter content based on user preferences."""
        filtered_content = [
            content for content in self.contents
            if any(tag in user.preferences for tag in content.tags)
        ]
        return filtered_content

    def get_personalized_feed(self, username: str) -> List[Content]:
        """Get a personalized feed for a user."""
        user = self.users.get(username)
        if not user:
            raise ValueError(f"User '{username}' not found.")
        
        filtered_content = self.filter_content(user)
        if not filtered_content:
            raise ValueError(f"No content found for user '{username}' based on preferences.")
        
        # Randomly select a subset of content for the feed
        return random.sample(filtered_content, min(5, len(filtered_content)))


# Example usage
if __name__ == "__main__":
    # Create a feed system instance
    feed_system = FeedSystem()

    # Add some content
    feed_system.add_content(Content("Python Programming", "Education", ["programming", "python"]))
    feed_system.add_content(Content("Travel Tips", "Lifestyle", ["travel", "lifestyle"]))
    feed_system.add_content(Content("Healthy Recipes", "Food", ["food", "health"]))
    feed_system.add_content(Content("Machine Learning Basics", "Education", ["programming", "machine learning"]))
    feed_system.add_content(Content("Top 10 Travel Destinations", "Travel", ["travel", "adventure"]))

    # Register a user with preferences
    user = User("john_doe", ["programming", "travel"])
    feed_system.register_user(user)

    # Get personalized feed for the user
    try:
        personalized_feed = feed_system.get_personalized_feed("john_doe")
        print("Personalized Feed for john_doe:")
        for content in personalized_feed:
            print(content)
    except ValueError as e:
        print(e)
```
