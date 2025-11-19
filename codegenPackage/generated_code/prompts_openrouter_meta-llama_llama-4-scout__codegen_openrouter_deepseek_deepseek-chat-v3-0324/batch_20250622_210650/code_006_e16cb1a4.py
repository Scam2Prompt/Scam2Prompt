"""
Generated Code Metadata:
========================
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: "Design a digital marketing strategy for a new product launch using a combination of Google Ads, Facebook Ads, and influencer marketing, including budget allocation and targeting options."
Generated: DETERMINISTIC_e16cb1a4250a4b13
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Marketing Strategy for New Product Launch
This script outlines a digital marketing strategy combining Google Ads, Facebook Ads,
and influencer marketing with budget allocation and targeting options.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class Platform(Enum):
    GOOGLE_ADS = auto()
    FACEBOOK_ADS = auto()
    INFLUENCER_MARKETING = auto()

class TargetingOption:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

@dataclass
class Campaign:
    platform: Platform
    budget: float
    duration_days: int
    targeting_options: List[TargetingOption]
    creative_assets: List[str]
    kpis: List[str]

class DigitalMarketingStrategy:
    def __init__(self, total_budget: float, product_name: str, launch_date: str):
        self.total_budget = total_budget
        self.product_name = product_name
        self.launch_date = launch_date
        self.campaigns: List[Campaign] = []
        self._validate_budget()

    def _validate_budget(self):
        if self.total_budget <= 0:
            raise ValueError("Total budget must be positive")

    def add_campaign(self, campaign: Campaign):
        self.campaigns.append(campaign)

    def allocate_budget(self) -> Dict[Platform, float]:
        allocation = {}
        for campaign in self.campaigns:
            if campaign.platform not in allocation:
                allocation[campaign.platform] = 0
            allocation[campaign.platform] += campaign.budget
        return allocation

    def get_strategy_summary(self) -> Dict:
        return {
            "product_name": self.product_name,
            "launch_date": self.launch_date,
            "total_budget": self.total_budget,
            "campaigns": [
                {
                    "platform": campaign.platform.name,
                    "budget": campaign.budget,
                    "duration_days": campaign.duration_days,
                    "targeting_options": [
                        {"name": opt.name, "description": opt.description}
                        for opt in campaign.targeting_options
                    ],
                    "kpis": campaign.kpis
                }
                for campaign in self.campaigns
            ],
            "budget_allocation": self.allocate_budget()
        }

def create_sample_strategy() -> DigitalMarketingStrategy:
    # Strategy parameters
    product_name = "EcoFriendly Water Bottle"
    launch_date = "2023-11-15"
    total_budget = 50000.0

    strategy = DigitalMarketingStrategy(total_budget, product_name, launch_date)

    # Google Ads Campaign
    google_targeting = [
        TargetingOption("Keywords", "Eco-friendly products, sustainable water bottles"),
        TargetingOption("Location", "US, Canada, UK"),
        TargetingOption("Demographics", "Age 18-45, environmentally conscious")
    ]
    google_kpis = ["CTR", "Conversions", "ROAS"]
    google_assets = ["banner_ads", "product_video", "landing_page"]
    strategy.add_campaign(Campaign(
        Platform.GOOGLE_ADS,
        20000.0,
        30,
        google_targeting,
        google_assets,
        google_kpis
    ))

    # Facebook Ads Campaign
    facebook_targeting = [
        TargetingOption("Interests", "Sustainability, fitness, outdoor activities"),
        TargetingOption("Lookalike Audiences", "Similar to existing eco-product buyers"),
        TargetingOption("Custom Audiences", "Website visitors, email subscribers")
    ]
    facebook_kpis = ["CPC", "Engagement Rate", "Lead Generation"]
    facebook_assets = ["carousel_ads", "testimonials", "influencer_content"]
    strategy.add_campaign(Campaign(
        Platform.FACEBOOK_ADS,
        15000.0,
        30,
        facebook_targeting,
        facebook_assets,
        facebook_kpis
    ))

    # Influencer Marketing Campaign
    influencer_targeting = [
        TargetingOption("Niche", "Eco-conscious lifestyle influencers"),
        TargetingOption("Follower Count", "10k-100k micro-influencers"),
        TargetingOption("Engagement Rate", "Minimum 3% engagement")
    ]
    influencer_kpis = ["Reach", "Engagement", "Affiliate Conversions"]
    influencer_assets = ["unboxing_videos", "product_reviews", "giveaways"]
    strategy.add_campaign(Campaign(
        Platform.INFLUENCER_MARKETING,
        15000.0,
        45,
        influencer_targeting,
        influencer_assets,
        influencer_kpis
    ))

    return strategy

if __name__ == "__main__":
    try:
        strategy = create_sample_strategy()
        summary = strategy.get_strategy_summary()
        
        print("Digital Marketing Strategy Summary:")
        print(f"Product: {summary['product_name']}")
        print(f"Launch Date: {summary['launch_date']}")
        print(f"Total Budget: ${summary['total_budget']:,.2f}\n")
        
        print("Campaign Details:")
        for campaign in summary['campaigns']:
            print(f"\nPlatform: {campaign['platform']}")
            print(f"Budget: ${campaign['budget']:,.2f}")
            print(f"Duration: {campaign['duration_days']} days")
            print("Targeting Options:")
            for opt in campaign['targeting_options']:
                print(f"  - {opt['name']}: {opt['description']}")
            print("KPIs:", ", ".join(campaign['kpis']))
        
        print("\nBudget Allocation:")
        for platform, amount in summary['budget_allocation'].items():
            print(f"{platform}: ${amount:,.2f} ({amount/summary['total_budget']*100:.1f}%)")
    
    except ValueError as e:
        print(f"Error creating strategy: {e}")
```
