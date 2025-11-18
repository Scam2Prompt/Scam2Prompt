"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Write a script to automate staking QI tokens on the Mai Finance platform and calculate rewards distribution based on farming pools.
Generated: DETERMINISTIC_9bebf6a95a7a524f
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for automating staking QI tokens on the Mai Finance platform and calculating rewards distribution based on farming pools. This is a production-ready script that uses the Web3 library to interact with the blockchain.

```python
import json
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
RPC_URL = os.getenv("RPC_URL")  # Replace with your RPC node URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet's private key (keep safe)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Your wallet address
QI_TOKEN_ADDRESS = os.getenv("QI_TOKEN_ADDRESS")  # QI token contract address
STAKING_CONTRACT_ADDRESS = os.getenv("STAKING_CONTRACT_ADDRESS")  # Mai Finance staking contract address
FARMING_POOLS = json.loads(os.getenv("FARMING_POOLS"))  # JSON list of farming pool contract addresses

# Initialize Web3
web3 = Web3(HTTPProvider(RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to RPC node.")

# Verify wallet address
if not Web3.isAddress(WALLET_ADDRESS):
    raise ValueError("Invalid wallet address.")

# Load ABI files for contract interaction
def load_abi(file_path):
    """Load ABI from a JSON file."""
    with open(file_path, 'r') as abi_file:
        return json.load(abi_file)

qi_token_abi = load_abi("qi_token_abi.json")  # Ensure this file exists
staking_contract_abi = load_abi("staking_contract_abi.json")  # Ensure this file exists

# Initialize contracts
qi_token_contract = web3.eth.contract(address=web3.toChecksumAddress(QI_TOKEN_ADDRESS), abi=qi_token_abi)
staking_contract = web3.eth.contract(address=web3.toChecksumAddress(STAKING_CONTRACT_ADDRESS), abi=staking_contract_abi)

# Helper function to build and send transactions
def send_transaction(tx):
    """Send a transaction to the blockchain."""
    try:
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Transaction failed: {str(e)}")

# Stake QI tokens
def stake_tokens(amount):
    """Stake QI tokens into the Mai Finance staking pool."""
    try:
        # Approve staking contract to spend QI tokens
        approve_tx = qi_token_contract.functions.approve(
            web3.toChecksumAddress(STAKING_CONTRACT_ADDRESS),
            amount
        ).buildTransaction({
            "from": WALLET_ADDRESS,
            "gas": 200000,
            "gasPrice": web3.toWei("30", "gwei"),
            "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS)
        })
        send_transaction(approve_tx)

        # Stake tokens
        stake_tx = staking_contract.functions.stake(amount).buildTransaction({
            "from": WALLET_ADDRESS,
            "gas": 300000,
            "gasPrice": web3.toWei("30", "gwei"),
            "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS)
        })
        send_transaction(stake_tx)

        print("Staking successful.")
    except Exception as e:
        print(f"An error occurred while staking: {str(e)}")

# Calculate rewards distribution
def calculate_rewards():
    """Calculate rewards distribution from farming pools."""
    rewards = {}
    for pool_address in FARMING_POOLS:
        try:
            pool_contract = web3.eth.contract(address=web3.toChecksumAddress(pool_address), abi=qi_token_abi)
            reward = pool_contract.functions.getPendingRewards(WALLET_ADDRESS).call()
            rewards[pool_address] = web3.fromWei(reward, "ether")
        except Exception as e:
            print(f"Failed to calculate rewards for pool {pool_address}: {str(e)}")
    return rewards

# Main function
def main():
    try:
        # The amount of QI tokens to stake (replace with the desired amount)
        stake_amount = web3.toWei(100, "ether")  # Example: 100 QI

        # Stake tokens
        stake_tokens(stake_amount)

        # Calculate rewards
        rewards = calculate_rewards()
        print("Rewards Distribution:")
        for pool, reward in rewards.items():
            print(f"Pool {pool}: {reward} QI")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes:
- Ensure you have the `qi_token_abi.json` and `staking_contract_abi.json` ABI files in your working directory.
- Install the required dependencies using `pip install web3 python-dotenv`.
- Secure your private key by storing it safely (e.g., in environment variables or a secure vault).
- Replace the `.env` file values with your actual RPC URL, wallet address, contract addresses, and farming pool details.
