"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Write code to analyze the performance of digital advertising campaigns, including reach and engagement metrics, for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_71960c1a5c20d403
Batch ID: 20250612_153224
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
import matplotlib.pyplot as plt

class AdCampaignAnalyzer:
    """
    A class to analyze the performance of digital advertising campaigns.
    
    Attributes:
        data (pd.DataFrame): A DataFrame containing campaign data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the AdCampaignAnalyzer with campaign data.

        Parameters:
            data (pd.DataFrame): A DataFrame containing campaign data with columns:
                                 'campaign_name', 'reach', 'engagement', 'impressions', 'clicks'.
        """
        self.data = data

    def calculate_metrics(self):
        """
        Calculates performance metrics for each campaign.

        Returns:
            pd.DataFrame: A DataFrame with calculated metrics including CTR and engagement rate.
        """
        try:
            # Ensure required columns are present
            required_columns = ['campaign_name', 'reach', 'engagement', 'impressions', 'clicks']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError("DataFrame must contain the following columns: " + ", ".join(required_columns))

            # Calculate Click-Through Rate (CTR) and Engagement Rate
            self.data['CTR'] = self.data['clicks'] / self.data['impressions']
            self.data['Engagement Rate'] = self.data['engagement'] / self.data['reach']

            return self.data[['campaign_name', 'reach', 'engagement', 'CTR', 'Engagement Rate']]
        except Exception as e:
            print(f"Error calculating metrics: {e}")
            return None

    def plot_metrics(self):
        """
        Plots the reach and engagement metrics for each campaign.
        """
        try:
            metrics = self.calculate_metrics()
            if metrics is None:
                return

            # Set up the plot
            fig, ax1 = plt.subplots(figsize=(10, 6))

            # Plot Reach
            ax1.bar(metrics['campaign_name'], metrics['reach'], color='b', alpha=0.6, label='Reach')
            ax1.set_xlabel('Campaign Name')
            ax1.set_ylabel('Reach', color='b')
            ax1.tick_params(axis='y', labelcolor='b')

            # Create a second y-axis for Engagement Rate
            ax2 = ax1.twinx()
            ax2.plot(metrics['campaign_name'], metrics['Engagement Rate'], color='r', marker='o', label='Engagement Rate')
            ax2.set_ylabel('Engagement Rate', color='r')
            ax2.tick_params(axis='y', labelcolor='r')

            # Add title and legend
            plt.title('Digital Advertising Campaign Performance')
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')

            # Show plot
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting metrics: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        'campaign_name': ['Campaign A', 'Campaign B', 'Campaign C'],
        'reach': [1000, 1500, 2000],
        'engagement': [100, 200, 300],
        'impressions': [5000, 7000, 8000],
        'clicks': [50, 70, 90]
    }

    # Create a DataFrame
    campaign_df = pd.DataFrame(sample_data)

    # Initialize the analyzer
    analyzer = AdCampaignAnalyzer(campaign_df)

    # Calculate metrics and print them
    metrics = analyzer.calculate_metrics()
    print(metrics)

    # Plot the metrics
    analyzer.plot_metrics()
```
