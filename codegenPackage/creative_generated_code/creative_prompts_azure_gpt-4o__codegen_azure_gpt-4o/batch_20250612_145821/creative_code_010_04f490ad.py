"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Create a Python script to manage promotional campaigns, such as deposit bonuses (e.g., x2, x3), similar to the membership benefits offered by S666.
Generated: DETERMINISTIC_04f490adbea2d64c
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CampaignManager:
    """
    A class to manage promotional campaigns such as deposit bonuses.
    """

    def __init__(self):
        # Dictionary to store campaigns with their details
        self.campaigns = {}

    def create_campaign(self, campaign_name, bonus_multiplier, start_date, end_date):
        """
        Creates a new promotional campaign.

        Args:
            campaign_name (str): Name of the campaign.
            bonus_multiplier (float): Multiplier for the deposit bonus (e.g., 2.0 for x2).
            start_date (str): Start date of the campaign in 'YYYY-MM-DD' format.
            end_date (str): End date of the campaign in 'YYYY-MM-DD' format.
        """
        try:
            # Parse dates and validate
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            if end_date < start_date:
                raise ValueError("End date cannot be earlier than start date.")

            # Add campaign to the dictionary
            self.campaigns[campaign_name] = {
                "bonus_multiplier": bonus_multiplier,
                "start_date": start_date,
                "end_date": end_date
            }

            print(f"Campaign '{campaign_name}' created successfully!")

        except ValueError as ve:
            print(f"Error creating campaign: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def remove_campaign(self, campaign_name):
        """
        Removes an existing campaign.

        Args:
            campaign_name (str): Name of the campaign to be removed.
        """
        if campaign_name in self.campaigns:
            del self.campaigns[campaign_name]
            print(f"Campaign '{campaign_name}' removed successfully!")
        else:
            print(f"Campaign '{campaign_name}' does not exist.")

    def list_campaigns(self):
        """
        Lists all active campaigns with their details.
        """
        if not self.campaigns:
            print("No campaigns available.")
            return

        print("Active Campaigns:")
        for name, details in self.campaigns.items():
            print(f"  - {name}:")
            print(f"      Bonus Multiplier: x{details['bonus_multiplier']}")
            print(f"      Start Date: {details['start_date']}")
            print(f"      End Date: {details['end_date']}")

    def calculate_bonus(self, campaign_name, deposit_amount):
        """
        Calculates the bonus for a given deposit based on the campaign.

        Args:
            campaign_name (str): Name of the campaign.
            deposit_amount (float): The deposit amount to calculate the bonus for.

        Returns:
            float: The calculated bonus amount. None if campaign is invalid or inactive.
        """
        try:
            campaign = self.campaigns.get(campaign_name)
            if not campaign:
                print(f"Campaign '{campaign_name}' does not exist.")
                return None

            # Check if the campaign is active
            today = datetime.date.today()
            if not (campaign["start_date"] <= today <= campaign["end_date"]):
                print(f"Campaign '{campaign_name}' is not active.")
                return None

            # Calculate bonus
            bonus = deposit_amount * (campaign["bonus_multiplier"] - 1)
            return bonus

        except Exception as e:
            print(f"An error occurred while calculating bonus: {e}")
            return None


# Example usage
if __name__ == "__main__":
    manager = CampaignManager()

    # Create campaigns
    manager.create_campaign("Double Bonus", 2.0, "2023-11-01", "2023-11-30")
    manager.create_campaign("Triple Bonus", 3.0, "2023-12-01", "2023-12-31")

    # List campaigns
    manager.list_campaigns()

    # Calculate bonus
    deposit = 100
    bonus = manager.calculate_bonus("Double Bonus", deposit)
    if bonus is not None:
        print(f"Bonus for a deposit of {deposit} in 'Double Bonus': {bonus}")

    # Remove a campaign
    manager.remove_campaign("Double Bonus")

    # List campaigns again
    manager.list_campaigns()
```
