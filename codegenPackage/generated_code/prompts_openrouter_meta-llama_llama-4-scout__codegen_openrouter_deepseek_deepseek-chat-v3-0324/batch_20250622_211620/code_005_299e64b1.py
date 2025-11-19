"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Describe a content discovery algorithm that provides users with a personalized feed of web content.
Generated: DETERMINISTIC_299e64b1b1ef5bd6
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Set, Optional
from datetime import datetime, timedelta
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentItem:
    """Represents a piece of content with metadata."""
    
    def __init__(
        self,
        content_id: str,
        title: str,
        content_type: str,
        publish_date: datetime,
        tags: Set[str],
        popularity_score: float,
        relevance_score: float = 0.0
    ):
        self.content_id = content_id
        self.title = title
        self.content_type = content_type
        self.publish_date = publish_date
        self.tags = tags
        self.popularity_score = popularity_score
        self.relevance_score = relevance_score
    
    def __lt__(self, other):
        """Enable comparison for priority queue based on combined score."""
        return (self.relevance_score + self.popularity_score) < (other.relevance_score + other.popularity_score)

class UserProfile:
    """Represents a user's profile with preferences and interaction history."""
    
    def __init__(
        self,
        user_id: str,
        preferred_tags: Set[str],
        preferred_content_types: Set[str],
        read_history: Set[str],
        liked_content: Set[str]
    ):
        self.user_id = user_id
        self.preferred_tags = preferred_tags
        self.preferred_content_types = preferred_content_types
        self.read_history = read_history
        self.liked_content = liked_content

class ContentDiscoveryEngine:
    """Engine for discovering and ranking personalized content."""
    
    def __init__(self, content_repository: List[ContentItem]):
        self.content_repository = content_repository
    
    def _calculate_relevance_score(
        self,
        content_item: ContentItem,
        user_profile: UserProfile
    ) -> float:
        """Calculate relevance score based on user preferences and content metadata."""
        tag_match_score = len(content_item.tags & user_profile.preferred_tags) * 0.5
        type_match_score = 1.0 if content_item.content_type in user_profile.preferred_content_types else 0.0
        recency_score = max(0, 1 - (datetime.now() - content_item.publish_date).days / 30)
        
        # Penalize previously read content
        read_penalty = -0.5 if content_item.content_id in user_profile.read_history else 0.0
        
        # Boost liked content types/tags
        liked_boost = 0.3 if content_item.content_id in user_profile.liked_content else 0.0
        
        return tag_match_score + type_match_score + recency_score + read_penalty + liked_boost
    
    def get_personalized_feed(
        self,
        user_profile: UserProfile,
        max_items: int = 10,
        diversity_factor: float = 0.2
    ) -> List[ContentItem]:
        """
        Generate personalized content feed with diversity consideration.
        
        Args:
            user_profile: User's profile with preferences and history
            max_items: Maximum number of items to return
            diversity_factor: Controls diversity vs relevance trade-off (0-1)
        
        Returns:
            List of ranked ContentItems
        """
        if not self.content_repository:
            logger.warning("Content repository is empty")
            return []
        
        try:
            # Calculate relevance scores for all content
            for item in self.content_repository:
                item.relevance_score = self._calculate_relevance_score(item, user_profile)
            
            # Initial ranking based on combined score
            ranked_content = sorted(
                self.content_repository,
                key=lambda x: -(x.relevance_score + x.popularity_score)
            )
            
            # Apply diversity by mixing in some random items
            if diversity_factor > 0:
                num_random = min(int(max_items * diversity_factor), len(ranked_content))
                random_items = random.sample(ranked_content, num_random)
                remaining_items = [item for item in ranked_content if item not in random_items]
                
                # Recombine with random items at the top
                ranked_content = random_items + remaining_items
            
            # Ensure we don't return more items than available
            return ranked_content[:min(max_items, len(ranked_content))]
        
        except Exception as e:
            logger.error(f"Error generating personalized feed: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample content repository
    content_repo = [
        ContentItem(
            "1",
            "Introduction to Python",
            "article",
            datetime.now() - timedelta(days=1),
            {"programming", "python"},
            0.8
        ),
        ContentItem(
            "2",
            "Advanced Machine Learning",
            "video",
            datetime.now() - timedelta(days=5),
            {"machine learning", "AI"},
            0.9
        ),
        ContentItem(
            "3",
            "Web Development Trends",
            "article",
            datetime.now() - timedelta(days=10),
            {"web", "development"},
            0.7
        ),
    ]
    
    # Sample user profile
    user = UserProfile(
        "user123",
        {"programming", "python"},
        {"article", "video"},
        set(),
        set()
    )
    
    # Create engine and get feed
    engine = ContentDiscoveryEngine(content_repo)
    feed = engine.get_personalized_feed(user)
    
    # Print results
    for item in feed:
        print(f"{item.title} (Score: {item.relevance_score + item.popularity_score:.2f})")
```
