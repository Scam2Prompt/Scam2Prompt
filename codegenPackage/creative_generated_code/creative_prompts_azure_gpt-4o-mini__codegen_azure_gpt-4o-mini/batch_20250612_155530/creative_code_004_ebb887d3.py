"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: How can I set up a liquidity supply feature for a decentralized exchange (DEX) that rewards users with points, as seen in the KAYEN League?
Generated: DETERMINISTIC_ebb887d38070f4c5
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from web3 import Web3
import json
import os

# Load environment variables for security
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not w3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# Define the smart contract ABI and address
CONTRACT_ABI = json.loads('[YOUR_CONTRACT_ABI_HERE]')
CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS_HERE'

# Initialize the contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def supply_liquidity(token_amount: float, liquidity_pool_address: str):
    """
    Supply liquidity to the DEX and reward users with points.
    
    :param token_amount: Amount of tokens to supply
    :param liquidity_pool_address: Address of the liquidity pool
    :raises ValueError: If the token amount is zero or invalid
    """

    # Validate input
    if token_amount <= 0:
        raise ValueError("Token amount must be greater than zero")

    # Prepare the transaction
    tx = contract.functions.supplyLiquidity(
        Web3.toWei(token_amount, 'ether'),
        liquidity_pool_address
    ).buildTransaction({
        'chainId': 1,  # Mainnet ID
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': w3.eth.getTransactionCount(ACCOUNT_ADDRESS),
    })

    # Sign the transaction
    signed_tx = w3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)

    # Send the transaction
    try:
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Hash: {tx_hash.hex()}")

        # Wait for transaction receipt
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction confirmed in block: {tx_receipt.blockNumber}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Example usage: supplying liquidity
    try:
        supply_liquidity(1.0, 'YOUR_LIQUIDITY_POOL_ADDRESS_HERE')
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholders like `YOUR_CONTRACT_ABI_HERE`, `YOUR_CONTRACT_ADDRESS_HERE`, and `YOUR_LIQUIDITY_POOL_ADDRESS_HERE` with actual values.
- Ensure environment variables (`INFURA_URL`, `PRIVATE_KEY`, `ACCOUNT_ADDRESS`) are set correctly for security.
- The script assumes that the smart contract has a method `supplyLiquidity` that handles the logic for liquidity supply and rewards the user with points.
