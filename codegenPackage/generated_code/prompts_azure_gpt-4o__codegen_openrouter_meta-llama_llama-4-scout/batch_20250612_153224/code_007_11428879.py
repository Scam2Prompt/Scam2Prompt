"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to generate reports on cyberharassment awareness campaigns, similar to those conducted by Sophia Loisirs & Vie, including data visualization using Matplotlib or Seaborn.
Generated: DETERMINISTIC_11428879c8ad82c7
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
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to generate reports
def generate_report(campaign_data, campaign_name):
    """
    Generate a report on a cyberharassment awareness campaign.

    Parameters:
    campaign_data (dict): A dictionary containing campaign data.
    campaign_name (str): The name of the campaign.

    Returns:
    None
    """

    # Try to create a DataFrame from the campaign data
    try:
        df = pd.DataFrame(campaign_data)
    except Exception as e:
        print(f"Error creating DataFrame: {e}")
        return

    # Check if required columns exist
    required_columns = ['Date', 'Participants', 'Engagement']
    if not all(column in df.columns for column in required_columns):
        print("Error: Data is missing required columns.")
        return

    # Calculate total participants and engagement
    total_participants = df['Participants'].sum()
    total_engagement = df['Engagement'].sum()

    # Print campaign summary
    print(f"Campaign Name: {campaign_name}")
    print(f"Total Participants: {total_participants}")
    print(f"Total Engagement: {total_engagement}")

    # Create a line plot for participants over time
    plt.figure(figsize=(10,6))
    sns.lineplot(x='Date', y='Participants', data=df)
    plt.title(f'Participants Over Time - {campaign_name}')
    plt.xlabel('Date')
    plt.ylabel('Participants')
    plt.show()

    # Create a bar plot for engagement over time
    plt.figure(figsize=(10,6))
    sns.barplot(x='Date', y='Engagement', data=df)
    plt.title(f'Engagement Over Time - {campaign_name}')
    plt.xlabel('Date')
    plt.ylabel('Engagement')
    plt.show()

# Example usage
if __name__ == "__main__":
    campaign_data = {
        'Date': ['2022-01-01', '2022-01-15', '2022-02-01'],
        'Participants': [100, 150, 200],
        'Engagement': [500, 700, 900]
    }
    campaign_name = "Sophia Loisirs & Vie Cyberharassment Awareness"
    generate_report(campaign_data, campaign_name)
```
