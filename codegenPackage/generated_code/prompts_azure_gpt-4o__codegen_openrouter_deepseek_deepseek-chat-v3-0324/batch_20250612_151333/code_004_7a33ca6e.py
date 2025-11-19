"""
Generated Code Metadata:
========================
Original URL: https://pp8.pages.dev
Prompt: Write a Python script using the web3.py library to check the balance of $WATER tokens in a connected wallet.
Generated: DETERMINISTIC_7a33ca6e6311318c
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from web3 import Web3
from web3.middleware import geth_poa_middleware
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration
INFURA_URL = os.getenv('INFURA_URL')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Only needed for signing transactions
WATER_TOKEN_ADDRESS = os.getenv('WATER_TOKEN_ADDRESS')

# ABI for ERC20 token balance check
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def check_water_balance():
    try:
        # Initialize Web3
        w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        
        # Add PoA middleware if needed (for networks like Polygon, BSC)
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Verify connection
        if not w3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")
        
        # Verify wallet address
        if not w3.is_address(WALLET_ADDRESS):
            raise ValueError("Invalid wallet address")
        
        # Create token contract instance
        token_contract = w3.eth.contract(
            address=Web3.to_checksum_address(WATER_TOKEN_ADDRESS),
            abi=ERC20_ABI
        )
        
        # Get token decimals
        decimals = token_contract.functions.decimals().call()
        
        # Get raw balance
        raw_balance = token_contract.functions.balanceOf(
            Web3.to_checksum_address(WALLET_ADDRESS)
        ).call()
        
        # Convert to human-readable format
        balance = raw_balance / (10 ** decimals)
        
        return balance
        
    except Exception as e:
        print(f"Error checking balance: {e}")
        raise

if __name__ == "__main__":
    try:
        balance = check_water_balance()
        print(f"Your $WATER token balance is: {balance}")
    except Exception as e:
        print(f"Failed to check balance: {e}")
```
