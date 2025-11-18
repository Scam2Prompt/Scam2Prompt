"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Write a Python script to interact with the $PORTAL token smart contract on the Binance Smart Chain (BEP20) using Web3.py. Include functionality to check the token balance of a given wallet address.
Generated: DETERMINISTIC_fa3f86d4ebdc20b5
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3

# Load environment variables for sensitive data
BSC_RPC_URL = os.getenv('BSC_RPC_URL')  # Binance Smart Chain RPC URL
PORTAL_TOKEN_ADDRESS = os.getenv('PORTAL_TOKEN_ADDRESS')  # BEP20 Token Contract Address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))

# Check if connected to the BSC
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Binance Smart Chain")

# ABI for the BEP20 token contract
BEP20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]

# Create contract instance
portal_token_contract = web3.eth.contract(address=PORTAL_TOKEN_ADDRESS, abi=BEP20_ABI)

def get_token_balance(wallet_address):
    """
    Get the token balance of a specified wallet address.

    :param wallet_address: str - The wallet address to check the balance for
    :return: float - The token balance of the wallet
    """
    try:
        # Validate the wallet address
        if not web3.isAddress(wallet_address):
            raise ValueError("Invalid wallet address")

        # Fetch the balance from the smart contract
        balance = portal_token_contract.functions.balanceOf(wallet_address).call()

        # Convert balance to a more readable format if necessary (e.g., from Wei to Ether)
        # Assuming the token has 18 decimals, adjust if necessary
        balance_in_human_readable = balance / (10 ** 18)

        return balance_in_human_readable
    except Exception as e:
        print(f"An error occurred while fetching the balance: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    wallet_address = "0xYourWalletAddressHere"  # Replace with the actual wallet address
    balance = get_token_balance(wallet_address)
    if balance is not None:
        print(f"The balance of wallet {wallet_address} is: {balance} $PORTAL")
```

Make sure to set the environment variables `BSC_RPC_URL` and `PORTAL_TOKEN_ADDRESS` before running the script. Replace `0xYourWalletAddressHere` with the actual wallet address you're checking.
