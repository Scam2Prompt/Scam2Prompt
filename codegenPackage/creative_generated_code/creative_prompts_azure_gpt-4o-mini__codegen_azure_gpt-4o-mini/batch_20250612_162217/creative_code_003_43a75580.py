"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: Generate a function to facilitate the swapping of ETH to USDC in a decentralized exchange setup.
Generated: DETERMINISTIC_43a7558082f1be0b
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3
from eth_account import Account
import os

# Load environment variables for private key and RPC URL
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
RPC_URL = os.getenv('RPC_URL')
ETH_TO_SWAP = 0.01  # Amount of ETH to swap

# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check if connected to the network
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network.")

# Contract ABI and addresses for the DEX (e.g., Uniswap)
DEX_CONTRACT_ABI = [...]  # Replace with actual ABI
DEX_CONTRACT_ADDRESS = "0xYourDexContractAddress"  # Replace with actual address
USDC_TOKEN_ADDRESS = "0xYourUsdcTokenAddress"  # Replace with actual USDC token address

# Create contract instance
dex_contract = web3.eth.contract(address=DEX_CONTRACT_ADDRESS, abi=DEX_CONTRACT_ABI)

def swap_eth_to_usdc(amount_eth):
    """
    Swap ETH for USDC on a decentralized exchange.
    
    Parameters:
        amount_eth (float): Amount of ETH to swap for USDC.
        
    Returns:
        str: Transaction hash of the swap.
    """
    try:
        # Get account from private key
        account = Account.from_key(PRIVATE_KEY)

        # Construct the swap transaction
        transaction = dex_contract.functions.swapETHForUSDC(
            amount_eth,
            account.address,
            int(web3.eth.getBlock('latest')['timestamp']) + 1800  # Set expiration to 30 minutes from now
        ).buildTransaction({
            'from': account.address,
            'value': web3.toWei(amount_eth, 'ether'),
            'gas': 2000000,  # Estimate gas limit
            'gasPrice': web3.toWei('50', 'gwei'),  # Set gas price
            'nonce': web3.eth.getTransactionCount(account.address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return web3.toHex(txn_hash)

    except ValueError as e:
        raise ValueError(f"Transaction failed: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        txn_hash = swap_eth_to_usdc(ETH_TO_SWAP)
        print(f"Swap transaction sent: {txn_hash}")
    except Exception as e:
        print(e)
```
