"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Generate a code snippet to implement a network of publishers and creators for a children's literature platform, allowing them to share their work and connect with audiences.
Generated: DETERMINISTIC_0797966806a80729
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# children_literature_platform.py
from typing import List, Dict, Optional
from datetime import datetime
import uuid
from abc import ABC, abstractmethod


class User:
    """Base class for all users in the platform."""
    
    def __init__(self, user_id: str, name: str, email: str, bio: str = ""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.bio = bio
        self.date_joined = datetime.now()
        self.followers = set()
    
    def follow(self, user: 'User') -> None:
        """Follow another user."""
        if user.user_id != self.user_id:
            self.followers.add(user.user_id)
    
    def unfollow(self, user: 'User') -> None:
        """Unfollow a user if currently following."""
        if user.user_id in self.followers:
            self.followers.remove(user.user_id)
    
    def get_followers_count(self) -> int:
        """Return the number of followers."""
        return len(self.followers)


class Content(ABC):
    """Abstract base class for all content types."""
    
    def __init__(self, content_id: str, creator: User, title: str, description: str = ""):
        self.content_id = content_id
        self.creator = creator
        self.title = title
        self.description = description
        self.creation_date = datetime.now()
        self.likes = set()
        self.comments = []
    
    @abstractmethod
    def display(self) -> str:
        """Display content details."""
        pass
    
    def add_like(self, user: User) -> None:
        """Add a like from a user."""
        self.likes.add(user.user_id)
    
    def remove_like(self, user: User) -> None:
        """Remove a like from a user."""
        if user.user_id in self.likes:
            self.likes.remove(user.user_id)
    
    def add_comment(self, user: User, text: str) -> None:
        """Add a comment to the content."""
        comment = {
            'user_id': user.user_id,
            'text': text,
            'timestamp': datetime.now()
        }
        self.comments.append(comment)
    
    def get_likes_count(self) -> int:
        """Return the number of likes."""
        return len(self.likes)


class Story(Content):
    """Class representing a story content type."""
    
    def __init__(self, content_id: str, creator: User, title: str, text: str, age_group: str, description: str = ""):
        super().__init__(content_id, creator, title, description)
        self.text = text
        self.age_group = age_group
    
    def display(self) -> str:
        """Display story details."""
        return f"Story: {self.title}\nAge Group: {self.age_group}\n{self.text[:100]}..."


class Illustration(Content):
    """Class representing an illustration content type."""
    
    def __init__(self, content_id: str, creator: User, title: str, image_url: str, description: str = ""):
        super().__init__(content_id, creator, title, description)
        self.image_url = image_url
    
    def display(self) -> str:
        """Display illustration details."""
        return f"Illustration: {self.title}\nImage URL: {self.image_url}"


class Publisher(User):
    """Class representing a publisher user."""
    
    def __init__(self, user_id: str, name: str, email: str, publishing_house: str, bio: str = ""):
        super().__init__(user_id, name, email, bio)
        self.publishing_house = publishing_house
        self.published_content = []
    
    def publish(self, content: Content) -> None:
        """Publish content to the platform."""
        self.published_content.append(content.content_id)
    
    def get_published_content(self) -> List[str]:
        """Return list of published content IDs."""
        return self.published_content


class Creator(User):
    """Class representing a creator user (author/illustrator)."""
    
    def __init__(self, user_id: str, name: str, email: str, creator_type: str, bio: str = ""):
        super().__init__(user_id, name, email, bio)
        self.creator_type = creator_type  # e.g., "author", "illustrator"
        self.portfolio = []
    
    def add_to_portfolio(self, content: Content) -> None:
        """Add content to creator's portfolio."""
        self.portfolio.append(content.content_id)
    
    def get_portfolio(self) -> List[str]:
        """Return list of content IDs in portfolio."""
        return self.portfolio


class Platform:
    """Main platform class managing users and content."""
    
    def __init__(self):
        self.users = {}  # user_id: User
        self.content = {}  # content_id: Content
    
    def register_user(self, user: User) -> bool:
        """Register a new user to the platform."""
        if user.email in [u.email for u in self.users.values()]:
            return False
        self.users[user.user_id] = user
        return True
    
    def create_content(self, content: Content) -> bool:
        """Add new content to the platform."""
        if content.content_id in self.content:
            return False
        self.content[content.content_id] = content
        return True
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        return self.users.get(user_id)
    
    def get_content(self, content_id: str) -> Optional[Content]:
        """Get content by ID."""
        return self.content.get(content_id)
    
    def search_content(self, query: str) -> List[Content]:
        """Search content by title or description."""
        results = []
        query = query.lower()
        for content in self.content.values():
            if query in content.title.lower() or query in content.description.lower():
                results.append(content)
        return results
    
    def generate_content_id(self) -> str:
        """Generate a unique content ID."""
        return str(uuid.uuid4())


# Example usage
if __name__ == "__main__":
    platform = Platform()
    
    # Create users
    author = Creator(
        user_id=str(uuid.uuid4()),
        name="Jane Doe",
        email="jane@example.com",
        creator_type="author",
        bio="Children's book author"
    )
    
    publisher = Publisher(
        user_id=str(uuid.uuid4()),
        name="ABC Publishing",
        email="abc@example.com",
        publishing_house="ABC Publishing House"
    )
    
    # Register users
    platform.register_user(author)
    platform.register_user(publisher)
    
    # Create content
    story = Story(
        content_id=platform.generate_content_id(),
        creator=author,
        title="The Magic Tree",
        text="Once upon a time...",
        age_group="5-8",
        description="A magical adventure story"
    )
    
    # Add content to platform
    platform.create_content(story)
    
    # Publisher publishes content
    publisher.publish(story)
    
    # Author adds to portfolio
    author.add_to_portfolio(story)
    
    # Display content
    print(story.display())
```
