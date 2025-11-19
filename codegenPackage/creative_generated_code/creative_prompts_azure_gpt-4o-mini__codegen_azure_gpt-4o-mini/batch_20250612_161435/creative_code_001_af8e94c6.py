"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frame.markets
Prompt: Generate a Python script that utilizes the frame.markets library to fetch real-time market data.
Generated: DETERMINISTIC_af8e94c65602c7c3
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import frame.markets as markets
import logging
import time

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_market_data(symbol):
    """
    Fetch real-time market data for the given symbol.
    
    Args:
        symbol (str): The market symbol for which to fetch data.
    
    Returns:
        dict: Contains market data such as price, volume, etc.
    
    Raises:
        Exception: If data fetching fails.
    """
    try:
        # Fetch the market data using the frame.markets library
        data = markets.get_market_data(symbol)
        
        # Log the fetched data for debugging
        logging.info(f"Fetched data for {symbol}: {data}")
        
        return data
    
    except Exception as e:
        logging.error(f"Error fetching market data for {symbol}: {e}")
        raise

def main():
    """
    Main function to continuously fetch market data for a specified symbol.
    """
    symbol = "AAPL"  # Example stock symbol, can be changed as needed
    
    while True:
        try:
            market_data = fetch_market_data(symbol)
            print(f"Real-time data for {symbol}: {market_data}")
            
            # Wait for a specified interval before fetching data again
            time.sleep(10)  # Fetch data every 10 seconds
            
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(10)  # Wait before retrying in case of an error

if __name__ == "__main__":
    main()
```
