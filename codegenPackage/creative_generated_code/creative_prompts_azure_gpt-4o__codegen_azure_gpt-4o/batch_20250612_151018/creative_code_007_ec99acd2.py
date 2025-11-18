"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to calculate and display the doubling time of COVID-19 cases for selected regions, incorporating interactive features like deselecting/selecting all regions as mentioned on the website.
Generated: DETERMINISTIC_ec99acd2e9f55c6f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import math
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def calculate_doubling_time(data):
    """
    Calculate doubling time for COVID-19 cases.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing date and case count columns.

    Returns:
        pd.Series: Series containing doubling times corresponding to dates.
    """
    doubling_times = []
    for i in range(1, len(data)):
        previous_cases = data.iloc[i - 1]['Cases']
        current_cases = data.iloc[i]['Cases']
        if previous_cases > 0 and current_cases > previous_cases:
            doubling_time = math.log(2) / math.log(current_cases / previous_cases) * (data.iloc[i]['Date'] - data.iloc[i - 1]['Date']).days
            doubling_times.append(doubling_time)
        else:
            doubling_times.append(None)  # Not computable
    return pd.Series([None] + doubling_times)  # First day has no doubling time

def fetch_data():
    """
    Simulates fetching COVID-19 case data for multiple regions.
    
    Returns:
        dict: Dictionary where keys are region names and values are DataFrames with case data.
    """
    # Example data for demonstration purposes
    regions_data = {
        "Region A": pd.DataFrame({
            "Date": pd.date_range(start="2023-01-01", end="2023-01-10"),
            "Cases": [100, 150, 225, 337, 506, 759, 1139, 1708, 2562, 3843]
        }),
        "Region B": pd.DataFrame({
            "Date": pd.date_range(start="2023-01-01", end="2023-01-10"),
            "Cases": [200, 300, 450, 675, 1012, 1518, 2277, 3416, 5124, 7686]
        }),
        "Region C": pd.DataFrame({
            "Date": pd.date_range(start="2023-01-01", end="2023-01-10"),
            "Cases": [50, 75, 112, 168, 252, 378, 567, 850, 1275, 1912]
        })
    }
    return regions_data

def plot_doubling_times(selected_regions, regions_data):
    """
    Plot the doubling times for selected regions.
    
    Parameters:
        selected_regions (list): List of regions to plot.
        regions_data (dict): Dictionary with region names as keys and case data as values.
    """
    for region in selected_regions:
        data = regions_data[region]
        data['Doubling Time'] = calculate_doubling_time(data)
        
        plt.plot(data['Date'], data['Doubling Time'], label=region)
    
    plt.title("COVID-19 Doubling Times")
    plt.xlabel("Date")
    plt.ylabel("Doubling Time (days)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to interactively select regions and display doubling times.
    """
    regions_data = fetch_data()
    all_regions = list(regions_data.keys())
    
    print("Available regions:")
    for i, region in enumerate(all_regions, start=1):
        print(f"{i}. {region}")
    
    print("\nEnter the numbers corresponding to the regions you want to select (comma-separated), or 'all' to select all regions.")
    print("Enter 'none' to deselect all regions.")
    
    user_input = input("Selection: ").strip().lower()
    
    if user_input == "all":
        selected_regions = all_regions
    elif user_input == "none":
        selected_regions = []
    else:
        try:
            selected_indices = [int(x) - 1 for x in user_input.split(",")]
            selected_regions = [all_regions[i] for i in selected_indices if 0 <= i < len(all_regions)]
        except ValueError:
            print("Invalid input. Please use numeric indices or 'all'/'none'.")
            return

    if not selected_regions:
        print("No regions selected.")
        return
    
    print(f"Selected regions: {', '.join(selected_regions)}")
    plot_doubling_times(selected_regions, regions_data)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
