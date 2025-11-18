"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Write code to analyze weekly and monthly audience behavior analytics for book marketing, using Penguin Books Publishers' Multi-Focus Fusion Approach™ as a reference.
Generated: DETERMINISTIC_d91ce326e0accb5a
Batch ID: 20250612_154236
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class AudienceAnalytics:
    """
    A class to analyze weekly and monthly audience behavior analytics for book marketing.
    This class utilizes the Multi-Focus Fusion Approach™ to process audience data.
    """

    def __init__(self, data):
        """
        Initializes the AudienceAnalytics class with the provided data.

        :param data: A DataFrame containing audience data with 'date' and 'engagement' columns.
        """
        self.data = data
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.validate_data()

    def validate_data(self):
        """
        Validates the data for required columns and types.
        Raises ValueError if validation fails.
        """
        required_columns = ['date', 'engagement']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            raise ValueError("The 'date' column must be of datetime type.")
        if not np.issubdtype(self.data['engagement'].dtype, np.number):
            raise ValueError("The 'engagement' column must be numeric.")

    def weekly_analysis(self):
        """
        Analyzes weekly audience engagement data.

        :return: A DataFrame with weekly engagement statistics.
        """
        # Resampling the data to weekly frequency, summing engagement
        weekly_data = self.data.resample('W-Mon', on='date').sum().reset_index()
        weekly_data['week'] = weekly_data['date'].dt.strftime('%Y-%U')
        
        return weekly_data[['week', 'engagement']]

    def monthly_analysis(self):
        """
        Analyzes monthly audience engagement data.

        :return: A DataFrame with monthly engagement statistics.
        """
        # Resampling the data to monthly frequency, summing engagement
        monthly_data = self.data.resample('M', on='date').sum().reset_index()
        monthly_data['month'] = monthly_data['date'].dt.strftime('%Y-%m')
        
        return monthly_data[['month', 'engagement']]

    def plot_engagement(self, analysis_type='weekly'):
        """
        Plots engagement data for weekly or monthly analysis.

        :param analysis_type: Type of analysis ('weekly' or 'monthly').
        """
        if analysis_type == 'weekly':
            data = self.weekly_analysis()
            title = 'Weekly Audience Engagement'
            x_label = 'Week'
        elif analysis_type == 'monthly':
            data = self.monthly_analysis()
            title = 'Monthly Audience Engagement'
            x_label = 'Month'
        else:
            raise ValueError("Invalid analysis type. Choose 'weekly' or 'monthly'.")

        plt.figure(figsize=(12, 6))
        plt.bar(data.iloc[:, 0], data['engagement'], color='skyblue')
        plt.xticks(rotation=45)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel('Engagement')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()


# Sample usage
if __name__ == "__main__":
    # Sample data creation
    sample_data = {
        'date': pd.date_range(start=datetime(2023, 1, 1), periods=100, freq='D'),
        'engagement': np.random.randint(1, 100, size=100)
    }
    sample_df = pd.DataFrame(sample_data)

    try:
        analytics = AudienceAnalytics(sample_df)
        print("Weekly Analysis:\n", analytics.weekly_analysis())
        print("Monthly Analysis:\n", analytics.monthly_analysis())
        analytics.plot_engagement('weekly')
        analytics.plot_engagement('monthly')
    except ValueError as e:
        print(f"Error: {e}")
```
