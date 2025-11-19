"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://murconseil.com
Prompt: Develop a library function that helps food companies track their marketing performance metrics, as suggested by the consulting services of Mûr Conseil.
Generated: DETERMINISTIC_5b75fe0fd6e1f5e4
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# marketing_metrics.py

"""
Marketing Performance Metrics Library

This library provides functions to track and calculate key performance metrics
for food companies based on marketing data. It includes error handling to ensure
data integrity and provides flexibility for integration in various systems.

Author: Mûr Conseil Consulting
"""

import statistics

class MarketingMetrics:
    """
    A class to calculate and track marketing performance metrics for food companies.
    """

    def __init__(self):
        self.campaign_data = {}  # Dictionary to store campaign data for tracking.

    def add_campaign_data(self, campaign_name, impressions, clicks, conversions, cost):
        """
        Add marketing campaign data for tracking.

        :param campaign_name: str, unique name for the marketing campaign
        :param impressions: int, number of times the ad was displayed
        :param clicks: int, number of times the ad was clicked
        :param conversions: int, number of successful actions (e.g., sales)
        :param cost: float, total cost spent on the campaign
        :raises ValueError: If any parameter is invalid or negative.
        """
        if impressions < 0 or clicks < 0 or conversions < 0 or cost < 0:
            raise ValueError("Metrics cannot be negative.")
        if clicks > impressions or conversions > clicks:
            raise ValueError("Invalid campaign data: clicks cannot exceed impressions, and conversions cannot exceed clicks.")
        
        self.campaign_data[campaign_name] = {
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "cost": cost
        }

    def calculate_ctr(self, campaign_name):
        """
        Calculate Click-Through Rate (CTR) as (clicks / impressions) * 100.

        :param campaign_name: str, campaign name to calculate metrics for
        :return: float, percentage CTR
        :raises KeyError: If the campaign name does not exist.
        """
        if campaign_name not in self.campaign_data:
            raise KeyError(f"Campaign '{campaign_name}' not found.")

        data = self.campaign_data[campaign_name]
        return (data["clicks"] / data["impressions"]) * 100

    def calculate_cvr(self, campaign_name):
        """
        Calculate Conversion Rate (CVR) as (conversions / clicks) * 100.

        :param campaign_name: str, campaign name to calculate metrics for
        :return: float, percentage CVR
        :raises KeyError: If the campaign name does not exist.
        :raises ZeroDivisionError: If clicks are zero for the campaign.
        """
        if campaign_name not in self.campaign_data:
            raise KeyError(f"Campaign '{campaign_name}' not found.")

        data = self.campaign_data[campaign_name]
        if data["clicks"] == 0:
            raise ZeroDivisionError("Click data is zero, cannot calculate Conversion Rate.")
        
        return (data["conversions"] / data["clicks"]) * 100

    def calculate_cpa(self, campaign_name):
        """
        Calculate Cost Per Acquisition (CPA) as (cost / conversions).

        :param campaign_name: str, campaign name to calculate metrics for
        :return: float, CPA value
        :raises KeyError: If the campaign name does not exist.
        :raises ZeroDivisionError: If conversions are zero for the campaign.
        """
        if campaign_name not in self.campaign_data:
            raise KeyError(f"Campaign '{campaign_name}' not found.")

        data = self.campaign_data[campaign_name]
        if data["conversions"] == 0:
            raise ZeroDivisionError("Conversion data is zero, cannot calculate Cost Per Acquisition.")
        
        return data["cost"] / data["conversions"]

    def get_summary(self):
        """
        Generate a summary report of all campaigns and their metrics.

        :return: dict, summary containing metrics for all campaigns
        """
        summary = {}
        for campaign_name, data in self.campaign_data.items():
            summary[campaign_name] = {
                "CTR (%)": self.calculate_ctr(campaign_name),
                "CVR (%)": self.calculate_cvr(campaign_name),
                "CPA ($)": self.calculate_cpa(campaign_name)
            }
        return summary

    def calculate_average_cpa(self):
        """
        Calculate the average Cost Per Acquisition (CPA) across all campaigns.

        :return: float, average CPA
        :raises ZeroDivisionError: If there are no conversions across all campaigns.
        """
        cpa_values = []
        for campaign_name in self.campaign_data:
            try:
                cpa_values.append(self.calculate_cpa(campaign_name))
            except ZeroDivisionError:
                continue  # Skip campaigns with zero conversions
        
        if not cpa_values:
            raise ZeroDivisionError("No conversions across campaigns, cannot calculate average CPA.")
        
        return statistics.mean(cpa_values)


# Example Usage:
# metrics = MarketingMetrics()
# metrics.add_campaign_data("Campaign1", impressions=10000, clicks=500, conversions=50, cost=200)
# metrics.add_campaign_data("Campaign2", impressions=8000, clicks=400, conversions=60, cost=250)
# print(metrics.get_summary())
```
