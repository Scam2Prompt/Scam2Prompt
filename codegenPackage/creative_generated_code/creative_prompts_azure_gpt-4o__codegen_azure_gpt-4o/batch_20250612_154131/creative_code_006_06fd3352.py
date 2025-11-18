"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap---x.fi
Prompt: Generate a tutorial for using Orbs' dTWAP protocol on SwapX to execute time-weighted average price orders for token swaps.
Generated: DETERMINISTIC_06fd335256052a62
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, and production-ready example tutorial for using Orbs' dTWAP protocol via SwapX to execute time-weighted average price token swaps. The code is written in Python and assumes interaction with a blockchain through Web3.py.

```python
"""
Tutorial: Using Orbs' dTWAP Protocol on SwapX for Token Swaps

This script demonstrates how to execute a time-weighted average price (TWAP)
order using Orbs' dTWAP protocol on SwapX. The code assumes familiarity 
with Web3.py and Ethereum-based smart contract interactions.

Requirements:
- Python 3.x
- Web3.py library installed
- Access to an Ethereum node or provider (e.g., Infura or Alchemy)
- Wallet private key and address with sufficient funds

Note: Replace placeholders with actual contract addresses, ABI files, and token details.
"""

from web3 import Web3
import json

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura URL
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your wallet private key
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
DTWAP_CONTRACT_ADDRESS = "DTWAP_CONTRACT_ADDRESS"  # Replace with the dTWAP contract address
DTWAP_CONTRACT_ABI_PATH = "path/to/dtwap_abi.json"  # Replace with the path to the dTWAP ABI JSON file
SWAPX_ROUTER_ADDRESS = "SWAPX_ROUTER_ADDRESS"  # Replace with the SwapX router contract address
TOKEN_IN_ADDRESS = "TOKEN_IN_CONTRACT_ADDRESS"  # Replace with the token you want to swap
TOKEN_OUT_ADDRESS = "TOKEN_OUT_CONTRACT_ADDRESS"  # Replace with the token you want to receive

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection to the Ethereum network
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network via Infura.")

# Load dTWAP contract ABI
with open(DTWAP_CONTRACT_ABI_PATH, 'r') as abi_file:
    dtwap_abi = json.load(abi_file)

# Initialize dTWAP contract
dtwap_contract = web3.eth.contract(address=DTWAP_CONTRACT_ADDRESS, abi=dtwap_abi)

# Helper function to sign and send transactions
def send_signed_transaction(transaction):
    """
    Signs and sends a transaction to the Ethereum network.

    Args:
        transaction (dict): The transaction object to be signed and sent.

    Returns:
        str: The transaction hash (tx_hash).
    """
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)

# Define TWAP order parameters
twap_parameters = {
    "token_in": web3.toChecksumAddress(TOKEN_IN_ADDRESS),
    "token_out": web3.toChecksumAddress(TOKEN_OUT_ADDRESS),
    "amount_in_total": web3.toWei(10, "ether"),  # Total amount to swap (e.g., 10 TOKEN_IN)
    "num_intervals": 5,  # Number of intervals for TWAP execution
    "interval_seconds": 60,  # Interval duration in seconds
    "swap_router_address": web3.toChecksumAddress(SWAPX_ROUTER_ADDRESS)
}

# Build dTWAP order transaction
try:
    # Create the transaction object
    tx = dtwap_contract.functions.createTWAPOrder(
        twap_parameters["token_in"],
        twap_parameters["token_out"],
        twap_parameters["amount_in_total"],
        twap_parameters["num_intervals"],
        twap_parameters["interval_seconds"],
        twap_parameters["swap_router_address"]
    ).buildTransaction({
        "chainId": 1,  # Mainnet
        "gas": 300000,  # Gas limit (adjust based on estimation)
        "gasPrice": web3.toWei(30, "gwei"),  # Gas price
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS)
    })

    # Sign and send the transaction
    tx_hash = send_signed_transaction(tx)
    print(f"TWAP order created successfully! Transaction hash: {tx_hash}")

except Exception as e:
    print(f"An error occurred while creating the TWAP order: {e}")
```

Before running this script, ensure you've replaced all placeholders with real values (e.g., contract addresses, wallet details, ABI file paths). Additionally, confirm that your wallet has sufficient ETH for gas fees and the token to be swapped.
