"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a Python script to calculate marketing-sourced revenue and track performance metrics, inspired by the case studies shared on the 3rd & Taylor website.
Generated: DETERMINISTIC_8ec1384a2542c8f5
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marketing_performance_tracker.py

import pandas as pd
from datetime import datetime

class MarketingPerformanceTracker:
    """
    Tracks marketing-sourced revenue and performance metrics.
    """

    def __init__(self, marketing_data, sales_data):
        """
        Initializes the tracker with marketing and sales data.

        Args:
            marketing_data (pd.DataFrame): Marketing campaign data.
            sales_data (pd.DataFrame): Sales data.
        """
        self.marketing_data = marketing_data
        self.sales_data = sales_data

    def calculate_marketing_sourced_revenue(self):
        """
        Calculates marketing-sourced revenue.

        Returns:
            float: Marketing-sourced revenue.
        """
        # Merge marketing and sales data on campaign ID
        merged_data = pd.merge(self.marketing_data, self.sales_data, on='campaign_id')

        # Filter for marketing-sourced sales
        marketing_sourced_sales = merged_data[merged_data['source'] == 'marketing']

        # Calculate marketing-sourced revenue
        marketing_sourced_revenue = marketing_sourced_sales['revenue'].sum()

        return marketing_sourced_revenue

    def track_performance_metrics(self):
        """
        Tracks performance metrics.

        Returns:
            dict: Performance metrics.
        """
        # Calculate marketing-sourced revenue
        marketing_sourced_revenue = self.calculate_marketing_sourced_revenue()

        # Calculate return on ad spend (ROAS)
        total_ad_spend = self.marketing_data['ad_spend'].sum()
        roas = marketing_sourced_revenue / total_ad_spend if total_ad_spend > 0 else 0

        # Calculate conversion rate
        total_conversions = self.sales_data['conversion'].sum()
        total_visitors = self.marketing_data['visitors'].sum()
        conversion_rate = total_conversions / total_visitors if total_visitors > 0 else 0

        # Create performance metrics dictionary
        performance_metrics = {
            'marketing_sourced_revenue': marketing_sourced_revenue,
            'roas': roas,
            'conversion_rate': conversion_rate
        }

        return performance_metrics

def load_data(marketing_data_file, sales_data_file):
    """
    Loads marketing and sales data from CSV files.

    Args:
        marketing_data_file (str): Marketing data file path.
        sales_data_file (str): Sales data file path.

    Returns:
        tuple: Marketing and sales data.
    """
    try:
        marketing_data = pd.read_csv(marketing_data_file)
        sales_data = pd.read_csv(sales_data_file)
        return marketing_data, sales_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: Data file is empty.")
        return None, None
    except pd.errors.ParserError as e:
        print(f"Error: {e}")
        return None, None

def main():
    marketing_data_file = 'marketing_data.csv'
    sales_data_file = 'sales_data.csv'

    marketing_data, sales_data = load_data(marketing_data_file, sales_data_file)

    if marketing_data is not None and sales_data is not None:
        tracker = MarketingPerformanceTracker(marketing_data, sales_data)
        marketing_sourced_revenue = tracker.calculate_marketing_sourced_revenue()
        performance_metrics = tracker.track_performance_metrics()

        print("Marketing-Sourced Revenue: $", marketing_sourced_revenue)
        print("Performance Metrics:")
        for metric, value in performance_metrics.items():
            print(f"{metric.capitalize().replace('_', ' ')}: {value:.2f}")

if __name__ == "__main__":
    main()
```
