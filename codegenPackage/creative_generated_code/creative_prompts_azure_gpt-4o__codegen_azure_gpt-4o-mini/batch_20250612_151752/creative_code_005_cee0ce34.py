"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Create a Python script to analyze the ROI of social media video campaigns produced by Kraken Media, focusing on metrics like clicks, conversions, and revenue.
Generated: DETERMINISTIC_cee0ce349527f72b
Batch ID: 20250612_151752
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

class SocialMediaCampaignROIAnalyzer:
    """
    A class to analyze the ROI of social media video campaigns.
    """

    def __init__(self, data_frame):
        """
        Initializes the analyzer with a DataFrame containing campaign data.

        Args:
            data_frame (pd.DataFrame): A DataFrame with columns 'campaign', 'clicks', 'conversions', 'revenue'.
        """
        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        
        required_columns = {'campaign', 'clicks', 'conversions', 'revenue'}
        if not required_columns.issubset(data_frame.columns):
            raise ValueError(f"Input DataFrame must contain the following columns: {required_columns}")

        self.data_frame = data_frame

    def calculate_roi(self):
        """
        Calculates the ROI for each campaign.

        Returns:
            pd.DataFrame: A DataFrame with campaigns and their respective ROIs.
        """
        # Calculate ROI as (Revenue - Cost) / Cost
        # Assuming Cost is a fixed percentage of Revenue for this example.
        cost_percentage = 0.2  # Assuming 20% of revenue is the cost
        self.data_frame['cost'] = self.data_frame['revenue'] * cost_percentage
        self.data_frame['roi'] = (self.data_frame['revenue'] - self.data_frame['cost']) / self.data_frame['cost']

        return self.data_frame[['campaign', 'clicks', 'conversions', 'revenue', 'roi']]

    def summary(self):
        """
        Provides a summary of the campaign metrics.

        Returns:
            dict: A dictionary containing total clicks, total conversions, total revenue, and average ROI.
        """
        total_clicks = self.data_frame['clicks'].sum()
        total_conversions = self.data_frame['conversions'].sum()
        total_revenue = self.data_frame['revenue'].sum()
        average_roi = self.data_frame['roi'].mean()

        return {
            'Total Clicks': total_clicks,
            'Total Conversions': total_conversions,
            'Total Revenue': total_revenue,
            'Average ROI': average_roi
        }

def main():
    # Sample campaign data for demonstration
    data = {
        'campaign': ['Campaign A', 'Campaign B', 'Campaign C'],
        'clicks': [1000, 1500, 2000],
        'conversions': [100, 150, 200],
        'revenue': [5000, 7500, 10000]
    }

    # Create a DataFrame
    campaign_data = pd.DataFrame(data)

    try:
        # Initialize the analyzer
        analyzer = SocialMediaCampaignROIAnalyzer(campaign_data)
        
        # Calculate ROI
        roi_results = analyzer.calculate_roi()
        print("ROI Results:")
        print(roi_results)

        # Get summary of metrics
        summary = analyzer.summary()
        print("\nCampaign Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
