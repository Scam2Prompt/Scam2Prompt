"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamadver.com
Prompt: Develop a performance monitoring dashboard for social media campaigns, incorporating analytics similar to those offered by Team Adver.
Generated: DETERMINISTIC_768fe70732324207
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for data handling and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class SocialMediaCampaignMonitor:
    """
    A class to monitor and analyze social media campaign performance.
    
    Attributes:
        campaigns (DataFrame): A DataFrame to hold campaign data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SocialMediaCampaignMonitor with campaign data.
        
        Parameters:
            data (pd.DataFrame): A DataFrame containing campaign data with columns:
                                 ['Campaign Name', 'Date', 'Impressions', 'Clicks', 'Conversions']
        """
        self.campaigns = data

    def preprocess_data(self):
        """
        Preprocess the campaign data: converts date strings to datetime objects and drops any rows with missing values.
        """
        try:
            self.campaigns['Date'] = pd.to_datetime(self.campaigns['Date'])
            self.campaigns.dropna(inplace=True)
        except Exception as e:
            print(f"Error in preprocessing data: {e}")

    def calculate_metrics(self):
        """
        Calculate performance metrics for each campaign.
        
        Returns:
            pd.DataFrame: A DataFrame with calculated metrics including CTR and Conversion Rate.
        """
        try:
            self.campaigns['CTR'] = self.campaigns['Clicks'] / self.campaigns['Impressions'] * 100
            self.campaigns['Conversion Rate'] = self.campaigns['Conversions'] / self.campaigns['Clicks'] * 100
            return self.campaigns[['Campaign Name', 'Date', 'Impressions', 'Clicks', 'Conversions', 'CTR', 'Conversion Rate']]
        except Exception as e:
            print(f"Error in calculating metrics: {e}")
            return pd.DataFrame()

    def plot_performance(self):
        """
        Plot campaign performance metrics.
        """
        try:
            plt.figure(figsize=(12, 8))
            sns.lineplot(data=self.campaigns, x='Date', y='CTR', hue='Campaign Name', marker='o')
            plt.title('Campaign Click-Through Rate (CTR) Over Time')
            plt.xlabel('Date')
            plt.ylabel('CTR (%)')
            plt.xticks(rotation=45)
            plt.legend(title='Campaign Name')
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(12, 8))
            sns.lineplot(data=self.campaigns, x='Date', y='Conversion Rate', hue='Campaign Name', marker='o')
            plt.title('Campaign Conversion Rate Over Time')
            plt.xlabel('Date')
            plt.ylabel('Conversion Rate (%)')
            plt.xticks(rotation=45)
            plt.legend(title='Campaign Name')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error in plotting performance: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration purposes
    data = {
        'Campaign Name': ['Campaign A', 'Campaign A', 'Campaign B', 'Campaign B'],
        'Date': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-02'],
        'Impressions': [1000, 1500, 800, 1200],
        'Clicks': [100, 200, 50, 100],
        'Conversions': [10, 30, 5, 15]
    }

    # Create a DataFrame
    campaign_data = pd.DataFrame(data)

    # Initialize the monitor
    monitor = SocialMediaCampaignMonitor(campaign_data)

    # Preprocess data
    monitor.preprocess_data()

    # Calculate metrics
    metrics_df = monitor.calculate_metrics()
    print(metrics_df)

    # Plot performance
    monitor.plot_performance()
```
