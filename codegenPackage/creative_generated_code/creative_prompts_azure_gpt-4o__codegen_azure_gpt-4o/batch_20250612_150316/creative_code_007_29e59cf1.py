"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Provide code to query Google Trends data for "RACA" and visualize its search growth, focusing on regions like Brazil, Portugal, and Turkey as highlighted on the website.
Generated: DETERMINISTIC_29e59cf176fd451b
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch and visualize Google Trends data
def fetch_and_visualize_trends(keyword, regions):
    """
    Fetches Google Trends data for a specified keyword and visualizes search interest growth for given regions.

    Parameters:
        keyword (str): The search term to query on Google Trends.
        regions (list): List of region codes (e.g., 'BR', 'PT', 'TR') to analyze search interest.

    Returns:
        None
    """
    try:
        # Initialize pytrends request
        pytrends = TrendReq(hl='en-US', tz=360)
        
        # Create a payload with the keyword
        pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo='', gprop='')

        # Fetch interest over time data
        interest_over_time = pytrends.interest_over_time()

        if interest_over_time.empty:
            print("No data found for the specified keyword.")
            return

        # Drop the 'isPartial' column if it exists
        if 'isPartial' in interest_over_time.columns:
            interest_over_time.drop(columns=['isPartial'], inplace=True)

        # Fetch interest by region
        interest_by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=True)

        if interest_by_region.empty:
            print("No regional data found for the specified keyword.")
            return

        # Filter for specific regions
        region_data = interest_by_region.loc[interest_by_region.index.intersection(regions)]

        if region_data.empty:
            print("No data available for the specified regions.")
            return

        # Normalize the data for visualization
        normalized_data = region_data.div(region_data.max(axis=0)).sort_values(by=keyword, ascending=False)

        # Plot interest over time
        plt.figure(figsize=(12, 6))
        interest_over_time[keyword].plot(color='blue', label=f'Search Interest: {keyword}')
        plt.title(f'Google Trends Search Interest Over Time for "{keyword}"')
        plt.xlabel('Date')
        plt.ylabel('Search Interest')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot interest by region
        plt.figure(figsize=(12, 6))
        normalized_data[keyword].plot(kind='bar', color='green', alpha=0.7)
        plt.title(f'Normalized Search Interest by Region for "{keyword}"')
        plt.xlabel('Region')
        plt.ylabel('Normalized Search Interest')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        # Handle exceptions and provide feedback
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Keyword to search and regions of interest
    keyword = "RACA"
    regions = ['BR', 'PT', 'TR']  # Brazil, Portugal, Turkey

    # Fetch and visualize trends
    fetch_and_visualize_trends(keyword, regions)
```
