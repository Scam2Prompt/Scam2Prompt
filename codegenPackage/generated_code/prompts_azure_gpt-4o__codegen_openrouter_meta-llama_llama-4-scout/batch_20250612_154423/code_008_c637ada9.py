"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Generate code for tracking and managing offshore marketing campaigns, ensuring alignment with Connext's offshore marketing specialist services.
Generated: DETERMINISTIC_c637ada96f9be8e1
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marketing_campaign_tracker.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class CampaignStatus(str, Enum):
    """Enum for campaign status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class MarketingCampaign:
    """Class representing a marketing campaign"""
    
    def __init__(self, 
                 campaign_id: int, 
                 name: str, 
                 start_date: datetime, 
                 end_date: datetime, 
                 status: CampaignStatus = CampaignStatus.PENDING):
        """
        Initialize a marketing campaign.

        Args:
        - campaign_id (int): Unique identifier for the campaign.
        - name (str): Name of the campaign.
        - start_date (datetime): Start date of the campaign.
        - end_date (datetime): End date of the campaign.
        - status (CampaignStatus): Status of the campaign. Defaults to PENDING.
        """
        self.campaign_id = campaign_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.budget: float = 0.0
        self.expenses: List[Dict] = []

    def update_status(self, status: CampaignStatus):
        """Update the status of the campaign"""
        self.status = status

    def add_expense(self, expense: Dict):
        """Add an expense to the campaign"""
        self.expenses.append(expense)

    def update_budget(self, budget: float):
        """Update the budget of the campaign"""
        self.budget = budget

class OffshoreMarketingSpecialist:
    """Class representing an offshore marketing specialist"""
    
    def __init__(self, specialist_id: int, name: str):
        """
        Initialize an offshore marketing specialist.

        Args:
        - specialist_id (int): Unique identifier for the specialist.
        - name (str): Name of the specialist.
        """
        self.specialist_id = specialist_id
        self.name = name
        self.campaigns: List[MarketingCampaign] = []

    def assign_campaign(self, campaign: MarketingCampaign):
        """Assign a campaign to the specialist"""
        self.campaigns.append(campaign)

class MarketingCampaignTracker:
    """Class for tracking and managing offshore marketing campaigns"""
    
    def __init__(self):
        self.campaigns: List[MarketingCampaign] = []
        self.specialists: List[OffshoreMarketingSpecialist] = []

    def create_campaign(self, 
                       campaign_id: int, 
                       name: str, 
                       start_date: datetime, 
                       end_date: datetime) -> MarketingCampaign:
        """
        Create a new marketing campaign.

        Args:
        - campaign_id (int): Unique identifier for the campaign.
        - name (str): Name of the campaign.
        - start_date (datetime): Start date of the campaign.
        - end_date (datetime): End date of the campaign.

        Returns:
        - MarketingCampaign: The created campaign.
        """
        campaign = MarketingCampaign(campaign_id, name, start_date, end_date)
        self.campaigns.append(campaign)
        return campaign

    def create_specialist(self, specialist_id: int, name: str) -> OffshoreMarketingSpecialist:
        """
        Create a new offshore marketing specialist.

        Args:
        - specialist_id (int): Unique identifier for the specialist.
        - name (str): Name of the specialist.

        Returns:
        - OffshoreMarketingSpecialist: The created specialist.
        """
        specialist = OffshoreMarketingSpecialist(specialist_id, name)
        self.specialists.append(specialist)
        return specialist

def main():
    tracker = MarketingCampaignTracker()

    # Create a new campaign
    campaign = tracker.create_campaign(
        campaign_id=1, 
        name="Summer Sale", 
        start_date=datetime(2024, 6, 1), 
        end_date=datetime(2024, 6, 30)
    )

    # Create a new specialist
    specialist = tracker.create_specialist(specialist_id=1, name="John Doe")

    # Assign the campaign to the specialist
    specialist.assign_campaign(campaign)

    # Update campaign status and budget
    campaign.update_status(CampaignStatus.IN_PROGRESS)
    campaign.update_budget(10000.0)

    # Add an expense to the campaign
    expense = {"date": datetime(2024, 6, 15), "amount": 500.0, "description": "Advertisement"}
    campaign.add_expense(expense)

    # Print campaign details
    print(f"Campaign ID: {campaign.campaign_id}")
    print(f"Campaign Name: {campaign.name}")
    print(f"Campaign Status: {campaign.status.value}")
    print(f"Campaign Budget: {campaign.budget}")
    print("Campaign Expenses:")
    for expense in campaign.expenses:
        print(f"  - Date: {expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}")

if __name__ == "__main__":
    main()
```
