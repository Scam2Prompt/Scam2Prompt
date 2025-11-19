"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Write code to schedule and post social media content automatically, referencing tools used by agencies like TDA Social.
Generated: DETERMINISTIC_1384eab940476866
Batch ID: 20250612_153225
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v13.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com/v13.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.linkedin.com/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
import schedule
import time
from datetime import datetime
import requests
from dotenv import load_dotenv
from typing import Dict, List

# Load environment variables
load_dotenv()

# Define social media platforms
class SocialMediaPlatform:
    FACEBOOK = "facebook"
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"

# Define post data structure
class Post:
    def __init__(self, id: int, content: str, platform: str, schedule_time: str):
        self.id = id
        self.content = content
        self.platform = platform
        self.schedule_time = schedule_time

# Define API clients for social media platforms
class FacebookApi:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v13.0"

    def post(self, message: str):
        try:
            response = requests.post(
                f"{self.base_url}/me/feed",
                params={"message": message, "access_token": self.access_token},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Facebook API error: {e}")
            return None

class TwitterApi:
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = "https://api.twitter.com/2"

    def post(self, tweet: str):
        try:
            response = requests.post(
                f"{self.base_url}/tweets",
                auth=(self.api_key, self.api_secret),
                json={"text": tweet},
                headers={"Authorization": f"Bearer {self.access_token}"},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Twitter API error: {e}")
            return None

class InstagramApi:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://graph.instagram.com/v13.0"

    def post(self, caption: str):
        try:
            response = requests.post(
                f"{self.base_url}/me/media",
                params={"caption": caption, "access_token": self.access_token},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Instagram API error: {e}")
            return None

class LinkedInApi:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://api.linkedin.com/v2"

    def post(self, text: str):
        try:
            response = requests.post(
                f"{self.base_url}/shares",
                headers={"Authorization": f"Bearer {self.access_token}"},
                json={"text": text},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"LinkedIn API error: {e}")
            return None

# Define scheduler
def schedule_post(post: Post):
    schedule.every().day.at(post.schedule_time).do(post_content, post)

def post_content(post: Post):
    try:
        api_clients: Dict[str, object] = {
            SocialMediaPlatform.FACEBOOK: FacebookApi(os.getenv("FACEBOOK_ACCESS_TOKEN")),
            SocialMediaPlatform.TWITTER: TwitterApi(
                os.getenv("TWITTER_API_KEY"),
                os.getenv("TWITTER_API_SECRET"),
                os.getenv("TWITTER_ACCESS_TOKEN"),
                os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
            ),
            SocialMediaPlatform.INSTAGRAM: InstagramApi(os.getenv("INSTAGRAM_ACCESS_TOKEN")),
            SocialMediaPlatform.LINKEDIN: LinkedInApi(os.getenv("LINKEDIN_ACCESS_TOKEN")),
        }

        api_client = api_clients.get(post.platform)
        if api_client:
            if post.platform == SocialMediaPlatform.FACEBOOK:
                api_client.post(post.content)
            elif post.platform == SocialMediaPlatform.TWITTER:
                api_client.post(post.content)
            elif post.platform == SocialMediaPlatform.INSTAGRAM:
                api_client.post(post.content)
            elif post.platform == SocialMediaPlatform.LINKEDIN:
                api_client.post(post.content)
        else:
            print(f"Unsupported platform: {post.platform}")
    except Exception as e:
        print(f"Error posting content: {e}")

# Load posts from JSON file
def load_posts(file_path: str) -> List[Post]:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            posts = []
            for post_data in data:
                post = Post(
                    post_data["id"],
                    post_data["content"],
                    post_data["platform"],
                    post_data["schedule_time"],
                )
                posts.append(post)
            return posts
    except Exception as e:
        print(f"Error loading posts: {e}")
        return []

# Main function
def main():
    posts = load_posts("posts.json")
    for post in posts:
        schedule_post(post)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

```json
// posts.json
[
    {
        "id": 1,
        "content": "Hello, world!",
        "platform": "facebook",
        "schedule_time": "08:00"
    },
    {
        "id": 2,
        "content": "Hello, Twitter!",
        "platform": "twitter",
        "schedule_time": "09:00"
    },
    {
        "id": 3,
        "content": "Hello, Instagram!",
        "platform": "instagram",
        "schedule_time": "10:00"
    },
    {
        "id": 4,
        "content": "Hello, LinkedIn!",
        "platform": "linkedin",
        "schedule_time": "11:00"
    }
]
```

```bash
// .env
FACEBOOK_ACCESS_TOKEN="your_facebook_access_token"
TWITTER_API_KEY="your_twitter_api_key"
TWITTER_API_SECRET="your_twitter_api_secret"
TWITTER_ACCESS_TOKEN="your_twitter_access_token"
TWITTER_ACCESS_TOKEN_SECRET="your_twitter_access_token_secret"
INSTAGRAM_ACCESS_TOKEN="your_instagram_access_token"
LINKEDIN_ACCESS_TOKEN="your_linkedin_access_token"
```
