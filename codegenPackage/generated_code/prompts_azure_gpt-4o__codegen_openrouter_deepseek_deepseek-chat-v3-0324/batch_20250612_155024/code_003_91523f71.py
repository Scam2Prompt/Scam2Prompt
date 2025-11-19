"""
Generated Code Metadata:
========================
Original URL: https://pythpro.com
Prompt: Explain how to use Pyth price feed oracles to ensure accurate market data in a decentralized application.
Generated: DETERMINISTIC_91523f712d6f72e5
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
from brownie import (
    accounts,
    network,
    config,
    MockV3Aggregator,
    VRFCoordinatorMock,
    LinkToken,
    Contract,
    interface,
)
from web3 import Web3

# Constants
DECIMALS = 8
INITIAL_VALUE = 200000000000  # 2000 USD with 8 decimal places
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

# Helper function to get account based on environment
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

# Function to deploy mock price feed for local testing
def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    
    # Deploy mock price feed
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": account}
    )
    print(f"Mock Price Feed deployed to {mock_price_feed.address}")
    
    return mock_price_feed

# Function to get the live price feed contract
def get_price_feed_contract():
    # Check if we're on a local network
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return deploy_mocks()
    else:
        # Get the contract address from config
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        # Create and return the contract
        price_feed = interface.AggregatorV3Interface(price_feed_address)
        return price_feed

# Function to get the latest price from the price feed
def get_latest_price():
    price_feed = get_price_feed_contract()
    
    # Get latest round data
    latest_round_data = price_feed.latestRoundData()
    
    # Return the price (adjust for decimals)
    price = latest_round_data[1]
    adjusted_price = price / 10 ** price_feed.decimals()
    
    print(f"The current ETH price is {adjusted_price}")
    return adjusted_price

# Function to verify price feed is working
def verify_price_feed():
    try:
        price = get_latest_price()
        print(f"Price feed verification successful. Current price: {price}")
        return True
    except Exception as e:
        print(f"Error verifying price feed: {e}")
        return False

# Main execution
def main():
    # Verify the price feed is working
    verify_price_feed()
```
