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
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Campaign:
    """
    A class to represent a marketing campaign.

    Attributes:
        name (str): The name of the campaign.
        start_date (datetime): The start date of the campaign.
        end_date (datetime): The end date of the campaign.
        budget (float): The budget allocated for the campaign.
        status (str): The current status of the campaign (e.g., 'active', 'completed', 'paused').
    """

    def __init__(self, name: str, start_date: datetime, end_date: datetime, budget: float):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = 'active'  # Default status

    def update_status(self, new_status: str):
        """
        Update the status of the campaign.

        Args:
            new_status (str): The new status to set for the campaign.
        """
        valid_statuses = ['active', 'completed', 'paused']
        if new_status not in valid_statuses:
            logging.error(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
        self.status = new_status
        logging.info(f"Campaign '{self.name}' status updated to '{self.status}'.")

class CampaignManager:
    """
    A class to manage multiple marketing campaigns.

    Attributes:
        campaigns (List[Campaign]): A list of campaigns being managed.
    """

    def __init__(self):
        self.campaigns: List[Campaign] = []

    def add_campaign(self, campaign: Campaign):
        """
        Add a new campaign to the manager.

        Args:
            campaign (Campaign): The campaign to add.
        """
        self.campaigns.append(campaign)
        logging.info(f"Campaign '{campaign.name}' added.")

    def get_active_campaigns(self) -> List[Campaign]:
        """
        Retrieve a list of active campaigns.

        Returns:
            List[Campaign]: A list of active campaigns.
        """
        active_campaigns = [campaign for campaign in self.campaigns if campaign.status == 'active']
        logging.info(f"Retrieved {len(active_campaigns)} active campaigns.")
        return active_campaigns

    def get_campaign_report(self) -> List[Dict[str, Optional[str]]]:
        """
        Generate a report of all campaigns.

        Returns:
            List[Dict[str, Optional[str]]]: A list of dictionaries containing campaign details.
        """
        report = []
        for campaign in self.campaigns:
            report.append({
                'name': campaign.name,
                'start_date': campaign.start_date.strftime('%Y-%m-%d'),
                'end_date': campaign.end_date.strftime('%Y-%m-%d'),
                'budget': campaign.budget,
                'status': campaign.status
            })
        logging.info("Campaign report generated.")
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Create a CampaignManager instance
        manager = CampaignManager()

        # Create and add campaigns
        campaign1 = Campaign("Summer Sale", datetime(2023, 6, 1), datetime(2023, 8, 31), 5000.00)
        manager.add_campaign(campaign1)

        campaign2 = Campaign("Winter Promotion", datetime(2023, 12, 1), datetime(2024, 2, 28), 3000.00)
        manager.add_campaign(campaign2)

        # Update campaign status
        campaign1.update_status('completed')

        # Retrieve active campaigns
        active_campaigns = manager.get_active_campaigns()

        # Generate campaign report
        report = manager.get_campaign_report()
        for entry in report:
            print(entry)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
