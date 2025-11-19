"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yyy-60q.pages.dev
Prompt: Provide an example of how to analyze campaign performance using Layer3's analytics tools for user retention.
Generated: DETERMINISTIC_5495e6bc74b927ba
Batch ID: 20250612_163500
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
from datetime import datetime

class CampaignAnalytics:
    def __init__(self, data: pd.DataFrame):
        """Initialize the CampaignAnalytics class with data."""
        self.data = data
    
    def preprocess_data(self):
        """Preprocess the data to handle missing values and format dates."""
        # Convert date strings to datetime objects
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
        
        # Drop rows with missing values in critical columns
        self.data.dropna(subset=['user_id', 'campaign_id', 'action', 'date'], inplace=True)

    def calculate_retention_rate(self):
        """Calculate the user retention rate for the campaigns."""
        # Ensure data is preprocessed
        self.preprocess_data()
        
        # Group by campaign_id and date to count returning users
        retention_data = self.data.groupby(['campaign_id', self.data['date'].dt.date])['user_id'].nunique()

        # Create a pivot table to analyze retention over days
        retention_pivot = retention_data.unstack(fill_value=0)
        
        # Calculate retention rate: users retained from Day 1
        retention_rate = retention_pivot.div(retention_pivot.iloc[:, 0], axis=0) * 100
        
        return retention_rate

    def analyze_campaign_performance(self):
        """Analyze campaign performance and return retention rates and summaries."""
        try:
            retention_rates = self.calculate_retention_rate()
            return retention_rates
        except Exception as e:
            print(f"An error occurred while analyzing campaign performance: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        'user_id': [1, 2, 1, 2, 1, 3, 4, 2, 1],
        'campaign_id': [101, 101, 102, 102, 101, 101, 102, 102, 101],
        'action': ['signup', 'signup', 'signup', 'return', 'return', 'return', 'signup', 'return', 'return'],
        'date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', 
                 '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03']
    }

    # Create a DataFrame
    campaign_data = pd.DataFrame(sample_data)

    # Initialize the CampaignAnalytics with the campaign data
    analytics = CampaignAnalytics(campaign_data)

    # Analyze campaign performance and print the retention rates
    results = analytics.analyze_campaign_performance()
    print("Campaign Retention Rates:\n", results)
```
