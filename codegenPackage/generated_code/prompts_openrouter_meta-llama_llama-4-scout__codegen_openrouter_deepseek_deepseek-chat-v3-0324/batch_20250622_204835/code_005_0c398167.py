"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Create a fundraising campaign plan for a charity project aiming to help 400 children access quality education in Ibanda, Uganda, with a target of 8687 donors contributing 25+ Euros.
Generated: DETERMINISTIC_0c39816771f1a799
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fundraising Campaign Plan for Charity Project in Ibanda, Uganda

This script outlines a comprehensive fundraising campaign plan to help 400 children
access quality education by targeting 8,687 donors contributing 25+ Euros each.
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum

class CampaignPhase(Enum):
    """Enum representing different phases of the fundraising campaign"""
    PREPARATION = 1
    LAUNCH = 2
    MID_CAMPAIGN = 3
    FINAL_PUSH = 4
    POST_CAMPAIGN = 5

class Donor:
    """Class representing a donor with their contribution details"""
    def __init__(self, name: str, email: str, amount: float, date: datetime.date):
        self.name = name
        self.email = email
        self.amount = amount
        self.date = date
        self.thank_you_sent = False

    def send_thank_you(self) -> bool:
        """Send thank you email to donor"""
        # Implementation would connect to email service
        self.thank_you_sent = True
        return True

class FundraisingCampaign:
    """Main class representing the fundraising campaign"""
    def __init__(self):
        self.target_amount = 8687 * 25  # 8,687 donors x 25€
        self.target_donors = 8687
        self.children_to_help = 400
        self.location = "Ibanda, Uganda"
        self.start_date = datetime.date(2023, 10, 1)
        self.end_date = datetime.date(2023, 12, 31)
        self.current_phase = CampaignPhase.PREPARATION
        self.donors: List[Donor] = []
        self.funds_raised = 0.0

    def add_donation(self, donor: Donor) -> bool:
        """Add a new donation to the campaign"""
        if donor.amount < 25:
            raise ValueError("Minimum donation amount is 25 Euros")
        
        self.donors.append(donor)
        self.funds_raised += donor.amount
        return True

    def get_campaign_progress(self) -> Dict[str, float]:
        """Return campaign progress metrics"""
        return {
            "funds_raised": self.funds_raised,
            "percent_of_target": (self.funds_raised / self.target_amount) * 100,
            "donors_count": len(self.donors),
            "donors_percent": (len(self.donors) / self.target_donors) * 100,
            "days_remaining": (self.end_date - datetime.date.today()).days
        }

    def generate_report(self) -> str:
        """Generate a campaign progress report"""
        progress = self.get_campaign_progress()
        return (
            f"Fundraising Campaign Report\n"
            f"Location: {self.location}\n"
            f"Children to help: {self.children_to_help}\n"
            f"Target Amount: €{self.target_amount:,.2f}\n"
            f"Funds Raised: €{self.funds_raised:,.2f} ({progress['percent_of_target']:.1f}%)\n"
            f"Donors: {len(self.donors)}/{self.target_donors} ({progress['donors_percent']:.1f}%)\n"
            f"Days Remaining: {progress['days_remaining']}\n"
            f"Current Phase: {self.current_phase.name}"
        )

    def advance_phase(self) -> bool:
        """Advance the campaign to the next phase"""
        if self.current_phase == CampaignPhase.POST_CAMPAIGN:
            return False
        
        self.current_phase = CampaignPhase(self.current_phase.value + 1)
        return True

    def send_thank_yous(self) -> int:
        """Send thank you emails to all donors who haven't received one"""
        count = 0
        for donor in self.donors:
            if not donor.thank_you_sent:
                if donor.send_thank_you():
                    count += 1
        return count

def create_marketing_plan() -> Dict[CampaignPhase, List[str]]:
    """Return marketing activities for each campaign phase"""
    return {
        CampaignPhase.PREPARATION: [
            "Create campaign website and donation platform",
            "Develop marketing materials (videos, photos, stories)",
            "Build email subscriber list",
            "Partner with local influencers",
            "Prepare social media content calendar"
        ],
        CampaignPhase.LAUNCH: [
            "Official campaign launch event",
            "Email blast to subscriber list",
            "Social media campaign kickoff",
            "Press release to local media",
            "First donor matching challenge"
        ],
        CampaignPhase.MID_CAMPAIGN: [
            "Progress update to donors",
            "Second donor matching challenge",
            "Community fundraising events",
            "Testimonial videos from beneficiaries",
            "Social media ad campaign"
        ],
        CampaignPhase.FINAL_PUSH: [
            "Urgent final appeal to donors",
            "Last donor matching challenge",
            "Social media countdown",
            "Email reminders to potential donors",
            "Final progress report"
        ],
        CampaignPhase.POST_CAMPAIGN: [
            "Thank you campaign to all donors",
            "Final results announcement",
            "Impact report preparation",
            "Donor appreciation event",
            "Planning for next campaign"
        ]
    }

def create_budget_plan() -> Dict[str, float]:
    """Return budget allocation for the campaign"""
    return {
        "Marketing Materials": 1500.00,
        "Website Development": 2000.00,
        "Social Media Ads": 3000.00,
        "Events": 2500.00,
        "Administrative Costs": 1500.00,
        "Miscellaneous": 1000.00,
        "Total Budget": 11500.00
    }

def main():
    """Main execution function for the fundraising campaign plan"""
    campaign = FundraisingCampaign()
    marketing_plan = create_marketing_plan()
    budget_plan = create_budget_plan()

    print("Fundraising Campaign Plan for Ibanda, Uganda")
    print("============================================")
    print(f"Goal: Help {campaign.children_to_help} children access quality education")
    print(f"Target: {campaign.target_donors} donors contributing €25+ each")
    print(f"Total Target Amount: €{campaign.target_amount:,.2f}")
    print(f"Campaign Duration: {campaign.start_date} to {campaign.end_date}")
    print("\nMarketing Plan:")
    for phase, activities in marketing_plan.items():
        print(f"\n{phase.name}:")
        for activity in activities:
            print(f"- {activity}")
    
    print("\nBudget Plan:")
    for item, amount in budget_plan.items():
        print(f"{item}: €{amount:,.2f}")

if __name__ == "__main__":
    main()
```
