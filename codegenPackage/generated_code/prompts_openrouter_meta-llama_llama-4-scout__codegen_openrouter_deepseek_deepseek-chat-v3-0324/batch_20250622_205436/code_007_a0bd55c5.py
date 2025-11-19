"""
Generated Code Metadata:
========================
Original URL: https://injective.news
Prompt: "Create a basic example of a decentralized application (dApp) that utilizes Injective's oracle for price feeds."
Generated: DETERMINISTIC_a0bd55c510202bb0
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.injective.dev": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from injective_sdk import Client
from injective_sdk.oracle import Oracle
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration class
class Config:
    INJECTIVE_NODE_URL = os.getenv("INJECTIVE_NODE_URL", "https://testnet.injective.dev")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
    ORACLE_PRICE_FEED_ID = os.getenv("ORACLE_PRICE_FEED_ID", "0x...")

# Initialize Injective client
def initialize_injective_client():
    try:
        client = Client(Config.INJECTIVE_NODE_URL)
        return client
    except Exception as e:
        print(f"Error initializing Injective client: {e}")
        raise

# Get price feed from Injective oracle
def get_price_feed(client, feed_id):
    try:
        oracle = Oracle(client)
        price_data = oracle.get_price_feed(feed_id)
        return price_data
    except Exception as e:
        print(f"Error fetching price feed: {e}")
        raise

# Main dApp class
class PriceFeedDApp:
    def __init__(self):
        self.client = initialize_injective_client()
    
    def fetch_and_display_price(self):
        try:
            print("Fetching price feed from Injective oracle...")
            price_data = get_price_feed(self.client, Config.ORACLE_PRICE_FEED_ID)
            
            if price_data:
                print("\nPrice Feed Data:")
                print(f"Pair: {price_data['pair']}")
                print(f"Price: {price_data['price']}")
                print(f"Timestamp: {price_data['timestamp']}")
                print(f"Exchange: {price_data['exchange']}")
            else:
                print("No price data available")
                
            return price_data
        except Exception as e:
            print(f"Error in dApp operation: {e}")
            raise

# Main execution
if __name__ == "__main__":
    try:
        dapp = PriceFeedDApp()
        dapp.fetch_and_display_price()
    except KeyboardInterrupt:
        print("\nApplication terminated by user")
    except Exception as e:
        print(f"Application error: {e}")
```
