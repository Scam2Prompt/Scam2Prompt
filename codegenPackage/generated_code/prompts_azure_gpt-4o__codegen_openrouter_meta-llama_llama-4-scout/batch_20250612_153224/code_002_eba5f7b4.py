"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Generate code to analyze the effectiveness of a marketing strategy for small businesses, using data visualization libraries like Matplotlib or Seaborn to display trends in campaign performance.
Generated: DETERMINISTIC_eba5f7b4efd74f18
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to analyze marketing strategy effectiveness
def analyze_marketing_strategy(data):
    """
    Analyze the effectiveness of a marketing strategy for small businesses.

    Parameters:
    data (pandas.DataFrame): DataFrame containing marketing campaign data.
        Required columns: 'campaign_name', 'cost', 'revenue', 'date'

    Returns:
    None
    """

    # Check if required columns exist in the DataFrame
    required_columns = ['campaign_name', 'cost', 'revenue', 'date']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("DataFrame is missing required columns")

    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Calculate return on investment (ROI)
    data['roi'] = (data['revenue'] - data['cost']) / data['cost']

    # Group data by campaign and calculate total cost, revenue, and ROI
    campaign_data = data.groupby('campaign_name').agg({
        'cost': 'sum',
        'revenue': 'sum',
        'roi': 'mean'
    }).reset_index()

    # Sort campaign data by ROI in descending order
    campaign_data = campaign_data.sort_values(by='roi', ascending=False)

    # Create a bar chart to display campaign performance
    plt.figure(figsize=(10, 6))
    sns.barplot(x='campaign_name', y='roi', data=campaign_data)
    plt.title('Campaign Performance (ROI)')
    plt.xlabel('Campaign Name')
    plt.ylabel('Return on Investment (ROI)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    # Create a line chart to display revenue and cost over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='revenue', data=data, label='Revenue')
    sns.lineplot(x='date', y='cost', data=data, label='Cost')
    plt.title('Revenue and Cost Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.show()

    # Create a scatter plot to display relationship between cost and revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='cost', y='revenue', data=data)
    plt.title('Relationship Between Cost and Revenue')
    plt.xlabel('Cost')
    plt.ylabel('Revenue')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample marketing campaign data
    data = pd.DataFrame({
        'campaign_name': ['Campaign 1', 'Campaign 1', 'Campaign 2', 'Campaign 2', 'Campaign 3', 'Campaign 3'],
        'cost': [1000, 2000, 500, 1500, 2000, 3000],
        'revenue': [2000, 4000, 1000, 3000, 4000, 6000],
        'date': ['2022-01-01', '2022-02-01', '2022-01-01', '2022-02-01', '2022-01-01', '2022-02-01']
    })

    analyze_marketing_strategy(data)
```
