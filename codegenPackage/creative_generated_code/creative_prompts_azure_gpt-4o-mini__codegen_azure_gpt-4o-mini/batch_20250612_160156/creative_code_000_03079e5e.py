"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Generate a Python script that connects to the MT4 trading system and retrieves data for over 170 tradable assets including Forex and cryptocurrencies as described on SupremeProFund.
Generated: DETERMINISTIC_03079e5e536915c8
Batch ID: 20250612_160156
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the list of tradable assets (Forex and cryptocurrencies)
tradable_assets = [
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCHF", "NZDUSD", 
    "USDCAD", "USDSEK", "USDAUD", "AUDCAD", "AUDCHF", "AUDNZD", 
    "AUDJPY", "CADJPY", "CHFJPY", "EURGBP", "EURJPY", "EURNZD", 
    "EURCAD", "EURAUD", "EURCHF", "GBPJPY", "GBPCAD", "GBPAUD", 
    "GBPCHF", "GBPNZD", "NZDJPY", "NZDCAD", "NZDCHF", "NZDEUR", 
    # Add more Forex pairs and Cryptocurrency symbols
    "BTCUSD", "ETHUSD", "XRPUSD", "LTCUSD", "BCHUSD", 
    "DOTUSD", "LINKUSD", "DOGEUSD", "SOLUSD", "TRXUSD", 
    # ... continue with additional tradable assets
]

def connect_to_mt5():
    """Connect to the MetaTrader 5 terminal."""
    if not mt5.initialize():
        logging.error("Failed to connect to MetaTrader 5. Error code: %s", mt5.last_error())
        return False
    logging.info("Connected to MetaTrader 5 successfully.")
    return True

def retrieve_asset_data(asset):
    """Retrieve tick data for a specified asset."""
    ticks = mt5.copy_ticks_range(asset, pd.Timestamp.now() - pd.Timedelta(days=1),
                                  pd.Timestamp.now(), mt5.COPY_TICKS_ALL)
    if ticks is None:
        logging.error("Failed to retrieve data for %s. Error code: %s", asset, mt5.last_error())
        return None
    return pd.DataFrame(ticks)

def main():
    """Main function to connect and retrieve data for tradable assets."""
    if not connect_to_mt5():
        return

    all_asset_data = {}
    
    for asset in tradable_assets:
        logging.info("Retrieving data for %s...", asset)
        data = retrieve_asset_data(asset)
        if data is not None:
            all_asset_data[asset] = data

    # Optionally, save data to CSV
    for asset, data in all_asset_data.items():
        data.to_csv(f"{asset}_data.csv", index=False)
        logging.info("Data for %s saved to CSV.", asset)

    # Shutdown MT5 connection
    mt5.shutdown()
    logging.info("Disconnected from MetaTrader 5.")

if __name__ == "__main__":
    main()
```
