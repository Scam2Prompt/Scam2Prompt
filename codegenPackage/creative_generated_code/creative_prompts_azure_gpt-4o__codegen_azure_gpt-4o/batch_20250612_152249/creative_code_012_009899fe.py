"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a Python script to fetch real-time market data from CVEX's API and simulate a delta-hedged portfolio for options market-making.
Generated: DETERMINISTIC_009899fef1c6dc6c
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cvex.com/v1": {
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
import logging
import math
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_BASE_URL = "https://api.cvex.com/v1"  # Replace with the actual CVEX API base URL
API_KEY = "your_api_key_here"  # Replace with your CVEX API key
DELTA_THRESHOLD = 0.01  # Threshold for rebalancing delta
PORTFOLIO_BALANCE = 1000000  # Initial portfolio balance in USD
MIN_TRADE_SIZE = 0.01  # Minimum trade size in units of the asset

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Functions for interacting with CVEX API
def fetch_market_data(symbol):
    """
    Fetch real-time market data for a given symbol from CVEX API.
    
    Args:
        symbol (str): The market symbol (e.g., BTC-USD).
    
    Returns:
        dict: Market data including price and other details.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/markets/{symbol}/ticker", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch market data for {symbol}: {e}")
        return None


def fetch_option_chain(symbol):
    """
    Fetch the option chain for a given underlying symbol.
    
    Args:
        symbol (str): The underlying symbol (e.g., BTC-USD).
    
    Returns:
        list: List of available options.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/options/{symbol}/chain", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch option chain for {symbol}: {e}")
        return None


def calculate_delta(option_type, strike_price, underlying_price, time_to_expiry, volatility):
    """
    Calculate the delta of an option using the Black-Scholes formula.
    
    Args:
        option_type (str): The type of option ('call' or 'put').
        strike_price (float): The strike price of the option.
        underlying_price (float): Current price of the underlying asset.
        time_to_expiry (float): Time to expiry in years.
        volatility (float): Annualized volatility of the underlying asset.
    
    Returns:
        float: Delta value of the option.
    """
    try:
        # Simplified Black-Scholes delta calculation
        d1 = (math.log(underlying_price / strike_price) +
              (0.5 * volatility ** 2) * time_to_expiry) / (volatility * math.sqrt(time_to_expiry))
        if option_type == "call":
            return math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
        elif option_type == "put":
            return -math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
        else:
            raise ValueError("Invalid option type. Expected 'call' or 'put'.")
    except Exception as e:
        logging.error(f"Failed to calculate delta: {e}")
        return 0.0


def rebalance_portfolio(delta, current_cash_balance, asset_price):
    """
    Simulate rebalancing the portfolio to maintain a delta-hedged position.
    
    Args:
        delta (float): Current delta of the portfolio.
        current_cash_balance (float): Current cash balance of the portfolio.
        asset_price (float): Current price of the underlying asset.
    
    Returns:
        dict: Updated portfolio state including cash balance and asset quantity.
    """
    try:
        # Determine required adjustment
        hedge_units = -delta
        trade_cost = hedge_units * asset_price

        if abs(delta) > DELTA_THRESHOLD:
            if current_cash_balance - trade_cost >= 0:
                current_cash_balance -= trade_cost
                logging.info(f"Rebalanced portfolio: Bought {hedge_units:.4f} units at {asset_price:.2f}")
            else:
                logging.warning("Insufficient funds to rebalance portfolio.")
        else:
            logging.info("No rebalancing needed. Delta within threshold.")

        return {
            "cash_balance": current_cash_balance,
            "hedge_units": hedge_units
        }
    except Exception as e:
        logging.error(f"Error during portfolio rebalancing: {e}")
        return {
            "cash_balance": current_cash_balance,
            "hedge_units": 0.0
        }


# Main simulation
def main():
    """
    Main function to fetch market data, calculate option deltas, and simulate delta-hedging.
    """
    portfolio = {
        "cash_balance": PORTFOLIO_BALANCE,
        "hedge_units": 0.0
    }
    underlying_symbol = "BTC-USD"  # Replace with the desired underlying asset symbol

    # Fetch underlying market data
    market_data = fetch_market_data(underlying_symbol)
    if not market_data:
        logging.error("Failed to retrieve underlying market data. Exiting.")
        return

    underlying_price = float(market_data.get("price", 0))
    logging.info(f"Underlying price: {underlying_price:.2f}")

    # Fetch option chain
    option_chain = fetch_option_chain(underlying_symbol)
    if not option_chain:
        logging.error("Failed to retrieve option chain. Exiting.")
        return

    # Loop through each option and simulate delta-hedging
    for option in option_chain:
        option_type = option.get("type")
        strike_price = float(option.get("strike_price", 0))
        time_to_expiry = float(option.get("time_to_expiry", 0))
        volatility = float(option.get("volatility", 0))

        delta = calculate_delta(option_type, strike_price, underlying_price, time_to_expiry, volatility)
        logging.info(f"Option {option_type.upper()} @ Strike {strike_price:.2f}: Delta = {delta:.4f}")

        # Rebalance portfolio
        portfolio = rebalance_portfolio(delta, portfolio["cash_balance"], underlying_price)

    # Output final portfolio state
    logging.info(f"Final Portfolio: Cash Balance = {portfolio['cash_balance']:.2f}, Hedge Units = {portfolio['hedge_units']:.4f}")


if __name__ == "__main__":
    main()
```
