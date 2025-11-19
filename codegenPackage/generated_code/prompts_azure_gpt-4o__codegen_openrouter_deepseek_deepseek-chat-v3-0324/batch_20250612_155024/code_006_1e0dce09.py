"""
Generated Code Metadata:
========================
Original URL: https://pythcall.com
Prompt: Provide an example of using Pyth Network's price feed oracles to retrieve stock market data in a decentralized application.
Generated: DETERMINISTIC_1e0dce09b85a01fb
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from brownie import accounts, network, config, Contract
from web3 import Web3
import json

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration
PRICE_FEED_ADDRESS = "0xe5BbBdb2Bb953371841318E1Edfbf727447CeF2E"  # Example Pyth price feed address
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")

# Connect to Ethereum network
def connect_to_network():
    if network.is_connected():
        return
    
    network_name = "mainnet"  # or "kovan", "rinkeby", etc.
    network.connect(f"{network_name}-infura", project_id=INFURA_PROJECT_ID)

# Get Pyth price feed ABI
def get_price_feed_abi():
    # Simplified ABI for demonstration - in production use the full ABI
    return json.loads('''
        [
            {
                "inputs": [],
                "name": "getPrice",
                "outputs": [
                    {
                        "internalType": "int256",
                        "name": "",
                        "type": "int256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "getEmaPrice",
                "outputs": [
                    {
                        "internalType": "int256",
                        "name": "",
                        "type": "int256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ]
    ''')

# Main function to fetch price data
def get_stock_price(stock_symbol):
    try:
        # Connect to network
        connect_to_network()
        
        # Set up account
        account = accounts.add(PRIVATE_KEY) if PRIVATE_KEY else accounts[0]
        
        # Create contract instance
        price_feed = Contract.from_abi(
            "PythPriceFeed",
            PRICE_FEED_ADDRESS,
            get_price_feed_abi()
        )
        
        # Get current price and EMA
        current_price = price_feed.getPrice()
        ema_price = price_feed.getEmaPrice()
        
        return {
            "symbol": stock_symbol,
            "current_price": Web3.fromWei(current_price, 'ether'),
            "ema_price": Web3.fromWei(ema_price, 'ether')
        }
        
    except Exception as e:
        print(f"Error fetching price data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    stock_data = get_stock_price("AAPL")
    if stock_data:
        print(f"Stock Data for {stock_data['symbol']}:")
        print(f"Current Price: {stock_data['current_price']}")
        print(f"EMA Price: {stock_data['ema_price']}")
```
