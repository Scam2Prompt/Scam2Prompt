"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.morpo.org
Prompt: Develop a script to automate the process of supplying USDC to a vault and borrowing wETH using Morpho's bundling mechanism.
Generated: DETERMINISTIC_64b4fb61ee66f3ce
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants for the script
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for Ethereum network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the user
MORPHO_CONTRACT_ADDRESS = "0x..."  # Replace with Morpho contract address
USDC_ADDRESS = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC token address
WETH_ADDRESS = "0xC02aaa39b223FE8D0a0e5C4F27eAD9083C756Cc2"  # wETH token address

# ABI for the Morpho contract (simplified for example purposes)
MORPHO_CONTRACT_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "asset", "type": "address"},
            {"name": "amount", "type": "uint256"},
            {"name": "borrowAsset", "type": "address"}
        ],
        "name": "supplyAndBorrow",
        "outputs": [],
        "type": "function"
    },
]

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# Set up the user's account
user_account = Account.from_key(PRIVATE_KEY)

# Initialize Morpho contract instance
morpho_contract = web3.eth.contract(address=MORPHO_CONTRACT_ADDRESS, abi=MORPHO_CONTRACT_ABI)

# Function to automate supply and borrow
async def supply_and_borrow(amount_usdc: int, borrow_asset: str):
    """
    Supply USDC to Morpho vault and borrow wETH.
    
    :param amount_usdc: Amount of USDC to supply (in smallest unit)
    :param borrow_asset: Asset to borrow (e.g., wETH address)
    """
    try:
        # Prepare transaction data
        tx = morpho_contract.functions.supplyAndBorrow(
            USDC_ADDRESS,
            amount_usdc,
            borrow_asset
        ).build_transaction({
            'from': user_account.address,
            'gas': 2000000,  # Set gas limit
            'gasPrice': web3.toWei('20', 'gwei'),  # Set gas price
            'nonce': web3.eth.get_transaction_count(user_account.address),
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        
        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(tx_hash)}")
        
        # Wait for transaction to be mined
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction mined! Status: {receipt.status}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual USDC amount and wETH address
    # Example: 100 USDC (1 USDC = 10**6 smallest unit)
    asyncio.run(supply_and_borrow(amount_usdc=100 * 10**6, borrow_asset=WETH_ADDRESS))
```

**Note:** Replace `"0x..."` in `MORPHO_CONTRACT_ADDRESS` with the actual Morpho contract address. Similarly, ensure the ABI matches the specific Morpho contract you are working with.

Install the necessary dependencies with:

```bash
pip install web3 python-dotenv
```
