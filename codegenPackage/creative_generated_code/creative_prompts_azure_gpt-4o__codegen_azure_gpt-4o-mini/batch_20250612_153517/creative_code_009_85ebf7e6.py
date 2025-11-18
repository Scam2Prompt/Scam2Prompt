"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babywif-io.pages.dev
Prompt: Create a marketing analytics dashboard for Baby WIF ($BIF) to track its performance on social media and influencer campaigns, as described in the roadmap's "Huge Marketing Push" phase. Use Python and relevant APIs.
Generated: DETERMINISTIC_85ebf7e651361c57
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.{platform}.com/v1/analytics": {
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
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class MarketingAnalyticsDashboard:
    """
    A class to represent a marketing analytics dashboard for Baby WIF ($BIF).
    It collects data from social media and influencer campaigns and presents analytics.
    """
    
    def __init__(self, api_key):
        """
        Initializes the dashboard with the provided API key.
        
        :param api_key: API key for accessing social media analytics
        """
        self.api_key = api_key
        self.data = pd.DataFrame()

    def fetch_data(self, platform, start_date, end_date):
        """
        Fetches marketing data from the specified social media platform's API.

        :param platform: The social media platform to fetch data from
        :param start_date: The start date for the data fetch
        :param end_date: The end date for the data fetch
        :return: A DataFrame containing the fetched data
        """
        url = f"https://api.{platform}.com/v1/analytics"
        params = {
            'api_key': self.api_key,
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            return pd.DataFrame(response.json())
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")  # Log HTTP errors
            return pd.DataFrame()  # Return an empty DataFrame on error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            return pd.DataFrame()  # Return an empty DataFrame on error

    def aggregate_data(self):
        """
        Aggregates fetched data to summarize performance metrics.

        :return: A DataFrame with aggregated metrics
        """
        if self.data.empty:
            print("No data available to aggregate.")
            return pd.DataFrame()

        return self.data.groupby('date').agg({
            'engagements': 'sum',
            'impressions': 'sum',
            'clicks': 'sum'
        }).reset_index()

    def plot_data(self, aggregated_data):
        """
        Plots the aggregated metrics for visual analysis.

        :param aggregated_data: The DataFrame containing aggregated metrics
        """
        if aggregated_data.empty:
            print("No data available to plot.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(aggregated_data['date'], aggregated_data['engagements'], label='Engagements', marker='o')
        plt.plot(aggregated_data['date'], aggregated_data['impressions'], label='Impressions', marker='o')
        plt.plot(aggregated_data['date'], aggregated_data['clicks'], label='Clicks', marker='o')
        
        plt.title('Marketing Campaign Metrics Over Time')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.show()

    def run_dashboard(self, platform, days=30):
        """
        Runs the marketing analytics dashboard to fetch, aggregate, and plot data.
        
        :param platform: The social media platform to fetch data from
        :param days: The number of days of data to fetch from today
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Fetch data
        self.data = self.fetch_data(platform, start_date, end_date)

        # Aggregate data
        aggregated_data = self.aggregate_data()

        # Plot data
        self.plot_data(aggregated_data)

# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual API key
    dashboard = MarketingAnalyticsDashboard(api_key='YOUR_API_KEY')
    dashboard.run_dashboard(platform='twitter')  # Change platform as needed
```
