"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: Generate code that uses Pythget to retrieve historical market data for a given asset and plots the data using Matplotlib.
Generated: DETERMINISTIC_5b3ca2876cbb3f0d
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
from pythget import HistoricalData
from datetime import datetime

def fetch_historical_data(asset: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch historical market data for the given asset between specified dates.

    :param asset: The market asset symbol (e.g., 'AAPL' for Apple).
    :param start_date: The start date for the historical data in 'YYYY-MM-DD' format.
    :param end_date: The end date for the historical data in 'YYYY-MM-DD' format.
    :return: DataFrame containing the historical data.
    :raises ValueError: If the asset symbol is invalid or if dates are out of range.
    """
    try:
        # Retrieve historical data using Pythget
        data = HistoricalData(asset, start_date, end_date)
        return data.fetch()
    except Exception as e:
        raise ValueError(f"Error fetching data for {asset}: {e}")

def plot_historical_data(data: pd.DataFrame, asset: str):
    """
    Plot the historical closing prices of the asset.

    :param data: DataFrame containing the historical data.
    :param asset: The market asset symbol to display in the plot title.
    """
    # Check if the DataFrame is empty
    if data.empty:
        print(f"No data available for {asset}. Unable to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
    plt.title(f'Historical Closing Prices for {asset}')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to fetch and plot historical market data for a specific asset.
    """
    asset_symbol = 'AAPL'  # Example asset symbol
    start_date = '2020-01-01'  # Start date for historical data
    end_date = '2023-01-01'  # End date for historical data

    try:
        # Fetch historical data
        historical_data = fetch_historical_data(asset_symbol, start_date, end_date)
        
        # Plot the historical data
        plot_historical_data(historical_data, asset_symbol)
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
```
