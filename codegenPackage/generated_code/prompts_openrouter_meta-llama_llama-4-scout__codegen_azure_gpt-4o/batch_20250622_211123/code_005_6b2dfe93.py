"""
Generated Code Metadata:
========================
Original URL: https://pgfc.com.cn
Prompt: Create a simple blockchain-based application using the Binance API and a programming language of choice, demonstrating its potential use cases.
Generated: DETERMINISTIC_6b2dfe93826cf15b
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A simple blockchain-based application using the Binance API.
This script demonstrates fetching account balances and recent trades
from the Binance exchange using Python and the Binance API.

Dependencies:
- Install the Binance API Python library: pip install binance
- Install dotenv for environment variable management: pip install python-dotenv

Note:
- Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your Binance API credentials.
- Ensure you have enabled API access in your Binance account.
"""

import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Binance API credentials (stored securely in environment variables)
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

def get_account_balances():
    """
    Fetch and display account balances for assets with non-zero balances.
    """
    try:
        # Fetch account information
        account_info = client.get_account()
        balances = account_info['balances']

        print("Account Balances:")
        for balance in balances:
            asset = balance['asset']
            free = float(balance['free'])
            locked = float(balance['locked'])
            # Display only assets with non-zero balances
            if free > 0 or locked > 0:
                print(f"{asset}: Free = {free}, Locked = {locked}")
    except BinanceAPIException as e:
        print(f"Binance API error: {e}")
    except BinanceRequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_recent_trades(symbol, limit=10):
    """
    Fetch and display recent trades for a given trading pair.

    Args:
        symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
        limit (int): The number of recent trades to fetch (default is 10).
    """
    try:
        # Fetch recent trades
        trades = client.get_recent_trades(symbol=symbol, limit=limit)

        print(f"Recent Trades for {symbol}:")
        for trade in trades:
            print(f"Price: {trade['price']}, Quantity: {trade['qty']}, Time: {trade['time']}")
    except BinanceAPIException as e:
        print(f"Binance API error: {e}")
    except BinanceRequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to demonstrate the application's functionality.
    """
    print("Welcome to the Binance Blockchain Application!")

    # Fetch and display account balances
    get_account_balances()

    # Fetch and display recent trades for a specific trading pair
    trading_pair = "BTCUSDT"  # Example trading pair
    get_recent_trades(symbol=trading_pair, limit=5)

if __name__ == "__main__":
    main()
```

### Notes:
1. Create a `.env` file in the same directory as the script and add the following:
   ```
   BINANCE_API_KEY=YOUR_API_KEY
   BINANCE_API_SECRET=YOUR_API_SECRET
   ```
2. Ensure you have installed the required dependencies (`binance` and `python-dotenv`) before running the script.
3. This script is designed for demonstration purposes and should be extended for production use cases, such as integrating with a database or handling sensitive data securely.
