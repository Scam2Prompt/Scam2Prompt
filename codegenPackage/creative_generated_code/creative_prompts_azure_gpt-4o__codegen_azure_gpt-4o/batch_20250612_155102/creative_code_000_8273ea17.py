"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonx.xyz
Prompt: Write a Python script to interact with the SafeMoonX token on Binance Smart Chain (BSC), including functions for checking token balance and executing trades using PancakeSwap.
Generated: DETERMINISTIC_8273ea17ae41afa1
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from decimal import Decimal
from eth_account import Account

# Configuration constants
NODE_URL = "https://bsc-dataseed.binance.org/"  # Binance Smart Chain public node
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Wallet's private key
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Wallet address
SAFE_MOONX_CONTRACT_ADDRESS = "0xYourSafeMoonXContractAddress"  # Replace with SafeMoonX token address
PANCAKESWAP_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"  # PancakeSwap Router V2 Address

# Load the ABI for SafeMoonX and PancakeSwap Router (replace with actual ABIs if needed)
SAFE_MOONX_ABI = json.loads('[...]')  # Replace with SafeMoonX ABI
PANCAKESWAP_ROUTER_ABI = json.loads('[...]')  # Replace with PancakeSwap Router ABI

# Connect to Web3
web3 = Web3(Web3.HTTPProvider(NODE_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to Binance Smart Chain")

# Initialize contracts
safe_moonx_contract = web3.eth.contract(address=web3.toChecksumAddress(SAFE_MOONX_CONTRACT_ADDRESS), abi=SAFE_MOONX_ABI)
pancakeswap_router = web3.eth.contract(address=web3.toChecksumAddress(PANCAKESWAP_ROUTER_ADDRESS), abi=PANCAKESWAP_ROUTER_ABI)

# Utility function to convert private key into an account
account = Account.from_key(PRIVATE_KEY)

# Function to check SafeMoonX token balance
def get_token_balance(wallet_address):
    """
    Get the balance of SafeMoonX tokens for a given wallet address.

    :param wallet_address: Address of the wallet to check balance for.
    :return: Token balance as a Decimal value.
    """
    try:
        balance = safe_moonx_contract.functions.balanceOf(web3.toChecksumAddress(wallet_address)).call()
        decimals = safe_moonx_contract.functions.decimals().call()
        return Decimal(balance) / (10 ** decimals)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch token balance: {str(e)}")

# Function to execute a trade on PancakeSwap (buy or sell SafeMoonX)
def execute_trade(token_in, token_out, amount_in, slippage=0.005):
    """
    Execute a trade on PancakeSwap using SafeMoonX.

    :param token_in: Address of the token to trade (input token).
    :param token_out: Address of the token to receive (output token).
    :param amount_in: Amount of input token to trade (in smallest units).
    :param slippage: Slippage tolerance for the trade (default is 0.5%).
    :return: Transaction hash if successful.
    """
    try:
        # Get amounts out with slippage tolerance
        amounts_out = pancakeswap_router.functions.getAmountsOut(amount_in, [token_in, token_out]).call()
        amount_out_min = int(amounts_out[1] * (1 - slippage))

        # Build the transaction
        nonce = web3.eth.getTransactionCount(account.address)
        gas_price = web3.eth.gas_price
        tx = pancakeswap_router.functions.swapExactTokensForTokens(
            amount_in,
            amount_out_min,
            [web3.toChecksumAddress(token_in), web3.toChecksumAddress(token_out)],
            account.address,
            int(web3.eth.get_block('latest')['timestamp']) + 600  # Transaction expires in 10 minutes
        ).buildTransaction({
            'from': account.address,
            'gas': 200000,
            'gasPrice': gas_price,
            'nonce': nonce,
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.toHex(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Failed to execute trade: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Fetch SafeMoonX token balance
        balance = get_token_balance(WALLET_ADDRESS)
        print(f"SafeMoonX Balance: {balance}")

        # Execute a trade (replace token addresses and amounts as appropriate)
        # Example: Buy SafeMoonX using BNB
        BNB_ADDRESS = "0x0000000000000000000000000000000000000000"  # Replace with actual BNB address
        AMOUNT_IN = web3.toWei(0.1, 'ether')  # Amount of BNB to spend
        tx_hash = execute_trade(BNB_ADDRESS, SAFE_MOONX_CONTRACT_ADDRESS, AMOUNT_IN)
        print(f"Trade executed successfully, transaction hash: {tx_hash}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
