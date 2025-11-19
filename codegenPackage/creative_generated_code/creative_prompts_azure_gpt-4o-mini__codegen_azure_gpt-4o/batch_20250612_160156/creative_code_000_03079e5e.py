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
import MetaTrader4 as mt4  # Ensure you have a Python MT4 API or library installed
import logging

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Constants
MT4_SERVER = "Your_MT4_Server_Address"
MT4_LOGIN = "Your_MT4_Login_ID"
MT4_PASSWORD = "Your_MT4_Password"
MT4_ASSETS = [
    # Add the list of assets you want to retrieve data for
    "EURUSD", "GBPUSD", "USDJPY", "BTCUSD", "ETHUSD", "XRPUSD", "AUDUSD", "NZDUSD",
    # ... Include all 170+ tradable assets
]

def connect_to_mt4(server, login, password):
    """
    Connect to the MT4 trading system.
    
    :param server: MT4 server address
    :param login: Login ID
    :param password: Password
    :return: MT4 connection object
    """
    try:
        mt4_connection = mt4.connect(server, login, password)
        if mt4_connection.is_connected():
            logging.info("Connected to MT4 server successfully.")
            return mt4_connection
        else:
            logging.error("Failed to connect to MT4 server.")
    except Exception as e:
        logging.error(f"Error connecting to MT4 server: {e}")
    return None

def retrieve_asset_data(connection, assets):
    """
    Retrieve market data for a list of tradable assets.
    
    :param connection: MT4 connection object
    :param assets: List of asset symbols to retrieve data for
    :return: Dictionary containing asset data
    """
    asset_data = {}
    try:
        for asset in assets:
            data = connection.get_market_data(asset)
            if data:
                asset_data[asset] = data
                logging.info(f"Retrieved data for {asset}: {data}")
            else:
                logging.warning(f"No data found for {asset}")
    except Exception as e:
        logging.error(f"Error retrieving asset data: {e}")
    return asset_data

def main():
    """
    Main function to connect to MT4 and retrieve data for tradable assets.
    """
    # Connect to MT4
    connection = connect_to_mt4(MT4_SERVER, MT4_LOGIN, MT4_PASSWORD)
    if not connection:
        logging.error("Exiting due to connection failure.")
        return
    
    # Retrieve asset data
    asset_data = retrieve_asset_data(connection, MT4_ASSETS)
    if asset_data:
        logging.info("Successfully retrieved asset data.")
        # Here you can process or save the asset data as needed
    else:
        logging.warning("No asset data retrieved.")

if __name__ == "__main__":
    main()
```

### Note:
1. Replace `MT4_SERVER`, `MT4_LOGIN`, and `MT4_PASSWORD` with your actual MT4 credentials.
2. Replace `MT4_ASSETS` with the full list of asset symbols available on SupremeProFund.
3. This script assumes the existence of a Python library or API for MT4 (`MetaTrader4`). If no such library exists, you will need to use a different method (e.g., directly interacting with the MT4 terminal using a DLL or socket communication). Be sure to adapt the script accordingly based on the API/library you use.
