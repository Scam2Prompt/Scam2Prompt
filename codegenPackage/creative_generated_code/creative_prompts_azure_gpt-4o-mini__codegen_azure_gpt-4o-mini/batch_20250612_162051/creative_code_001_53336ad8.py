"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write a code snippet to automate the tracking of marketing campaign results for a small business, inspired by the marketing solutions provided by NMKT.
Generated: DETERMINISTIC_53336ad8e134f2b1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaignTracker:
    def __init__(self):
        """
        Initializes the MarketingCampaignTracker with an empty dataframe.
        """
        self.campaign_data = pd.DataFrame(columns=['Campaign Name', 'Start Date', 'End Date', 'Budget', 
                                                   'Clicks', 'Impressions', 'Conversions', 'ROI'])

    def add_campaign(self, name, start_date, end_date, budget):
        """
        Adds a new marketing campaign to the tracker.
        
        Args:
            name (str): The name of the campaign.
            start_date (str): The start date of the campaign in 'YYYY-MM-DD' format.
            end_date (str): The end date of the campaign in 'YYYY-MM-DD' format.
            budget (float): The budget allocated for the campaign.
        """
        try:
            # Validate date formats
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")

            # Add campaign data
            new_campaign = {
                'Campaign Name': name,
                'Start Date': start_date,
                'End Date': end_date,
                'Budget': budget,
                'Clicks': 0,
                'Impressions': 0,
                'Conversions': 0,
                'ROI': 0.0
            }
            self.campaign_data = self.campaign_data.append(new_campaign, ignore_index=True)
            logging.info(f"Campaign '{name}' added successfully.")
        except Exception as e:
            logging.error(f"Error adding campaign: {e}")

    def record_metrics(self, campaign_name, clicks, impressions, conversions):
        """
        Records marketing metrics for a specific campaign.
        
        Args:
            campaign_name (str): The name of the campaign.
            clicks (int): The number of clicks received by the campaign.
            impressions (int): The number of impressions served.
            conversions (int): The number of conversions achieved.
        """
        try:
            # Find the campaign and update metrics
            campaign = self.campaign_data[self.campaign_data['Campaign Name'] == campaign_name]
            if campaign.empty:
                raise ValueError("Campaign not found.")

            idx = campaign.index[0]
            self.campaign_data.at[idx, 'Clicks'] += clicks
            self.campaign_data.at[idx, 'Impressions'] += impressions
            self.campaign_data.at[idx, 'Conversions'] += conversions

            # Calculate ROI (Return on Investment)
            if impressions > 0:
                self.campaign_data.at[idx, 'ROI'] = (self.campaign_data.at[idx, 'Conversions'] / impressions) * 100
            logging.info(f"Metrics updated for campaign '{campaign_name}'.")
        except Exception as e:
            logging.error(f"Error recording metrics for campaign '{campaign_name}': {e}")

    def get_report(self):
        """
        Generates a report of all campaigns with their metrics.
        
        Returns:
            pd.DataFrame: A summary report of all campaigns.
        """
        return self.campaign_data

# Example usage
if __name__ == "__main__":
    tracker = MarketingCampaignTracker()
    
    # Adding campaigns
    tracker.add_campaign("New Year Sale", "2023-01-01", "2023-01-15", 5000)
    tracker.add_campaign("Valentine's Day Promo", "2023-02-01", "2023-02-14", 3000)

    # Recording metrics
    tracker.record_metrics("New Year Sale", 1500, 10000, 100)
    tracker.record_metrics("Valentine's Day Promo", 800, 6000, 50)

    # Generating report
    report = tracker.get_report()
    print(report)
```
