"""
Generated Code Metadata:
========================
Original URL: https://pythcash.com
Prompt: Write code to fetch and display live market data using Pyth oracles in a decentralized application (dApp).
Generated: DETERMINISTIC_60975fbfdeb6dfd4
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from anchorpy import Client, Program
from anchorpy.provider import Provider
from anchorpy.utils.rpc import get_cluster_rpc_url
from solana.rpc.api import Client as SolanaClient

# Set up Pyth oracle constants
PYTH_PROGRAM_ID = "pythoracle"
PYTH_PRICE_FEED_PREFIX = "pyth:price:"

# Set up Solana client and provider
def setup_solana_client():
    """Set up Solana client and provider"""
    url = get_cluster_rpc_url("devnet")
    client = SolanaClient(url, commitment="confirmed")
    provider = Provider(client, Provider.localnet("devnet"))
    return client, provider

# Fetch live market data using Pyth oracles
def fetch_live_market_data(client, symbol):
    """Fetch live market data using Pyth oracles"""
    try:
        # Construct Pyth price feed account address
        price_feed_address = f"{PYTH_PRICE_FEED_PREFIX}{symbol.lower()}"

        # Get Pyth price feed account info
        account_info = client.get_account_info(price_feed_address)

        # Check if account info is valid
        if not account_info.value:
            raise Exception(f"Failed to retrieve Pyth price feed account info for {symbol}")

        # Parse Pyth price feed data
        price_feed_data = account_info.value.data

        # Extract price data
        price = int.from_bytes(price_feed_data[36:44], "little") / 10**8

        return price

    except Exception as e:
        print(f"Error fetching live market data: {str(e)}")
        return None

# Display live market data
def display_live_market_data(client, symbols):
    """Display live market data"""
    for symbol in symbols:
        price = fetch_live_market_data(client, symbol)

        if price:
            print(f"Live market data for {symbol}: ${price:.2f}")

# Main function
def main():
    client, _ = setup_solana_client()
    symbols = ["BTC/USD", "ETH/USD"]
    display_live_market_data(client, symbols)

if __name__ == "__main__":
    main()
```
