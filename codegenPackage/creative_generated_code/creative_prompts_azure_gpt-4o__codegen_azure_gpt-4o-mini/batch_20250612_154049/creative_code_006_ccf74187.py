"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silvansong.com
Prompt: Develop a program to track and measure the effectiveness of promotional campaigns, using the data-driven strategies described on Silvansong.com.
Generated: DETERMINISTIC_ccf741875b333620
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import logging
from datetime import datetime

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Campaign:
    """
    Class to represent a promotional campaign.
    """
    
    def __init__(self, name, start_date, end_date, budget):
        """
        Initializes a new campaign.

        :param name: str - The name of the campaign
        :param start_date: str - Start date of the campaign in 'YYYY-MM-DD' format
        :param end_date: str - End date of the campaign in 'YYYY-MM-DD' format
        :param budget: float - Budget allocated for the campaign
        """
        try:
            self.name = name
            self.start_date = pd.to_datetime(start_date)
            self.end_date = pd.to_datetime(end_date)
            self.budget = budget
            self.data = pd.DataFrame(columns=['date', 'impressions', 'clicks', 'conversions', 'spend'])
            logging.info(f"Campaign '{self.name}' created successfully.")
        except Exception as e:
            logging.error("Error initializing campaign: %s", e)
            raise

    def record_data(self, date, impressions, clicks, conversions, spend):
        """
        Records performance data for the campaign.

        :param date: str - Date of the recorded data in 'YYYY-MM-DD' format
        :param impressions: int - Number of impressions
        :param clicks: int - Number of clicks
        :param conversions: int - Number of conversions
        :param spend: float - Amount spent on that date
        """
        try:
            date = pd.to_datetime(date)
            if self.start_date <= date <= self.end_date:
                self.data = self.data.append({
                    'date': date,
                    'impressions': impressions,
                    'clicks': clicks,
                    'conversions': conversions,
                    'spend': spend
                }, ignore_index=True)
                logging.info(f"Data recorded for {self.name} on {date.date()}.")
            else:
                logging.warning("Date %s is out of the campaign range.", date.date())
        except Exception as e:
            logging.error("Error recording data: %s", e)
            raise

    def calculate_metrics(self):
        """
        Calculates key performance metrics for the campaign.

        :return: dict - A dictionary containing calculated metrics
        """
        try:
            total_impressions = self.data['impressions'].sum()
            total_clicks = self.data['clicks'].sum()
            total_conversions = self.data['conversions'].sum()
            total_spend = self.data['spend'].sum()

            metrics = {
                'CTR': (total_clicks / total_impressions * 100) if total_impressions > 0 else 0,
                'CPC': (total_spend / total_clicks) if total_clicks > 0 else 0,
                'ConversionRate': (total_conversions / total_clicks * 100) if total_clicks > 0 else 0,
                'ROI': ((total_conversions * 100) / total_spend) if total_spend > 0 else 0
            }
            logging.info("Metrics calculated for campaign '%s'.", self.name)
            return metrics
        except Exception as e:
            logging.error("Error calculating metrics: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    try:
        campaign = Campaign(name="Summer Sale", start_date="2023-06-01", end_date="2023-06-30", budget=5000)
        campaign.record_data("2023-06-01", impressions=1000, clicks=50, conversions=5, spend=200)
        campaign.record_data("2023-06-02", impressions=1500, clicks=75, conversions=10, spend=300)

        metrics = campaign.calculate_metrics()
        logging.info("Campaign Metrics: %s", metrics)

    except Exception as e:
        logging.error("An error occurred in the campaign tracking: %s", e)
```
