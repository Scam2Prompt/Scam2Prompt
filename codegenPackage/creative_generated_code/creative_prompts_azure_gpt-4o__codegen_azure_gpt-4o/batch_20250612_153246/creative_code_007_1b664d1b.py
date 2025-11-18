"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Generate a code example to integrate Pyth Network's price feeds into a decentralized exchange (DEX) on the BNB Chain. Include steps for fetching and validating price data.
Generated: DETERMINISTIC_1b664d1ba0e08091
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1/price_feed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed1.binance.org:443": {
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
"""
Integration of Pyth Network's price feeds into a decentralized exchange (DEX) on the BNB Chain.
This script fetches and validates price data from the Pyth Network Oracle.
"""

from web3 import Web3
from pyth_sdk import PythHttpClient, PriceFeed

# Constants
BNB_CHAIN_RPC_URL = "https://bsc-dataseed1.binance.org:443"  # BNB Chain RPC endpoint
PYTH_PRICE_FEED_URL = "https://api.pyth.network/v1/price_feed"  # Pyth network price feed API
CONTRACT_ADDRESS = "0xYourDexContractAddress"  # Replace with your DEX's contract address
PRICE_FEED_ID = "0xYourPriceFeedId"  # Replace with the Pyth price feed ID for the asset you want

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(BNB_CHAIN_RPC_URL))

# Ensure Web3 connection is established
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the BNB Chain RPC endpoint.")

# DEX contract ABI (replace with the actual ABI of your DEX contract)
DEX_CONTRACT_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "getPrice",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function",
    },
    # Add other methods from your DEX contract ABI as needed
]

# Initialize the DEX contract instance
dex_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=DEX_CONTRACT_ABI)

# Function to fetch the price data from Pyth Network
def fetch_price_data(price_feed_id):
    """
    Fetches price data from Pyth Network using the price feed ID.

    :param price_feed_id: The Pyth price feed ID of the asset.
    :return: The latest price and confidence interval.
    """
    try:
        pyth_client = PythHttpClient(PYTH_PRICE_FEED_URL)
        price_feed = pyth_client.get_price_feed(price_feed_id)

        if price_feed.status != PriceFeed.STATUS_OK:
            raise ValueError("Invalid price feed status: {}".format(price_feed.status))

        # Extract latest price and confidence interval
        latest_price = price_feed.price
        confidence_interval = price_feed.confidence_interval

        return latest_price, confidence_interval
    except Exception as e:
        raise RuntimeError(f"Failed to fetch price data: {str(e)}")


# Function to validate price data
def validate_price_data(price, confidence_interval):
    """
    Validates the price data fetched from Pyth Network.

    :param price: The latest price of the asset.
    :param confidence_interval: The confidence interval for the price.
    :return: True if valid, False otherwise.
    """
    if price <= 0:
        return False

    # Example confidence interval check (customize as needed for your DEX logic)
    max_allowed_interval = 0.05  # 5% confidence interval threshold
    if confidence_interval / price > max_allowed_interval:
        return False

    return True


# Fetch and validate price data
try:
    latest_price, confidence_interval = fetch_price_data(PRICE_FEED_ID)

    if validate_price_data(latest_price, confidence_interval):
        print(f"Validated price: {latest_price} with confidence interval: {confidence_interval}")
        # Update the price in the DEX contract (example usage)
        # Ensure you have proper permissions to update the contract
        # transaction = dex_contract.functions.updatePrice(latest_price).transact({"from": web3.eth.default_account})
        # print(f"Price updated in DEX contract. Transaction hash: {transaction.hex()}")
    else:
        print(f"Price data validation failed. Price: {latest_price}, Confidence Interval: {confidence_interval}")

except Exception as e:
    print(f"Error: {str(e)}")
```
