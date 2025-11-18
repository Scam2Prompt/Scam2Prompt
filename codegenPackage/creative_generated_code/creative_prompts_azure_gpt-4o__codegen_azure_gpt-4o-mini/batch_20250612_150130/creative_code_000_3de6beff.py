"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Write Python code to create a personalized feed system that filters web content based on user preferences, similar to the functionality described in Stumble! ®.
Generated: DETERMINISTIC_3de6beff7dae762a
Batch ID: 20250612_150130
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

class User:
    """Represents a user in the personalized feed system."""
    
    def __init__(self, user_id: str, preferences: List[str]):
        """
        Initialize a user with a unique ID and a list of content preferences.
        
        :param user_id: Unique identifier for the user.
        :param preferences: List of content categories the user prefers.
        """
        self.user_id = user_id
        self.preferences = preferences

class Content:
    """Represents a piece of web content."""
    
    def __init__(self, content_id: str, category: str):
        """
        Initialize content with a unique ID and a category.
        
        :param content_id: Unique identifier for the content.
        :param category: Category of the content.
        """
        self.content_id = content_id
        self.category = category

class Feed:
    """Generates a personalized feed of content based on user preferences."""
    
    def __init__(self, user: User, content_list: List[Content]):
        """
        Initialize the feed with a user and a list of available content.
        
        :param user: User for whom the feed is being generated.
        :param content_list: List of all available content.
        """
        self.user = user
        self.content_list = content_list

    def generate_feed(self) -> List[Content]:
        """
        Generate a personalized content feed based on user preferences.
        
        :return: List of content items that match user preferences.
        """
        # Filter content based on user preferences
        filtered_content = [content for content in self.content_list if content.category in self.user.preferences]
        
        # Shuffle the filtered content for randomness
        random.shuffle(filtered_content)
        
        return filtered_content

def main():
    # Sample users and content
    users = [
        User("user1", ["technology", "science"]),
        User("user2", ["food", "travel"]),
    ]
    
    content_list = [
        Content("content1", "technology"),
        Content("content2", "science"),
        Content("content3", "food"),
        Content("content4", "travel"),
        Content("content5", "health"),
    ]
    
    # Generate personalized feeds for each user
    for user in users:
        try:
            feed = Feed(user, content_list)
            personalized_feed = feed.generate_feed()
            print(f"Personalized Feed for {user.user_id}: {[content.content_id for content in personalized_feed]}")
        except Exception as e:
            print(f"Error generating feed for {user.user_id}: {str(e)}")

if __name__ == "__main__":
    main()
```
