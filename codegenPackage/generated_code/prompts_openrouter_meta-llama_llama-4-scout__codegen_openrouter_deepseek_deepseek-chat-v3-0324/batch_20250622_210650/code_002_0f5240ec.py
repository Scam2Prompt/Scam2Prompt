"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Generate a sample social media marketing strategy using Facebook advertising for a small business, including content creation and targeting options."
Generated: DETERMINISTIC_0f5240ec26a8caf5
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
Facebook Marketing Strategy Generator for Small Businesses

This script generates a sample social media marketing strategy for Facebook ads,
including content creation ideas and targeting options.
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple

class FacebookMarketingStrategy:
    """
    Generates a Facebook marketing strategy with content ideas and targeting options.
    """
    
    def __init__(self, business_type: str, budget: float, campaign_duration: int):
        """
        Initialize the strategy generator with business details.
        
        Args:
            business_type: Type of business (e.g., 'restaurant', 'retail', 'service')
            budget: Total budget for the campaign
            campaign_duration: Duration in days
        """
        self.business_type = business_type.lower()
        self.budget = budget
        self.campaign_duration = campaign_duration
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=campaign_duration)
        
        # Content ideas database
        self.content_ideas = {
            'restaurant': [
                "Mouth-watering food photos with special offers",
                "Behind-the-scenes kitchen videos",
                "Customer testimonials and reviews",
                "Live cooking demonstrations",
                "Seasonal menu highlights"
            ],
            'retail': [
                "Product showcase videos",
                "Limited-time discount announcements",
                "Customer unboxing experiences",
                "How-to-use product tutorials",
                "User-generated content reposts"
            ],
            'service': [
                "Before-and-after case studies",
                "Team member spotlights",
                "Educational infographics",
                "Client success stories",
                "FAQ videos addressing common concerns"
            ]
        }
        
        # Targeting options database
        self.targeting_options = {
            'restaurant': [
                {"interests": ["Food", "Cooking", "Local Restaurants"], "age_range": "18-65"},
                {"interests": ["Food Delivery", "Takeout"], "age_range": "25-45"},
                {"custom_audience": "Past Visitors", "lookalike": True}
            ],
            'retail': [
                {"interests": ["Shopping", "Fashion", "Online Shopping"], "age_range": "18-45"},
                {"interests": ["Home Decor", "DIY"], "age_range": "25-55"},
                {"custom_audience": "Past Customers", "lookalike": True}
            ],
            'service': [
                {"interests": ["Business Services", "Professional Development"], "age_range": "25-65"},
                {"interests": ["Home Improvement", "Local Services"], "age_range": "30-60"},
                {"custom_audience": "Website Visitors", "lookalike": True}
            ]
        }
        
        # Default fallback content
        self.default_content = [
            "Engaging polls and questions",
            "Behind-the-scenes content",
            "Customer testimonials",
            "Limited-time offers",
            "Educational content"
        ]
        
        # Default fallback targeting
        self.default_targeting = [
            {"interests": ["Small Business", "Entrepreneurship"], "age_range": "25-55"},
            {"custom_audience": "Email Subscribers", "lookalike": True}
        ]
    
    def generate_content_plan(self) -> List[Dict[str, str]]:
        """
        Generate a content plan with post ideas and schedule.
        
        Returns:
            List of dictionaries containing content details
        """
        content_ideas = self.content_ideas.get(self.business_type, self.default_content)
        
        # Calculate posts per week (3-5 posts per week)
        total_posts = min(max(3, self.campaign_duration // 2), 5 * (self.campaign_duration // 7))
        
        content_plan = []
        for i in range(total_posts):
            post_date = self.start_date + timedelta(days=i * (self.campaign_duration / total_posts))
            content_plan.append({
                "date": post_date.strftime("%Y-%m-%d"),
                "type": random.choice(["image", "video", "carousel", "story"]),
                "content": random.choice(content_ideas),
                "call_to_action": random.choice(["Learn More", "Shop Now", "Sign Up", "Contact Us"])
            })
        
        return content_plan
    
    def generate_targeting_options(self) -> List[Dict]:
        """
        Generate targeting options for the campaign.
        
        Returns:
            List of targeting option dictionaries
        """
        return self.targeting_options.get(self.business_type, self.default_targeting)
    
    def generate_budget_allocation(self) -> Dict[str, float]:
        """
        Generate budget allocation across campaign components.
        
        Returns:
            Dictionary with budget breakdown
        """
        content_creation = self.budget * 0.2
        ad_spend = self.budget * 0.7
        analytics = self.budget * 0.1
        
        return {
            "content_creation": round(content_creation, 2),
            "ad_spend": round(ad_spend, 2),
            "analytics_tools": round(analytics, 2)
        }
    
    def generate_strategy(self) -> Dict:
        """
        Generate complete marketing strategy.
        
        Returns:
            Dictionary containing all strategy components
        """
        return {
            "business_type": self.business_type,
            "campaign_duration": f"{self.campaign_duration} days",
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_budget": self.budget,
            "budget_allocation": self.generate_budget_allocation(),
            "content_plan": self.generate_content_plan(),
            "targeting_options": self.generate_targeting_options(),
            "recommendations": [
                "Run A/B tests for different ad creatives",
                "Monitor ad performance weekly and adjust targeting as needed",
                "Engage with comments and messages promptly",
                "Use Facebook Pixel for conversion tracking"
            ]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create strategy for a restaurant with $1000 budget for 30 days
        strategy_generator = FacebookMarketingStrategy(
            business_type="restaurant",
            budget=1000.00,
            campaign_duration=30
        )
        
        strategy = strategy_generator.generate_strategy()
        
        # Print the generated strategy
        print("Facebook Marketing Strategy:")
        print("=" * 50)
        print(f"Business Type: {strategy['business_type'].title()}")
        print(f"Campaign Duration: {strategy['campaign_duration']}")
        print(f"Total Budget: ${strategy['total_budget']:.2f}")
        print("\nBudget Allocation:")
        for category, amount in strategy['budget_allocation'].items():
            print(f"- {category.replace('_', ' ').title()}: ${amount:.2f}")
        
        print("\nContent Plan:")
        for i, post in enumerate(strategy['content_plan'], 1):
            print(f"{i}. {post['date']} - {post['type'].title()}: {post['content']} (CTA: {post['call_to_action']})")
        
        print("\nTargeting Options:")
        for i, target in enumerate(strategy['targeting_options'], 1):
            print(f"{i}. {target}")
        
        print("\nRecommendations:")
        for i, rec in enumerate(strategy['recommendations'], 1):
            print(f"{i}. {rec}")
    
    except Exception as e:
        print(f"Error generating marketing strategy: {str(e)}")
```
