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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def generate_report(data):
    """
    Generate a report on cyberharassment awareness campaigns.

    Parameters:
    data (pd.DataFrame): DataFrame containing campaign data.
    """
    if data is None or data.empty:
        print("No data available to generate report.")
        return

    # Summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Visualize the number of campaigns over time
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='year', palette='viridis')
    plt.title('Number of Cyberharassment Awareness Campaigns Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Campaigns')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('campaigns_over_years.png')
    plt.show()

    # Visualize the distribution of campaign types
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='campaign_type', palette='pastel')
    plt.title('Distribution of Campaign Types')
    plt.xlabel('Campaign Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('campaign_types_distribution.png')
    plt.show()

def main():
    """
    Main function to execute the report generation.
    """
    # Define the path to the data file
    data_file_path = 'cyberharassment_campaigns.csv'

    # Load the data
    campaign_data = load_data(data_file_path)

    # Generate the report
    generate_report(campaign_data)

if __name__ == "__main__":
    main()
```
