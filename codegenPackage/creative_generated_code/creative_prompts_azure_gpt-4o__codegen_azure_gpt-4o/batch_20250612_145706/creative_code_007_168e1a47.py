"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-protocol-ui.vercel.app
Prompt: Develop a script to monitor collateral health and trigger alerts using the Venus Protocol on Binance Smart Chain.
Generated: DETERMINISTIC_168e1a47336471e3
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to monitor collateral health and trigger alerts using the Venus Protocol on Binance Smart Chain.

Requirements:
- Python 3.9+ 
- Web3.py library
- dotenv for environment variables
- Venus Protocol ABI and Contract addresses

This script uses Web3.py to interact with the Binance Smart Chain and checks the health of user collateral
on Venus Protocol. Alerts are triggered if the collateral health falls below a specified threshold.
"""

import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
BSC_RPC_URL = os.getenv("BSC_RPC_URL")  # Binance Smart Chain RPC URL from .env
ALERT_THRESHOLD = 1.5  # Collateral health alert threshold
USER_WALLET_ADDRESS = os.getenv("USER_WALLET_ADDRESS")  # User wallet address to monitor
VENUS_COMPTROLLER_ADDRESS = "0xfD36E2c2a6789Db23113685031d7F16329158384"  # Venus Comptroller Contract
VENUS_ABI_PATH = "venus_comptroller_abi.json"  # Path to Venus Comptroller ABI file

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Binance Smart Chain RPC.")

# Load Venus Comptroller ABI
try:
    with open(VENUS_ABI_PATH, "r") as abi_file:
        venus_comptroller_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError("Venus Comptroller ABI file not found.")
except json.JSONDecodeError:
    raise ValueError("Error decoding Venus Comptroller ABI file.")

# Create contract instance
venus_comptroller = web3.eth.contract(
    address=VENUS_COMPTROLLER_ADDRESS, abi=venus_comptroller_abi
)

def get_account_liquidity(user_address):
    """
    Fetches account liquidity and collateral health for the specified address.

    Parameters:
        user_address (str): Wallet address of the user.

    Returns:
        tuple: (liquidity in USD, shortfall in USD, collateral health ratio)
    """
    try:
        # Venus Comptroller's `getAccountLiquidity` function
        liquidity, shortfall, result = venus_comptroller.functions.getAccountLiquidity(
            Web3.toChecksumAddress(user_address)
        ).call()
        if result != 0:
            raise ValueError("Error fetching account liquidity.")
        
        # Calculate collateral health ratio
        collateral_health = liquidity / shortfall if shortfall > 0 else float("inf")
        return liquidity, shortfall, collateral_health
    except Exception as e:
        raise RuntimeError(f"Failed to fetch account liquidity: {e}")

def monitor_collateral_health():
    """
    Monitors collateral health and triggers an alert if health drops below the threshold.
    """
    try:
        liquidity, shortfall, collateral_health = get_account_liquidity(USER_WALLET_ADDRESS)
        
        print(f"Liquidity: {liquidity} USD")
        print(f"Shortfall: {shortfall} USD")
        print(f"Collateral Health Ratio: {collateral_health:.2f}")
        
        if collateral_health < ALERT_THRESHOLD:
            print("⚠️ Alert: Collateral health is below the threshold!")
            # Add your custom alert logic here (e.g., email, SMS, or webhook)
    except Exception as e:
        print(f"Error during monitoring: {e}")

if __name__ == "__main__":
    print("Starting Venus Protocol collateral health monitoring...")
    monitor_collateral_health()
```

### Notes:
- Replace `BSC_RPC_URL` and `USER_WALLET_ADDRESS` with your Binance Smart Chain RPC URL and wallet address in a `.env` file.
- Ensure the `venus_comptroller_abi.json` file contains the correct ABI for the Venus Comptroller contract.
- Add alert integration (e.g., email, SMS, webhook) to the alert logic section.
