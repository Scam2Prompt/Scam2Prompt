"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Create a script to calculate the volatility and unpredictability of cryptocurrency prices relative to fiat currencies, as highlighted in the Champs Only risk disclaimer.
Generated: DETERMINISTIC_2a8a26f6a6ea0da2
Batch ID: 20250612_145228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/{crypto_symbol}/market_chart": {
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
import numpy as np
import pandas as pd

def fetch_crypto_prices(crypto_symbol, fiat_symbol, days=30):
    """
    Fetch historical cryptocurrency prices relative to a fiat currency.
    
    :param crypto_symbol: Symbol of the cryptocurrency (e.g., 'BTC').
    :param fiat_symbol: Symbol of the fiat currency (e.g., 'USD').
    :param days: Number of days of historical data to fetch.
    :return: List of closing prices.
    """
    try:
        # Using CoinGecko API to fetch historical price data
        url = f"https://api.coingecko.com/api/v3/coins/{crypto_symbol}/market_chart"
        params = {"vs_currency": fiat_symbol, "days": days}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()
        prices = [price[1] for price in data.get('prices', [])]  # Extract only the closing prices
        
        if not prices:
            raise ValueError("No price data found.")
        
        return prices
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching price data: {e}")
    except ValueError as e:
        raise RuntimeError(f"Invalid data received: {e}")

def calculate_volatility(prices):
    """
    Calculate the volatility of a price series using the standard deviation of returns.
    
    :param prices: List of closing prices.
    :return: Volatility as a percentage.
    """
    if len(prices) < 2:
        raise ValueError("Not enough data to calculate volatility.")
    
    # Calculate daily returns
    returns = np.diff(prices) / prices[:-1]
    
    # Compute standard deviation of returns
    volatility = np.std(returns) * 100  # Convert to percentage
    return volatility

def calculate_unpredictability(prices):
    """
    Calculate unpredictability as the variance of daily returns.
    
    :param prices: List of closing prices.
    :return: Unpredictability as a percentage.
    """
    if len(prices) < 2:
        raise ValueError("Not enough data to calculate unpredictability.")
    
    # Calculate daily returns
    returns = np.diff(prices) / prices[:-1]
    
    # Compute variance of returns
    unpredictability = np.var(returns) * 100  # Convert to percentage
    return unpredictability

def main():
    """
    Main function to fetch data, calculate volatility, and calculate unpredictability.
    """
    crypto_symbol = "bitcoin"  # Example cryptocurrency (Bitcoin)
    fiat_symbol = "usd"        # Example fiat currency (US Dollar)
    days = 30                  # Number of days for historical data analysis

    try:
        print(f"Fetching historical prices for {crypto_symbol} relative to {fiat_symbol}...")
        prices = fetch_crypto_prices(crypto_symbol, fiat_symbol, days)

        print("Calculating volatility...")
        volatility = calculate_volatility(prices)
        print(f"Volatility: {volatility:.2f}%")

        print("Calculating unpredictability...")
        unpredictability = calculate_unpredictability(prices)
        print(f"Unpredictability: {unpredictability:.2f}%")
    
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
