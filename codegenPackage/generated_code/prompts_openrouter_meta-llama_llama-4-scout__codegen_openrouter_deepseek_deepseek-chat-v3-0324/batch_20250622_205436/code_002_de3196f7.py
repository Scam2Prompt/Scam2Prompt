"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Create a social media video content strategy for a brand that wants to increase engagement and drive real results, focusing on building a personality-driven brand as suggested by Kraken Media.
Generated: DETERMINISTIC_de3196f7c102362d
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Video Content Strategy Generator
Based on Kraken Media's personality-driven brand approach
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import random
from datetime import datetime, timedelta

class ContentType(Enum):
    EDUCATIONAL = auto()
    ENTERTAINING = auto()
    BEHIND_THE_SCENES = auto()
    USER_GENERATED = auto()
    PROMOTIONAL = auto()
    TESTIMONIAL = auto()

@dataclass
class VideoContent:
    title: str
    description: str
    content_type: ContentType
    duration: int  # in seconds
    call_to_action: str
    posting_time: datetime
    platform: str
    hashtags: List[str]
    engagement_boosters: List[str]

class ContentStrategyGenerator:
    def __init__(self, brand_name: str, brand_personality: Dict[str, str]):
        self.brand_name = brand_name
        self.brand_personality = brand_personality
        self.content_types = list(ContentType)
        
    def _generate_hashtags(self) -> List[str]:
        base_tags = [f"#{self.brand_name}", "#BrandPersonality", "#EngagementBoost"]
        personality_tags = [f"#{value.replace(' ', '')}" for value in self.brand_personality.values()]
        return base_tags + personality_tags
    
    def _generate_engagement_boosters(self) -> List[str]:
        return [
            "Ask a question in the comments!",
            "Tag a friend who needs to see this!",
            "Double-tap if you agree!",
            "Save for later!",
            "What's your take? Comment below!"
        ]
    
    def _generate_cta(self, content_type: ContentType) -> str:
        ctas = {
            ContentType.EDUCATIONAL: "Learn more in our bio!",
            ContentType.ENTERTAINING: "Follow for more fun content!",
            ContentType.BEHIND_THE_SCENES: "Want to see more BTS? Let us know!",
            ContentType.USER_GENERATED: "Tag us in your posts!",
            ContentType.PROMOTIONAL: "Limited time offer - check bio!",
            ContentType.TESTIMONIAL: "Ready to experience it yourself?"
        }
        return ctas.get(content_type, "Check out our bio for more!")
    
    def _generate_title(self, content_type: ContentType) -> str:
        titles = {
            ContentType.EDUCATIONAL: f"Did you know this about {self.brand_name}?",
            ContentType.ENTERTAINING: f"Fun with {self.brand_name} - you won't believe this!",
            ContentType.BEHIND_THE_SCENES: f"What really happens at {self.brand_name}...",
            ContentType.USER_GENERATED: f"Our favorite {self.brand_name} moments from YOU!",
            ContentType.PROMOTIONAL: f"Exciting news from {self.brand_name}!",
            ContentType.TESTIMONIAL: f"Real people, real results with {self.brand_name}"
        }
        return titles.get(content_type, f"New from {self.brand_name}!")
    
    def _generate_description(self, content_type: ContentType) -> str:
        descriptions = {
            ContentType.EDUCATIONAL: f"Learn something new about {self.brand_name} today!",
            ContentType.ENTERTAINING: f"Because {self.brand_personality.get('tone', 'we')} know how to have fun!",
            ContentType.BEHIND_THE_SCENES: f"Get an exclusive look at how {self.brand_name} works!",
            ContentType.USER_GENERATED: f"Featuring our amazing community! {self.brand_personality.get('community_callout', '')}",
            ContentType.PROMOTIONAL: f"Don't miss this special offer from {self.brand_name}!",
            ContentType.TESTIMONIAL: f"See what people are saying about {self.brand_name}!"
        }
        return descriptions.get(content_type, f"New content from {self.brand_name}!")
    
    def _get_optimal_posting_time(self) -> datetime:
        # Simplified optimal posting times (would be more sophisticated in production)
        now = datetime.now()
        optimal_hours = [9, 12, 15, 18, 21]  # 9AM, 12PM, 3PM, 6PM, 9PM
        hour = random.choice(optimal_hours)
        return now.replace(hour=hour, minute=0, second=0) + timedelta(days=random.randint(1, 7))
    
    def generate_content_plan(self, weeks: int = 4) -> List[VideoContent]:
        plan = []
        for _ in range(weeks * 3):  # 3 posts per week
            content_type = random.choice(self.content_types)
            duration = random.randint(15, 90)  # 15-90 seconds
            
            content = VideoContent(
                title=self._generate_title(content_type),
                description=self._generate_description(content_type),
                content_type=content_type,
                duration=duration,
                call_to_action=self._generate_cta(content_type),
                posting_time=self._get_optimal_posting_time(),
                platform=random.choice(["Instagram", "TikTok", "YouTube Shorts"]),
                hashtags=self._generate_hashtags(),
                engagement_boosters=self._generate_engagement_boosters()
            )
            plan.append(content)
        
        return sorted(plan, key=lambda x: x.posting_time)

# Example usage
if __name__ == "__main__":
    brand_personality = {
        "tone": "fun and energetic",
        "values": "authenticity creativity community",
        "voice": "conversational",
        "community_callout": "You make this brand special!"
    }
    
    generator = ContentStrategyGenerator("KrakenMedia", brand_personality)
    content_plan = generator.generate_content_plan(weeks=4)
    
    print(f"Generated {len(content_plan)} video content ideas:")
    for i, content in enumerate(content_plan, 1):
        print(f"\n{i}. {content.title}")
        print(f"Type: {content.content_type.name}")
        print(f"Platform: {content.platform}")
        print(f"Posting time: {content.posting_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Description: {content.description}")
        print(f"CTA: {content.call_to_action}")
        print(f"Hashtags: {', '.join(content.hashtags)}")
```
