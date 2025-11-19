"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.network
Prompt: Explain how to use Aave's multi-network capabilities in a DeFi application.
Generated: DETERMINISTIC_dac028929630e376
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use Aave's multi-network capabilities in a DeFi application.
The code connects to the Ethereum and Polygon networks, fetches lending pool data, and checks user balances.
It relies on web3.py and the Aave Protocol's JSON-RPC endpoints.

Dependencies:
- web3: `pip install web3`
- dotenv: `pip install python-dotenv`
- Aave Contract ABI (fetch from Aave's GitHub or the official documentation)

Environment Variables:
- ETH_RPC_URL: Ethereum network RPC URL
- POLYGON_RPC_URL: Polygon network RPC URL
"""

import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file for RPC endpoints
load_dotenv()

# Constants
ETH_RPC_URL = os.getenv("ETH_RPC_URL")  # Ethereum Mainnet RPC URL
POLYGON_RPC_URL = os.getenv("POLYGON_RPC_URL")  # Polygon RPC URL
AAVE_LENDING_POOL_ADDRESS_PROVIDER = {
    "eth": "0xb53C1a33016B2DC2fF3653530bFF1848a515c8c5",  # Ethereum Mainnet
    "polygon": "0xa97684ead0e402dC232d5A977953DF7ECBaB3cdB",  # Polygon
}

# Load Aave Lending Pool ABI
with open("AaveLendingPoolABI.json", "r") as abi_file:
    LENDING_POOL_ABI = json.load(abi_file)


def connect_to_network(network_name, rpc_url):
    """
    Connect to a blockchain network using Web3.
    :param network_name: Name of the network (e.g., "eth", "polygon").
    :param rpc_url: RPC endpoint URL.
    :return: Web3 instance connected to the network.
    """
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not web3.isConnected():
            raise ConnectionError(f"Failed to connect to {network_name} network.")
        print(f"Connected to {network_name.capitalize()} network.")
        return web3
    except Exception as e:
        print(f"Error connecting to {network_name} network: {str(e)}")
        raise


def get_lending_pool(web3, address_provider):
    """
    Get the Lending Pool contract instance for Aave.
    :param web3: Web3 instance.
    :param address_provider: Lending Pool Address Provider contract address.
    :return: Lending Pool contract instance.
    """
    try:
        address_provider_contract = web3.eth.contract(
            address=Web3.to_checksum_address(address_provider),
            abi=LENDING_POOL_ABI
        )
        lending_pool_address = address_provider_contract.functions.getLendingPool().call()
        lending_pool_contract = web3.eth.contract(
            address=Web3.to_checksum_address(lending_pool_address),
            abi=LENDING_POOL_ABI
        )
        return lending_pool_contract
    except Exception as e:
        print(f"Error fetching Lending Pool contract: {str(e)}")
        raise


def check_user_balance(web3, user_address):
    """
    Check the native token balance of a user on the given network.
    :param web3: Web3 instance.
    :param user_address: User's wallet address.
    :return: Balance in native tokens (ETH or MATIC).
    """
    try:
        balance = web3.eth.get_balance(Web3.to_checksum_address(user_address))
        return web3.fromWei(balance, "ether")
    except Exception as e:
        print(f"Error checking user balance: {str(e)}")
        raise


# Main Function
if __name__ == "__main__":
    try:
        # Connect to Ethereum and Polygon networks
        eth_web3 = connect_to_network("eth", ETH_RPC_URL)
        polygon_web3 = connect_to_network("polygon", POLYGON_RPC_URL)

        # Fetch Lending Pool contract instances
        eth_lending_pool = get_lending_pool(eth_web3, AAVE_LENDING_POOL_ADDRESS_PROVIDER["eth"])
        polygon_lending_pool = get_lending_pool(polygon_web3, AAVE_LENDING_POOL_ADDRESS_PROVIDER["polygon"])

        # Example: Check user balance on both networks
        user_wallet_address = input("Enter your wallet address: ")
        eth_balance = check_user_balance(eth_web3, user_wallet_address)
        polygon_balance = check_user_balance(polygon_web3, user_wallet_address)

        print(f"User's ETH Balance: {eth_balance} ETH")
        print(f"User's MATIC Balance: {polygon_balance} MATIC")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
