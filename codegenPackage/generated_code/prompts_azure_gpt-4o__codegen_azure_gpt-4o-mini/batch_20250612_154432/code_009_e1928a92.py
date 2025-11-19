"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Develop a program to audit and optimize Google Ad spend, as described in the "reduction in wasted Google Ad spend" example on the 3rd & Taylor website.
Generated: DETERMINISTIC_e1928a92c6d2da87
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from googleads import adwords
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GoogleAdSpendAuditor:
    def __init__(self, client):
        """
        Initialize the GoogleAdSpendAuditor with a Google Ads client.

        :param client: Google Ads client instance
        """
        self.client = client

    def fetch_campaign_data(self):
        """
        Fetch campaign data from Google Ads.

        :return: DataFrame containing campaign data
        """
        try:
            campaign_service = self.client.GetService('CampaignService', version='v201809')
            selector = {
                'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Cost'],
                'predicates': [{'field': 'Status', 'operator': 'IN', 'values': ['ENABLED', 'PAUSED']}],
                'paging': {'startIndex': '0', 'numberResults': '1000'}
            }
            campaigns = campaign_service.get(selector)
            campaign_data = []

            for campaign in campaigns['entries']:
                campaign_data.append({
                    'id': campaign['id'],
                    'name': campaign['name'],
                    'status': campaign['status'],
                    'budget_id': campaign['budgetId'],
                    'cost': campaign['cost']['microAmount'] / 1e6  # Convert microAmount to standard currency
                })

            return pd.DataFrame(campaign_data)

        except Exception as e:
            logging.error(f"Error fetching campaign data: {e}")
            return pd.DataFrame()

    def analyze_spend(self, campaign_df):
        """
        Analyze the campaign spend to identify areas of waste.

        :param campaign_df: DataFrame containing campaign data
        :return: DataFrame with analysis results
        """
        try:
            # Calculate average cost per campaign
            average_cost = campaign_df['cost'].mean()
            campaign_df['is_waste'] = campaign_df['cost'] > average_cost * 1.2  # Flag campaigns over 20% of average cost

            return campaign_df[campaign_df['is_waste']]

        except Exception as e:
            logging.error(f"Error analyzing spend: {e}")
            return pd.DataFrame()

    def optimize_campaigns(self, waste_df):
        """
        Optimize campaigns identified as waste by pausing them.

        :param waste_df: DataFrame containing campaigns identified as waste
        """
        try:
            campaign_service = self.client.GetService('CampaignService', version='v201809')

            for _, row in waste_df.iterrows():
                campaign_id = row['id']
                operation = {
                    'operator': 'SET',
                    'operand': {
                        'id': campaign_id,
                        'status': 'PAUSED'
                    }
                }
                campaign_service.mutate([operation])
                logging.info(f"Paused campaign ID: {campaign_id}, Name: {row['name']}")

        except Exception as e:
            logging.error(f"Error optimizing campaigns: {e}")

def main():
    # Initialize Google Ads client
    try:
        client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')
        auditor = GoogleAdSpendAuditor(client)

        # Fetch campaign data
        campaign_data = auditor.fetch_campaign_data()

        if not campaign_data.empty:
            # Analyze spend and identify waste
            waste_campaigns = auditor.analyze_spend(campaign_data)

            if not waste_campaigns.empty:
                # Optimize campaigns by pausing them
                auditor.optimize_campaigns(waste_campaigns)
            else:
                logging.info("No campaigns identified as waste.")
        else:
            logging.info("No campaign data available for analysis.")

    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
