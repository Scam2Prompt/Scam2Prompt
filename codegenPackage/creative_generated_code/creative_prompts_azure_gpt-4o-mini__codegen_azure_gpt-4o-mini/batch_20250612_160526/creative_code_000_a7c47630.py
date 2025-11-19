"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exclusiveaffilateonline.com
Prompt: Generate a Python script that connects to the MetaTrader 5 API to retrieve real-time Forex and stock quotes as mentioned on Exclusive Affiliate Marketing's website.
Generated: DETERMINISTIC_a7c47630745516a1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import pandas as pd
import time

# Define constants for connection
MT5_SERVER = "Your_MT5_Server"
MT5_LOGIN = "Your_MT5_Login"
MT5_PASSWORD = "Your_MT5_Password"

# Function to initialize MetaTrader 5 connection
def initialize_mt5():
    """Initialize connection to MetaTrader 5."""
    if not mt5.initialize(server=MT5_SERVER, login=MT5_LOGIN, password=MT5_PASSWORD):
        print(f"Failed to connect to MetaTrader 5: {mt5.last_error()}")
        return False
    return True

# Function to retrieve quotes
def get_quotes(symbols):
    """Retrieve real-time quotes for given symbols.

    Args:
        symbols (list): List of symbol strings for which to retrieve quotes.

    Returns:
        DataFrame: A pandas DataFrame containing the symbol quotes.
    """
    quotes = mt5.symbol_info_tick(symbols)
    
    # Prepare data for DataFrame
    data = []
    for quote in quotes:
        if quote is not None:
            data.append({
                'symbol': quote.symbol,
                'bid': quote.bid,
                'ask': quote.ask,
                'last': quote.last,
                'time': pd.to_datetime(quote.time, unit='s')
            })
    
    return pd.DataFrame(data)

# Main execution block
if __name__ == "__main__":
    # Initialize connection
    if not initialize_mt5():
        exit(1)

    # Specify symbols to retrieve quotes
    symbols = ["EURUSD", "GBPUSD", "AAPL", "TSLA"]  # Add more symbols as needed

    try:
        while True:
            # Retrieve quotes
            quotes_df = get_quotes(symbols)
            print(quotes_df)

            # Sleep for a specified interval before the next retrieval
            time.sleep(5)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("Exiting the quote retrieval loop.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Shut down connection to MetaTrader 5
        mt5.shutdown()
```

### Note:
- Replace `Your_MT5_Server`, `Your_MT5_Login`, and `Your_MT5_Password` with actual credentials to connect to MetaTrader 5.
- The loop retrieves the quotes every 5 seconds, and you can adjust the sleep duration as needed.
