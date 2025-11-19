"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write code to analyze trends in charitable giving by the Armourers & Brasiers' Company over the last decade, using historical data.
Generated: DETERMINISTIC_3bd1f14ddda041bd
Batch ID: 20250612_150651
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

def load_historical_data(file_path):
    """
    Load historical charitable giving data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing historical data.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ['Year', 'Donation_Amount', 'Recipient_Type']
        if not all(column in data.columns for column in required_columns):
            raise ValueError("Invalid data format. Required columns: {}".format(required_columns))

        return data
    except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))
        return None
    except pd.errors.EmptyDataError:
        print("Error: No data in file at {}".format(file_path))
        return None
    except pd.errors.ParserError as e:
        print("Error: Failed to parse file at {}: {}".format(file_path, e))
        return None

def analyze_trends(data):
    """
    Analyze trends in charitable giving by the Armourers & Brasiers' Company.

    Args:
        data (pd.DataFrame): A DataFrame containing the historical data.

    Returns:
        dict: A dictionary containing trend analysis results.
    """
    # Ensure data is not empty
    if data is None or data.empty:
        return {}

    # Calculate total donations per year
    yearly_donations = data.groupby('Year')['Donation_Amount'].sum().reset_index()

    # Calculate average annual donation
    average_annual_donation = yearly_donations['Donation_Amount'].mean()

    # Identify top 5 recipients by total donation amount
    top_recipients = data.groupby('Recipient_Type')['Donation_Amount'].sum().sort_values(ascending=False).head(5)

    # Calculate donation distribution by recipient type
    recipient_distribution = data['Recipient_Type'].value_counts(normalize=True).sort_values(ascending=False)

    return {
        'yearly_donations': yearly_donations,
        'average_annual_donation': average_annual_donation,
        'top_recipients': top_recipients,
        'recipient_distribution': recipient_distribution
    }

def visualize_trends(trend_analysis):
    """
    Visualize trends in charitable giving by the Armourers & Brasiers' Company.

    Args:
        trend_analysis (dict): A dictionary containing trend analysis results.
    """
    # Plot yearly donations
    plt.figure(figsize=(10, 6))
    plt.plot(trend_analysis['yearly_donations']['Year'], trend_analysis['yearly_donations']['Donation_Amount'], marker='o')
    plt.title('Yearly Donations')
    plt.xlabel('Year')
    plt.ylabel('Donation Amount')
    plt.grid(True)
    plt.show()

    # Plot recipient distribution
    plt.figure(figsize=(10, 6))
    plt.bar(trend_analysis['recipient_distribution'].index, trend_analysis['recipient_distribution'].values)
    plt.title('Donation Distribution by Recipient Type')
    plt.xlabel('Recipient Type')
    plt.ylabel('Proportion of Total Donations')
    plt.grid(True)
    plt.show()

def main():
    file_path = 'charitable_giving_data.csv'  # Update with actual file path
    data = load_historical_data(file_path)
    trend_analysis = analyze_trends(data)

    if trend_analysis:
        print("Average Annual Donation: {}".format(trend_analysis['average_annual_donation']))
        print("Top 5 Recipients by Total Donation Amount:")
        print(trend_analysis['top_recipients'])
        visualize_trends(trend_analysis)

if __name__ == "__main__":
    main()
```
