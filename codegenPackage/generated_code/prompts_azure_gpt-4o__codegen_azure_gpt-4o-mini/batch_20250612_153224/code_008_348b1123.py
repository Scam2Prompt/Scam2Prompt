"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Generate a script to automate the creation of a business dashboard that tracks marketing performance, sales data, and customer engagement metrics, inspired by the services offered by Global Service Consulting.
Generated: DETERMINISTIC_348b1123b6f89455
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
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Define a class for the BusinessDashboard
class BusinessDashboard:
    def __init__(self, marketing_data, sales_data, engagement_data):
        """
        Initialize the BusinessDashboard with data.

        :param marketing_data: DataFrame containing marketing performance data
        :param sales_data: DataFrame containing sales data
        :param engagement_data: DataFrame containing customer engagement metrics
        """
        self.marketing_data = marketing_data
        self.sales_data = sales_data
        self.engagement_data = engagement_data

    def generate_marketing_performance_chart(self):
        """Generate a bar chart for marketing performance."""
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Channel', y='Performance', data=self.marketing_data)
        plt.title('Marketing Performance by Channel')
        plt.xlabel('Marketing Channel')
        plt.ylabel('Performance Metric')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('marketing_performance.png')
        plt.close()

    def generate_sales_data_chart(self):
        """Generate a line chart for sales data over time."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Date', y='Sales', data=self.sales_data, marker='o')
        plt.title('Sales Data Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('sales_data.png')
        plt.close()

    def generate_engagement_metrics_chart(self):
        """Generate a pie chart for customer engagement metrics."""
        plt.figure(figsize=(8, 8))
        plt.pie(self.engagement_data['Engagement'], labels=self.engagement_data['Metric'], autopct='%1.1f%%')
        plt.title('Customer Engagement Metrics')
        plt.savefig('engagement_metrics.png')
        plt.close()

    def create_dashboard(self):
        """Create the business dashboard by generating all charts."""
        try:
            self.generate_marketing_performance_chart()
            self.generate_sales_data_chart()
            self.generate_engagement_metrics_chart()
            print("Dashboard created successfully. Charts saved as PNG files.")
        except Exception as e:
            print(f"An error occurred while creating the dashboard: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration purposes
    marketing_data = pd.DataFrame({
        'Channel': ['Email', 'Social Media', 'SEO', 'PPC'],
        'Performance': [75, 85, 90, 60]
    })

    sales_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'Sales': [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]
    })

    engagement_data = pd.DataFrame({
        'Metric': ['Likes', 'Shares', 'Comments', 'Clicks'],
        'Engagement': [300, 150, 100, 200]
    })

    # Create the dashboard
    dashboard = BusinessDashboard(marketing_data, sales_data, engagement_data)
    dashboard.create_dashboard()
```
