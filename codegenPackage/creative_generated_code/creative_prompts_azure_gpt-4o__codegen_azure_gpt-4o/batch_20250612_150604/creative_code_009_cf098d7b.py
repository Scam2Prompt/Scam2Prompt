"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penpie.io
Prompt: Provide a script to swap mPENDLE tokens back to PENDLE on PancakeSwap and calculate the exchange rate based on current market conditions.
Generated: DETERMINISTIC_cf098d7b1e80b1c3
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from decimal import Decimal
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Environment variables
RPC_URL = os.getenv("RPC_URL")  # Your blockchain node URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address
PANCAKESWAP_ROUTER_ADDRESS = os.getenv("PANCAKESWAP_ROUTER_ADDRESS")  # PancakeSwap Router address
MPENDLE_ADDRESS = os.getenv("MPENDLE_ADDRESS")  # mPENDLE token address
PENDLE_ADDRESS = os.getenv("PENDLE_ADDRESS")  # PENDLE token address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise Exception("Failed to connect to the blockchain node.")

# Load PancakeSwap Router ABI
# Assume the ABI is stored locally in a JSON file named 'pancakeswap_router_abi.json'
with open('pancakeswap_router_abi.json', 'r') as abi_file:
    PANCAKESWAP_ROUTER_ABI = json.load(abi_file)

# Initialize contract instances
router_contract = web3.eth.contract(address=web3.toChecksumAddress(PANCAKESWAP_ROUTER_ADDRESS), abi=PANCAKESWAP_ROUTER_ABI)
mPENDLE_contract = web3.eth.contract(address=web3.toChecksumAddress(MPENDLE_ADDRESS), abi=json.loads('[...]'))  # Replace [...] with mPENDLE ABI
PENDLE_contract = web3.eth.contract(address=web3.toChecksumAddress(PENDLE_ADDRESS), abi=json.loads('[...]'))  # Replace [...] with PENDLE ABI

# Function to swap mPENDLE for PENDLE
def swap_mPENDLE_to_PENDLE(amount_in):
    """
    Perform a token swap from mPENDLE to PENDLE using PancakeSwap.

    :param amount_in: Amount of mPENDLE to swap (in wei).
    :return: Transaction hash if successful.
    """
    try:
        # Fetch current gas price
        gas_price = web3.eth.gas_price

        # Calculate minimum amount out (1% slippage tolerance)
        amounts_out = router_contract.functions.getAmountsOut(amount_in, [MPENDLE_ADDRESS, PENDLE_ADDRESS]).call()
        amount_out_min = int(Decimal(amounts_out[1]) * Decimal('0.99'))

        # Build transaction
        tx = router_contract.functions.swapExactTokensForTokens(
            amount_in,
            amount_out_min,
            [MPENDLE_ADDRESS, PENDLE_ADDRESS],
            WALLET_ADDRESS,
            int(web3.eth.getBlock('latest')['timestamp']) + 600  # Set deadline to 10 minutes
        ).buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': 200000,  # Estimated gas limit
            'gasPrice': gas_price,
            'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
        })

        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return tx_hash.hex()

    except Exception as e:
        print(f"Error during swap: {str(e)}")
        return None

# Function to calculate exchange rate
def get_exchange_rate():
    """
    Calculate the current exchange rate between mPENDLE and PENDLE.

    :return: Exchange rate (PENDLE per mPENDLE).
    """
    try:
        amounts_out = router_contract.functions.getAmountsOut(
            web3.toWei(1, 'ether'), [MPENDLE_ADDRESS, PENDLE_ADDRESS]
        ).call()
        rate = Decimal(amounts_out[1]) / Decimal(web3.toWei(1, 'ether'))
        return rate
    except Exception as e:
        print(f"Error fetching exchange rate: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Example: Swap 10 mPENDLE
    mPENDLE_amount = web3.toWei(10, 'ether')  # Replace 10 with the desired amount
    tx_hash = swap_mPENDLE_to_PENDLE(mPENDLE_amount)

    if tx_hash:
        print(f"Swap successful! Transaction hash: {tx_hash}")
    else:
        print("Swap failed.")

    # Fetch and display exchange rate
    exchange_rate = get_exchange_rate()

    if exchange_rate:
        print(f"Current exchange rate: 1 mPENDLE = {exchange_rate} PENDLE")
    else:
        print("Failed to fetch exchange rate.")
```

### Notes:
1. Replace the `[...]` placeholders with the ABI for the respective tokens.
2. Ensure you have the proper `.env` file setup with the required values.
3. The code assumes you have permissions to spend mPENDLE from your wallet. If not, an `approve` step is required before swapping.
4. Make sure the `pancakeswap_router_abi.json` file is located in the same directory as the script, or adjust the path accordingly.
