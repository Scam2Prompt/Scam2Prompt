"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Write code to generate reports on influencer campaign performance across multiple platforms, using PulseX Media's campaign tracking methods as a guide.
Generated: DETERMINISTIC_4f3612cb9bf6f476
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class CampaignPerformanceReport:
    def __init__(self, campaigns: List[Dict[str, Any]]):
        """
        Initializes the CampaignPerformanceReport with a list of campaign data.

        :param campaigns: List of campaign dictionaries containing campaign performance data
        """
        self.campaigns = campaigns

    def generate_report(self) -> pd.DataFrame:
        """
        Generates a performance report based on the provided campaign data.

        :return: DataFrame containing the aggregated performance report
        """
        try:
            # Create a DataFrame from the campaign data
            df = pd.DataFrame(self.campaigns)

            # Validate required columns
            required_columns = ['platform', 'impressions', 'clicks', 'conversions', 'spend']
            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f'Missing required column: {column}')

            # Group the data by platform and aggregate the performance metrics
            report = df.groupby('platform').agg(
                total_impressions=pd.NamedAgg(column='impressions', aggfunc='sum'),
                total_clicks=pd.NamedAgg(column='clicks', aggfunc='sum'),
                total_conversions=pd.NamedAgg(column='conversions', aggfunc='sum'),
                total_spend=pd.NamedAgg(column='spend', aggfunc='sum'),
                click_through_rate=pd.NamedAgg(column='clicks', aggfunc=lambda x: x.sum() / df['impressions'].sum() * 100),
                conversion_rate=pd.NamedAgg(column='conversions', aggfunc=lambda x: x.sum() / x.count() * 100)
            ).reset_index()

            return report

        except Exception as e:
            print(f"Error generating report: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    campaign_data = [
        {'platform': 'Instagram', 'impressions': 10000, 'clicks': 500, 'conversions': 50, 'spend': 200},
        {'platform': 'Facebook', 'impressions': 15000, 'clicks': 600, 'conversions': 40, 'spend': 250},
        {'platform': 'Twitter', 'impressions': 8000, 'clicks': 300, 'conversions': 30, 'spend': 150},
    ]

    # Initialize the report generator
    report_generator = CampaignPerformanceReport(campaign_data)

    # Generate the report
    report = report_generator.generate_report()

    # Print the report
    print(report)
```
