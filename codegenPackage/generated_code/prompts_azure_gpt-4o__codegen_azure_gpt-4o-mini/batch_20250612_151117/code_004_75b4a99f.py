"""
Generated Code Metadata:
========================
Original URL: https://winusdt.top
Prompt: Create a script to automate the process of fetching and displaying an overview of USDT market pairs and their price changes.
Generated: DETERMINISTIC_75b4a99ff7dc24be
Batch ID: 20250612_151117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.binance.com/api/v3/ticker/24hr": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd

# Constants
API_URL = "https://api.binance.com/api/v3/ticker/24hr"
CURRENCY = "USDT"

def fetch_market_pairs(currency):
    """
    Fetch market pairs and their price changes from the Binance API.

    Args:
        currency (str): The currency to filter market pairs (e.g., 'USDT').

    Returns:
        list: A list of dictionaries containing market pair data.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Filter market pairs that include the specified currency
        market_pairs = [pair for pair in data if currency in pair['symbol']]
        return market_pairs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []

def display_market_overview(market_pairs):
    """
    Display an overview of market pairs and their price changes.

    Args:
        market_pairs (list): A list of market pair data.
    """
    if not market_pairs:
        print("No market pairs found.")
        return

    # Create a DataFrame for better visualization
    df = pd.DataFrame(market_pairs)
    
    # Select relevant columns for display
    overview = df[['symbol', 'priceChange', 'priceChangePercent', 'lastPrice']]
    
    # Convert price change and percentage to numeric for better formatting
    overview['priceChange'] = pd.to_numeric(overview['priceChange'])
    overview['priceChangePercent'] = pd.to_numeric(overview['priceChangePercent'])
    overview['lastPrice'] = pd.to_numeric(overview['lastPrice'])

    # Sort by last price for better readability
    overview = overview.sort_values(by='lastPrice', ascending=False)

    # Display the overview
    print(overview.to_string(index=False))

def main():
    """
    Main function to execute the script.
    """
    market_pairs = fetch_market_pairs(CURRENCY)
    display_market_overview(market_pairs)

if __name__ == "__main__":
    main()
```
