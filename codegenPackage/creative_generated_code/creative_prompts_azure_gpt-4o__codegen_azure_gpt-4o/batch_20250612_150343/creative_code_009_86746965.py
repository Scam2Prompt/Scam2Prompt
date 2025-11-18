"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinzat.com
Prompt: Recommend tools for tracking and visualizing cryptocurrency portfolio growth over time, as discussed in Bitcoinzat.com's "8 Hard-Earned Lessons from 8 Years in Crypto."
Generated: DETERMINISTIC_8674696509d49930
Batch ID: 20250612_150343
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
API_URL = "https://api.coingecko.com/api/v3/simple/price"
FIAT_CURRENCY = "usd"  # Default fiat currency for valuation

# Function to fetch current cryptocurrency prices from CoinGecko API
def fetch_crypto_prices(crypto_ids, fiat_currency=FIAT_CURRENCY):
    """
    Fetch current prices for specified cryptocurrencies.

    Args:
        crypto_ids (list): List of cryptocurrency IDs.
        fiat_currency (str): Fiat currency to value cryptocurrencies (default: USD).

    Returns:
        dict: Cryptocurrency prices in the specified fiat currency.
    """
    try:
        ids = ",".join(crypto_ids)
        response = requests.get(f"{API_URL}?ids={ids}&vs_currencies={fiat_currency}")
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching cryptocurrency prices: {e}")
        return {}  # Return empty dictionary on failure


# Function to visualize portfolio growth over time
def visualize_portfolio_growth(portfolio_data):
    """
    Visualize the portfolio growth over time using a line graph.

    Args:
        portfolio_data (dict): Dictionary where keys are timestamps and values are portfolio values.
    """
    try:
        # Prepare data for plotting
        timestamps = [datetime.fromtimestamp(ts) for ts in portfolio_data.keys()]
        portfolio_values = list(portfolio_data.values())
        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, portfolio_values, label="Portfolio Value (USD)", marker='o')
        plt.title("Cryptocurrency Portfolio Growth")
        plt.xlabel("Time")
        plt.ylabel("Portfolio Value (USD)")
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing portfolio growth: {e}")


# Example usage
if __name__ == "__main__":
    # Define the cryptocurrency portfolio
    portfolio = {
        "bitcoin": 0.05,
        "ethereum": 1.0,
        "dogecoin": 1000.0
    }

    # Fetch current prices for portfolio cryptocurrencies
    crypto_prices = fetch_crypto_prices(list(portfolio.keys()))
    if not crypto_prices:
        print("Failed to fetch cryptocurrency prices. Exiting.")
        exit(1)

    # Calculate portfolio value over time (example data)
    portfolio_data = {
        # Example timestamps (UNIX) and portfolio values
        1633046400: sum(portfolio[crypto] * crypto_prices.get(crypto, {}).get(FIAT_CURRENCY, 0) for crypto in portfolio),
        1633132800: sum(portfolio[crypto] * crypto_prices.get(crypto, {}).get(FIAT_CURRENCY, 0) * 1.02 for crypto in portfolio),
        1633219200: sum(portfolio[crypto] * crypto_prices.get(crypto, {}).get(FIAT_CURRENCY, 0) * 1.05 for crypto in portfolio),
    }

    # Visualize portfolio growth over time
    visualize_portfolio_growth(portfolio_data)
```
