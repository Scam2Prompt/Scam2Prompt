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
# social_marketing_campaign.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class MarketingChannel(Enum):
    """Marketing channels for the campaign"""
    ONLINE = "online"
    EMAIL = "email"

@dataclass
class Campaign:
    """Social marketing campaign plan"""
    name: str
    description: str
    channels: List[MarketingChannel]
    start_date: datetime.date
    end_date: datetime.date
    budget: float

@dataclass
class OnlineMarketingTactic:
    """Online marketing tactic"""
    tactic: str
    channel: str
    budget: float

@dataclass
class EmailMarketingTactic:
    """Email marketing tactic"""
    subject: str
    body: str
    sender: str
    recipients: List[str]

class SocialMarketingCampaign:
    """Social marketing campaign plan generator"""
    def __init__(self, campaign: Campaign):
        self.campaign = campaign
        self.online_tactics = []
        self.email_tactics = []

    def add_online_tactic(self, tactic: OnlineMarketingTactic):
        """Add online marketing tactic"""
        self.online_tactics.append(tactic)

    def add_email_tactic(self, tactic: EmailMarketingTactic):
        """Add email marketing tactic"""
        self.email_tactics.append(tactic)

    def generate_plan(self):
        """Generate social marketing campaign plan"""
        plan = f"Campaign Name: {self.campaign.name}\n"
        plan += f"Description: {self.campaign.description}\n"
        plan += f"Channels: {[channel.value for channel in self.campaign.channels]}\n"
        plan += f"Start Date: {self.campaign.start_date}\n"
        plan += f"End Date: {self.campaign.end_date}\n"
        plan += f"Budget: {self.campaign.budget}\n\n"

        plan += "Online Marketing Tactics:\n"
        for tactic in self.online_tactics:
            plan += f"- Tactic: {tactic.tactic}, Channel: {tactic.channel}, Budget: {tactic.budget}\n"

        plan += "\nEmail Marketing Tactics:\n"
        for tactic in self.email_tactics:
            plan += f"- Subject: {tactic.subject}, Sender: {tactic.sender}, Recipients: {tactic.recipients}\n"

        return plan

    def measure_success(self):
        """Measure success of the campaign"""
        # Define metrics for measuring success
        metrics = {
            "online": {
                "engagement_rate": 0.05,
                "conversion_rate": 0.01,
                "cost_per_click": 0.5
            },
            "email": {
                "open_rate": 0.2,
                "click_through_rate": 0.05,
                "conversion_rate": 0.01
            }
        }

        # Calculate metrics
        online_engagement_rate = sum(tactic.budget * metrics["online"]["engagement_rate"] for tactic in self.online_tactics)
        online_conversion_rate = sum(tactic.budget * metrics["online"]["conversion_rate"] for tactic in self.online_tactics)
        email_open_rate = sum(metrics["email"]["open_rate"] for _ in self.email_tactics)
        email_click_through_rate = sum(metrics["email"]["click_through_rate"] for _ in self.email_tactics)
        email_conversion_rate = sum(metrics["email"]["conversion_rate"] for _ in self.email_tactics)

        # Print metrics
        print("Metrics:")
        print(f"Online Engagement Rate: {online_engagement_rate}")
        print(f"Online Conversion Rate: {online_conversion_rate}")
        print(f"Email Open Rate: {email_open_rate}")
        print(f"Email Click Through Rate: {email_click_through_rate}")
        print(f"Email Conversion Rate: {email_conversion_rate}")

def main():
    try:
        # Create campaign
        campaign = Campaign(
            name="Summer Sale",
            description="Summer sale campaign",
            channels=[MarketingChannel.ONLINE, MarketingChannel.EMAIL],
            start_date=datetime.date(2024, 6, 1),
            end_date=datetime.date(2024, 6, 30),
            budget=1000.0
        )

        # Create social marketing campaign plan
        social_marketing_campaign = SocialMarketingCampaign(campaign)

        # Add online marketing tactics
        social_marketing_campaign.add_online_tactic(OnlineMarketingTactic(
            tactic="Facebook Ads",
            channel="Facebook",
            budget=500.0
        ))
        social_marketing_campaign.add_online_tactic(OnlineMarketingTactic(
            tactic="Google Ads",
            channel="Google",
            budget=300.0
        ))

        # Add email marketing tactics
        social_marketing_campaign.add_email_tactic(EmailMarketingTactic(
            subject="Summer Sale",
            body="Check out our summer sale!",
            sender="example@example.com",
            recipients=["recipient1@example.com", "recipient2@example.com"]
        ))

        # Generate plan
        plan = social_marketing_campaign.generate_plan()
        print(plan)

        # Measure success
        social_marketing_campaign.measure_success()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
