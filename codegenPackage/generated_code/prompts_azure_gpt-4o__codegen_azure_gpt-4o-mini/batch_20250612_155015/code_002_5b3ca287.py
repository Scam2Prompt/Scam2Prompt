"""
Generated Code Metadata:
========================
Original URL: https://pythget.com
Prompt: Generate code that uses Pythget to retrieve historical market data for a given asset and plots the data using Matplotlib.
Generated: DETERMINISTIC_5b3ca2876cbb3f0d
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
from pythget import Pythget
from datetime import datetime, timedelta

# Function to retrieve historical market data for a given asset
def fetch_historical_data(asset_symbol, start_date, end_date):
    """
    Fetch historical market data for a specified asset.

    Parameters:
    asset_symbol (str): The symbol of the asset to retrieve data for.
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the historical market data.
    """
    try:
        # Initialize Pythget client
        client = Pythget()

        # Retrieve historical data
        historical_data = client.get_historical_data(asset_symbol, start_date, end_date)

        # Convert to DataFrame
        df = pd.DataFrame(historical_data)

        # Ensure the DataFrame is not empty
        if df.empty:
            raise ValueError("No data found for the specified asset and date range.")

        return df

    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

# Function to plot historical market data
def plot_historical_data(df, asset_symbol):
    """
    Plot historical market data for a specified asset.

    Parameters:
    df (pd.DataFrame): DataFrame containing the historical market data.
    asset_symbol (str): The symbol of the asset being plotted.
    """
    try:
        # Check if DataFrame is valid
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None. Cannot plot data.")

        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Plotting the data
        plt.figure(figsize=(12, 6))
        plt.plot(df['date'], df['close'], label='Close Price', color='blue')
        plt.title(f'Historical Market Data for {asset_symbol}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error plotting data: {e}")

# Main execution block
if __name__ == "__main__":
    # Define asset symbol and date range
    asset_symbol = 'AAPL'  # Example asset symbol
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')  # Last year

    # Fetch and plot historical data
    historical_data = fetch_historical_data(asset_symbol, start_date, end_date)
    plot_historical_data(historical_data, asset_symbol)
```
