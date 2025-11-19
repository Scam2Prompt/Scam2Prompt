"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Suggest a method to implement a personalized feed algorithm for a content discovery platform, ensuring it aligns with the ad-free experience highlighted on the Stumble! ® site.
Generated: DETERMINISTIC_671a909924c0e41b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from scipy import spatial
from typing import Dict, List

class User:
    """Represents a user with their preferences."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.interests: List[str] = []
        self.engaged_content: List[int] = []

class Content:
    """Represents a piece of content."""
    def __init__(self, content_id: int, categories: List[str]):
        self.content_id = content_id
        self.categories = categories

class PersonalizedFeed:
    """Implements a personalized feed algorithm."""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.content: Dict[int, Content] = {}

    def add_user(self, user_id: int):
        """Adds a new user."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_content(self, content_id: int, categories: List[str]):
        """Adds new content."""
        if content_id not in self.content:
            self.content[content_id] = Content(content_id, categories)

    def update_user_interests(self, user_id: int, interests: List[str]):
        """Updates a user's interests."""
        if user_id in self.users:
            self.users[user_id].interests = interests

    def log_user_engagement(self, user_id: int, content_id: int):
        """Logs user engagement with content."""
        if user_id in self.users:
            self.users[user_id].engaged_content.append(content_id)

    def _calculate_similarity(self, user_interests: List[str], content_categories: List[str]):
        """Calculates the similarity between user interests and content categories."""
        user_vector = np.array([int(interest in user_interests) for interest in set(user_interests + content_categories)])
        content_vector = np.array([int(category in user_interests) for category in set(user_interests + content_categories)])
        return 1 - spatial.distance.cosine(user_vector, content_vector)

    def _rank_content(self, user_id: int):
        """Ranks content for a user based on their interests and engagement."""
        if user_id not in self.users:
            return []

        user = self.users[user_id]
        ranked_content = []

        for content_id, content in self.content.items():
            if content_id not in user.engaged_content:
                similarity = self._calculate_similarity(user.interests, content.categories)
                ranked_content.append((content_id, similarity))

        ranked_content.sort(key=lambda x: x[1], reverse=True)
        return [content_id for content_id, _ in ranked_content]

    def get_personalized_feed(self, user_id: int, num_items: int = 10):
        """Generates a personalized feed for a user."""
        try:
            ranked_content = self._rank_content(user_id)
            return ranked_content[:num_items]
        except Exception as e:
            print(f"Error generating personalized feed: {e}")
            return []

# Example usage
if __name__ == "__main__":
    feed = PersonalizedFeed()

    # Add users
    feed.add_user(1)
    feed.add_user(2)

    # Add content
    feed.add_content(1, ["tech", "programming"])
    feed.add_content(2, ["fashion", "lifestyle"])
    feed.add_content(3, ["tech", "gaming"])

    # Update user interests
    feed.update_user_interests(1, ["tech", "programming"])
    feed.update_user_interests(2, ["fashion", "lifestyle"])

    # Log user engagement
    feed.log_user_engagement(1, 1)

    # Generate personalized feed
    print(feed.get_personalized_feed(1))
    print(feed.get_personalized_feed(2))
```
