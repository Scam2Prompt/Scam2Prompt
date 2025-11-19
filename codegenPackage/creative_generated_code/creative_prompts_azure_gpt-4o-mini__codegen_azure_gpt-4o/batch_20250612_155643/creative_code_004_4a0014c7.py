"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benqi.cc
Prompt: Explain how to seamlessly use BENQI for staking AVAX and earning rewards in a DeFi ecosystem.
Generated: DETERMINISTIC_4a0014c71ce3fe9f
Batch ID: 20250612_155643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the BENQI protocol to stake AVAX and earn rewards.
The script assumes you have a Web3 wallet and some AVAX tokens available for staking.
Ensure you have Python installed with web3.py and dotenv libraries configured.
"""

from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Avalanche network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet's private key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Your wallet address
BENQI_STAKING_CONTRACT = "0x0000000000000000000000000000000000000000"  # Example contract address; replace with actual

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Add middleware for Avalanche's Consensus (if required)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Validate connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Avalanche network")

# ABI for BENQI Staking Contract
BENQI_ABI = [
    # Replace with the actual ABI of the BENQI staking contract
    # Minimum example ABI structure for interacting with staking functions
    {
        "constant": True,
        "inputs": [],
        "name": "stake",
        "outputs": [],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "claimRewards",
        "outputs": [],
        "type": "function"
    }
]

# Initialize contract instance
staking_contract = web3.eth.contract(address=BENQI_STAKING_CONTRACT, abi=BENQI_ABI)

# Helper function to build and send transactions
def send_transaction(wallet_address, private_key, txn):
    """
    Signs and sends a transaction to the Avalanche network.
    :param wallet_address: Address of the sender wallet.
    :param private_key: Private key of the sender wallet.
    :param txn: Transaction object.
    :return: Transaction hash.
    """
    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash.hex()

# Function to stake AVAX tokens
def stake_avax(amount):
    """
    Stakes AVAX tokens on the BENQI protocol.
    :param amount: Amount of AVAX to stake (in WEI).
    """
    try:
        # Build transaction
        txn = staking_contract.functions.stake().buildTransaction({
            'from': WALLET_ADDRESS,
            'value': amount,  # Amount in WEI
            'gas': 200000,   # Adjust gas limit based on the contract's requirements
            'gasPrice': web3.toWei('25', 'gwei'),  # Adjust gas price based on current network conditions
            'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
        })

        # Send transaction
        tx_hash = send_transaction(WALLET_ADDRESS, PRIVATE_KEY, txn)
        print(f"Staking transaction sent. TX Hash: {tx_hash}")
    except Exception as e:
        print(f"Failed to stake AVAX: {e}")

# Function to claim staking rewards
def claim_rewards():
    """
    Claims staking rewards from the BENQI protocol.
    """
    try:
        # Build transaction
        txn = staking_contract.functions.claimRewards().buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': 200000,   # Adjust gas limit based on the contract's requirements
            'gasPrice': web3.toWei('25', 'gwei'),  # Adjust gas price based on current network conditions
            'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
        })

        # Send transaction
        tx_hash = send_transaction(WALLET_ADDRESS, PRIVATE_KEY, txn)
        print(f"Claim rewards transaction sent. TX Hash: {tx_hash}")
    except Exception as e:
        print(f"Failed to claim rewards: {e}")

# Example usage
if __name__ == "__main__":
    # Replace the amount with the desired staking amount in WEI
    stake_amount = web3.toWei(1, 'ether')  # 1 AVAX converted to WEI

    # Stake AVAX tokens
    stake_avax(stake_amount)

    # Claim rewards (optional, can be done periodically)
    claim_rewards()
```

**Note:** Replace placeholders (e.g., `BENQI_STAKING_CONTRACT`, ABI details) with the actual contract address and ABI provided by BENQI. Ensure your `.env` file contains `INFURA_URL`, `PRIVATE_KEY`, and `WALLET_ADDRESS` correctly configured.
