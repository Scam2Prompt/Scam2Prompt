"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: "Develop a social media content calendar for a marketing agency specializing in agricultural businesses, similar to NMKT's approach."
Generated: DETERMINISTIC_91e88e1453ee63dd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Content Calendar for Agricultural Marketing Agency

This script manages a content calendar for scheduling social media posts
for agricultural businesses. It includes features for adding, editing,
viewing, and exporting scheduled posts.

Features:
- Post scheduling with date/time, platform, content type
- Content categorization by agricultural themes
- Export to CSV for sharing with clients
- Basic analytics on scheduled content
"""

import csv
from datetime import datetime
from typing import List, Dict, Optional
import json
import os
from enum import Enum


class Platform(Enum):
    """Supported social media platforms"""
    FACEBOOK = "Facebook"
    INSTAGRAM = "Instagram"
    TWITTER = "Twitter"
    LINKEDIN = "LinkedIn"
    TIKTOK = "TikTok"


class ContentType(Enum):
    """Types of content that can be scheduled"""
    IMAGE = "Image"
    VIDEO = "Video"
    TEXT = "Text"
    LINK = "Link"
    REEL = "Reel"
    STORY = "Story"


class AgriculturalTheme(Enum):
    """Agricultural content themes"""
    CROP_UPDATE = "Crop Update"
    LIVESTOCK = "Livestock"
    FARM_EQUIPMENT = "Farm Equipment"
    AG_TECH = "Agricultural Technology"
    SUSTAINABILITY = "Sustainability"
    MARKET_TRENDS = "Market Trends"
    FARMER_SPOTLIGHT = "Farmer Spotlight"
    SEASONAL = "Seasonal Content"


class SocialMediaPost:
    """Class representing a single social media post"""
    
    def __init__(
        self,
        post_date: datetime,
        platform: Platform,
        content_type: ContentType,
        theme: AgriculturalTheme,
        content: str,
        client: str,
        scheduled: bool = False
    ):
        self.post_date = post_date
        self.platform = platform
        self.content_type = content_type
        self.theme = theme
        self.content = content
        self.client = client
        self.scheduled = scheduled
    
    def to_dict(self) -> Dict:
        """Convert post to dictionary for serialization"""
        return {
            "post_date": self.post_date.isoformat(),
            "platform": self.platform.value,
            "content_type": self.content_type.value,
            "theme": self.theme.value,
            "content": self.content,
            "client": self.client,
            "scheduled": self.scheduled
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SocialMediaPost':
        """Create post from dictionary"""
        return cls(
            post_date=datetime.fromisoformat(data["post_date"]),
            platform=Platform(data["platform"]),
            content_type=ContentType(data["content_type"]),
            theme=AgriculturalTheme(data["theme"]),
            content=data["content"],
            client=data["client"],
            scheduled=data["scheduled"]
        )


class ContentCalendar:
    """Main content calendar class"""
    
    def __init__(self):
        self.posts: List[SocialMediaPost] = []
        self.clients: List[str] = []
    
    def add_post(self, post: SocialMediaPost) -> None:
        """Add a new post to the calendar"""
        self.posts.append(post)
        if post.client not in self.clients:
            self.clients.append(post.client)
    
    def edit_post(
        self,
        post_index: int,
        new_post: SocialMediaPost
    ) -> bool:
        """Edit an existing post"""
        if 0 <= post_index < len(self.posts):
            self.posts[post_index] = new_post
            return True
        return False
    
    def delete_post(self, post_index: int) -> bool:
        """Delete a post from the calendar"""
        if 0 <= post_index < len(self.posts):
            del self.posts[post_index]
            return True
        return False
    
    def get_posts_by_client(self, client: str) -> List[SocialMediaPost]:
        """Get all posts for a specific client"""
        return [post for post in self.posts if post.client == client]
    
    def get_posts_by_date_range(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> List[SocialMediaPost]:
        """Get posts within a date range"""
        return [
            post for post in self.posts
            if start_date <= post.post_date <= end_date
        ]
    
    def get_posts_by_theme(
        self,
        theme: AgriculturalTheme
    ) -> List[SocialMediaPost]:
        """Get posts with a specific agricultural theme"""
        return [post for post in self.posts if post.theme == theme]
    
    def export_to_csv(self, filename: str) -> bool:
        """Export calendar to CSV file"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'post_date', 'platform', 'content_type',
                    'theme', 'content', 'client', 'scheduled'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for post in self.posts:
                    writer.writerow(post.to_dict())
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def import_from_csv(self, filename: str) -> bool:
        """Import calendar from CSV file"""
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    post = SocialMediaPost.from_dict(row)
                    self.add_post(post)
            return True
        except Exception as e:
            print(f"Error importing from CSV: {e}")
            return False
    
    def save_to_json(self, filename: str) -> bool:
        """Save calendar to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([post.to_dict() for post in self.posts], f)
            return True
        except Exception as e:
            print(f"Error saving to JSON: {e}")
            return False
    
    def load_from_json(self, filename: str) -> bool:
        """Load calendar from JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.posts = [SocialMediaPost.from_dict(item) for item in data]
                self.clients = list(set(post.client for post in self.posts))
            return True
        except Exception as e:
            print(f"Error loading from JSON: {e}")
            return False
    
    def get_content_analytics(self) -> Dict:
        """Generate basic analytics about scheduled content"""
        analytics = {
            "total_posts": len(self.posts),
            "posts_by_platform": {},
            "posts_by_theme": {},
            "posts_by_client": {},
            "scheduled_vs_unscheduled": {
                "scheduled": 0,
                "unscheduled": 0
            }
        }
        
        for post in self.posts:
            # Count by platform
            platform = post.platform.value
            analytics["posts_by_platform"][platform] = analytics["posts_by_platform"].get(platform, 0) + 1
            
            # Count by theme
            theme = post.theme.value
            analytics["posts_by_theme"][theme] = analytics["posts_by_theme"].get(theme, 0) + 1
            
            # Count by client
            client = post.client
            analytics["posts_by_client"][client] = analytics["posts_by_client"].get(client, 0) + 1
            
            # Count scheduled vs unscheduled
            if post.scheduled:
                analytics["scheduled_vs_unscheduled"]["scheduled"] += 1
            else:
                analytics["scheduled_vs_unscheduled"]["unscheduled"] += 1
        
        return analytics


def example_usage():
    """Example usage of the ContentCalendar class"""
    calendar = ContentCalendar()
    
    # Add some example posts
    post1 = SocialMediaPost(
        post_date=datetime(2023, 11, 15, 9, 0),
        platform=Platform.FACEBOOK,
        content_type=ContentType.IMAGE,
        theme=AgriculturalTheme.CROP_UPDATE,
        content="Check out our latest wheat harvest!",
        client="Greenfield Farms",
        scheduled=True
    )
    
    post2 = SocialMediaPost(
        post_date=datetime(2023, 11, 16, 10, 30),
        platform=Platform.INSTAGRAM,
        content_type=ContentType.REEL,
        theme=AgriculturalTheme.AG_TECH,
        content="New drone technology for crop monitoring",
        client="AgriTech Solutions",
        scheduled=False
    )
    
    calendar.add_post(post1)
    calendar.add_post(post2)
    
    # Export to CSV
    calendar.export_to_csv("content_calendar.csv")
    
    # Print analytics
    analytics = calendar.get_content_analytics()
    print("Content Analytics:")
    print(json.dumps(analytics, indent=2))


if __name__ == "__
