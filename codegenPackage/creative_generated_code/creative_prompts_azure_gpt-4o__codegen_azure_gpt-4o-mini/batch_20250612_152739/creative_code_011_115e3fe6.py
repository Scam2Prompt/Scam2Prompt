"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Create a script to fetch and visualize the price history of $TPAD tokens using TrustPad's API and external data sources like CoinGecko.
Generated: DETERMINISTIC_115e3fe64c5dd0f4
Batch ID: 20250612_152739
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.trustpad.io/api/tokens/price_history?token=$TPAD": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/coins/trustpad/market_chart": {
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

# Constants
TRUSTPAD_API_URL = "https://api.trustpad.io/api/tokens/price_history?token=$TPAD"
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/trustpad/market_chart"
COINGECKO_PARAMS = {
    'vs_currency': 'usd',
    'days': '30',  # Fetch data for the last 30 days
    'interval': 'daily'
}

def fetch_trustpad_price_history():
    """Fetch the price history of $TPAD tokens from TrustPad's API."""
    try:
        response = requests.get(TRUSTPAD_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.RequestException as e:
        print(f"Error fetching data from TrustPad API: {e}")
        return None

def fetch_coingecko_price_history():
    """Fetch the price history of $TPAD tokens from CoinGecko's API."""
    try:
        response = requests.get(COINGECKO_API_URL, params=COINGECKO_PARAMS)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {e}")
        return None

def visualize_price_history(trustpad_data, coingecko_data):
    """Visualize the price history using Matplotlib."""
    # Prepare TrustPad data
    trustpad_dates = [datetime.fromtimestamp(item['timestamp']) for item in trustpad_data['prices']]
    trustpad_prices = [item['price'] for item in trustpad_data['prices']]

    # Prepare CoinGecko data
    coingecko_prices = coingecko_data['prices']
    coingecko_dates = [datetime.fromtimestamp(item[0] / 1000) for item in coingecko_prices]
    coingecko_prices = [item[1] for item in coingecko_prices]

    # Create DataFrame for plotting
    df_trustpad = pd.DataFrame({'Date': trustpad_dates, 'Price': trustpad_prices})
    df_coingecko = pd.DataFrame({'Date': coingecko_dates, 'Price': coingecko_prices})

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(df_trustpad['Date'], df_trustpad['Price'], label='$TPAD Price (TrustPad)', color='blue')
    plt.plot(df_coingecko['Date'], df_coingecko['Price'], label='$TPAD Price (CoinGecko)', color='orange')

    plt.title('Price History of $TPAD Tokens')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the script."""
    trustpad_data = fetch_trustpad_price_history()
    coingecko_data = fetch_coingecko_price_history()
    
    if trustpad_data and coingecko_data:
        visualize_price_history(trustpad_data, coingecko_data)
    else:
        print("Failed to retrieve price data.")

if __name__ == "__main__":
    main()
```
