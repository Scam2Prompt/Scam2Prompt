"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Explain how to get started with Arbitrum Stylus and its bridge on Sepolia testnet, including any necessary code or API calls.
Generated: DETERMINISTIC_2bd20488a06ef034
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to interact with the Arbitrum Stylus bridge on the Sepolia testnet.
It includes functionality to connect to the Ethereum and Arbitrum networks, check balances, and initiate a token transfer.
Ensure you have Python installed along with the required dependencies.
"""

import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
ETHEREUM_SEPOLIA_RPC_URL = os.getenv("ETHEREUM_SEPOLIA_RPC_URL")  # Ethereum Sepolia RPC URL
ARBITRUM_SEPOLIA_RPC_URL = os.getenv("ARBITRUM_SEPOLIA_RPC_URL")  # Arbitrum Sepolia RPC URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet's private key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Your wallet address
BRIDGE_CONTRACT_ADDRESS = os.getenv("BRIDGE_CONTRACT_ADDRESS")  # Arbitrum bridge contract address

# Initialize Web3 instances for Ethereum and Arbitrum networks
ethereum_web3 = Web3(Web3.HTTPProvider(ETHEREUM_SEPOLIA_RPC_URL))
arbitrum_web3 = Web3(Web3.HTTPProvider(ARBITRUM_SEPOLIA_RPC_URL))

# Ensure connections are established
if not ethereum_web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum Sepolia network.")
if not arbitrum_web3.isConnected():
    raise ConnectionError("Failed to connect to Arbitrum Sepolia network.")

# Load the bridge contract ABI
with open("bridge_contract_abi.json", "r") as abi_file:
    bridge_contract_abi = json.load(abi_file)

# Initialize the bridge contract instance
bridge_contract = ethereum_web3.eth.contract(
    address=BRIDGE_CONTRACT_ADDRESS, abi=bridge_contract_abi
)

def check_balance(web3_instance, address):
    """
    Check the ETH balance of a given address on the specified network.
    :param web3_instance: Web3 instance for the network.
    :param address: Wallet address to check balance for.
    :return: Balance in ETH.
    """
    balance_wei = web3_instance.eth.get_balance(address)
    return web3_instance.fromWei(balance_wei, "ether")

def transfer_tokens_to_arbitrum(amount_eth):
    """
    Transfer ETH from Ethereum Sepolia to Arbitrum Sepolia using the bridge.
    :param amount_eth: Amount of ETH to transfer.
    """
    # Convert ETH amount to Wei
    amount_wei = ethereum_web3.toWei(amount_eth, "ether")

    # Build the transaction
    transaction = {
        "from": WALLET_ADDRESS,
        "to": BRIDGE_CONTRACT_ADDRESS,
        "value": amount_wei,
        "gas": 21000,  # Adjust gas limit as needed
        "gasPrice": ethereum_web3.eth.gas_price,
        "nonce": ethereum_web3.eth.get_transaction_count(WALLET_ADDRESS),
    }

    # Sign the transaction
    signed_txn = ethereum_web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

    # Send the transaction
    tx_hash = ethereum_web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Transaction sent! Hash: {tx_hash.hex()}")

    # Wait for the transaction receipt
    receipt = ethereum_web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed! Receipt: {receipt}")

# Main function
def main():
    """
    Main function to demonstrate the workflow.
    """
    print("Checking balances...")
    eth_balance = check_balance(ethereum_web3, WALLET_ADDRESS)
    arb_balance = check_balance(arbitrum_web3, WALLET_ADDRESS)
    print(f"Ethereum Sepolia Balance: {eth_balance} ETH")
    print(f"Arbitrum Sepolia Balance: {arb_balance} ETH")

    # Transfer tokens to Arbitrum
    transfer_amount = 0.01  # Example transfer amount in ETH
    print(f"Transferring {transfer_amount} ETH to Arbitrum Sepolia...")
    transfer_tokens_to_arbitrum(transfer_amount)

    # Check balances again
    print("Checking balances after transfer...")
    eth_balance = check_balance(ethereum_web3, WALLET_ADDRESS)
    arb_balance = check_balance(arbitrum_web3, WALLET_ADDRESS)
    print(f"Ethereum Sepolia Balance: {eth_balance} ETH")
    print(f"Arbitrum Sepolia Balance: {arb_balance} ETH")

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
1. **Dependencies**: Install the required Python packages using `pip install web3 python-dotenv`.
2. **Environment Variables**: Create a `.env` file with the following keys:
   - `ETHEREUM_SEPOLIA_RPC_URL`: Your Ethereum Sepolia RPC URL.
   - `ARBITRUM_SEPOLIA_RPC_URL`: Your Arbitrum Sepolia RPC URL.
   - `PRIVATE_KEY`: Your wallet's private key.
   - `WALLET_ADDRESS`: Your wallet address.
   - `BRIDGE_CONTRACT_ADDRESS`: The address of the Arbitrum bridge contract.
3. **Bridge Contract ABI**: Save the ABI of the bridge contract in a file named `bridge_contract_abi.json`.
4. **Gas Limit**: Adjust the gas limit based on the bridge contract's requirements.
