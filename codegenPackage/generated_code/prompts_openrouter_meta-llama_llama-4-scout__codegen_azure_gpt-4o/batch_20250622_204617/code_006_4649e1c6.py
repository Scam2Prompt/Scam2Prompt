"""
Generated Code Metadata:
========================
Original URL: https://cryptokeninvestimentos.com.br
Prompt: "Provide an example of using the CCXT library in Python to fetch cryptocurrency exchange data."
Generated: DETERMINISTIC_4649e1c618528f50
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import the CCXT library
import ccxt

# Function to fetch and display cryptocurrency exchange data
<<<<<<< HEAD
def fetch_exchange_data(exchange_name, symbol):
    """
    Fetches ticker data for a given cryptocurrency symbol from a specified exchange.

    Args:
        exchange_name (str): The name of the cryptocurrency exchange (e.g., 'binance').
        symbol (str): The trading pair symbol (e.g., 'BTC/USDT').

    Returns:
        dict: Ticker data for the specified trading pair.
    """
    try:
        # Initialize the exchange object
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()

        # Check if the exchange supports the trading pair
        if symbol not in exchange.symbols:
            raise ValueError(f"The trading pair '{symbol}' is not supported by {exchange_name}.")

        # Fetch ticker data for the specified trading pair
        ticker = exchange.fetch_ticker(symbol)

        # Return the ticker data
        return ticker

    except AttributeError:
        # Handle the case where the exchange name is invalid
        raise ValueError(f"Exchange '{exchange_name}' is not recognized. Please check the name.")
    except Exception as e:
        # Handle other errors (e.g., network issues, invalid symbol)
        raise RuntimeError(f"An error occurred while fetching data: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Specify the exchange and trading pair
        exchange_name = "binance"
        trading_pair = "BTC/USDT"

        # Fetch and display the ticker data
        ticker_data = fetch_exchange_data(exchange_name, trading_pair)
        print("Ticker Data:")
        print(ticker_data)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
=======
def fetch_exchange_data(exchange_name, symbol, timeframe='1h', limit=10):
    """
    Fetches OHLCV (Open, High, Low, Close, Volume) data for a given cryptocurrency pair
    from the specified exchange using the CCXT library.

    Parameters:
        exchange_name (str): Name of the cryptocurrency exchange (e.g., 'binance').
        symbol (str): Trading pair symbol (e.g., 'BTC/USDT').
        timeframe (str): Timeframe for the OHLCV data (default is '1h').
        limit (int): Number of data points to fetch (default is 10).

    Returns:
        list: A list of OHLCV data points.
    """
    try:
        # Initialize the exchange instance
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class()

        # Check if the exchange supports fetching OHLCV data
        if not exchange.has.get('fetchOHLCV', False):
            raise NotImplementedError(f"{exchange_name} does not support fetching OHLCV data.")

        # Load markets to ensure the symbol is valid
        exchange.load_markets()
        if symbol not in exchange.symbols:
            raise ValueError(f"Symbol {symbol} is not available on {exchange_name}.")

        # Fetch OHLCV data
        ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

        # Return the fetched data
        return ohlcv_data

    except ccxt.BaseError as e:
        # Handle CCXT-specific errors
        print(f"An error occurred with the exchange: {str(e)}")
    except Exception as e:
        # Handle general errors
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Specify the exchange, trading pair, and other parameters
    exchange_name = 'binance'
    symbol = 'BTC/USDT'
    timeframe = '1h'
    limit = 5

    # Fetch and display the data
    data = fetch_exchange_data(exchange_name, symbol, timeframe, limit)
    if data:
        print(f"OHLCV data for {symbol} on {exchange_name}:")
        for entry in data:
            print(entry)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
