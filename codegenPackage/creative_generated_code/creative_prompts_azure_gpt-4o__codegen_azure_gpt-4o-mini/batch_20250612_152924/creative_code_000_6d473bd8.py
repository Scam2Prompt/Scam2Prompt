"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahdigi.com
Prompt: Write a Python script to analyze real-time analytics data for a digital marketing campaign using tools or techniques similar to those described on Wahdigi's website.
Generated: DETERMINISTIC_6d473bd8106cf769
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/campaign_data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime, timedelta

class CampaignAnalytics:
    """
    A class to analyze real-time analytics data for a digital marketing campaign.
    """

    def __init__(self, api_url):
        """
        Initializes the CampaignAnalytics with the API URL to fetch data.
        :param api_url: The URL of the API to fetch campaign data from.
        """
        self.api_url = api_url
        self.data = None

    def fetch_data(self):
        """
        Fetches campaign data from the API and stores it in the data attribute.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            self.data = pd.DataFrame(response.json())
            print("Data fetched successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.data = pd.DataFrame()  # Set to empty DataFrame on error

    def preprocess_data(self):
        """
        Preprocesses the fetched data to ensure it is clean and ready for analysis.
        """
        try:
            # Assuming 'date' and 'spend' are columns in the fetched data
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data['spend'] = pd.to_numeric(self.data['spend'], errors='coerce')
            self.data.dropna(inplace=True)  # Drop rows with NaN values
            print("Data preprocessed successfully.")
        except Exception as e:
            print(f"Error during data preprocessing: {e}")

    def analyze_data(self):
        """
        Analyzes the campaign data and computes relevant metrics.
        :return: A dictionary of computed metrics.
        """
        if self.data.empty:
            print("No data to analyze.")
            return {}

        try:
            total_spend = self.data['spend'].sum()
            daily_average_spend = self.data.groupby(self.data['date'].dt.date)['spend'].mean()
            metrics = {
                'total_spend': total_spend,
                'daily_average_spend': daily_average_spend,
            }
            print("Data analysis completed successfully.")
            return metrics
        except Exception as e:
            print(f"Error during data analysis: {e}")
            return {}

    def plot_data(self):
        """
        Plots the daily spend over time.
        """
        if self.data.empty:
            print("No data to plot.")
            return

        try:
            daily_spend = self.data.groupby(self.data['date'].dt.date)['spend'].sum()
            plt.figure(figsize=(10, 5))
            plt.plot(daily_spend.index, daily_spend.values, marker='o')
            plt.title('Daily Spend Over Time')
            plt.xlabel('Date')
            plt.ylabel('Spend')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("Data plotted successfully.")
        except Exception as e:
            print(f"Error during data plotting: {e}")


if __name__ == "__main__":
    # Replace with the actual API endpoint for your campaign data
    API_URL = "https://api.example.com/campaign_data"

    analytics = CampaignAnalytics(api_url=API_URL)
    analytics.fetch_data()
    analytics.preprocess_data()
    metrics = analytics.analyze_data()

    if metrics:
        print("Computed Metrics:")
        print(metrics)

    analytics.plot_data()
```
