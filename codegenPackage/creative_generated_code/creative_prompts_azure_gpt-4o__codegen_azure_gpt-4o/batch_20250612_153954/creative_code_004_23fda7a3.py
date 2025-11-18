"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axgt-sushi.lat
Prompt: Write a script to automate the process of swapping tokens on SushiSwap, including support for limit orders as described in the content.
Generated: DETERMINISTIC_23fda7a3fe908ab0
Batch ID: 20250612_153954
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/simple/price": {
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
# sushi_swap_bot.py

import json
import time
import requests
from web3 import Web3
from decimal import Decimal

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your wallet's private key
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
SUSHISWAP_ROUTER_ADDRESS = "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"  # SushiSwap Router address
SUSHISWAP_ROUTER_ABI = "path_to_sushiswap_router_abi.json"  # Replace with the local path to SushiSwap Router ABI
GAS_LIMIT = 200000  # Standard gas limit for swapping
GAS_PRICE = Web3.toWei("20", "gwei")  # Replace with desired gas price

# Web3 initialization
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise Exception("Unable to connect to Ethereum network via Infura")

# Load SushiSwap Router contract
with open(SUSHISWAP_ROUTER_ABI, "r") as abi_file:
    router_abi = json.load(abi_file)
router_contract = web3.eth.contract(address=SUSHISWAP_ROUTER_ADDRESS, abi=router_abi)

# Helper function to check allowance
def check_allowance(token_address, owner_address, spender_address):
    token_abi = '[{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'  # ERC20 ABI for allowance
    token_contract = web3.eth.contract(address=token_address, abi=json.loads(token_abi))
    return token_contract.functions.allowance(owner_address, spender_address).call()

# Helper function to approve tokens
def approve_token(token_address, spender_address, amount):
    token_abi = '[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # ERC20 ABI for approve
    token_contract = web3.eth.contract(address=token_address, abi=json.loads(token_abi))
    txn = token_contract.functions.approve(spender_address, amount).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)

# Function to swap tokens
def swap_tokens(token_in, token_out, amount_in, amount_out_min, deadline):
    # Check allowance and approve if necessary
    allowance = check_allowance(token_in, WALLET_ADDRESS, SUSHISWAP_ROUTER_ADDRESS)
    if allowance < amount_in:
        print(f"Approving {amount_in} tokens...")
        approve_token(token_in, SUSHISWAP_ROUTER_ADDRESS, amount_in)
    
    # Build transaction
    txn = router_contract.functions.swapExactTokensForTokens(
        amount_in,
        amount_out_min,
        [token_in, token_out],
        WALLET_ADDRESS,
        deadline
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })

    # Sign transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)

# Utility to set up limit orders
def limit_order(token_in, token_out, amount_in, target_price, timeout_minutes):
    print(f"Setting up limit order: {amount_in} {token_in} -> {token_out} at target price {target_price}")
    start_time = time.time()
    while time.time() - start_time < timeout_minutes * 60:
        # Fetch price data (using a public API for simplicity, replace with a robust price oracle in production)
        response = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": token_in, "vs_currencies": token_out})
        response_data = response.json()
        current_price = Decimal(response_data[token_in][token_out])
        
        print(f"Current price for {token_in} -> {token_out}: {current_price}")
        if current_price >= Decimal(target_price):
            deadline = int(time.time()) + 300  # 5 minutes from now
            tx_hash = swap_tokens(token_in, token_out, amount_in, 0, deadline)
            print(f"Limit order executed! Transaction hash: {tx_hash}")
            return tx_hash
        
        time.sleep(10)  # Check price every 10 seconds
    
    print("Limit order expired")
    return None

# Example usage (replace token addresses, amounts, and target price as needed)
if __name__ == "__main__":
    TOKEN_IN = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48"  # USDC
    TOKEN_OUT = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # DAI
    AMOUNT_IN = Web3.toWei(100, "ether")  # Example: 100 USDC
    TARGET_PRICE = "0.999"  # Target price for the swap
    TIMEOUT_MINUTES = 10  # Limit order timeout

    limit_order(TOKEN_IN, TOKEN_OUT, AMOUNT_IN, TARGET_PRICE, TIMEOUT_MINUTES)
```
