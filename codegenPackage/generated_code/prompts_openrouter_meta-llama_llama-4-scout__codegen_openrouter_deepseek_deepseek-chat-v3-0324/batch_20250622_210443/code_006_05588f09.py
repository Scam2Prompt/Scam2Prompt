"""
Generated Code Metadata:
========================
Original URL: https://karlakarita.com.br
Prompt: "Generate a social media posting schedule for promoting a fashion brand's new collection, including discounts and sustainability features."
Generated: DETERMINISTIC_05588f09fd9801d3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class SocialMediaPost:
    def __init__(self, platform: str, content: str, post_time: datetime.datetime, media_path: str = None):
        self.platform = platform
        self.content = content
        self.post_time = post_time
        self.media_path = media_path

class PostSchedule:
    def __init__(self, brand_name: str, collection_name: str, start_date: datetime.date, duration_days: int):
        self.brand_name = brand_name
        self.collection_name = collection_name
        self.start_date = start_date
        self.duration_days = duration_days
        self.posts: List[SocialMediaPost] = []
    
    def generate_schedule(self):
        """Generate a posting schedule for the fashion brand's new collection"""
        current_date = self.start_date
        
        # Week 1: Collection Launch
        self._add_launch_posts(current_date)
        
        # Week 2: Sustainability Features
        current_date += datetime.timedelta(days=7)
        self._add_sustainability_posts(current_date)
        
        # Week 3: Discount Promotions
        current_date += datetime.timedelta(days=7)
        self._add_discount_posts(current_date)
        
        # Week 4: User Engagement
        current_date += datetime.timedelta(days=7)
        self._add_engagement_posts(current_date)
    
    def _add_launch_posts(self, start_date: datetime.date):
        """Add posts for collection launch week"""
        platforms = ["Instagram", "Facebook", "Twitter"]
        for i, platform in enumerate(platforms):
            post_time = datetime.datetime.combine(
                start_date + datetime.timedelta(days=i),
                datetime.time(hour=10 + i, minute=0)
            )
            content = f"🌟 New Collection Alert! 🌟\n\nOur {self.collection_name} is finally here! " \
                     f"Shop now and be the first to rock these stunning pieces. " \
                     f"#NewCollection #{self.brand_name}"
            self.posts.append(SocialMediaPost(platform, content, post_time, "media/launch.jpg"))
    
    def _add_sustainability_posts(self, start_date: datetime.date):
        """Add posts highlighting sustainability features"""
        sustainability_points = [
            "Made with 100% organic cotton",
            "Zero-waste production process",
            "Eco-friendly packaging",
            "Carbon-neutral shipping"
        ]
        
        for i, point in enumerate(sustainability_points):
            post_time = datetime.datetime.combine(
                start_date + datetime.timedelta(days=i*2),
                datetime.time(hour=12, minute=0)
            )
            content = f"🌱 Sustainable Fashion 🌱\n\nDid you know? Our {self.collection_name} features:\n\n" \
                    f"- {point}\n\n" \
                    f"We're committed to a greener future. #SustainableFashion #{self.brand_name}"
            self.posts.append(SocialMediaPost("Instagram", content, post_time, f"media/sustainability_{i+1}.jpg"))
    
    def _add_discount_posts(self, start_date: datetime.date):
        """Add posts promoting discounts"""
        discount_days = ["Monday", "Wednesday", "Friday"]
        discounts = ["15% OFF", "Free Shipping", "Buy 1 Get 1 50% OFF"]
        
        for i, (day, discount) in enumerate(zip(discount_days, discounts)):
            post_time = datetime.datetime.combine(
                start_date + datetime.timedelta(days=i*2),
                datetime.time(hour=14, minute=0)
            )
            content = f"🛍️ Exclusive Deal Alert! 🛍️\n\nThis {day} only: {discount} on our {self.collection_name}!\n\n" \
                    f"Use code: {self.brand_name.upper()}{i+1} at checkout. Limited time offer! " \
                    f"#FashionDeals #{self.brand_name}"
            self.posts.append(SocialMediaPost("Instagram", content, post_time, "media/discount.jpg"))
    
    def _add_engagement_posts(self, start_date: datetime.date):
        """Add posts to engage users"""
        engagement_types = [
            ("Which piece from our new collection is your favorite?", "poll"),
            ("Share your look with #My{self.brand_name}Style for a chance to be featured!", "hashtag"),
            ("Behind the scenes: Our design process for {self.collection_name}", "bts")
        ]
        
        for i, (text, post_type) in enumerate(engagement_types):
            post_time = datetime.datetime.combine(
                start_date + datetime.timedelta(days=i*2),
                datetime.time(hour=11, minute=30)
            )
            content = text.format(self=self)
            self.posts.append(SocialMediaPost("Instagram", content, post_time, f"media/engagement_{post_type}.jpg"))
    
    def get_schedule(self) -> List[Dict]:
        """Return the schedule as a list of dictionaries"""
        return [
            {
                "platform": post.platform,
                "content": post.content,
                "datetime": post.post_time.strftime("%Y-%m-%d %H:%M"),
                "media": post.media_path
            }
            for post in sorted(self.posts, key=lambda x: x.post_time)
        ]

# Example usage
if __name__ == "__main__":
    brand_name = "EcoChic"
    collection_name = "Summer Essentials 2023"
    start_date = datetime.date(2023, 6, 1)
    duration = 28  # 4 weeks
    
    schedule = PostSchedule(brand_name, collection_name, start_date, duration)
    schedule.generate_schedule()
    
    # Print the schedule
    for post in schedule.get_schedule():
        print(f"{post['datetime']} - {post['platform']}:")
        print(post['content'])
        print(f"Media: {post['media']}")
        print("-" * 50)
```
