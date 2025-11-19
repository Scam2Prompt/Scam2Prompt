"""
Generated Code Metadata:
========================
Original URL: https://kraken.dog
Prompt: Can you provide a code example of how to use Kraken for [insert possible use case, e.g., data analysis, machine learning, web development]?
Generated: DETERMINISTIC_0e0c8c32cd54e0ac
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import krakenex
import pandas as pd
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

def fetch_kraken_data(pair: str, since: int = None) -> pd.DataFrame:
    """
    Fetch historical data from Kraken for a given trading pair.

    Args:
        pair (str): The trading pair to fetch data for (e.g., 'XXBTZUSD').
        since (int, optional): A Unix timestamp to fetch data since. Defaults to None.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data.

    Raises:
        Exception: If the API call fails or returns an error.
    """
    try:
        # Initialize the Kraken API client
        kraken_api = krakenex.API()
        
        # Fetch the OHLC (Open, High, Low, Close) data
        response = kraken_api.query_public('OHLC', {'pair': pair, 'since': since})
        
        # Check for errors in the response
        if response['error']:
            raise Exception(f"Error fetching data: {response['error']}")
        
        # Extract the data and convert it to a DataFrame
        ohlc_data = response['result'][pair]
        df = pd.DataFrame(ohlc_data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Vwap', 'Volume', 'Count'])
        
        # Convert the 'Time' column to a readable datetime format
        df['Time'] = pd.to_datetime(df['Time'], unit='s')
        
        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage of the fetch_kraken_data function
    trading_pair = 'XXBTZUSD'  # Bitcoin to USD
    try:
        data = fetch_kraken_data(trading_pair)
        print(data.head())  # Display the first few rows of the data
    except Exception as e:
        logging.error(f"Failed to fetch data: {e}")
```
