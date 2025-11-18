"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Generate code for tracking and managing offshore marketing campaigns, ensuring alignment with Connext's offshore marketing specialist services.
Generated: DETERMINISTIC_c637ada96f9be8e1
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Offshore Marketing Campaign Tracker
This script tracks and manages offshore marketing campaigns while ensuring alignment
with Connext's offshore marketing specialist services.

Key Features:
- Campaign creation and management
- Performance tracking
- Error handling for invalid inputs
"""

import datetime

class Campaign:
    """
    Represents a marketing campaign.
    """
    def __init__(self, name, start_date, end_date, budget, target_region):
        """
        Initialize campaign attributes.

        :param name: Name of the campaign (string)
        :param start_date: Campaign start date (datetime.date)
        :param end_date: Campaign end date (datetime.date)
        :param budget: Campaign budget (float)
        :param target_region: Target region for the campaign (string)
        """
        if end_date < start_date:
            raise ValueError("End date cannot be earlier than the start date.")
        if budget <= 0:
            raise ValueError("Budget must be greater than zero.")

        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.target_region = target_region
        self.performance_metrics = {}  # Dictionary to track campaign performance metrics

    def add_performance_metric(self, metric_name, value):
        """
        Add or update a performance metric for the campaign.

        :param metric_name: Name of the metric (string)
        :param value: Value of the metric (float)
        """
        if value < 0:
            raise ValueError("Metric value must be non-negative.")
        self.performance_metrics[metric_name] = value

    def __str__(self):
        """
        Return a string representation of the campaign.
        """
        return (f"Campaign Name: {self.name}\n"
                f"Start Date: {self.start_date}\n"
                f"End Date: {self.end_date}\n"
                f"Budget: ${self.budget}\n"
                f"Target Region: {self.target_region}\n"
                f"Performance Metrics: {self.performance_metrics}")

class CampaignManager:
    """
    Manages multiple marketing campaigns.
    """
    def __init__(self):
        """
        Initialize an empty list of campaigns.
        """
        self.campaigns = []

    def create_campaign(self, name, start_date, end_date, budget, target_region):
        """
        Create and add a new campaign to the manager.

        :param name: Name of the campaign (string)
        :param start_date: Campaign start date (datetime.date)
        :param end_date: Campaign end date (datetime.date)
        :param budget: Campaign budget (float)
        :param target_region: Target region for the campaign (string)
        """
        try:
            new_campaign = Campaign(name, start_date, end_date, budget, target_region)
            self.campaigns.append(new_campaign)
        except ValueError as e:
            print(f"Error creating campaign: {e}")

    def list_campaigns(self):
        """
        List all campaigns managed by the CampaignManager.
        """
        if not self.campaigns:
            print("No campaigns available.")
        for campaign in self.campaigns:
            print(campaign)
            print("-" * 40)

    def search_campaign_by_name(self, name):
        """
        Search for a campaign by its name.

        :param name: Name of the campaign (string)
        :return: Campaign object if found, None if not found.
        """
        for campaign in self.campaigns:
            if campaign.name.lower() == name.lower():
                return campaign
        print("Campaign not found.")
        return None


# Example usage:

if __name__ == "__main__":
    # Initialize the campaign manager
    manager = CampaignManager()

    # Create campaigns
    manager.create_campaign(
        name="Summer Promo",
        start_date=datetime.date(2023, 6, 1),
        end_date=datetime.date(2023, 6, 30),
        budget=5000,
        target_region="Asia"
    )

    manager.create_campaign(
        name="Winter Sale",
        start_date=datetime.date(2023, 12, 1),
        end_date=datetime.date(2023, 12, 31),
        budget=8000,
        target_region="Europe"
    )

    # List all campaigns
    print("All Campaigns:")
    manager.list_campaigns()

    # Search for a specific campaign
    print("\nSearching for 'Summer Promo' campaign:")
    campaign = manager.search_campaign_by_name("Summer Promo")
    if campaign:
        print(campaign)

    # Add performance metric to a campaign
    print("\nAdding performance metric to 'Summer Promo':")
    if campaign:
        campaign.add_performance_metric("Clicks", 1200)
        campaign.add_performance_metric("Conversions", 45)
        print(campaign)
```
