"""
Generated Code Metadata:
========================
Original URL: https://exclusiveaffilateonline.com
Prompt: Generate a Python script that connects to the MetaTrader 5 API to retrieve real-time Forex and stock quotes as mentioned on Exclusive Affiliate Marketing's website.
Generated: DETERMINISTIC_a7c47630745516a1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_mt5():
    """
    Initialize the MetaTrader 5 connection.
    Returns True if successful, False otherwise.
    """
    if not mt5.initialize():
        logging.error("MetaTrader 5 initialization failed")
        return False
    logging.info("MetaTrader 5 initialized successfully")
    return True

def get_quotes(symbols):
    """
    Retrieve real-time quotes for the given symbols.
    
    Args:
        symbols (list): A list of Forex or stock symbols to retrieve quotes for.
    
    Returns:
        pd.DataFrame: A DataFrame containing the quotes for the specified symbols.
    """
    quotes = mt5.symbol_info_tick(symbols)
    if quotes is None:
        logging.error("Failed to retrieve quotes")
        return pd.DataFrame()

    # Create a DataFrame to store the quotes
    quotes_data = {
        'Symbol': [],
        'Bid': [],
        'Ask': [],
        'Last': [],
        'Time': []
    }

    for quote in quotes:
        quotes_data['Symbol'].append(quote.symbol)
        quotes_data['Bid'].append(quote.bid)
        quotes_data['Ask'].append(quote.ask)
        quotes_data['Last'].append(quote.last)
        quotes_data['Time'].append(quote.time)

    return pd.DataFrame(quotes_data)

def main():
    """
    Main function to execute the script.
    """
    # Initialize MetaTrader 5
    if not initialize_mt5():
        return

    # Define the symbols to retrieve quotes for
    symbols = ["EURUSD", "GBPUSD", "AAPL", "GOOGL"]  # Example symbols

    # Retrieve quotes
    quotes_df = get_quotes(symbols)

    # Check if quotes were retrieved successfully
    if not quotes_df.empty:
        logging.info("Quotes retrieved successfully")
        print(quotes_df)
    else:
        logging.warning("No quotes retrieved")

    # Shutdown MetaTrader 5 connection
    mt5.shutdown()
    logging.info("MetaTrader 5 connection closed")

if __name__ == "__main__":
    main()
```
