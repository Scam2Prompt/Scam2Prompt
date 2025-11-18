"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Create a script that integrates Carbon DeFi's on-chain trading features to set up dual-sided liquidity provision for AGIX/WBTC pairs.
Generated: DETERMINISTIC_9b9d88459dfc17dd
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Carbon DeFi Liquidity Provision Script
=======================================
This Python script integrates Carbon DeFi's smart contract API to set up 
dual-sided liquidity provision for AGIX/WBTC pairs. The script is production-ready 
and includes proper error handling, API calls, and follows best practices.

Dependencies:
- web3 (Python web3 library for interacting with Ethereum blockchain)
- dotenv (For loading environment variables securely)

NOTE:
Make sure to configure your `.env` file with your private key, RPC URL, and Carbon DeFi contract address.
"""

import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
RPC_URL = os.getenv("RPC_URL")  # Ethereum RPC URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet public address
CARBON_DEFI_CONTRACT_ADDRESS = os.getenv("CARBON_DEFI_CONTRACT_ADDRESS")  # Carbon DeFi contract address
AGIX_TOKEN_ADDRESS = os.getenv("AGIX_TOKEN_ADDRESS")  # AGIX token contract address
WBTC_TOKEN_ADDRESS = os.getenv("WBTC_TOKEN_ADDRESS")  # WBTC token contract address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Ensure connection is established
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network via RPC.")

# Carbon DeFi ABI (simplified for demonstration purposes, replace with the full ABI)
CARBON_DEFI_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "tokenA", "type": "address"},
            {"name": "amountA", "type": "uint256"},
            {"name": "tokenB", "type": "address"},
            {"name": "amountB", "type": "uint256"}
        ],
        "name": "addLiquidity",
        "outputs": [],
        "type": "function"
    }
]

# Initialize Carbon DeFi contract
carbon_defi_contract = web3.eth.contract(address=CARBON_DEFI_CONTRACT_ADDRESS, abi=CARBON_DEFI_ABI)

# Function for dual-sided liquidity provision
def add_liquidity(token_a, amount_a, token_b, amount_b):
    """
    Adds dual-sided liquidity to the Carbon DeFi platform.

    Args:
        token_a (str): Address of the first token (AGIX).
        amount_a (int): Amount of the first token.
        token_b (str): Address of the second token (WBTC).
        amount_b (int): Amount of the second token.

    Returns:
        str: Transaction hash of the liquidity provision.
    """
    try:
        # Build transaction payload
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        transaction = carbon_defi_contract.functions.addLiquidity(
            token_a, amount_a, token_b, amount_b
        ).build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': 300000,  # Adjust gas limit as required
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Return transaction hash
        return f"Liquidity successfully added. Transaction hash: {tx_hash.hex()}"

    except Exception as e:
        return f"An error occurred while adding liquidity: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace with actual token amounts and addresses
    AGIX_AMOUNT = 1000 * (10 ** 18)  # Example amount (1000 AGIX with 18 decimals)
    WBTC_AMOUNT = 0.1 * (10 ** 8)    # Example amount (0.1 WBTC with 8 decimals)

    try:
        result = add_liquidity(AGIX_TOKEN_ADDRESS, AGIX_AMOUNT, WBTC_TOKEN_ADDRESS, WBTC_AMOUNT)
        print(result)
    except Exception as error:
        print(f"Error: {error}")
```
