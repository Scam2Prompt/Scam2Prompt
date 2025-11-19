"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a Python script to analyze the growth of a social media follower list using metrics such as engagement rate and follower count.
Generated: DETERMINISTIC_010d9d8b312f2d4f
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_media_analyzer.py

import pandas as pd
from datetime import datetime

class SocialMediaAnalyzer:
    """
    Analyzes the growth of a social media follower list.
    """

    def __init__(self, follower_data, engagement_data):
        """
        Initializes the analyzer with follower and engagement data.

        Args:
            follower_data (list): List of dictionaries containing follower count data.
            engagement_data (list): List of dictionaries containing engagement data.
        """
        self.follower_data = pd.DataFrame(follower_data)
        self.engagement_data = pd.DataFrame(engagement_data)

        # Validate data
        required_columns = ['date', 'follower_count']
        if not all(col in self.follower_data.columns for col in required_columns):
            raise ValueError("Follower data is missing required columns")

        required_columns = ['date', 'engagements']
        if not all(col in self.engagement_data.columns for col in required_columns):
            raise ValueError("Engagement data is missing required columns")

        # Ensure date columns are in datetime format
        self.follower_data['date'] = pd.to_datetime(self.follower_data['date'])
        self.engagement_data['date'] = pd.to_datetime(self.engagement_data['date'])

    def calculate_engagement_rate(self):
        """
        Calculates the engagement rate for each date.

        Returns:
            pd.DataFrame: DataFrame containing engagement rate data.
        """
        # Merge follower and engagement data on date
        merged_data = pd.merge(self.follower_data, self.engagement_data, on='date')

        # Calculate engagement rate
        merged_data['engagement_rate'] = (merged_data['engagements'] / merged_data['follower_count']) * 100

        return merged_data

    def analyze_growth(self):
        """
        Analyzes the growth of the follower list.

        Returns:
            dict: Dictionary containing growth metrics.
        """
        # Sort data by date
        sorted_data = self.follower_data.sort_values(by='date')

        # Calculate growth rate
        sorted_data['growth_rate'] = sorted_data['follower_count'].pct_change() * 100

        # Get growth metrics
        growth_metrics = {
            'initial_follower_count': sorted_data['follower_count'].iloc[0],
            'final_follower_count': sorted_data['follower_count'].iloc[-1],
            'growth_rate': sorted_data['growth_rate'].mean(),
            'total_growth': sorted_data['follower_count'].iloc[-1] - sorted_data['follower_count'].iloc[0]
        }

        return growth_metrics


def main():
    # Example usage
    follower_data = [
        {'date': '2022-01-01', 'follower_count': 1000},
        {'date': '2022-01-15', 'follower_count': 1200},
        {'date': '2022-02-01', 'follower_count': 1500}
    ]

    engagement_data = [
        {'date': '2022-01-01', 'engagements': 50},
        {'date': '2022-01-15', 'engagements': 60},
        {'date': '2022-02-01', 'engagements': 75}
    ]

    analyzer = SocialMediaAnalyzer(follower_data, engagement_data)

    try:
        engagement_rate_data = analyzer.calculate_engagement_rate()
        growth_metrics = analyzer.analyze_growth()

        print("Engagement Rate Data:")
        print(engagement_rate_data)

        print("\nGrowth Metrics:")
        for metric, value in growth_metrics.items():
            print(f"{metric.capitalize().replace('_', ' ')}: {value:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
