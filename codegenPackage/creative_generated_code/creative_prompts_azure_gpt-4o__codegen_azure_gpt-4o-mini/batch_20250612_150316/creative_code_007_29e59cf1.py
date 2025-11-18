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
import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# Initialize the pytrends request
pytrends = TrendReq(hl='en-US', tz=360)

# Function to fetch Google Trends data
def fetch_trends_data(keyword, regions):
    """
    Fetches Google Trends data for a given keyword and specified regions.

    :param keyword: The search term to query trends for.
    :param regions: List of regions to filter data.
    :return: DataFrame containing the trends data.
    """
    try:
        # Build payload for the specified keyword
        pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo='', gprop='')

        # Initialize an empty DataFrame to store trends data
        trends_data = pd.DataFrame()

        # Iterate over each region to fetch data
        for region in regions:
            # Fetch interest by region
            region_data = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo=True)
            region_data = region_data[region_data.index == region]

            if not region_data.empty:
                trends_data = pd.concat([trends_data, region_data], axis=0)

        return trends_data

    except Exception as e:
        print(f"Error fetching trends data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Regions to focus on
regions_of_interest = ['BR', 'PT', 'TR']

# Fetch trends data for the keyword "RACA"
trends_df = fetch_trends_data("RACA", regions_of_interest)

# Check if data is retrieved
if not trends_df.empty:
    # Plotting the trends data
    plt.figure(figsize=(12, 6))
    for region in regions_of_interest:
        if region in trends_df.index:
            plt.plot(trends_df.columns, trends_df.loc[region], label=f'Trends in {region}')

    plt.title("Google Trends Data for 'RACA' in Selected Regions")
    plt.xlabel("Time")
    plt.ylabel("Interest Level")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()
else:
    print("No trends data available for the specified regions.")
```
