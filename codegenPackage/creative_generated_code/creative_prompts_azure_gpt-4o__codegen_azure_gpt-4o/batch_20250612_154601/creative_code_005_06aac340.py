"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Develop a script to track the market cap of stablecoins over the last 7 days using DefiLlama's API and plot the trend.
Generated: DETERMINISTIC_06aac34064ac5c42
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Constants
BASE_URL = "https://api.llama.fi"
STABLECOINS_ENDPOINT = "/stablecoins"
DAYS = 7  # Number of days to track

def fetch_stablecoins_data():
    """
    Fetches stablecoins data from DefiLlama API.
    Returns the JSON response.
    """
    try:
        response = requests.get(BASE_URL + STABLECOINS_ENDPOINT)
        response.raise_for_status()  # Ensure the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def extract_market_cap_trend(data, days):
    """
    Extracts the market cap trend for stablecoins over the last 'days' days.
    Args:
        data (dict): Stablecoins data from DefiLlama API.
        days (int): Number of days to extract data for.

    Returns:
        dict: A dictionary with dates as keys and total market cap as values.
    """
    trend = {}
    try:
        # Calculate the date range
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)

        # Iterate over stablecoins and aggregate market caps
        for coin in data.get("peggedAssets", []):
            for historical_data in coin.get("historicalMarketCap", []):
                date_str = historical_data["date"]
                market_cap = historical_data["marketCap"]
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")

                # Only include data within the desired date range
                if start_date <= date_obj <= end_date:
                    if date_str in trend:
                        trend[date_str] += market_cap
                    else:
                        trend[date_str] = market_cap

        # Sort the trend by date
        trend = dict(sorted(trend.items()))
    except Exception as e:
        print(f"Error processing data: {e}")
    return trend

def plot_market_cap_trend(trend):
    """
    Plots the market cap trend of stablecoins.
    Args:
        trend (dict): Market cap trend with dates as keys and total market cap as values.
    """
    try:
        dates = list(trend.keys())
        market_caps = list(trend.values())

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(dates, market_caps, marker='o', linestyle='-', color='blue', label="Market Cap")
        plt.xlabel("Date")
        plt.ylabel("Market Cap (USD)")
        plt.title("Stablecoins Market Cap Trend Over Last 7 Days")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting data: {e}")

def main():
    """
    Main function to orchestrate the data collection, processing, and plotting.
    """
    # Fetch data from API
    data = fetch_stablecoins_data()
    if not data:
        return

    # Extract market cap trend for the last 7 days
    trend = extract_market_cap_trend(data, DAYS)

    # Plot the trend
    if trend:
        plot_market_cap_trend(trend)
    else:
        print("No data available to plot.")

if __name__ == "__main__":
    main()
```
