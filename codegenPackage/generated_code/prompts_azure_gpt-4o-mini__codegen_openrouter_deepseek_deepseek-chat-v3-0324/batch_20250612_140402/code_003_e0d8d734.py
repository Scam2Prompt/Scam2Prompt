"""
Generated Code Metadata:
========================
Original URL: https://bearmybrand.com
Prompt: Create a Python script that automates social media posting for a digital marketing agency, including scheduling and content management.
Generated: DETERMINISTIC_e0d8d734025d5a05
Batch ID: 20250612_140402
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import schedule
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz
from social_media_apis import FacebookAPI, TwitterAPI, InstagramAPI  # Hypothetical APIs

# Configuration file path
CONFIG_FILE = "config.json"
POSTS_FILE = "posts.json"

class SocialMediaPost:
    def __init__(
        self,
        content: str,
        platforms: List[str],
        scheduled_time: datetime,
        image_path: Optional[str] = None,
        post_id: Optional[str] = None,
    ):
        self.content = content
        self.platforms = platforms
        self.scheduled_time = scheduled_time
        self.image_path = image_path
        self.post_id = post_id

    def to_dict(self) -> Dict:
        return {
            "content": self.content,
            "platforms": self.platforms,
            "scheduled_time": self.scheduled_time.isoformat(),
            "image_path": self.image_path,
            "post_id": self.post_id,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "SocialMediaPost":
        return cls(
            content=data["content"],
            platforms=data["platforms"],
            scheduled_time=datetime.fromisoformat(data["scheduled_time"]),
            image_path=data.get("image_path"),
            post_id=data.get("post_id"),
        )

class SocialMediaManager:
    def __init__(self):
        self.config = self._load_config()
        self.posts = self._load_posts()
        self._initialize_apis()
        self._schedule_posts()

    def _load_config(self) -> Dict:
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Config file not found. Please create config.json")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON in config file")

    def _load_posts(self) -> List[SocialMediaPost]:
        try:
            if not os.path.exists(POSTS_FILE):
                return []
            
            with open(POSTS_FILE, "r") as f:
                posts_data = json.load(f)
                return [SocialMediaPost.from_dict(post) for post in posts_data]
        except json.JSONDecodeError:
            raise Exception("Invalid JSON in posts file")

    def _save_posts(self):
        with open(POSTS_FILE, "w") as f:
            json.dump([post.to_dict() for post in self.posts], f, indent=2)

    def _initialize_apis(self):
        self.apis = {
            "facebook": FacebookAPI(
                api_key=self.config["facebook"]["api_key"],
                access_token=self.config["facebook"]["access_token"],
            ),
            "twitter": TwitterAPI(
                api_key=self.config["twitter"]["api_key"],
                api_secret=self.config["twitter"]["api_secret"],
                access_token=self.config["twitter"]["access_token"],
                access_secret=self.config["twitter"]["access_secret"],
            ),
            "instagram": InstagramAPI(
                username=self.config["instagram"]["username"],
                password=self.config["instagram"]["password"],
            ),
        }

    def _schedule_posts(self):
        now = datetime.now(pytz.utc)
        for post in self.posts:
            if post.scheduled_time > now and not post.post_id:
                schedule.every().day.at(post.scheduled_time.strftime("%H:%M")).do(
                    self._publish_post, post
                )

    def _publish_post(self, post: SocialMediaPost):
        try:
            for platform in post.platforms:
                if platform not in self.apis:
                    continue
                
                api = self.apis[platform]
                if post.image_path:
                    post_id = api.post_with_image(post.content, post.image_path)
                else:
                    post_id = api.post_text(post.content)
                
                post.post_id = post_id
            
            self._save_posts()
            print(f"Successfully published post at {datetime.now()}")
        except Exception as e:
            print(f"Error publishing post: {str(e)}")

    def add_post(
        self,
        content: str,
        platforms: List[str],
        scheduled_time: datetime,
        image_path: Optional[str] = None,
    ) -> None:
        post = SocialMediaPost(content, platforms, scheduled_time, image_path)
        self.posts.append(post)
        self._save_posts()
        self._schedule_posts()

    def get_upcoming_posts(self, limit: int = 10) -> List[SocialMediaPost]:
        now = datetime.now(pytz.utc)
        upcoming = [p for p in self.posts if p.scheduled_time > now]
        return sorted(upcoming, key=lambda p: p.scheduled_time)[:limit]

    def run_scheduler(self):
        print("Social media scheduler running...")
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    try:
        manager = SocialMediaManager()
        manager.run_scheduler()
    except Exception as e:
        print(f"Error initializing social media manager: {str(e)}")
```
