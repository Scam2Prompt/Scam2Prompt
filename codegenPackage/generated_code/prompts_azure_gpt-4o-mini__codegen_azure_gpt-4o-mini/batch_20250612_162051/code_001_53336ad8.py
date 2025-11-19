"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Write a code snippet to automate the tracking of marketing campaign results for a small business, inspired by the marketing solutions provided by NMKT.
Generated: DETERMINISTIC_53336ad8e134f2b1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaignTracker:
    def __init__(self):
        """Initialize the tracker with an empty DataFrame."""
        self.campaign_data = pd.DataFrame(columns=['Campaign', 'Date', 'Clicks', 'Conversions', 'Spend'])

    def add_campaign_data(self, campaign, date, clicks, conversions, spend):
        """
        Add data for a marketing campaign.

        Parameters:
        campaign (str): The name of the marketing campaign.
        date (str): The date of the campaign data in 'YYYY-MM-DD' format.
        clicks (int): The number of clicks received.
        conversions (int): The number of conversions made.
        spend (float): The amount spent on the campaign.
        """
        try:
            # Convert date string to datetime object
            date = datetime.strptime(date, '%Y-%m-%d')
            # Append new data to the DataFrame
            new_data = pd.DataFrame([[campaign, date, clicks, conversions, spend]], 
                                     columns=self.campaign_data.columns)
            self.campaign_data = pd.concat([self.campaign_data, new_data], ignore_index=True)
            logging.info(f"Added data for campaign: {campaign} on {date.date()}")
        except Exception as e:
            logging.error(f"Error adding campaign data: {e}")

    def generate_report(self):
        """Generate a report of the campaign results."""
        try:
            if self.campaign_data.empty:
                logging.warning("No campaign data available to generate a report.")
                return
            
            # Group by campaign and calculate total metrics
            report = self.campaign_data.groupby('Campaign').agg({
                'Clicks': 'sum',
                'Conversions': 'sum',
                'Spend': 'sum'
            }).reset_index()

            # Calculate conversion rate
            report['Conversion Rate'] = report['Conversions'] / report['Clicks'].replace(0, 1) * 100
            
            # Display the report
            print(report)
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")

    def visualize_results(self):
        """Visualize the campaign results using a bar chart."""
        try:
            report = self.generate_report()
            if report is None:
                return
            
            # Plotting the results
            report.set_index('Campaign')[['Clicks', 'Conversions', 'Spend']].plot(kind='bar', figsize=(10, 6))
            plt.title('Marketing Campaign Results')
            plt.ylabel('Count / Spend')
            plt.xlabel('Campaign')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logging.error(f"Error visualizing results: {e}")

# Example usage
if __name__ == "__main__":
    tracker = MarketingCampaignTracker()
    tracker.add_campaign_data('Spring Sale', '2023-03-01', 150, 30, 200.00)
    tracker.add_campaign_data('Summer Promo', '2023-06-15', 200, 50, 300.00)
    tracker.generate_report()
    tracker.visualize_results()
```
