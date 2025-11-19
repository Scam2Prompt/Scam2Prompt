"""
Generated Code Metadata:
========================
Original URL: https://thebalichili.com
Prompt: Design a content strategy for a local food business in Jakarta using social media platforms, including content creation and organic optimization.
Generated: DETERMINISTIC_71f59492b31fb8ce
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import random

class SocialMediaPlatform(Enum):
    """Enumeration of supported social media platforms."""
    INSTAGRAM = "Instagram"
    FACEBOOK = "Facebook"
    TIKTOK = "TikTok"
    TWITTER = "Twitter"

class ContentType(Enum):
    """Types of content that can be created."""
    IMAGE = "Image"
    VIDEO = "Video"
    STORY = "Story"
    REEL = "Reel"
    LIVE = "Live"
    POST = "Post"

class ContentTheme(Enum):
    """Themes for content creation."""
    PROMOTION = "Promotion"
    BEHIND_THE_SCENES = "Behind the Scenes"
    CUSTOMER_REVIEW = "Customer Review"
    RECIPE = "Recipe"
    LOCAL_CULTURE = "Local Culture"
    SPECIAL_EVENT = "Special Event"

class ContentStrategy:
    """Main class for managing content strategy."""
    
    def __init__(self, business_name: str, location: str = "Jakarta"):
        self.business_name = business_name
        self.location = location
        self.content_calendar: Dict[datetime.date, List[Dict]] = {}
        self.platforms: List[SocialMediaPlatform] = [
            SocialMediaPlatform.INSTAGRAM,
            SocialMediaPlatform.FACEBOOK,
            SocialMediaPlatform.TIKTOK
        ]
        
    def generate_content_ideas(self, theme: ContentTheme, count: int = 5) -> List[str]:
        """Generate content ideas based on theme."""
        ideas = {
            ContentTheme.PROMOTION: [
                f"New menu alert! Try our {random.choice(['spicy', 'sweet', 'crunchy'])} special",
                "Limited time offer: 20% off all desserts this weekend",
                "Happy hour deals from 4-6PM daily"
            ],
            ContentTheme.BEHIND_THE_SCENES: [
                "Meet our chef preparing today's special",
                "How we source our fresh ingredients locally",
                "A day in the life of our kitchen staff"
            ],
            ContentTheme.CUSTOMER_REVIEW: [
                "Customer spotlight: What people say about our food",
                "Our most popular dish according to customers",
                "Video testimonials from happy customers"
            ],
            ContentTheme.RECIPE: [
                "How to make our signature dish at home",
                "Secret family recipe revealed",
                "Cooking tutorial: Quick and easy version of our bestseller"
            ],
            ContentTheme.LOCAL_CULTURE: [
                "How our food connects to Jakarta's heritage",
                "Traditional cooking methods we still use today",
                "Local ingredients that make our food special"
            ],
            ContentTheme.SPECIAL_EVENT: [
                "Join us for our anniversary celebration",
                "Live music nights every Friday",
                "Cooking workshop for kids this Sunday"
            ]
        }
        
        return random.sample(ideas[theme], min(count, len(ideas[theme])))
    
    def schedule_content(
        self,
        date: datetime.date,
        content_type: ContentType,
        theme: ContentTheme,
        platforms: List[SocialMediaPlatform],
        caption: str,
        hashtags: Optional[List[str]] = None
    ) -> bool:
        """Schedule content for specific date and platforms."""
        if date < datetime.date.today():
            raise ValueError("Cannot schedule content in the past")
            
        if not platforms:
            raise ValueError("At least one platform must be specified")
            
        content = {
            "type": content_type,
            "theme": theme,
            "platforms": platforms,
            "caption": caption,
            "hashtags": hashtags or self._generate_hashtags(theme),
            "scheduled_time": datetime.datetime.now()
        }
        
        if date not in self.content_calendar:
            self.content_calendar[date] = []
            
        self.content_calendar[date].append(content)
        return True
    
    def _generate_hashtags(self, theme: ContentTheme) -> List[str]:
        """Generate relevant hashtags based on content theme."""
        base_tags = [f"#{self.business_name.replace(' ', '')}", "#JakartaEats", "#Foodie"]
        
        theme_tags = {
            ContentTheme.PROMOTION: ["#FoodDeals", "#EatLocal", "#SpecialOffer"],
            ContentTheme.BEHIND_THE_SCENES: ["#KitchenLife", "#MeetTheTeam", "#HowItsMade"],
            ContentTheme.CUSTOMER_REVIEW: ["#CustomerLove", "#FoodReview", "#Testimonial"],
            ContentTheme.RECIPE: ["#HomeCooking", "#RecipeOfTheDay", "#CookingTips"],
            ContentTheme.LOCAL_CULTURE: ["#JakartaFood", "#LocalFlavors", "#CulturalFood"],
            ContentTheme.SPECIAL_EVENT: ["#FoodEvent", "#WhatsHappening", "#JoinUs"]
        }
        
        return base_tags + theme_tags[theme]
    
    def optimize_post_time(self, platform: SocialMediaPlatform) -> datetime.time:
        """Suggest optimal posting time based on platform."""
        optimal_times = {
            SocialMediaPlatform.INSTAGRAM: datetime.time(11, 0),
            SocialMediaPlatform.FACEBOOK: datetime.time(13, 0),
            SocialMediaPlatform.TIKTOK: datetime.time(17, 0),
            SocialMediaPlatform.TWITTER: datetime.time(9, 0)
        }
        return optimal_times.get(platform, datetime.time(12, 0))
    
    def generate_weekly_plan(self, start_date: datetime.date) -> Dict[datetime.date, List[Dict]]:
        """Generate a weekly content plan."""
        if start_date < datetime.date.today():
            raise ValueError("Start date cannot be in the past")
            
        themes = list(ContentTheme)
        content_types = list(ContentType)
        
        for day in range(7):
            current_date = start_date + datetime.timedelta(days=day)
            theme = random.choice(themes)
            content_type = random.choice(content_types)
            
            ideas = self.generate_content_ideas(theme, 1)
            if not ideas:
                continue
                
            self.schedule_content(
                date=current_date,
                content_type=content_type,
                theme=theme,
                platforms=self.platforms,
                caption=ideas[0]
            )
            
        return self.content_calendar
    
    def get_scheduled_content(self, date: datetime.date) -> List[Dict]:
        """Retrieve scheduled content for a specific date."""
        return self.content_calendar.get(date, [])

# Example usage
if __name__ == "__main__":
    strategy = ContentStrategy(business_name="Jakarta Bites")
    
    # Generate weekly plan starting tomorrow
    start_date = datetime.date.today() + datetime.timedelta(days=1)
    weekly_plan = strategy.generate_weekly_plan(start_date)
    
    # Print scheduled content
    for date, contents in weekly_plan.items():
        print(f"\nDate: {date}")
        for content in contents:
            print(f"Type: {content['type'].value}")
            print(f"Theme: {content['theme'].value}")
            print(f"Platforms: {[p.value for p in content['platforms']]}")
            print(f"Caption: {content['caption']}")
            print(f"Hashtags: {content['hashtags']}")
            print("---")
```
