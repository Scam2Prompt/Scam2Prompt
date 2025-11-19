"""
Generated Code Metadata:
========================
Original URL: https://pass-vee.com
Prompt: Write a Python script using the MetaTrader 5 (MT5) API to fetch real-time quotes for CFD instruments on the Changexcapital platform, specifically for the S&P 500 (ES) and Bitcoin.
Generated: DETERMINISTIC_7508a1fb1130c3a7
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import time

# Constants
CFD_SYMBOLS = ["ES", "BTCUSD"]  # S&P 500 (ES) and Bitcoin (BTCUSD)
FETCH_INTERVAL = 5  # Interval in seconds to fetch quotes

def initialize_mt5():
    """
    Initialize the MetaTrader 5 connection.
    """
    if not mt5.initialize():
        raise ConnectionError(f"Failed to initialize MT5: {mt5.last_error()}")
    print("MetaTrader 5 initialized successfully.")

def fetch_quotes(symbols):
    """
    Fetch real-time quotes for the given symbols.
    
    :param symbols: List of CFD instrument symbols to fetch quotes for.
    :return: Dictionary containing symbol quotes.
    """
    quotes = {}
    for symbol in symbols:
        quote = mt5.symbol_info_tick(symbol)
        if quote is None:
            print(f"Warning: Failed to fetch quote for {symbol}.")
            continue
        quotes[symbol] = {
            "bid": quote.bid,
            "ask": quote.ask,
            "last": quote.last,
            "time": quote.time
        }
    return quotes

def main():
    """
    Main function to fetch and display real-time quotes.
    """
    try:
        initialize_mt5()
        
        # Ensure symbols are available in the MT5 terminal
        for symbol in CFD_SYMBOLS:
            if not mt5.symbol_select(symbol, True):
                print(f"Error: Failed to select symbol {symbol}.")
                return
        
        print("Fetching real-time quotes...")
        while True:
            quotes = fetch_quotes(CFD_SYMBOLS)
            for symbol, data in quotes.items():
                print(f"{symbol} - Bid: {data['bid']}, Ask: {data['ask']}, Last: {data['last']}, Time: {data['time']}")
            time.sleep(FETCH_INTERVAL)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Shutdown MT5 connection
        mt5.shutdown()
        print("MetaTrader 5 connection closed.")

if __name__ == "__main__":
    main()
```
