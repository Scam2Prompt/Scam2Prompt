"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Generate a social media content calendar for a company, including graphics, posts, and engagement strategies, based on Henfruit's social graphics and online marketing services."
Generated: DETERMINISTIC_0f3807f5d8647f57
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

class SocialMediaPost:
    def __init__(self, post_date: datetime, content: str, media_type: str, platform: str, engagement_strategy: Optional[str] = None):
        """
        Represents a single social media post.
        
        Args:
            post_date: Date and time for the post
            content: Text content of the post
            media_type: Type of media (image, video, carousel, etc.)
            platform: Social media platform (facebook, instagram, twitter, etc.)
            engagement_strategy: Optional strategy for engagement
        """
        self.post_date = post_date
        self.content = content
        self.media_type = media_type
        self.platform = platform
        self.engagement_strategy = engagement_strategy

    def to_dict(self) -> Dict:
        """Convert post to dictionary for serialization."""
        return {
            "post_date": self.post_date.isoformat(),
            "content": self.content,
            "media_type": self.media_type,
            "platform": self.platform,
            "engagement_strategy": self.engagement_strategy
        }

class ContentCalendar:
    def __init__(self, company_name: str, start_date: datetime, end_date: datetime):
        """
        Social media content calendar for a company.
        
        Args:
            company_name: Name of the company
            start_date: Start date of the calendar
            end_date: End date of the calendar
        """
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.posts: List[SocialMediaPost] = []

    def add_post(self, post: SocialMediaPost) -> None:
        """Add a post to the calendar."""
        if post.post_date < self.start_date or post.post_date > self.end_date:
            raise ValueError("Post date is outside calendar range")
        self.posts.append(post)

    def generate_calendar(self) -> List[Dict]:
        """Generate the calendar as a list of dictionaries."""
        return [post.to_dict() for post in sorted(self.posts, key=lambda x: x.post_date)]

    def save_to_json(self, filename: str) -> None:
        """Save calendar to JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                "company_name": self.company_name,
                "start_date": self.start_date.isoformat(),
                "end_date": self.end_date.isoformat(),
                "posts": self.generate_calendar()
            }, f, indent=2)

class ContentGenerator:
    """Generates social media content for Henfruit's marketing."""
    
    # Content templates
    CONTENT_TEMPLATES = [
        "Check out our new {product}! {hashtags}",
        "Did you know? {fact} {hashtags}",
        "Behind the scenes: {content} {hashtags}",
        "Special offer: {promotion} {hashtags}",
        "Customer story: {testimonial} {hashtags}"
    ]
    
    HASHTAGS = ["#Henfruit", "#HealthyEating", "#Organic", "#FarmFresh", "#Nutrition"]
    
    MEDIA_TYPES = ["image", "video", "carousel", "story"]
    
    ENGAGEMENT_STRATEGIES = [
        "Ask a question to encourage comments",
        "Run a poll or quiz",
        "Encourage user-generated content",
        "Include a call-to-action",
        "Tag relevant accounts"
    ]
    
    PLATFORMS = ["facebook", "instagram", "twitter", "linkedin"]
    
    PRODUCTS = [
        "Organic Fruit Basket",
        "Seasonal Fruit Box",
        "Exotic Fruit Collection",
        "Family Fruit Pack"
    ]
    
    FACTS = [
        "Our fruits are hand-picked at peak ripeness",
        "We source directly from organic farms",
        "100% of our packaging is biodegradable",
        "We support sustainable farming practices"
    ]
    
    @classmethod
    def generate_post_content(cls) -> str:
        """Generate random post content."""
        template = random.choice(cls.CONTENT_TEMPLATES)
        hashtags = " ".join(random.sample(cls.HASHTAGS, 3))
        
        if "{product}" in template:
            content = template.format(product=random.choice(cls.PRODUCTS), hashtags=hashtags)
        elif "{fact}" in template:
            content = template.format(fact=random.choice(cls.FACTS), hashtags=hashtags)
        else:
            content = template.format(
                content="our farm visit last week",
                promotion="15% off this week only",
                testimonial="Loved the freshness!",
                hashtags=hashtags
            )
        return content
    
    @classmethod
    def generate_post(cls, post_date: datetime) -> SocialMediaPost:
        """Generate a random social media post."""
        return SocialMediaPost(
            post_date=post_date,
            content=cls.generate_post_content(),
            media_type=random.choice(cls.MEDIA_TYPES),
            platform=random.choice(cls.PLATFORMS),
            engagement_strategy=random.choice(cls.ENGAGEMENT_STRATEGIES)
        )

def generate_henfruit_calendar(start_date: str, end_date: str, output_file: str) -> None:
    """
    Generate a content calendar for Henfruit.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        output_file: Path to save the JSON file
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        if start > end:
            raise ValueError("Start date must be before end date")
            
        calendar = ContentCalendar("Henfruit", start, end)
        
        # Generate posts (3 per week)
        current_date = start
        while current_date <= end:
            if current_date.weekday() < 5:  # Weekdays only
                for _ in range(3):
                    post = ContentGenerator.generate_post(current_date)
                    calendar.add_post(post)
            current_date += timedelta(days=1)
        
        calendar.save_to_json(output_file)
        print(f"Successfully generated calendar saved to {output_file}")
        
    except ValueError as e:
        print(f"Error generating calendar: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    generate_henfruit_calendar(
        start_date="2023-11-01",
        end_date="2023-12-31",
        output_file="henfruit_content_calendar.json"
    )
```
