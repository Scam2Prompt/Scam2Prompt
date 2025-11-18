"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Write code to implement a pay-per-click (PPC) advertising campaign using Rankraze's guidelines for maximizing ROI in digital marketing.
Generated: DETERMINISTIC_35b1c581e7d04fb4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from datetime import datetime

class PPCAdvertisingCampaign:
    def __init__(self, campaign_name, budget, target_audience):
        """
        Initializes a new PPC Advertising Campaign.

        :param campaign_name: Name of the campaign
        :param budget: Total budget for the campaign
        :param target_audience: Target audience for the campaign
        """
        self.campaign_name = campaign_name
        self.budget = budget
        self.target_audience = target_audience
        self.ads = []
        self.spent = 0

    def add_ad(self, ad):
        """
        Adds an ad to the campaign.

        :param ad: Ad object containing ad details
        """
        if not isinstance(ad, Ad):
            raise ValueError("ad must be an instance of Ad class")
        self.ads.append(ad)

    def run_campaign(self):
        """
        Starts the PPC campaign, monitoring performance and spending.
        """
        print(f"Running campaign: {self.campaign_name}")
        for ad in self.ads:
            ad.show_ad()
            self.spent += ad.click_cost  # Simulate cost per click
            self.check_budget()

    def check_budget(self):
        """
        Checks if the campaign budget has been exceeded.
        """
        if self.spent > self.budget:
            raise RuntimeError("Budget exceeded! Please adjust your campaign settings.")

    def get_performance_report(self):
        """
        Generates a performance report for the campaign.

        :return: Dictionary containing performance metrics
        """
        report = {
            "campaign_name": self.campaign_name,
            "total_spent": self.spent,
            "remaining_budget": self.budget - self.spent,
            "ads": [ad.get_report() for ad in self.ads]
        }
        return report


class Ad:
    def __init__(self, title, description, click_cost):
        """
        Initializes a new Ad.

        :param title: Title of the ad
        :param description: Description of the ad
        :param click_cost: Cost incurred for each click on the ad
        """
        self.title = title
        self.description = description
        self.click_cost = click_cost
        self.clicks = 0

    def show_ad(self):
        """
        Simulates displaying the ad and generating a click.
        """
        print(f"Ad Title: {self.title}")
        print(f"Description: {self.description}")
        self.clicks += 1  # Simulate a click
        print(f"Ad clicked! Cost incurred: ${self.click_cost}")

    def get_report(self):
        """
        Generates a report for the ad.

        :return: Dictionary containing ad performance metrics
        """
        return {
            "title": self.title,
            "description": self.description,
            "total_clicks": self.clicks,
            "cost_incurred": self.clicks * self.click_cost
        }


if __name__ == "__main__":
    try:
        # Example of creating a PPC campaign
        campaign = PPCAdvertisingCampaign("Spring Sale", 500, "Young Adults")
        
        # Adding ads to the campaign
        ad1 = Ad("50% Off on Shoes", "Don't miss out on our spring sale!", 5)
        ad2 = Ad("Free Shipping on Orders", "Shop now and enjoy free shipping!", 3)

        campaign.add_ad(ad1)
        campaign.add_ad(ad2)

        # Run the campaign
        campaign.run_campaign()

        # Generate and print the performance report
        report = campaign.get_performance_report()
        print(json.dumps(report, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
