"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7364500043-8sj.pages.dev
Prompt: Generate code to analyze on-chain Bitcoin data, inspired by the "Bitcoin : L'arme secrète pour démasquer la cupidité des investisseurs - Analyse on-chain" article on Journal Du Coin.
Generated: DETERMINISTIC_b4530b41646127fa
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.info/charts/": {
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
from datetime import datetime

# Constants for the API and endpoints
API_URL = "https://api.blockchain.info/charts/"
API_PARAMS = {
    'timespan': '1year',  # Specify the time span for data (1 year)
    'format': 'json',     # Request data in JSON format
    'sampled': 'true'     # Enable data sampling to reduce data points
}

# Function to fetch on-chain Bitcoin data from the Blockchain API
def fetch_bitcoin_data(chart_type):
    """
    Fetch on-chain Bitcoin data for a specific chart type.
    
    :param chart_type: Type of chart to fetch (e.g., 'market-price', 'n-transactions').
    :return: Data as a Pandas DataFrame (timestamp and value).
    """
    try:
        # Endpoint for the specific chart type
        url = f"{API_URL}{chart_type}"
        response = requests.get(url, params=API_PARAMS)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Convert data to a DataFrame
        values = pd.DataFrame(data['values'])
        values['x'] = pd.to_datetime(values['x'], unit='s')  # Convert timestamps to datetime
        values.rename(columns={'x': 'timestamp', 'y': 'value'}, inplace=True)  # Rename columns
        
        return values
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except KeyError as e:
        print(f"Error parsing data format: {e}")
        return None

# Function to plot Bitcoin data
def plot_bitcoin_data(data, chart_title):
    """
    Plot on-chain Bitcoin data.
    
    :param data: Pandas DataFrame containing the timestamp and value columns.
    :param chart_title: Title of the chart.
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(data['timestamp'], data['value'], label=chart_title, color='blue')
        plt.title(chart_title)
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error generating the plot: {e}")

# Main function to analyze Bitcoin on-chain data
def main():
    """
    Main function to analyze on-chain Bitcoin data.
    Fetches data for market price and number of transactions,
    and visualizes the trends.
    """
    print("Fetching market price data...")
    market_price_data = fetch_bitcoin_data('market-price')
    
    if market_price_data is not None:
        print("Market price data fetched successfully.")
        plot_bitcoin_data(market_price_data, "Bitcoin Market Price (USD)")
    else:
        print("Failed to fetch market price data.")
        
    print("\nFetching number of transactions data...")
    transactions_data = fetch_bitcoin_data('n-transactions')
    
    if transactions_data is not None:
        print("Number of transactions data fetched successfully.")
        plot_bitcoin_data(transactions_data, "Bitcoin Number of Transactions")
    else:
        print("Failed to fetch number of transactions data.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
