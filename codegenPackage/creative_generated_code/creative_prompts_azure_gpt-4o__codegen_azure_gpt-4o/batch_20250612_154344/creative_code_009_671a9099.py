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
# Import necessary modules
import random
from datetime import datetime, timedelta
from collections import defaultdict

class ContentDiscoveryFeed:
    """
    A class to implement a personalized feed algorithm for a content discovery platform.
    The feed prioritizes user preferences, engagement history, and recency of content.
    """
    
    def __init__(self):
        """
        Initializes the content discovery feed system.
        """
        self.user_preferences = defaultdict(list)  # Stores user preferences (e.g., topics or categories)
        self.user_engagement_history = defaultdict(list)  # Tracks user interactions with content
        self.content_repository = []  # Store all available content
        self.last_accessed_timestamp = defaultdict(lambda: datetime.min)  # Tracks when last accessed
    
    def add_content(self, content_id, category, publish_date, metadata):
        """
        Adds content to the repository.

        Args:
            content_id (str): Unique identifier for the content.
            category (str): Category of the content.
            publish_date (datetime): Date when the content was published.
            metadata (dict): Additional metadata about the content.
        """
        self.content_repository.append({
            "content_id": content_id,
            "category": category,
            "publish_date": publish_date,
            "metadata": metadata
        })
    
    def update_user_preferences(self, user_id, preferences):
        """
        Updates the user's preferences.

        Args:
            user_id (str): Unique identifier for the user.
            preferences (list): List of preferred categories/topics.
        """
        self.user_preferences[user_id] = preferences
    
    def log_user_engagement(self, user_id, content_id):
        """
        Logs user's engagement with specific content.

        Args:
            user_id (str): Unique identifier for the user.
            content_id (str): Unique identifier of the content.
        """
        self.user_engagement_history[user_id].append({
            "content_id": content_id,
            "timestamp": datetime.now()
        })
    
    def _filter_and_rank_content(self, user_id):
        """
        Filters and ranks content based on user preferences and engagement history.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            list: Ranked list of content IDs for the user.
        """
        preferences = self.user_preferences[user_id]
        engagement_history = {entry['content_id'] for entry in self.user_engagement_history[user_id]}
        now = datetime.now()
        
        # Filter content by preferences and exclude already engaged content
        filtered_content = [
            content for content in self.content_repository
            if content["category"] in preferences and content["content_id"] not in engagement_history
        ]
        
        # Rank content based on recency and user preferences
        ranked_content = sorted(
            filtered_content,
            key=lambda c: (
                (now - c["publish_date"]).days,  # Content recency
                preferences.index(c["category"]) if c["category"] in preferences else float("inf")  # Match preferences order
            )
        )
        
        return [content["content_id"] for content in ranked_content]
    
    def get_personalized_feed(self, user_id, limit=10):
        """
        Generates a personalized feed for the user.

        Args:
            user_id (str): Unique identifier for the user.
            limit (int): Maximum number of content items to return.

        Returns:
            list: Personalized feed content IDs.
        """
        try:
            # Generate feed
            ranked_content = self._filter_and_rank_content(user_id)
            
            # Return top `limit` items
            return ranked_content[:limit]
        except Exception as e:
            # Log and handle errors (in production, use a proper logging system)
            print(f"Error generating feed for user {user_id}: {e}")
            return []
    

# Example Usage
if __name__ == "__main__":
    feed_system = ContentDiscoveryFeed()
    
    # Add some content to the repository
    feed_system.add_content("content_1", "technology", datetime.now() - timedelta(days=1), {"title": "Tech News"})
    feed_system.add_content("content_2", "science", datetime.now() - timedelta(days=2), {"title": "Science Update"})
    feed_system.add_content("content_3", "technology", datetime.now() - timedelta(days=5), {"title": "Old Tech Article"})
    
    # Update a user's preferences
    feed_system.update_user_preferences("user_123", ["technology", "science"])
    
    # Log user engagement
    feed_system.log_user_engagement("user_123", "content_3")
    
    # Generate personalized feed
    personalized_feed = feed_system.get_personalized_feed("user_123", limit=2)
    print("Personalized Feed:", personalized_feed)
```
