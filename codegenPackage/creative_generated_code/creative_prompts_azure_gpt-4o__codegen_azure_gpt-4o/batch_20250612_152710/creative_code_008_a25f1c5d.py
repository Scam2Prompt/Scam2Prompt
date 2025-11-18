"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malikbashira.blogspot.com
Prompt: Create a script to automate the process of adding liquidity for ARB tokens on Pancakeswap using the contract address `0x267AF7E2d7A42E33A21454Ac59548F3e66788605`.
Generated: DETERMINISTIC_a25f1c5d684ed6c6
Batch ID: 20250612_152710
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

Here is the clean, well-documented, production-ready Python script using Web3.py to automate the process of adding liquidity for ARB tokens on PancakeSwap.

```python
import json
from web3 import Web3
from eth_account import Account
from decimal import Decimal

# Configuration
INFURA_URL = "https://bsc-dataseed.binance.org/"  # Replace with your Binance Smart Chain RPC endpoint
PRIVATE_KEY = "your-private-key-here"  # Replace with your wallet's private key
WALLET_ADDRESS = "your-wallet-address-here"  # Replace with your wallet address
PANCAKESWAP_ROUTER = "0x10ED43C718714eb63d5aA57B78B54704E256024E"  # PancakeSwap Router V2
ARB_TOKEN_ADDRESS = "0x267AF7E2d7A42E33A21454Ac59548F3e66788605"  # ARB Token Address
WBNB_ADDRESS = "0xBB4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"  # Wrapped BNB Address

# Constants
GAS_PRICE = Web3.toWei("5", "gwei")  # Adjust based on current network conditions
GAS_LIMIT = 300000  # Estimated gas limit for the transaction

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Binance Smart Chain RPC endpoint.")

# Load the Router ABI
with open("pancakeswap_router_abi.json", "r") as f:  # PancakeSwap Router ABI required
    pancakeswap_router_abi = json.load(f)

# Create Router contract instance
router_contract = web3.eth.contract(address=PANCAKESWAP_ROUTER, abi=pancakeswap_router_abi)

# Helper function to calculate slippage
def calculate_slippage(amount: int, slippage_percentage: float) -> int:
    """
    Calculate the acceptable slippage amount.
    :param amount: Original token amount.
    :param slippage_percentage: Slippage percentage (e.g., 1.0 for 1%).
    :return: Adjusted token amount after slippage.
    """
    return int(amount * (1 - slippage_percentage / 100))

# Helper function to approve token spending
def approve_token(token_address, spender, amount):
    """
    Approve a spender to use tokens on behalf of the wallet address.
    :param token_address: The contract address of the token to approve.
    :param spender: The contract address of the spender (router in this case).
    :param amount: The amount of tokens to approve.
    """
    erc20_abi = json.loads('[...]')  # Replace with ERC20 ABI
    token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)

    tx = token_contract.functions.approve(spender, amount).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": nonce
    })

    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Approve transaction sent, TX hash: {web3.toHex(tx_hash)}")
    web3.eth.wait_for_transaction_receipt(tx_hash)

# Add liquidity to PancakeSwap
def add_liquidity(amount_arb, amount_bnb, slippage_percentage):
    """
    Add liquidity for ARB tokens on PancakeSwap.
    :param amount_arb: Amount of ARB tokens to provide.
    :param amount_bnb: Amount of BNB to provide.
    :param slippage_percentage: Acceptable slippage in percentage (e.g., 1 for 1%).
    """
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    amount_arb_min = calculate_slippage(amount_arb, slippage_percentage)
    amount_bnb_min = calculate_slippage(amount_bnb, slippage_percentage)
    deadline = int(web3.eth.get_block("latest")["timestamp"]) + 300  # Transaction deadline (5 minutes)

    tx = router_contract.functions.addLiquidityETH(
        ARB_TOKEN_ADDRESS,
        amount_arb,
        amount_arb_min,
        amount_bnb_min,
        WALLET_ADDRESS,
        deadline
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "value": amount_bnb,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": nonce
    })

    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Add liquidity transaction sent, TX hash: {web3.toHex(tx_hash)}")
    web3.eth.wait_for_transaction_receipt(tx_hash)

if __name__ == "__main__":
    # Example usage
    arb_amount = Web3.toWei("10", "ether")  # Replace with desired ARB token amount
    bnb_amount = Web3.toWei("0.1", "ether")  # Replace with desired BNB amount
    slippage = 1.0  # Slippage tolerance percentage

    # Approving ARB tokens for PancakeSwap Router
    approve_token(ARB_TOKEN_ADDRESS, PANCAKESWAP_ROUTER, arb_amount)

    # Adding liquidity
    add_liquidity(arb_amount, bnb_amount, slippage)
```

**Notes:**
1. Replace `"your-private-key-here"` and `"your-wallet-address-here"` with the actual values from your wallet.
2. Ensure `pancakeswap_router_abi.json` contains the proper PancakeSwap Router ABI file, and provide the ERC20 ABI as necessary in the script.
3. Test the script on the Binance Smart Chain testnet before deploying it to production.
4. Keep your private key secure and never expose it in a public repository.
