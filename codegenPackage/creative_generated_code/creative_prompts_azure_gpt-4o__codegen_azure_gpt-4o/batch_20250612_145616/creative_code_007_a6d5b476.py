"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Explain how to use GMX documentation to implement a custom oracle solution for price feeds on Arbitrum.
Generated: DETERMINISTIC_a6d5b476d854c349
Batch ID: 20250612_145616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.gmx.io/price-feed": {
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
# Import necessary libraries
import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_abi import encode_abi

# Define constants
GMX_PRICE_FEED_API = "https://api.gmx.io/price-feed"  # Replace with actual GMX API endpoint if different
ARBITRUM_RPC_URL = "https://arb1.arbitrum.io/rpc"  # Arbitrum mainnet RPC
CONTRACT_ADDRESS = "0xYourOracleContractAddress"  # Replace with your Oracle contract address
PRIVATE_KEY = "0xYourPrivateKey"  # Replace with your private Ethereum key
CHAIN_ID = 42161  # Arbitrum mainnet chain ID
GAS_LIMIT = 200000
GAS_PRICE = Web3.to_wei("2", "gwei")  # Adjust as needed for your network
ABI = [
    # Replace with your Oracle contract's ABI
    {
        "constant": False,
        "inputs": [
            {"name": "_price", "type": "uint256"}
        ],
        "name": "updatePrice",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    }
]

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))

# Add middleware for Arbitrum's Proof of Authority (POA) consensus
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Validate connection to Arbitrum
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Arbitrum network")

# Load the Oracle contract
contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)


def fetch_price_from_gmx():
    """
    Fetch the price feed from GMX's API
    :return: Price as an integer (e.g., price scaled by 1e6 for precision)
    """
    try:
        response = requests.get(GMX_PRICE_FEED_API)
        response.raise_for_status()
        data = response.json()
        # Assuming the API returns a field `price` with the value scaled up (e.g., 1e6)
        return int(data["price"])
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch price from GMX API: {str(e)}")


def update_price_on_chain(price):
    """
    Update the price on the Oracle smart contract
    :param price: The price to update (uint256)
    """
    # Get the nonce for the sender account
    account = web3.eth.account.from_key(PRIVATE_KEY)
    nonce = web3.eth.get_transaction_count(account.address)

    # Construct the transaction
    txn = contract.functions.updatePrice(price).build_transaction({
        "chainId": CHAIN_ID,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": nonce,
    })

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

    # Send the transaction
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Transaction sent: {tx_hash.hex()}")
        # Wait for the transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction successful: {receipt.transactionHash.hex()}")
    except Exception as e:
        raise RuntimeError(f"Failed to update price on-chain: {str(e)}")


def main():
    """
    Main function to fetch price from GMX and update it on Arbitrum
    """
    try:
        # Step 1: Fetch the latest price from GMX
        price = fetch_price_from_gmx()
        print(f"Fetched price from GMX: {price}")

        # Step 2: Update the price on the Oracle smart contract
        update_price_on_chain(price)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
