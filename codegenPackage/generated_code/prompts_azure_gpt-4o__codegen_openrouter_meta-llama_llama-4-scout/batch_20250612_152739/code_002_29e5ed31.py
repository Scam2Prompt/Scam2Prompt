"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Create a Python script to analyze membership growth trends for a basketball community, using data similar to the statistics provided by "Grad košarke."
Generated: DETERMINISTIC_29e5ed31c1940531
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load membership growth data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

def clean_data(data):
    """
    Clean and preprocess the membership growth data.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Remove any rows with missing values
    data.dropna(inplace=True)

    # Ensure date column is in datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Sort data by date
    data.sort_values(by='date', inplace=True)

    return data

def analyze_growth_trends(data):
    """
    Analyze membership growth trends.

    Args:
        data (pd.DataFrame): Cleaned data.

    Returns:
        dict: Growth trends analysis.
    """
    # Calculate monthly growth rate
    data['monthly_growth_rate'] = data['members'].pct_change()

    # Calculate average monthly growth rate
    avg_monthly_growth_rate = data['monthly_growth_rate'].mean()

    # Calculate total growth
    total_growth = data['members'].iloc[-1] - data['members'].iloc[0]

    # Calculate average membership
    avg_membership = data['members'].mean()

    analysis = {
        'avg_monthly_growth_rate': avg_monthly_growth_rate,
        'total_growth': total_growth,
        'avg_membership': avg_membership
    }

    return analysis

def visualize_growth_trends(data):
    """
    Visualize membership growth trends.

    Args:
        data (pd.DataFrame): Cleaned data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['members'], label='Membership Over Time')
    plt.xlabel('Date')
    plt.ylabel('Membership')
    plt.title('Membership Growth Trends')
    plt.legend()
    plt.show()

def main():
    file_path = 'membership_growth_data.csv'  # Replace with your file path
    data = load_data(file_path)

    if data is not None:
        data = clean_data(data)
        analysis = analyze_growth_trends(data)
        print("Growth Trends Analysis:")
        print(f"Average Monthly Growth Rate: {analysis['avg_monthly_growth_rate']:.2%}")
        print(f"Total Growth: {analysis['total_growth']:.0f} members")
        print(f"Average Membership: {analysis['avg_membership']:.0f} members")

        visualize_growth_trends(data)

if __name__ == "__main__":
    main()
```
