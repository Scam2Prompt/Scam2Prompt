"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to generate reports on cyberharassment awareness campaigns, similar to those conducted by Sophia Loisirs & Vie, including data visualization using Matplotlib or Seaborn.
Generated: DETERMINISTIC_11428879c8ad82c7
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
import os

# Set the aesthetics for seaborn
sns.set(style="whitegrid")

def load_campaign_data(file_path):
    """
    Load campaign data from a CSV file.

    :param file_path: str, path to the CSV file containing campaign data.
    :return: DataFrame containing the campaign data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse the file {file_path}.")
        return None

def visualize_campaign_data(data):
    """
    Visualize the awareness campaign data.

    :param data: DataFrame containing the campaign data.
    """
    # Check if data is valid
    if data is None or data.empty:
        print("No data available for visualization.")
        return

    # Generate a bar plot for campaigns by reach
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Campaign_Name', y='Reach', data=data, palette='viridis')
    plt.title('Awareness Campaign Reach')
    plt.xlabel('Campaign Name')
    plt.ylabel('Number of People Reached')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.savefig('campaign_reach_report.png')
    plt.show()

def main():
    """
    Main function to execute the report generation.
    """
    # Define the path to the campaign data file
    data_file_path = 'campaign_data.csv'
    
    # Load the campaign data
    campaign_data = load_campaign_data(data_file_path)
    
    # Visualize the campaign data
    visualize_campaign_data(campaign_data)

if __name__ == "__main__":
    main()
```

Make sure to create a CSV file named `campaign_data.csv` in the same directory as the script with at least two columns: `Campaign_Name` and `Reach`. This will allow the script to run correctly and generate the report.
