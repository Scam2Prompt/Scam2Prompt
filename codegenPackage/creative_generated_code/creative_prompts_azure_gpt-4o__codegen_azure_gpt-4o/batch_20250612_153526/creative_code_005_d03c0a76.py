"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackder.pages.dev
Prompt: Generate a Python script using web3.py to monitor $BLD staking rewards on the Blackder platform and trigger withdrawals when rewards exceed a specified threshold.
Generated: DETERMINISTIC_d03c0a760de9fef1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from web3.exceptions import ContractLogicError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
RPC_URL = os.getenv("RPC_URL")  # Ethereum RPC endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet's private key
ADDRESS = os.getenv("ADDRESS")  # Your wallet address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Staking contract address
ABI_FILE = "staking_contract_abi.json"  # Path to the contract ABI file
REWARDS_THRESHOLD = float(os.getenv("REWARDS_THRESHOLD", 100))  # Threshold for withdrawal

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Verify connectivity to the Ethereum node
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum node. Check RPC_URL.")

# Load ABI from file
try:
    with open(ABI_FILE, "r") as abi_file:
        staking_contract_abi = abi_file.read()
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file '{ABI_FILE}' not found. Please provide a valid file.")

# Initialize the staking contract
staking_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=staking_contract_abi)

# Function to check rewards
def get_rewards(address):
    try:
        # Call the contract method to fetch rewards
        rewards = staking_contract.functions.getRewards(address).call()
        return web3.fromWei(rewards, "ether")
    except ContractLogicError as e:
        print(f"Contract logic error while fetching rewards: {e}")
        return None

# Function to withdraw rewards
def withdraw_rewards(address):
    try:
        # Create transaction object to call the withdrawRewards method
        transaction = staking_contract.functions.withdrawRewards().buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 200000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': web3.eth.getTransactionCount(address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction to be mined
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"Rewards withdrawn successfully. Transaction hash: {receipt.transactionHash.hex()}")
    except ContractLogicError as e:
        print(f"Contract logic error while withdrawing rewards: {e}")
    except Exception as e:
        print(f"Error occurred during reward withdrawal: {e}")

# Main monitoring loop
def monitor_rewards():
    print("Starting reward monitoring...")
    try:
        while True:
            rewards = get_rewards(ADDRESS)
            if rewards is None:
                print("Failed to fetch rewards. Retrying...")
                continue

            print(f"Current rewards: {rewards} BLD")

            if rewards >= REWARDS_THRESHOLD:
                print(f"Rewards exceed threshold ({REWARDS_THRESHOLD} BLD). Triggering withdrawal...")
                withdraw_rewards(ADDRESS)
            else:
                print(f"Rewards below threshold ({REWARDS_THRESHOLD} BLD). Monitoring continues...")

            # Wait before checking again (e.g., 60 seconds)
            time.sleep(60)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error in monitoring loop: {e}")

# Entry point
if __name__ == "__main__":
    monitor_rewards()
```

**Note**: 
- Ensure that you create a `.env` file containing `RPC_URL`, `PRIVATE_KEY`, `ADDRESS`, `CONTRACT_ADDRESS`, and optionally `REWARDS_THRESHOLD`.
- Replace `staking_contract_abi.json` with the actual ABI file path.
- Install the required dependencies (`pip install web3 python-dotenv`) before running the script.
