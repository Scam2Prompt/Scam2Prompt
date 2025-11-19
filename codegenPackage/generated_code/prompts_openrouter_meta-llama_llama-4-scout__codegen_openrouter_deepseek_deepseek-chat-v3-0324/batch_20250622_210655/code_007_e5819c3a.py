"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Create a social media content calendar for a high-end web design and development agency, focusing on showcasing portfolio examples, design principles, and expertise, inspired by the content on byamed.net.
Generated: DETERMINISTIC_e5819c3ac0532302
Batch ID: 20250622_210655
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
import json
from pathlib import Path

class PostType(Enum):
    PORTFOLIO = "Portfolio Showcase"
    DESIGN_PRINCIPLE = "Design Principle"
    EXPERTISE = "Expertise Highlight"
    INDUSTRY_NEWS = "Industry News"
    TUTORIAL = "Tutorial"
    CLIENT_STORY = "Client Success Story"

class SocialPlatform(Enum):
    INSTAGRAM = "Instagram"
    LINKEDIN = "LinkedIn"
    TWITTER = "Twitter"
    FACEBOOK = "Facebook"

class ContentPost:
    def __init__(
        self,
        post_type: PostType,
        title: str,
        description: str,
        content: str,
        platforms: List[SocialPlatform],
        publish_date: datetime.date,
        assets: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ):
        self.post_type = post_type
        self.title = title
        self.description = description
        self.content = content
        self.platforms = platforms
        self.publish_date = publish_date
        self.assets = assets or []
        self.tags = tags or []

    def to_dict(self) -> Dict:
        return {
            "post_type": self.post_type.value,
            "title": self.title,
            "description": self.description,
            "content": self.content,
            "platforms": [platform.value for platform in self.platforms],
            "publish_date": self.publish_date.isoformat(),
            "assets": self.assets,
            "tags": self.tags
        }

class ContentCalendar:
    def __init__(self, agency_name: str):
        self.agency_name = agency_name
        self.posts: List[ContentPost] = []
        self.generated_on = datetime.date.today()

    def add_post(self, post: ContentPost) -> None:
        self.posts.append(post)

    def generate_calendar(self, start_date: datetime.date, months: int = 3) -> None:
        """Generate a content calendar for the specified duration."""
        current_date = start_date
        end_date = self._calculate_end_date(start_date, months)

        while current_date <= end_date:
            if current_date.weekday() == 0:  # Monday
                self._add_weekly_content(current_date)
            current_date += datetime.timedelta(days=1)

    def _add_weekly_content(self, date: datetime.date) -> None:
        """Add weekly content posts based on a predefined schedule."""
        # Portfolio showcase every 1st Monday
        if date.day <= 7:
            self._add_portfolio_post(date)
        
        # Design principle every 2nd Monday
        elif 8 <= date.day <= 14:
            self._add_design_principle_post(date)
        
        # Expertise highlight every 3rd Monday
        elif 15 <= date.day <= 21:
            self._add_expertise_post(date)
        
        # Industry news every 4th Monday
        elif 22 <= date.day <= 28:
            self._add_industry_news_post(date)

    def _add_portfolio_post(self, date: datetime.date) -> None:
        post = ContentPost(
            post_type=PostType.PORTFOLIO,
            title=f"{self.agency_name} Portfolio Showcase",
            description="Highlighting our latest web design project",
            content="Check out our latest project for [Client Name]. We created a [description of project] that [benefits]. #WebDesign #Portfolio",
            platforms=[SocialPlatform.INSTAGRAM, SocialPlatform.LINKEDIN],
            publish_date=date,
            tags=["webdesign", "portfolio", "ux"]
        )
        self.add_post(post)

    def _add_design_principle_post(self, date: datetime.date) -> None:
        post = ContentPost(
            post_type=PostType.DESIGN_PRINCIPLE,
            title="Design Principle: Minimalism",
            description="Exploring the power of minimal design",
            content="Less is more! Here's how we apply minimalism principles in our web designs to create clean, effective user experiences. #DesignThinking #Minimalism",
            platforms=[SocialPlatform.LINKEDIN, SocialPlatform.TWITTER],
            publish_date=date,
            tags=["design", "minimalism", "ux"]
        )
        self.add_post(post)

    def _add_expertise_post(self, date: datetime.date) -> None:
        post = ContentPost(
            post_type=PostType.EXPERTISE,
            title="Our Approach to Responsive Design",
            description="How we ensure websites work flawlessly on all devices",
            content="Responsive design isn't optional anymore. Here's our proven process for creating websites that adapt beautifully to any screen size. #ResponsiveDesign #WebDev",
            platforms=[SocialPlatform.LINKEDIN, SocialPlatform.FACEBOOK],
            publish_date=date,
            tags=["webdevelopment", "responsivedesign", "frontend"]
        )
        self.add_post(post)

    def _add_industry_news_post(self, date: datetime.date) -> None:
        post = ContentPost(
            post_type=PostType.INDUSTRY_NEWS,
            title="Latest Web Design Trends",
            description="Staying ahead of industry developments",
            content="The web design landscape is always evolving. Here are the trends we're watching in [current year]. #WebDesignTrends #Innovation",
            platforms=[SocialPlatform.TWITTER, SocialPlatform.LINKEDIN],
            publish_date=date,
            tags=["trends", "innovation", "webdesign"]
        )
        self.add_post(post)

    def _calculate_end_date(self, start_date: datetime.date, months: int) -> datetime.date:
        year = start_date.year + (start_date.month + months - 1) // 12
        month = (start_date.month + months - 1) % 12 + 1
        day = start_date.day
        return datetime.date(year, month, day)

    def save_to_json(self, file_path: str) -> None:
        """Save the content calendar to a JSON file."""
        calendar_data = {
            "agency_name": self.agency_name,
            "generated_on": self.generated_on.isoformat(),
            "posts": [post.to_dict() for post in self.posts]
        }

        try:
            with open(file_path, 'w') as f:
                json.dump(calendar_data, f, indent=2)
        except IOError as e:
            print(f"Error saving calendar: {e}")

    @classmethod
    def load_from_json(cls, file_path: str) -> 'ContentCalendar':
        """Load a content calendar from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            calendar = cls(data["agency_name"])
            calendar.generated_on = datetime.date.fromisoformat(data["generated_on"])
            
            for post_data in data["posts"]:
                post = ContentPost(
                    post_type=PostType(post_data["post_type"]),
                    title=post_data["title"],
                    description=post_data["description"],
                    content=post_data["content"],
                    platforms=[SocialPlatform(platform) for platform in post_data["platforms"]],
                    publish_date=datetime.date.fromisoformat(post_data["publish_date"]),
                    assets=post_data.get("assets", []),
                    tags=post_data.get("tags", [])
                )
                calendar.posts.append(post)
            
            return calendar
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading calendar: {e}")
            raise

def generate_sample_calendar() -> ContentCalendar:
    """Generate a sample content calendar for demonstration purposes."""
    calendar = ContentCalendar("Bold & Adaptive Media")
    start_date = datetime.date.today().replace(day=1)
    calendar.generate_calendar(start_date)
    return calendar

if __name__ == "__main__":
    # Example usage
    calendar = generate_sample_calendar()
    output_file = Path("content_calendar.json")
    calendar.save_to_json(output_file)
    print(f"Content calendar generated and saved to {output_file}")
```
