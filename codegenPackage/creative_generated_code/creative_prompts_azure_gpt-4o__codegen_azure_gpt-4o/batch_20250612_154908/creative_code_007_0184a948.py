"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap3.vercel.app
Prompt: Provide an example of how to set up a custom price oracle using Uniswap v3's pool data.
Generated: DETERMINISTIC_0184a94827e3bb40
Batch ID: 20250612_154908
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import math
from decimal import Decimal

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
POOL_ADDRESS = "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8"  # Replace with the Uniswap V3 Pool address
ABI_PATH = "./uniswap_v3_pool_abi.json"  # Path to Uniswap V3 Pool ABI

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Inject middleware for compatibility with some networks

# Load ABI for Uniswap V3 Pool
try:
    with open(ABI_PATH, "r") as abi_file:
        pool_abi = json.load(abi_file)
except FileNotFoundError as e:
    raise FileNotFoundError("ABI file not found. Ensure the path is correct.") from e

# Connect to the pool contract
pool_contract = web3.eth.contract(address=POOL_ADDRESS, abi=pool_abi)

# Function to fetch the current price from the pool contract
def get_current_price(pool_contract, decimals0, decimals1):
    try:
        slot0 = pool_contract.functions.slot0().call()  # Fetch slot0 data from the pool
        sqrt_price_x96 = slot0[0]  # Extract sqrtPriceX96 from slot0
        
        # Calculate the price using formula: (sqrtPriceX96^2 / 2^192) * (10**decimals1 / 10**decimals0)
        price = (Decimal(sqrt_price_x96) ** 2 / Decimal(2 ** 192)) * (10 ** decimals1 / 10 ** decimals0)
        return price
    except Exception as e:
        raise RuntimeError(f"Error fetching price from pool: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    # Define the decimals for token0 and token1 (replace with actual token decimals)
    decimals_token0 = 18  # Example: 18 decimals for ETH
    decimals_token1 = 6   # Example: 6 decimals for USDC

    try:
        price = get_current_price(pool_contract, decimals_token0, decimals_token1)
        print(f"Current price from the pool: {price}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

Ensure to replace placeholders (`YOUR_INFURA_PROJECT_ID`, `uniswap_v3_pool_abi.json`, `POOL_ADDRESS`) with actual values relevant to your implementation. The code assumes the ABI for the Uniswap V3 Pool is stored locally as a JSON file.
