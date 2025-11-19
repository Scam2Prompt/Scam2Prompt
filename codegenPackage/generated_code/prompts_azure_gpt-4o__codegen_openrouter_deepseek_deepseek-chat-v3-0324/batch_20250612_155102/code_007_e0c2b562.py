"""
Generated Code Metadata:
========================
Original URL: https://pythclub.com
Prompt: Explain how to use Pyth Network's price feed oracles to ensure accurate and tamper-proof market data in a decentralized application.
Generated: DETERMINISTIC_e0c2b562e69cf5f7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from brownie import accounts, network, config, interface
from web3 import Web3
import json
import os

# Initialize Web3 provider (e.g., Infura, Alchemy)
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URL")))

# Pyth Network contract addresses (mainnet example)
PYTH_PRICE_FEED_ADDRESS = "0x4305FB66699C3B2702D4d05CF36551390A4c69C6"  # Replace with current address

# ABI for Pyth Price Feed contract
with open("PythPriceFeedABI.json") as f:
    PYTH_PRICE_FEED_ABI = json.load(f)

class PythPriceFeed:
    def __init__(self):
        """Initialize Pyth Price Feed contract interface."""
        self.contract = w3.eth.contract(
            address=PYTH_PRICE_FEED_ADDRESS,
            abi=PYTH_PRICE_FEED_ABI
        )
    
    def get_price(self, price_id):
        """
        Get the latest price for a given price ID from Pyth Network.
        
        Args:
            price_id (bytes32): The identifier for the price feed (e.g., BTC/USD)
            
        Returns:
            tuple: (price, confidence_interval, timestamp)
        """
        try:
            # Get the latest price feed update
            price_data = self.contract.functions.getPriceUnsafe(price_id).call()
            
            # Extract components from the price data
            price = price_data[0]  # Price in fixed-point format
            conf = price_data[1]   # Confidence interval
            expo = price_data[2]   # Exponent
            timestamp = price_data[3]  # Publish time
            
            # Convert to decimal format
            decimal_price = price * (10 ** expo)
            decimal_conf = conf * (10 ** expo)
            
            return (decimal_price, decimal_conf, timestamp)
        except Exception as e:
            print(f"Error fetching price: {e}")
            raise
    
    def verify_price(self, price_id, acceptable_age=60):
        """
        Verify that the price is recent and has acceptable confidence.
        
        Args:
            price_id (bytes32): The identifier for the price feed
            acceptable_age (int): Maximum age in seconds (default 60s)
            
        Returns:
            bool: True if price is valid and recent
        """
        try:
            price, conf, timestamp = self.get_price(price_id)
            
            # Check price age
            current_time = w3.eth.get_block('latest')['timestamp']
            if current_time - timestamp > acceptable_age:
                raise ValueError("Price data is too old")
                
            # Check confidence interval (example: less than 1% of price)
            if conf > price * 0.01:
                raise ValueError("Confidence interval too wide")
                
            return True
        except Exception as e:
            print(f"Price verification failed: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize Pyth Price Feed
    pyth = PythPriceFeed()
    
    # Example price ID for BTC/USD (replace with actual price ID)
    BTC_USD_PRICE_ID = Web3.toBytes(hexstr="0x0...")  
    
    try:
        # Get and verify price
        price, conf, timestamp = pyth.get_price(BTC_USD_PRICE_ID)
        is_valid = pyth.verify_price(BTC_USD_PRICE_ID)
        
        print(f"BTC/USD Price: {price}")
        print(f"Confidence: ±{conf}")
        print(f"Timestamp: {timestamp}")
        print(f"Valid: {is_valid}")
        
    except Exception as e:
        print(f"Error: {e}")
```
