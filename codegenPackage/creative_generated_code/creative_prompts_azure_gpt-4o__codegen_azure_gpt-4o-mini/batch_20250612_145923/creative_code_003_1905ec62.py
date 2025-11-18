"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Develop a feature in a music streaming platform that allows fans to earn $GROOVE tokens by reviewing and promoting music through short videos, as outlined in the GrooveUP Influencer hub.
Generated: DETERMINISTIC_1905ec6275be74bc
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import uuid
from datetime import datetime
from typing import List, Optional

# Constants for the token reward system
TOKEN_REWARD_PER_REVIEW = 50
TOKEN_REWARD_PER_VIDEO = 20

# Define a simple User class to represent a user in the system
class User:
    def __init__(self, username: str):
        self.username = username
        self.tokens = 0
        self.reviews = []
        self.videos = []

    def add_tokens(self, amount: int):
        """Add tokens to the user's balance."""
        if amount < 0:
            raise ValueError("Cannot add negative tokens.")
        self.tokens += amount

    def __str__(self):
        return f"User({self.username}, Tokens: {self.tokens})"

# Define a Review class to represent a music review
class Review:
    def __init__(self, user: User, content: str):
        self.id = str(uuid.uuid4())
        self.user = user
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Review by {self.user.username}: {self.content} at {self.timestamp}"

# Define a Video class to represent a promotional video
class Video:
    def __init__(self, user: User, content: str):
        self.id = str(uuid.uuid4())
        self.user = user
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Video by {self.user.username}: {self.content} at {self.timestamp}"

# Define the MusicStreamingPlatform class to manage users, reviews, and videos
class MusicStreamingPlatform:
    def __init__(self):
        self.users = []

    def register_user(self, username: str) -> User:
        """Register a new user in the platform."""
        new_user = User(username)
        self.users.append(new_user)
        return new_user

    def submit_review(self, user: User, content: str) -> Optional[Review]:
        """Allow users to submit a review and earn tokens."""
        if not content:
            raise ValueError("Review content cannot be empty.")
        
        review = Review(user, content)
        user.reviews.append(review)
        user.add_tokens(TOKEN_REWARD_PER_REVIEW)
        return review

    def submit_video(self, user: User, content: str) -> Optional[Video]:
        """Allow users to submit a promotional video and earn tokens."""
        if not content:
            raise ValueError("Video content cannot be empty.")
        
        video = Video(user, content)
        user.videos.append(video)
        user.add_tokens(TOKEN_REWARD_PER_VIDEO)
        return video

    def get_user_info(self, user: User) -> str:
        """Get information about a user, including their token balance and contributions."""
        return str(user)

# Example usage
if __name__ == "__main__":
    # Create an instance of the music streaming platform
    platform = MusicStreamingPlatform()

    # Register a user
    user1 = platform.register_user("fan123")
    
    # Submit a review
    review = platform.submit_review(user1, "This song is amazing!")
    
    # Submit a promotional video
    video = platform.submit_video(user1, "Check out this awesome track!")

    # Print user info
    print(platform.get_user_info(user1))

    # Print review and video details
    print(review)
    print(video)
```
