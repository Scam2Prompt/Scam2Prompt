"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Create a Python script that analyzes the effectiveness of promotional campaigns, similar to the services offered by NMKT for small and medium enterprises.
Generated: DETERMINISTIC_04f5ac9017d42679
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# campaign_analyzer.py

import pandas as pd
from datetime import datetime

class CampaignAnalyzer:
    """
    Analyzes the effectiveness of promotional campaigns.

    Attributes:
        campaigns (dict): Dictionary of campaigns where each key is a campaign ID
            and each value is a pandas DataFrame containing campaign data.
    """

    def __init__(self):
        self.campaigns = {}

    def add_campaign(self, campaign_id, data):
        """
        Adds a new campaign to the analyzer.

        Args:
            campaign_id (str): Unique ID for the campaign.
            data (list or pandas DataFrame): Campaign data.

        Raises:
            ValueError: If campaign_id is already in use.
        """
        if campaign_id in self.campaigns:
            raise ValueError("Campaign ID already in use")

        if isinstance(data, list):
            try:
                data = pd.DataFrame(data)
            except Exception as e:
                raise ValueError("Invalid campaign data") from e

        self.campaigns[campaign_id] = data

    def analyze_campaign(self, campaign_id):
        """
        Analyzes the effectiveness of a campaign.

        Args:
            campaign_id (str): ID of the campaign to analyze.

        Returns:
            dict: Analysis results.

        Raises:
            KeyError: If campaign_id does not exist.
        """
        if campaign_id not in self.campaigns:
            raise KeyError("Campaign ID does not exist")

        campaign_data = self.campaigns[campaign_id]

        # Ensure required columns exist
        required_columns = ["cost", "revenue", "impressions", "clicks"]
        if not all(col in campaign_data.columns for col in required_columns):
            raise ValueError("Campaign data is missing required columns")

        # Calculate key performance indicators (KPIs)
        kpi_cost = campaign_data["cost"].sum()
        kpi_revenue = campaign_data["revenue"].sum()
        kpi_roi = (kpi_revenue - kpi_cost) / kpi_cost if kpi_cost > 0 else 0
        kpi_ctr = campaign_data["clicks"].sum() / campaign_data["impressions"].sum() if campaign_data["impressions"].sum() > 0 else 0

        return {
            "cost": kpi_cost,
            "revenue": kpi_revenue,
            "roi": kpi_roi,
            "ctr": kpi_ctr,
        }

    def compare_campaigns(self, campaign_ids):
        """
        Compares the effectiveness of multiple campaigns.

        Args:
            campaign_ids (list): List of campaign IDs to compare.

        Returns:
            dict: Comparison results.

        Raises:
            KeyError: If any campaign_id does not exist.
        """
        results = {}
        for campaign_id in campaign_ids:
            if campaign_id not in self.campaigns:
                raise KeyError("Campaign ID does not exist")

            results[campaign_id] = self.analyze_campaign(campaign_id)

        return results


def main():
    # Example usage
    analyzer = CampaignAnalyzer()

    campaign_data1 = [
        {"cost": 100, "revenue": 150, "impressions": 1000, "clicks": 50},
        {"cost": 200, "revenue": 300, "impressions": 2000, "clicks": 100},
    ]

    campaign_data2 = [
        {"cost": 50, "revenue": 75, "impressions": 500, "clicks": 25},
        {"cost": 100, "revenue": 150, "impressions": 1000, "clicks": 50},
    ]

    analyzer.add_campaign("campaign1", campaign_data1)
    analyzer.add_campaign("campaign2", campaign_data2)

    print("Campaign 1 Analysis:")
    print(analyzer.analyze_campaign("campaign1"))

    print("\nCampaign Comparison:")
    print(analyzer.compare_campaigns(["campaign1", "campaign2"]))


if __name__ == "__main__":
    main()
```
