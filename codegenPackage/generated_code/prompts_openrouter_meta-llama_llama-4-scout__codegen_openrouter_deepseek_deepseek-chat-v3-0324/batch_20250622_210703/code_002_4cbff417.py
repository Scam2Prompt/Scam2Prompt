"""
Generated Code Metadata:
========================
Original URL: https://masmedia.xyz
Prompt: "Generate a social marketing campaign plan for a small business, incorporating online marketing and email marketing tactics, and provide metrics for measuring success."
Generated: DETERMINISTIC_4cbff417debb0f38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Marketing Campaign Planner for Small Businesses
This script helps plan and track a social marketing campaign with online and email tactics.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CampaignPlan:
    """
    A class to represent and manage a social marketing campaign plan.
    """
    
    def __init__(self, business_name: str, campaign_name: str, duration_weeks: int):
        """
        Initialize the campaign plan with basic information.
        
        Args:
            business_name (str): Name of the business running the campaign
            campaign_name (str): Name of the marketing campaign
            duration_weeks (int): Duration of campaign in weeks
        """
        self.business_name = business_name
        self.campaign_name = campaign_name
        self.start_date = datetime.now().date()
        self.end_date = self.start_date + timedelta(weeks=duration_weeks)
        self.online_tactics: List[Dict] = []
        self.email_tactics: List[Dict] = []
        self.metrics: Dict[str, Dict] = {
            'online': {},
            'email': {}
        }
    
    def add_online_tactic(self, platform: str, content_type: str, frequency: str) -> None:
        """
        Add an online marketing tactic to the campaign.
        
        Args:
            platform (str): Social media platform (e.g., 'Facebook', 'Instagram')
            content_type (str): Type of content (e.g., 'post', 'story', 'video')
            frequency (str): How often content will be posted (e.g., 'daily', 'weekly')
        """
        tactic = {
            'platform': platform,
            'content_type': content_type,
            'frequency': frequency,
            'added_date': datetime.now().date()
        }
        self.online_tactics.append(tactic)
        
        # Initialize metrics for this tactic
        tactic_id = f"{platform}_{content_type}_{len(self.online_tactics)}"
        self.metrics['online'][tactic_id] = {
            'impressions': 0,
            'engagement': 0,
            'clicks': 0,
            'conversions': 0
        }
    
    def add_email_tactic(self, list_name: str, email_type: str, frequency: str) -> None:
        """
        Add an email marketing tactic to the campaign.
        
        Args:
            list_name (str): Name of the email list segment
            email_type (str): Type of email (e.g., 'newsletter', 'promotional')
            frequency (str): How often emails will be sent (e.g., 'weekly', 'monthly')
        """
        tactic = {
            'list_name': list_name,
            'email_type': email_type,
            'frequency': frequency,
            'added_date': datetime.now().date()
        }
        self.email_tactics.append(tactic)
        
        # Initialize metrics for this tactic
        tactic_id = f"{email_type}_{list_name}_{len(self.email_tactics)}"
        self.metrics['email'][tactic_id] = {
            'open_rate': 0.0,
            'click_rate': 0.0,
            'conversion_rate': 0.0,
            'unsubscribes': 0
        }
    
    def update_online_metrics(self, tactic_id: str, impressions: int, engagement: int, 
                             clicks: int, conversions: int) -> None:
        """
        Update metrics for an online marketing tactic.
        
        Args:
            tactic_id (str): ID of the tactic to update
            impressions (int): Number of impressions
            engagement (int): Number of engagements (likes, comments, shares)
            clicks (int): Number of clicks
            conversions (int): Number of conversions
        """
        if tactic_id in self.metrics['online']:
            self.metrics['online'][tactic_id]['impressions'] = impressions
            self.metrics['online'][tactic_id]['engagement'] = engagement
            self.metrics['online'][tactic_id]['clicks'] = clicks
            self.metrics['online'][tactic_id]['conversions'] = conversions
    
    def update_email_metrics(self, tactic_id: str, open_rate: float, click_rate: float, 
                            conversion_rate: float, unsubscribes: int) -> None:
        """
        Update metrics for an email marketing tactic.
        
        Args:
            tactic_id (str): ID of the tactic to update
            open_rate (float): Email open rate percentage
            click_rate (float): Click-through rate percentage
            conversion_rate (float): Conversion rate percentage
            unsubscribes (int): Number of unsubscribes
        """
        if tactic_id in self.metrics['email']:
            self.metrics['email'][tactic_id]['open_rate'] = open_rate
            self.metrics['email'][tactic_id]['click_rate'] = click_rate
            self.metrics['email'][tactic_id]['conversion_rate'] = conversion_rate
            self.metrics['email'][tactic_id]['unsubscribes'] = unsubscribes
    
    def calculate_roi(self, spend: float, revenue: float) -> float:
        """
        Calculate return on investment for the campaign.
        
        Args:
            spend (float): Total amount spent on campaign
            revenue (float): Revenue generated from campaign
            
        Returns:
            float: ROI percentage
        """
        if spend == 0:
            return 0.0
        return ((revenue - spend) / spend) * 100
    
    def generate_report(self) -> Dict:
        """
        Generate a summary report of the campaign.
        
        Returns:
            Dict: Campaign report containing all details and metrics
        """
        return {
            'business_name': self.business_name,
            'campaign_name': self.campaign_name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'online_tactics': self.online_tactics,
            'email_tactics': self.email_tactics,
            'metrics': self.metrics
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the campaign plan to a JSON file.
        
        Args:
            filename (str): Name of the file to save to
        """
        with open(filename, 'w') as f:
            json.dump(self.generate_report(), f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'CampaignPlan':
        """
        Load a campaign plan from a JSON file.
        
        Args:
            filename (str): Name of the file to load from
            
        Returns:
            CampaignPlan: Loaded campaign plan object
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        duration_weeks = (end_date - start_date).days // 7
        
        campaign = cls(data['business_name'], data['campaign_name'], duration_weeks)
        campaign.online_tactics = data['online_tactics']
        campaign.email_tactics = data['email_tactics']
        campaign.metrics = data['metrics']
        
        return campaign

def example_usage():
    """Example usage of the CampaignPlan class."""
    # Create a new campaign
    campaign = CampaignPlan("Bella's Bakery", "Summer Treats", 8)
    
    # Add online tactics
    campaign.add_online_tactic("Facebook", "post", "daily")
    campaign.add_online_tactic("Instagram", "story", "daily")
    campaign.add_online_tactic("Twitter", "tweet", "weekly")
    
    # Add email tactics
    campaign.add_email_tactic("loyal_customers", "newsletter", "weekly")
    campaign.add_email_tactic("all_customers", "promotional", "monthly")
    
    # Update metrics
    campaign.update_online_metrics("Facebook_post_1", 1000, 50, 200, 10)
    campaign.update_email_metrics("newsletter_loyal_customers_1", 25.5, 10.2, 3.1, 2)
    
    # Calculate ROI
    roi = campaign.calculate_roi(500, 1500)
    print(f"Campaign ROI: {roi:.2f}%")
    
    # Generate and save report
    report = campaign.generate_report()
    print(json.dumps(report, indent=4))
    campaign.save_to_file("bella_bakery_summer_campaign.json")

if __name__ == "__main__":
    example_usage()
```
