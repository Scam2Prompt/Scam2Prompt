"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Develop a digital marketing campaign plan using data-driven strategies as outlined by Alpha Digital Solutions, focusing on local businesses in Ethiopia.
Generated: DETERMINISTIC_1e9fbafa8f2974fe
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Marketing Campaign Planner for Local Businesses in Ethiopia
This script helps plan data-driven digital marketing campaigns based on Alpha Digital Solutions' strategies.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd
from enum import Enum

class CampaignChannel(Enum):
    """Enumeration of available digital marketing channels"""
    SOCIAL_MEDIA = "Social Media"
    SEARCH_ENGINE = "Search Engine"
    EMAIL = "Email"
    DISPLAY_ADS = "Display Ads"
    SMS = "SMS"

class BusinessCategory(Enum):
    """Common business categories in Ethiopia"""
    RETAIL = "Retail"
    HOSPITALITY = "Hospitality"
    SERVICES = "Services"
    MANUFACTURING = "Manufacturing"
    AGRICULTURE = "Agriculture"

class CampaignPlan:
    """Main class for creating digital marketing campaign plans"""
    
    def __init__(self, business_name: str, category: BusinessCategory, budget: float, duration_weeks: int):
        """
        Initialize a new campaign plan
        
        Args:
            business_name: Name of the business
            category: Business category from BusinessCategory enum
            budget: Total budget in ETB
            duration_weeks: Duration of campaign in weeks
        """
        self.business_name = business_name
        self.category = category
        self.budget = budget
        self.duration_weeks = duration_weeks
        self.channels = []
        self.key_metrics = {}
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(weeks=duration_weeks)
        self.audience = {}
        self.content_plan = []
        
    def add_channel(self, channel: CampaignChannel, allocation: float, strategy: str):
        """
        Add a marketing channel to the campaign
        
        Args:
            channel: Channel from CampaignChannel enum
            allocation: Budget allocation (0-1)
            strategy: Strategy description for this channel
        """
        if allocation < 0 or allocation > 1:
            raise ValueError("Allocation must be between 0 and 1")
            
        if sum(c['allocation'] for c in self.channels) + allocation > 1:
            raise ValueError("Total channel allocations cannot exceed 1")
            
        self.channels.append({
            'channel': channel,
            'allocation': allocation,
            'budget': self.budget * allocation,
            'strategy': strategy
        })
    
    def set_audience(self, demographics: Dict, interests: List[str], locations: List[str]):
        """
        Define target audience for the campaign
        
        Args:
            demographics: Dictionary of demographic info (age_range, gender, etc.)
            interests: List of audience interests
            locations: List of target locations in Ethiopia
        """
        self.audience = {
            'demographics': demographics,
            'interests': interests,
            'locations': locations
        }
    
    def add_content(self, content_type: str, theme: str, platforms: List[str], schedule: datetime):
        """
        Add content to the content plan
        
        Args:
            content_type: Type of content (post, video, ad, etc.)
            theme: Content theme/message
            platforms: Platforms to publish on
            schedule: When to publish
        """
        self.content_plan.append({
            'content_type': content_type,
            'theme': theme,
            'platforms': platforms,
            'schedule': schedule
        })
    
    def set_metrics(self, primary_goal: str, secondary_goals: List[str], kpis: Dict):
        """
        Define campaign metrics and KPIs
        
        Args:
            primary_goal: Main campaign goal
            secondary_goals: List of secondary goals
            kpis: Dictionary of key performance indicators
        """
        self.key_metrics = {
            'primary_goal': primary_goal,
            'secondary_goals': secondary_goals,
            'kpis': kpis
        }
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive campaign report"""
        return {
            'business': self.business_name,
            'category': self.category.value,
            'budget': self.budget,
            'duration_weeks': self.duration_weeks,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'channels': [{
                'channel': c['channel'].value,
                'allocation': c['allocation'],
                'budget': c['budget'],
                'strategy': c['strategy']
            } for c in self.channels],
            'audience': self.audience,
            'content_plan': [{
                'content_type': c['content_type'],
                'theme': c['theme'],
                'platforms': c['platforms'],
                'schedule': c['schedule'].strftime('%Y-%m-%d %H:%M')
            } for c in self.content_plan],
            'metrics': self.key_metrics
        }
    
    def save_to_json(self, filename: str):
        """Save the campaign plan to a JSON file"""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

def load_ethiopian_cities() -> List[str]:
    """Load list of major Ethiopian cities for targeting"""
    return [
        "Addis Ababa", "Dire Dawa", "Mekelle", "Gondar", "Awasa",
        "Bahir Dar", "Jimma", "Dessie", "Jijiga", "Shashamane"
    ]

def suggest_channels_for_category(category: BusinessCategory) -> List[CampaignChannel]:
    """Suggest appropriate channels based on business category"""
    suggestions = {
        BusinessCategory.RETAIL: [
            CampaignChannel.SOCIAL_MEDIA,
            CampaignChannel.SEARCH_ENGINE,
            CampaignChannel.SMS
        ],
        BusinessCategory.HOSPITALITY: [
            CampaignChannel.SOCIAL_MEDIA,
            CampaignChannel.SEARCH_ENGINE,
            CampaignChannel.EMAIL
        ],
        BusinessCategory.SERVICES: [
            CampaignChannel.SOCIAL_MEDIA,
            CampaignChannel.SEARCH_ENGINE,
            CampaignChannel.DISPLAY_ADS
        ],
        BusinessCategory.MANUFACTURING: [
            CampaignChannel.SEARCH_ENGINE,
            CampaignChannel.EMAIL,
            CampaignChannel.DISPLAY_ADS
        ],
        BusinessCategory.AGRICULTURE: [
            CampaignChannel.SOCIAL_MEDIA,
            CampaignChannel.SMS
        ]
    }
    return suggestions.get(category, [])

def create_sample_campaign() -> CampaignPlan:
    """Create a sample campaign for demonstration purposes"""
    campaign = CampaignPlan(
        business_name="Habesha Coffee",
        category=BusinessCategory.HOSPITALITY,
        budget=50000,
        duration_weeks=8
    )
    
    # Add channels
    campaign.add_channel(
        channel=CampaignChannel.SOCIAL_MEDIA,
        allocation=0.4,
        strategy="Engage local coffee lovers with daily posts and stories"
    )
    campaign.add_channel(
        channel=CampaignChannel.SEARCH_ENGINE,
        allocation=0.3,
        strategy="Target coffee-related keywords in Addis Ababa"
    )
    campaign.add_channel(
        channel=CampaignChannel.EMAIL,
        allocation=0.2,
        strategy="Send weekly newsletters to subscribers"
    )
    campaign.add_channel(
        channel=CampaignChannel.SMS,
        allocation=0.1,
        strategy="Send promotional offers to loyalty program members"
    )
    
    # Set audience
    campaign.set_audience(
        demographics={
            'age_range': (18, 45),
            'gender': 'all',
            'income_level': 'middle'
        },
        interests=["coffee", "cafes", "local business"],
        locations=["Addis Ababa", "Bole", "Megenagna"]
    )
    
    # Add content
    today = datetime.now()
    campaign.add_content(
        content_type="video",
        theme="Our coffee brewing process",
        platforms=["Facebook", "Instagram"],
        schedule=today + timedelta(days=2)
    )
    campaign.add_content(
        content_type="post",
        theme="Customer testimonials",
        platforms=["Facebook", "Telegram"],
        schedule=today + timedelta(days=5)
    )
    
    # Set metrics
    campaign.set_metrics(
        primary_goal="Increase foot traffic by 30%",
        secondary_goals=[
            "Grow social media following by 20%",
            "Collect 500 new email subscribers"
        ],
        kpis={
            'ctr': 0.05,
            'conversion_rate': 0.03,
            'roi': 2.5
        }
    )
    
    return campaign

if __name__ == "__main__":
    # Example usage
    try:
        campaign = create_sample_campaign()
        report = campaign.generate_report()
        print(json.dumps(report, indent=4))
        campaign.save_to_json("habesha_coffee_campaign.json")
