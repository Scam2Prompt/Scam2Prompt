"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Write code to analyze the performance of digital advertising campaigns, including reach and engagement metrics, for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_71960c1a5c20d403
Batch ID: 20250612_153224
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

class CampaignPerformanceAnalyzer:
    """
    A class to analyze the performance of digital advertising campaigns.
    """

    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initializes the CampaignPerformanceAnalyzer with campaign data.

        :param campaign_data: Pandas DataFrame containing campaign metrics 
                              (columns: campaign_name, impressions, clicks, engagements, cost)
        """
        self.campaign_data = campaign_data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input campaign data for required columns.
        Throws ValueError if required columns are missing.
        """
        required_columns = {'campaign_name', 'impressions', 'clicks', 'engagements', 'cost'}
        if not required_columns.issubset(self.campaign_data.columns):
            raise ValueError(f"Missing required columns in campaign data. Required columns are: {required_columns}")

    def calculate_metrics(self):
        """
        Calculates performance metrics for each campaign and returns a DataFrame.

        :return: DataFrame with calculated metrics
                 (columns: campaign_name, ctr, cpm, cpa, engagement_rate)
        """
        metrics = self.campaign_data.copy()

        # Calculate Click-Through Rate (CTR) = clicks / impressions * 100
        metrics['ctr'] = np.where(metrics['impressions'] > 0, (metrics['clicks'] / metrics['impressions']) * 100, 0)

        # Calculate Cost per Thousand Impressions (CPM) = cost / impressions * 1000
        metrics['cpm'] = np.where(metrics['impressions'] > 0, (metrics['cost'] / metrics['impressions']) * 1000, np.nan)

        # Calculate Cost per Acquisition (CPA) = cost / engagements
        metrics['cpa'] = np.where(metrics['engagements'] > 0, metrics['cost'] / metrics['engagements'], np.nan)

        # Calculate Engagement Rate = engagements / impressions * 100
        metrics['engagement_rate'] = np.where(metrics['impressions'] > 0, (metrics['engagements'] / metrics['impressions']) * 100, 0)

        return metrics[['campaign_name', 'ctr', 'cpm', 'cpa', 'engagement_rate']]

    def summarize_performance(self):
        """
        Summarizes overall campaign performance metrics.

        :return: Dictionary with aggregated metrics (avg_ctr, avg_cpm, avg_cpa, avg_engagement_rate).
        """
        metrics = self.calculate_metrics()
        summary = {
            'avg_ctr': metrics['ctr'].mean(),
            'avg_cpm': metrics['cpm'].mean(),
            'avg_cpa': metrics['cpa'].mean(),
            'avg_engagement_rate': metrics['engagement_rate'].mean()
        }
        return summary


def main():
    """
    Main function to load data, analyze campaign performance, and display results.
    """
    try:
        # Example campaign data
        campaign_data = pd.DataFrame({
            'campaign_name': ['Campaign A', 'Campaign B', 'Campaign C'],
            'impressions': [10000, 15000, 20000],
            'clicks': [200, 300, 400],
            'engagements': [50, 75, 100],
            'cost': [500, 750, 1000]
        })

        # Initialize analyzer
        analyzer = CampaignPerformanceAnalyzer(campaign_data)

        # Calculate metrics for each campaign
        metrics = analyzer.calculate_metrics()
        print("Campaign Metrics:")
        print(metrics)

        # Summarize overall performance
        summary = analyzer.summarize_performance()
        print("\nOverall Performance Summary:")
        print(summary)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
