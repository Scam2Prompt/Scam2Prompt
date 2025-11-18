"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Suggest a method to implement a personalized feed algorithm for a content discovery platform, ensuring it aligns with the ad-free experience highlighted on the Stumble! ® site.
Generated: DETERMINISTIC_671a909924c0e41b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Content:
    """Represents a piece of content."""
    
    def __init__(self, content_id: str, category: str, tags: List[str], score: float):
        self.content_id = content_id
        self.category = category
        self.tags = tags
        self.score = score

class User:
    """Represents a user with preferences and history."""
    
    def __init__(self, user_id: str, preferences: List[str], history: List[str]):
        self.user_id = user_id
        self.preferences = preferences  # User's preferred categories
        self.history = history  # Previously viewed content IDs

class PersonalizedFeed:
    """Generates a personalized content feed for a user."""
    
    def __init__(self, contents: List[Content]):
        self.contents = contents  # List of available contents

    def filter_content(self, user: User) -> List[Content]:
        """
        Filters the content based on user preferences and history.
        
        :param user: The user object containing preferences and history.
        :return: A list of filtered content.
        """
        filtered = [
            content for content in self.contents
            if content.category in user.preferences and content.content_id not in user.history
        ]
        return filtered

    def rank_content(self, filtered_content: List[Content]) -> List[Content]:
        """
        Ranks the filtered content based on their scores.
        
        :param filtered_content: The list of filtered content.
        :return: A list of ranked content.
        """
        return sorted(filtered_content, key=lambda x: x.score, reverse=True)

    def generate_feed(self, user: User, limit: int = 10) -> List[Content]:
        """
        Generates a personalized feed for the user.
        
        :param user: The user object.
        :param limit: The maximum number of content items to return.
        :return: A list of content for the personalized feed.
        """
        try:
            filtered_content = self.filter_content(user)
            ranked_content = self.rank_content(filtered_content)
            personalized_feed = ranked_content[:limit]
            return personalized_feed
        except Exception as e:
            print(f"Error generating feed: {e}")
            return []  # Return an empty list in case of error

# Example usage:
if __name__ == "__main__":
    # Sample contents
    contents = [
        Content("1", "Technology", ["AI", "Innovation"], 9.0),
        Content("2", "Health", ["Fitness", "Nutrition"], 8.5),
        Content("3", "Travel", ["Adventure", "Nature"], 9.5),
        Content("4", "Technology", ["Gadgets", "AI"], 8.0),
        Content("5", "Food", ["Recipes", "Cooking"], 7.5),
    ]

    # Sample user
    user = User("user1", preferences=["Technology", "Travel"], history=["1"])

    # Create personalized feed
    feed_generator = PersonalizedFeed(contents)
    personalized_feed = feed_generator.generate_feed(user, limit=3)

    # Display the personalized feed
    for content in personalized_feed:
        print(f"Content ID: {content.content_id}, Score: {content.score}")
```
