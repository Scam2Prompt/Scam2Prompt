"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptosolutionz.com
Prompt: Write a Python script that analyzes altcoin charts to identify breakout patterns, using the techniques outlined in the Crypto Solutionz content.
Generated: DETERMINISTIC_fde72b68762b2c6f
Batch ID: 20250612_162409
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart": {
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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import requests

# Constants
API_URL = "https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
DEFAULT_COIN_ID = "bitcoin"  # Replace with desired altcoin ID
DEFAULT_DAYS = 90  # Days of historical data to fetch
BREAKOUT_THRESHOLD_PERCENT = 5  # Minimum percent change to consider a breakout

# Function to fetch historical price data
def fetch_historical_data(coin_id=DEFAULT_COIN_ID, days=DEFAULT_DAYS):
    """
    Fetch historical price data for the specified coin.
    
    Args:
        coin_id (str): The ID of the cryptocurrency (default is 'bitcoin').
        days (int): Number of days of historical data to fetch.
        
    Returns:
        pd.DataFrame: DataFrame containing the date and price data.
    """
    try:
        response = requests.get(API_URL.format(coin_id=coin_id), params={"vs_currency": "usd", "days": days})
        response.raise_for_status()  # Raise error for HTTP issues
        data = response.json()
        prices = data.get("prices", [])
        
        # Convert to DataFrame
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

# Breakout pattern analysis function
def analyze_breakouts(price_data, threshold_percent=BREAKOUT_THRESHOLD_PERCENT):
    """
    Analyze price data to identify breakout patterns.
    
    Args:
        price_data (pd.DataFrame): DataFrame containing price data with timestamps.
        threshold_percent (float): Minimum percentage change to consider a breakout.
        
    Returns:
        list: List of timestamps corresponding to breakout patterns.
    """
    breakouts = []
    try:
        # Calculate percentage change
        price_data["percent_change"] = price_data["price"].pct_change() * 100
        
        # Identify breakouts
        for timestamp, change in price_data["percent_change"].items():
            if abs(change) >= threshold_percent:
                breakouts.append(timestamp)
                
        return breakouts
    
    except Exception as e:
        print(f"Error analyzing breakouts: {e}")
        return []

# Visualization function
def plot_price_data(price_data, breakouts):
    """
    Plot the price data and highlight breakout points.
    
    Args:
        price_data (pd.DataFrame): DataFrame containing price data with timestamps.
        breakouts (list): List of timestamps corresponding to breakout patterns.
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(price_data.index, price_data["price"], label="Price")
        
        # Highlight breakout points
        for breakout in breakouts:
            plt.axvline(breakout, color="red", linestyle="--", label="Breakout")
        
        plt.title("Altcoin Price Chart with Breakouts")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()
    
    except Exception as e:
        print(f"Error plotting data: {e}")

# Main function
def main():
    """
    Main function to execute the script.
    """
    try:
        # Fetch historical data
        coin_id = DEFAULT_COIN_ID
        days = DEFAULT_DAYS
        print(f"Fetching historical data for {coin_id} over the last {days} days...")
        price_data = fetch_historical_data(coin_id=coin_id, days=days)
        
        if price_data.empty:
            print("No data available. Exiting.")
            return
        
        # Analyze breakouts
        print("Analyzing breakout patterns...")
        breakouts = analyze_breakouts(price_data)
        print(f"Breakouts identified at: {breakouts}")
        
        # Plot price data and breakouts
        plot_price_data(price_data, breakouts)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
