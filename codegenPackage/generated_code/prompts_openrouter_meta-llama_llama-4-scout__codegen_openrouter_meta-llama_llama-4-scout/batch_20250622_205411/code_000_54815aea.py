"""
Generated Code Metadata:
========================
Original URL: https://okayvc.com
Prompt: "Generate a Python script to manage social media accounts for a small business, including posting and engagement metrics, inspired by Okay Visual Creations' social media management services."
Generated: DETERMINISTIC_54815aea26f3ff95
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_media_manager.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaAccount:
    """Represents a social media account."""

    def __init__(self, platform: str, username: str, password: str):
        """
        Initializes a SocialMediaAccount object.

        Args:
        - platform (str): The social media platform (e.g., Facebook, Twitter, Instagram).
        - username (str): The account username.
        - password (str): The account password.
        """
        self.platform = platform
        self.username = username
        self.password = password
        self.posts = []
        self.engagement_metrics = {"likes": 0, "comments": 0, "shares": 0}

    def post(self, content: str):
        """
        Posts content on the social media account.

        Args:
        - content (str): The post content.

        Returns:
        - post_id (int): The ID of the posted content.
        """
        post_id = len(self.posts) + 1
        self.posts.append({"id": post_id, "content": content, "timestamp": datetime.datetime.now()})
        logging.info(f"Posted on {self.platform} account: {content}")
        return post_id

    def track_engagement(self, post_id: int, likes: int = 0, comments: int = 0, shares: int = 0):
        """
        Tracks engagement metrics for a post.

        Args:
        - post_id (int): The ID of the post.
        - likes (int, optional): The number of likes. Defaults to 0.
        - comments (int, optional): The number of comments. Defaults to 0.
        - shares (int, optional): The number of shares. Defaults to 0.

        Raises:
        - ValueError: If the post ID is invalid.
        """
        post = next((post for post in self.posts if post["id"] == post_id), None)
        if post is None:
            raise ValueError("Invalid post ID")

        self.engagement_metrics["likes"] += likes
        self.engagement_metrics["comments"] += comments
        self.engagement_metrics["shares"] += shares
        logging.info(f"Tracked engagement for post {post_id} on {self.platform} account")

    def get_engagement_metrics(self) -> Dict[str, int]:
        """
        Retrieves the engagement metrics.

        Returns:
        - engagement_metrics (Dict[str, int]): A dictionary containing the engagement metrics.
        """
        return self.engagement_metrics


class SocialMediaManager:
    """Manages multiple social media accounts."""

    def __init__(self):
        """
        Initializes a SocialMediaManager object.
        """
        self.accounts = {}

    def add_account(self, platform: str, username: str, password: str):
        """
        Adds a social media account.

        Args:
        - platform (str): The social media platform.
        - username (str): The account username.
        - password (str): The account password.

        Raises:
        - ValueError: If the account already exists.
        """
        if username in self.accounts:
            raise ValueError("Account already exists")

        self.accounts[username] = SocialMediaAccount(platform, username, password)
        logging.info(f"Added {platform} account for {username}")

    def get_account(self, username: str) -> SocialMediaAccount:
        """
        Retrieves a social media account.

        Args:
        - username (str): The account username.

        Returns:
        - account (SocialMediaAccount): The social media account object.

        Raises:
        - ValueError: If the account does not exist.
        """
        account = self.accounts.get(username)
        if account is None:
            raise ValueError("Account does not exist")

        return account


def main():
    # Create a social media manager
    manager = SocialMediaManager()

    # Add social media accounts
    manager.add_account("Facebook", "example_facebook", "password123")
    manager.add_account("Twitter", "example_twitter", "password456")

    # Get a social media account
    facebook_account = manager.get_account("example_facebook")

    # Post content on the social media account
    post_id = facebook_account.post("Hello, world!")

    # Track engagement metrics
    facebook_account.track_engagement(post_id, likes=10, comments=5)

    # Retrieve engagement metrics
    engagement_metrics = facebook_account.get_engagement_metrics()
    logging.info(f"Engagement metrics: {engagement_metrics}")


if __name__ == "__main__":
    main()
```
