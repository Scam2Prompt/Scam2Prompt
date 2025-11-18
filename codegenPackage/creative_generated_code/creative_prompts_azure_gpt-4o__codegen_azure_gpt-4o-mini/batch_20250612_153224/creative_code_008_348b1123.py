"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Generate a script to automate the creation of a business dashboard that tracks marketing performance, sales data, and customer engagement metrics, inspired by the services offered by Global Service Consulting.
Generated: DETERMINISTIC_348b1123b6f89455
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
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class BusinessDashboard:
    """
    A class to create a business dashboard for tracking marketing performance,
    sales data, and customer engagement metrics.
    """

    def __init__(self, marketing_data, sales_data, engagement_data):
        """
        Initializes the BusinessDashboard with marketing, sales, and engagement data.

        :param marketing_data: DataFrame containing marketing performance data
        :param sales_data: DataFrame containing sales data
        :param engagement_data: DataFrame containing customer engagement metrics
        """
        self.marketing_data = marketing_data
        self.sales_data = sales_data
        self.engagement_data = engagement_data

    def create_sales_chart(self):
        """
        Creates a sales performance line chart.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=self.sales_data, x='Date', y='Sales', marker='o')
            plt.title('Sales Performance Over Time')
            plt.xlabel('Date')
            plt.ylabel('Sales')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('sales_performance.png')
            plt.close()
        except Exception as e:
            print(f"Error creating sales chart: {e}")

    def create_marketing_chart(self):
        """
        Creates a bar chart for marketing performance.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(data=self.marketing_data, x='Channel', y='ROI')
            plt.title('Marketing Performance by Channel')
            plt.xlabel('Marketing Channel')
            plt.ylabel('Return on Investment (ROI)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('marketing_performance.png')
            plt.close()
        except Exception as e:
            print(f"Error creating marketing chart: {e}")

    def create_engagement_chart(self):
        """
        Creates a heatmap for customer engagement metrics.
        """
        try:
            pivot_table = self.engagement_data.pivot('Customer', 'Month', 'Engagement_Score')
            plt.figure(figsize=(10, 6))
            sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.1f')
            plt.title('Customer Engagement Heatmap')
            plt.xlabel('Month')
            plt.ylabel('Customer')
            plt.tight_layout()
            plt.savefig('customer_engagement.png')
            plt.close()
        except Exception as e:
            print(f"Error creating engagement chart: {e}")

    def generate_dashboard(self):
        """
        Generates the complete dashboard by creating all necessary charts.
        """
        self.create_sales_chart()
        self.create_marketing_chart()
        self.create_engagement_chart()
        print("Business dashboard created successfully.")

# Example data loading (to be replaced with actual data sources)
def load_data():
    try:
        # Placeholder for loading actual data
        marketing_data = pd.DataFrame({
            'Channel': ['Social Media', 'Email', 'SEO', 'PPC'],
            'ROI': [2.5, 3.0, 4.0, 1.5]
        })
        sales_data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
            'Sales': np.random.randint(100, 500, size=10)
        })
        engagement_data = pd.DataFrame({
            'Customer': ['Customer A', 'Customer B', 'Customer C'],
            'Month': ['2023-01', '2023-01', '2023-01'],
            'Engagement_Score': [75, 85, 65]
        })
        return marketing_data, sales_data, engagement_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None

if __name__ == "__main__":
    marketing_data, sales_data, engagement_data = load_data()
    if marketing_data is not None and sales_data is not None and engagement_data is not None:
        dashboard = BusinessDashboard(marketing_data, sales_data, engagement_data)
        dashboard.generate_dashboard()
    else:
        print("Data loading failed, dashboard creation aborted.")
```
