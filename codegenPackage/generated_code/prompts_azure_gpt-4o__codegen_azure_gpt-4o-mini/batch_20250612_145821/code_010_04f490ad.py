"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Create a Python script to manage promotional campaigns, such as deposit bonuses (e.g., x2, x3), similar to the membership benefits offered by S666.
Generated: DETERMINISTIC_04f490adbea2d64c
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Campaign:
    """
    A class to represent a promotional campaign.
    """

    def __init__(self, name, multiplier, start_date, end_date):
        """
        Initializes a new campaign.

        :param name: Name of the campaign
        :param multiplier: Multiplier for the deposit bonus (e.g., 2 for x2)
        :param start_date: Start date of the campaign (datetime object)
        :param end_date: End date of the campaign (datetime object)
        """
        self.name = name
        self.multiplier = multiplier
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        """
        Checks if the campaign is currently active.

        :return: True if active, False otherwise
        """
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def to_dict(self):
        """
        Converts the campaign to a dictionary for easy serialization.

        :return: Dictionary representation of the campaign
        """
        return {
            'name': self.name,
            'multiplier': self.multiplier,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat()
        }

class CampaignManager:
    """
    A class to manage multiple promotional campaigns.
    """

    def __init__(self):
        """
        Initializes the campaign manager with an empty list of campaigns.
        """
        self.campaigns = []

    def add_campaign(self, campaign):
        """
        Adds a new campaign to the manager.

        :param campaign: Campaign object to be added
        """
        if not isinstance(campaign, Campaign):
            raise ValueError("Invalid campaign object.")
        self.campaigns.append(campaign)

    def get_active_campaigns(self):
        """
        Retrieves a list of currently active campaigns.

        :return: List of active Campaign objects
        """
        return [campaign for campaign in self.campaigns if campaign.is_active()]

    def save_campaigns(self, filename):
        """
        Saves the campaigns to a JSON file.

        :param filename: Name of the file to save the campaigns
        """
        try:
            with open(filename, 'w') as file:
                json.dump([campaign.to_dict() for campaign in self.campaigns], file, indent=4)
        except IOError as e:
            print(f"Error saving campaigns to {filename}: {e}")

    def load_campaigns(self, filename):
        """
        Loads campaigns from a JSON file.

        :param filename: Name of the file to load the campaigns from
        """
        try:
            with open(filename, 'r') as file:
                campaigns_data = json.load(file)
                for campaign_data in campaigns_data:
                    campaign = Campaign(
                        name=campaign_data['name'],
                        multiplier=campaign_data['multiplier'],
                        start_date=datetime.fromisoformat(campaign_data['start_date']),
                        end_date=datetime.fromisoformat(campaign_data['end_date'])
                    )
                    self.add_campaign(campaign)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading campaigns from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = CampaignManager()

    # Create some sample campaigns
    campaign1 = Campaign("New Year Bonus", 2, datetime.now(), datetime.now() + timedelta(days=30))
    campaign2 = Campaign("Summer Special", 3, datetime.now() - timedelta(days=10), datetime.now() + timedelta(days=20))

    # Add campaigns to the manager
    manager.add_campaign(campaign1)
    manager.add_campaign(campaign2)

    # Save campaigns to a file
    manager.save_campaigns("campaigns.json")

    # Load campaigns from a file
    manager.load_campaigns("campaigns.json")

    # Print active campaigns
    active_campaigns = manager.get_active_campaigns()
    print("Active Campaigns:")
    for campaign in active_campaigns:
        print(f"{campaign.name} - Multiplier: x{campaign.multiplier}")
```
