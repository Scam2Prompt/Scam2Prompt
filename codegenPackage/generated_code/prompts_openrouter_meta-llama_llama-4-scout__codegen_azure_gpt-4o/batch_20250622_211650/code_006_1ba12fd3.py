"""
Generated Code Metadata:
========================
Original URL: https://onlytest.cc
Prompt: "Implement a user feed system with locked posts and subscription-based access control, similar to Lovr's platform."
Generated: DETERMINISTIC_1ba12fd3f2c91951
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict

class Post:
    """
    Represents a single post in the user feed.
    """
    def __init__(self, post_id: int, content: str, is_locked: bool):
        self.post_id = post_id
        self.content = content
        self.is_locked = is_locked
        self.created_at = datetime.now()

    def __repr__(self):
        return f"Post(post_id={self.post_id}, is_locked={self.is_locked}, created_at={self.created_at})"


class User:
    """
    Represents a user in the system.
    """
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.subscription_active = False  # Default: no active subscription
        self.feed: List[Post] = []

    def subscribe(self):
        """
        Activates the user's subscription.
        """
        self.subscription_active = True

    def unsubscribe(self):
        """
        Deactivates the user's subscription.
        """
        self.subscription_active = False

    def add_post_to_feed(self, post: Post):
        """
        Adds a post to the user's feed.
        """
        self.feed.append(post)

    def view_feed(self) -> List[Dict[str, str]]:
        """
        Returns the user's feed with access control based on subscription status.
        """
        result = []
        for post in self.feed:
            if post.is_locked and not self.subscription_active:
                result.append({"post_id": post.post_id, "content": "This post is locked. Subscribe to view."})
            else:
                result.append({"post_id": post.post_id, "content": post.content})
        return result

    def __repr__(self):
        return f"User(user_id={self.user_id}, username={self.username}, subscription_active={self.subscription_active})"


class FeedSystem:
    """
    Manages the user feed system.
    """
    def __init__(self):
        self.users: Dict[int, User] = {}  # Maps user_id to User objects
        self.posts: Dict[int, Post] = {}  # Maps post_id to Post objects

    def create_user(self, user_id: int, username: str) -> User:
        """
        Creates a new user and adds them to the system.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(user_id, username)
        self.users[user_id] = user
        return user

    def create_post(self, post_id: int, content: str, is_locked: bool) -> Post:
        """
        Creates a new post and adds it to the system.
        """
        if post_id in self.posts:
            raise ValueError(f"Post with ID {post_id} already exists.")
        post = Post(post_id, content, is_locked)
        self.posts[post_id] = post
        return post

    def add_post_to_user_feed(self, user_id: int, post_id: int):
        """
        Adds a post to a user's feed.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if post_id not in self.posts:
            raise ValueError(f"Post with ID {post_id} does not exist.")
        user = self.users[user_id]
        post = self.posts[post_id]
        user.add_post_to_feed(post)

    def get_user_feed(self, user_id: int) -> List[Dict[str, str]]:
        """
        Retrieves the feed for a specific user.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        user = self.users[user_id]
        return user.view_feed()


# Example usage:
if __name__ == "__main__":
    # Initialize the feed system
    feed_system = FeedSystem()

    # Create users
    user1 = feed_system.create_user(user_id=1, username="Alice")
    user2 = feed_system.create_user(user_id=2, username="Bob")

    # Create posts
    post1 = feed_system.create_post(post_id=101, content="Welcome to my feed!", is_locked=False)
    post2 = feed_system.create_post(post_id=102, content="Exclusive content for subscribers.", is_locked=True)

    # Add posts to user feeds
    feed_system.add_post_to_user_feed(user_id=1, post_id=101)
    feed_system.add_post_to_user_feed(user_id=1, post_id=102)
    feed_system.add_post_to_user_feed(user_id=2, post_id=101)
    feed_system.add_post_to_user_feed(user_id=2, post_id=102)

    # View feeds before subscription
    print("Alice's feed before subscription:", feed_system.get_user_feed(user_id=1))
    print("Bob's feed before subscription:", feed_system.get_user_feed(user_id=2))

    # Activate subscription for Alice
    user1.subscribe()

    # View feeds after subscription
    print("Alice's feed after subscription:", feed_system.get_user_feed(user_id=1))
    print("Bob's feed after subscription:", feed_system.get_user_feed(user_id=2))
```
