"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: Write code for analytics and reporting that provides an overview of lead stages and revenue generated, as described in InfinitiAI's dashboard features.
Generated: DETERMINISTIC_2db97e6019d178fd
Batch ID: 20250612_154115
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

class LeadAnalytics:
    """
    A class to analyze lead stages and revenue generated.
    """

    def __init__(self, data):
        """
        Initializes the LeadAnalytics with the provided data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing lead information with columns:
                             'lead_id', 'stage', 'revenue', 'date_created'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns.
        Raises ValueError if any required column is missing.
        """
        required_columns = ['lead_id', 'stage', 'revenue', 'date_created']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def get_lead_stage_summary(self):
        """
        Summarizes the number of leads in each stage and total revenue generated.

        Returns:
        pd.DataFrame: A DataFrame summarizing lead stages and revenue.
        """
        summary = self.data.groupby('stage').agg(
            total_leads=('lead_id', 'count'),
            total_revenue=('revenue', 'sum')
        ).reset_index()
        return summary

    def plot_lead_stage_summary(self):
        """
        Plots a bar chart of lead stages and total revenue generated.
        """
        summary = self.get_lead_stage_summary()
        plt.figure(figsize=(10, 6))
        plt.bar(summary['stage'], summary['total_revenue'], color='skyblue')
        plt.title('Total Revenue by Lead Stage')
        plt.xlabel('Lead Stage')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def get_revenue_over_time(self):
        """
        Calculates total revenue generated over time.

        Returns:
        pd.DataFrame: A DataFrame with dates and corresponding total revenue.
        """
        self.data['date_created'] = pd.to_datetime(self.data['date_created'])
        revenue_over_time = self.data.groupby(self.data['date_created'].dt.to_period('M')).agg(
            total_revenue=('revenue', 'sum')
        ).reset_index()
        revenue_over_time['date_created'] = revenue_over_time['date_created'].dt.to_timestamp()
        return revenue_over_time

    def plot_revenue_over_time(self):
        """
        Plots a line chart of total revenue generated over time.
        """
        revenue_over_time = self.get_revenue_over_time()
        plt.figure(figsize=(10, 6))
        plt.plot(revenue_over_time['date_created'], revenue_over_time['total_revenue'], marker='o', color='orange')
        plt.title('Total Revenue Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Sample data creation
    data = {
        'lead_id': [1, 2, 3, 4, 5],
        'stage': ['New', 'Contacted', 'Qualified', 'Proposal', 'Closed'],
        'revenue': [1000, 1500, 2000, 2500, 3000],
        'date_created': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20']
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Initialize LeadAnalytics
    analytics = LeadAnalytics(df)

    # Get lead stage summary
    print(analytics.get_lead_stage_summary())

    # Plot lead stage summary
    analytics.plot_lead_stage_summary()

    # Plot revenue over time
    analytics.plot_revenue_over_time()
```
