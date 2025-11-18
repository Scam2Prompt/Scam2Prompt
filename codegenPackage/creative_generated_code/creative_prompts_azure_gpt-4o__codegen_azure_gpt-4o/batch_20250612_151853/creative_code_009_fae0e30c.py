"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-feat-optimism-subgraph-venus-protocol.vercel.app
Prompt: Generate a code example for integrating the Venus Protocol with Optimism, focusing on reducing transaction costs for DeFi operations.
Generated: DETERMINISTIC_fae0e30c27c67126
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integrate the Venus Protocol with Optimism, focusing on reducing transaction costs for DeFi operations.
The code uses Web3.py for Ethereum interaction and optimizes gas usage for transactions.
Ensure you have installed the required dependencies: `web3`, `dotenv`, `eth-account`.

"""

import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize variables from environment
OPTIMISM_RPC_URL = os.getenv("OPTIMISM_RPC_URL")  # Optimism RPC Endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address

# Venus Protocol contract details
# Replace with actual Venus contract addresses and ABIs
VENUS_COMPTROLLER_ADDRESS = "0x5eAe89DC1C671724A672ff0630122ee834098657"
VENUS_COMPTROLLER_ABI = [
    # Minimal ABI for demonstration; add full ABI for production use
    {
        "constant": True,
        "inputs": [],
        "name": "getAllMarkets",
        "outputs": [{"name": "", "type": "address[]"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]

VENUS_TOKEN_ADDRESS = "0xB6e5F0f58A572Edf61A4f3A2D51509a52ED78e13"
VENUS_TOKEN_ABI = [
    {
        "constant": False,
        "inputs": [{"name": "redeemAmount", "type": "uint256"}],
        "name": "redeemUnderlying",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    }
]

# Connect to Optimism
web3 = Web3(Web3.HTTPProvider(OPTIMISM_RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # For Optimism's PoA consensus

# Ensure connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Optimism RPC")

# Compile helper functions
def get_nonce(address):
    """Fetch the current nonce for the wallet."""
    return web3.eth.get_transaction_count(address)

def sign_and_send_transaction(transaction):
    """Sign and send a transaction."""
    try:
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.toHex(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Transaction failed: {str(e)}")

# Venus Comptroller Contract Instance
venus_comptroller = web3.eth.contract(address=VENUS_COMPTROLLER_ADDRESS, abi=VENUS_COMPTROLLER_ABI)

# Venus Token Contract Instance
venus_token = web3.eth.contract(address=VENUS_TOKEN_ADDRESS, abi=VENUS_TOKEN_ABI)

def redeem_underlying(amount):
    """
    Redeem a specific amount of underlying tokens from Venus Protocol.
    Uses Optimism to reduce transaction costs.
    """
    # Prepare transaction details
    nonce = get_nonce(WALLET_ADDRESS)
    function_call = venus_token.functions.redeemUnderlying(amount).build_transaction({
        "chainId": 10,  # Optimism chain ID
        "gas": 200000,  # Estimated gas limit
        "gasPrice": web3.eth.gas_price,  # Current gas price
        "nonce": nonce,
    })

    # Sign and send the transaction
    tx_hash = sign_and_send_transaction(function_call)
    return tx_hash

def get_all_markets():
    """
    Fetch all markets from the Venus Comptroller contract.
    """
    try:
        return venus_comptroller.functions.getAllMarkets().call()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch markets: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        print("Fetching all Venus markets...")
        markets = get_all_markets()
        print(f"Markets: {markets}")

        print("Redeeming underlying tokens...")
        redeem_amount = web3.toWei(0.1, "ether")  # Example: 0.1 ETH worth of tokens
        tx_hash = redeem_underlying(redeem_amount)
        print(f"Transaction successfully sent: {tx_hash}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
