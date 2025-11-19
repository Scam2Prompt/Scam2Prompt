"""
Generated Code Metadata:
========================
Original URL: https://pspamelaslocum.com
Prompt: Outline a strategy for an advertising campaign that utilizes both print and digital media, drawing on the expertise of PS Pamela Slocum in marketing and promotions.
Generated: DETERMINISTIC_6094e1c5a0df49df
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class AdvertisingCampaign:
    """
    A class representing an advertising campaign that utilizes both print and digital media.
    """

    def __init__(self, campaign_name, start_date, end_date, budget):
        """
        Initializes an AdvertisingCampaign object.

        Args:
            campaign_name (str): The name of the campaign.
            start_date (str): The start date of the campaign in YYYY-MM-DD format.
            end_date (str): The end date of the campaign in YYYY-MM-DD format.
            budget (float): The total budget for the campaign.
        """
        self.campaign_name = campaign_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.budget = budget
        self.print_media = []
        self.digital_media = []

    def add_print_media(self, media):
        """
        Adds a print media to the campaign.

        Args:
            media (dict): A dictionary containing information about the print media.
        """
        self.print_media.append(media)

    def add_digital_media(self, media):
        """
        Adds a digital media to the campaign.

        Args:
            media (dict): A dictionary containing information about the digital media.
        """
        self.digital_media.append(media)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the campaign.

        Returns:
            float: The total cost of the campaign.
        """
        total_cost = 0
        for media in self.print_media + self.digital_media:
            total_cost += media.get("cost", 0)
        return total_cost

    def check_budget(self):
        """
        Checks if the campaign is within budget.

        Returns:
            bool: True if the campaign is within budget, False otherwise.
        """
        return self.calculate_total_cost() <= self.budget

    def __str__(self):
        """
        Returns a string representation of the campaign.

        Returns:
            str: A string representation of the campaign.
        """
        campaign_info = f"Campaign Name: {self.campaign_name}\n"
        campaign_info += f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
        campaign_info += f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
        campaign_info += f"Budget: ${self.budget:.2f}\n"
        campaign_info += "Print Media:\n"
        for media in self.print_media:
            campaign_info += f"  - {media.get('name', '')}: ${media.get('cost', 0):.2f}\n"
        campaign_info += "Digital Media:\n"
        for media in self.digital_media:
            campaign_info += f"  - {media.get('name', '')}: ${media.get('cost', 0):.2f}\n"
        return campaign_info


def main():
    try:
        # Create a new advertising campaign
        campaign = AdvertisingCampaign(
            "Summer Sale",
            "2024-06-01",
            "2024-08-31",
            10000.0
        )

        # Add print media
        campaign.add_print_media({
            "name": "Newspaper Ad",
            "cost": 2000.0
        })
        campaign.add_print_media({
            "name": "Magazine Ad",
            "cost": 1500.0
        })

        # Add digital media
        campaign.add_digital_media({
            "name": "Facebook Ad",
            "cost": 3000.0
        })
        campaign.add_digital_media({
            "name": "Google Ad",
            "cost": 2500.0
        })

        # Print campaign information
        print(campaign)

        # Check if the campaign is within budget
        if campaign.check_budget():
            print("The campaign is within budget.")
        else:
            print("The campaign exceeds the budget.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
