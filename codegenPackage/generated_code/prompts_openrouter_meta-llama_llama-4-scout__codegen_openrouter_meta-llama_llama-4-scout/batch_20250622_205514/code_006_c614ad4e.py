"""
Generated Code Metadata:
========================
Original URL: https://exclusiveaffilateonline.com
Prompt: "Write a script to fetch and analyze historical stock prices and Forex rates from a platform like MetaTrader 5, focusing on assets with low minimum deposits and competitive spreads."
Generated: DETERMINISTIC_c614ad4ee9b93bd5
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import MetaTrader5 as mt5
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_metatrader5():
    """
    Establish a connection to MetaTrader 5.
    
    Returns:
        bool: True if connected, False otherwise.
    """
    try:
        # Check if MetaTrader 5 is connected
        if not mt5.is_connected():
            # Connect to MetaTrader 5
            mt5.initialize()
            logging.info("Connected to MetaTrader 5")
            return True
        else:
            logging.info("Already connected to MetaTrader 5")
            return True
    except Exception as e:
        logging.error(f"Failed to connect to MetaTrader 5: {e}")
        return False

def get_historical_stock_prices(symbol, timeframe, start_date, end_date):
    """
    Fetch historical stock prices from MetaTrader 5.
    
    Parameters:
        symbol (str): Stock symbol.
        timeframe (str): Timeframe (e.g., '1h', '1d').
        start_date (str): Start date (YYYY-MM-DD).
        end_date (str): End date (YYYY-MM-DD).
    
    Returns:
        pandas.DataFrame: Historical stock prices.
    """
    try:
        # Convert dates to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Get historical data
        rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        
        return df
    except Exception as e:
        logging.error(f"Failed to fetch historical stock prices: {e}")
        return None

def get_historical_forex_rates(symbol, timeframe, start_date, end_date):
    """
    Fetch historical Forex rates from MetaTrader 5.
    
    Parameters:
        symbol (str): Forex symbol (e.g., 'EURUSD').
        timeframe (str): Timeframe (e.g., '1h', '1d').
        start_date (str): Start date (YYYY-MM-DD).
        end_date (str): End date (YYYY-MM-DD).
    
    Returns:
        pandas.DataFrame: Historical Forex rates.
    """
    try:
        # Convert dates to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Get historical data
        rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        
        return df
    except Exception as e:
        logging.error(f"Failed to fetch historical Forex rates: {e}")
        return None

def analyze_spreads(df):
    """
    Analyze spreads in historical data.
    
    Parameters:
        df (pandas.DataFrame): Historical data.
    
    Returns:
        dict: Spread analysis results.
    """
    try:
        # Calculate spreads
        df['spread'] = df['ask'] - df['bid']
        
        # Calculate average and minimum spreads
        avg_spread = df['spread'].mean()
        min_spread = df['spread'].min()
        
        return {
            'average_spread': avg_spread,
            'minimum_spread': min_spread
        }
    except Exception as e:
        logging.error(f"Failed to analyze spreads: {e}")
        return None

def get_low_min_deposit_assets():
    """
    Get assets with low minimum deposits.
    
    Returns:
        list: Assets with low minimum deposits.
    """
    try:
        # Define assets with low minimum deposits
        low_min_deposit_assets = [
            'EURUSD',
            'GBPUSD',
            'USDJPY',
            'AAPL',
            'GOOGL'
        ]
        
        return low_min_deposit_assets
    except Exception as e:
        logging.error(f"Failed to get low minimum deposit assets: {e}")
        return []

def main():
    # Connect to MetaTrader 5
    if not connect_to_metatrader5():
        return

    # Get assets with low minimum deposits
    assets = get_low_min_deposit_assets()

    # Define timeframe and date range
    timeframe = '1d'
    start_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
    end_date = datetime.today().strftime("%Y-%m-%d")

    # Analyze historical data for each asset
    for asset in assets:
        logging.info(f"Analyzing {asset}...")
        
        # Get historical data
        if asset in ['EURUSD', 'GBPUSD', 'USDJPY']:
            df = get_historical_forex_rates(asset, timeframe, start_date, end_date)
        else:
            df = get_historical_stock_prices(asset, timeframe, start_date, end_date)
        
        if df is not None:
            # Analyze spreads
            spread_analysis = analyze_spreads(df)
            
            if spread_analysis is not None:
                logging.info(f"Spread analysis for {asset}:")
                logging.info(f"  Average spread: {spread_analysis['average_spread']}")
                logging.info(f"  Minimum spread: {spread_analysis['minimum_spread']}")

if __name__ == "__main__":
    main()
```
