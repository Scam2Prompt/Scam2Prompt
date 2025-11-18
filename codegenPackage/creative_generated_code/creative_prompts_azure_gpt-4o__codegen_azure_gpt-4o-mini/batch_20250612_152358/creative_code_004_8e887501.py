"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amlcheck-cv9.pages.dev
Prompt: Develop a Python script to compare the historical price data of Shiba Inu (SHIB) with its transaction volume using the CryptoCompare API.
Generated: DETERMINISTIC_8e8875012941df0a
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://min-api.cryptocompare.com/data": {
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
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class CryptoCompareAPI:
    BASE_URL = "https://min-api.cryptocompare.com/data"

    @staticmethod
    def fetch_historical_data(symbol, currency, limit):
        """
        Fetch historical price and volume data from CryptoCompare API.

        :param symbol: The cryptocurrency symbol (e.g., 'SHIB').
        :param currency: The fiat currency symbol (e.g., 'USD').
        :param limit: The number of days of historical data to fetch.
        :return: DataFrame with historical price and volume data.
        """
        try:
            endpoint = f"{CryptoCompareAPI.BASE_URL}/v2/histoday"
            params = {
                'fsym': symbol,
                'tsym': currency,
                'limit': limit,
                'toTs': int(datetime.now().timestamp())
            }
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()

            if 'Data' in data:
                return pd.DataFrame(data['Data'])
            else:
                raise ValueError("Unexpected response format: 'Data' not found.")
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

def plot_price_volume(price_data):
    """
    Plot historical price and transaction volume on a single graph.

    :param price_data: DataFrame containing historical price and volume data.
    """
    try:
        # Convert timestamp to datetime
        price_data['time'] = pd.to_datetime(price_data['time'], unit='s')
        price_data.set_index('time', inplace=True)

        # Create a figure and axis
        fig, ax1 = plt.subplots(figsize=(14, 7))

        # Plot price on the primary y-axis
        ax1.plot(price_data.index, price_data['close'], color='blue', label='Price (USD)', linewidth=2)
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price (USD)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        # Create a secondary y-axis for volume
        ax2 = ax1.twinx()
        ax2.bar(price_data.index, price_data['volumefrom'], color='orange', alpha=0.3, label='Volume')
        ax2.set_ylabel('Volume', color='orange')
        ax2.tick_params(axis='y', labelcolor='orange')

        # Title and legends
        plt.title('SHIB Price and Transaction Volume')
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Show the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting data: {e}")

def main():
    """
    Main function to execute the price and volume comparison script.
    """
    # Set parameters for the API call
    symbol = 'SHIB'
    currency = 'USD'
    limit = 30  # Number of days to fetch

    # Fetch historical data
    price_data = CryptoCompareAPI.fetch_historical_data(symbol, currency, limit)

    if not price_data.empty:
        # Plot the price and volume data
        plot_price_volume(price_data)

if __name__ == "__main__":
    main()
```
