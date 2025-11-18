"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Generate a Python script using Web3.py to interact with a staking pool on the Linea network, including functionality to connect a wallet, view staked tokens, and claim rewards.
Generated: DETERMINISTIC_e27f3d0957171d1b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
LINEA_RPC_URL = os.getenv("LINEA_RPC_URL")  # RPC URL for the Linea network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")     # Wallet private key (Keep secure!)
STAKING_CONTRACT_ADDRESS = os.getenv("STAKING_CONTRACT_ADDRESS")  # Address of the staking pool contract
ABI_PATH = "staking_pool_abi.json"  # Path to the ABI file of the staking contract

# Ensure required environment variables are set
if not LINEA_RPC_URL or not PRIVATE_KEY or not STAKING_CONTRACT_ADDRESS:
    raise EnvironmentError("Missing required environment variables.")

# Connect to the Linea network
web3 = Web3(Web3.HTTPProvider(LINEA_RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Linea network.")

# Load staking contract ABI
try:
    with open(ABI_PATH, "r") as abi_file:
        staking_contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at '{ABI_PATH}'.")

# Initialize the staking contract
staking_contract = web3.eth.contract(
    address=Web3.to_checksum_address(STAKING_CONTRACT_ADDRESS),
    abi=staking_contract_abi,
)

# Initialize wallet account
account = Account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Function to get staked tokens for the connected wallet
def get_staked_tokens():
    try:
        staked_balance = staking_contract.functions.getStakedBalance(wallet_address).call()
        print(f"Staked tokens for {wallet_address}: {staked_balance}")
        return staked_balance
    except Exception as e:
        print(f"Error fetching staked tokens: {e}")
        return None

# Function to claim rewards
def claim_rewards():
    try:
        # Build transaction
        tx = staking_contract.functions.claimRewards().buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 300000,  # Adjust gas limit based on contract complexity
            'gasPrice': web3.eth.gas_price,
        })

        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Claim rewards transaction sent! TX Hash: {web3.to_hex(tx_hash)}")

        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Transaction confirmed:", receipt)
        return receipt
    except Exception as e:
        print(f"Error claiming rewards: {e}")
        return None

# Main function to interact with the staking pool
def main():
    print(f"Connected to Linea network. Wallet address: {wallet_address}")
    
    choice = input("Enter 1 to view staked tokens, or 2 to claim rewards: ")
    if choice == '1':
        get_staked_tokens()
    elif choice == '2':
        claim_rewards()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `staking_pool_abi.json` with the actual ABI file for your staking pool contract.
- Ensure the `.env` file contains `LINEA_RPC_URL`, `PRIVATE_KEY`, and `STAKING_CONTRACT_ADDRESS`.
- Handle private keys securely. Do not hard-code them or share them publicly. Ensure proper security practices are followed in production environments.
