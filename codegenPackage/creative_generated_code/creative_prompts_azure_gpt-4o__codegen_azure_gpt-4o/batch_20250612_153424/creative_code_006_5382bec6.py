"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benq-i.fi
Prompt: Provide code to automate the process of staking AVAX on BENQI and converting the rewards into sAVAX for use in DeFi applications.
Generated: DETERMINISTIC_5382bec637d56c71
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Constants
RPC_URL = os.getenv("RPC_URL")  # URL of the Avalanche network RPC endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet
ADDRESS = os.getenv("ADDRESS")  # Wallet address
BENQI_STAKING_CONTRACT = os.getenv("BENQI_STAKING_CONTRACT")  # BENQI staking contract address
SAVAX_CONTRACT = os.getenv("SAVAX_CONTRACT")  # sAVAX contract address

# ABI files for BENQI staking and sAVAX contracts (replace with actual ABI files)
BENQI_STAKING_ABI = json.loads(os.getenv("BENQI_STAKING_ABI"))
SAVAX_ABI = json.loads(os.getenv("SAVAX_ABI"))

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure connection
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Avalanche network.")

# Unlock wallet
account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)

# Helper function to create and send transactions
def send_transaction(transaction):
    signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Stake AVAX on BENQI
def stake_avax(amount):
    """
    Stakes AVAX on BENQI staking contract.

    :param amount: Amount to stake in wei
    """
    contract = web3.eth.contract(address=BENQI_STAKING_CONTRACT, abi=BENQI_STAKING_ABI)
    staking_tx = contract.functions.stake().build_transaction({
        'from': ADDRESS,
        'value': amount,
        'gas': 3000000,
        'gasPrice': web3.toWei('30', 'gwei'),
        'nonce': web3.eth.get_transaction_count(ADDRESS)
    })

    receipt = send_transaction(staking_tx)
    return receipt

# Claim rewards from BENQI staking contract
def claim_rewards():
    """
    Claims rewards from BENQI staking contract.
    """
    contract = web3.eth.contract(address=BENQI_STAKING_CONTRACT, abi=BENQI_STAKING_ABI)
    claim_tx = contract.functions.claimRewards().build_transaction({
        'from': ADDRESS,
        'gas': 3000000,
        'gasPrice': web3.toWei('30', 'gwei'),
        'nonce': web3.eth.get_transaction_count(ADDRESS)
    })

    receipt = send_transaction(claim_tx)
    return receipt

# Convert rewards into sAVAX
def convert_to_savax(amount):
    """
    Converts AVAX rewards into sAVAX.

    :param amount: Amount of AVAX to convert in wei
    """
    contract = web3.eth.contract(address=SAVAX_CONTRACT, abi=SAVAX_ABI)
    convert_tx = contract.functions.deposit().build_transaction({
        'from': ADDRESS,
        'value': amount,
        'gas': 3000000,
        'gasPrice': web3.toWei('30', 'gwei'),
        'nonce': web3.eth.get_transaction_count(ADDRESS)
    })

    receipt = send_transaction(convert_tx)
    return receipt

# Main flow
def automate_staking(amount):
    """
    Automates the process of staking AVAX on BENQI and converting rewards into sAVAX.

    :param amount: Initial amount of AVAX to stake in wei
    """
    try:
        # Step 1: Stake AVAX on BENQI
        print("Staking AVAX...")
        stake_receipt = stake_avax(amount)
        print(f"Stake transaction successful: {stake_receipt.transactionHash.hex()}")

        # Wait for rewards to accumulate (placeholder for production-ready polling)
        print("Waiting for rewards to accumulate...")
        time.sleep(60 * 60)  # Wait for 1 hour (adjust for production use)

        # Step 2: Claim rewards
        print("Claiming rewards...")
        claim_receipt = claim_rewards()
        print(f"Rewards claimed: {claim_receipt.transactionHash.hex()}")

        # Step 3: Convert rewards to sAVAX
        reward_amount = web3.eth.get_balance(ADDRESS)  # Fetch balance post-rewards
        print("Converting rewards to sAVAX...")
        convert_receipt = convert_to_savax(reward_amount)
        print(f"Conversion successful: {convert_receipt.transactionHash.hex()}")

    except Exception as e:
        print(f"Error during automation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Amount to stake in AVAX (e.g., 1 AVAX = 10**18 wei)
    initial_stake = web3.toWei(1, 'ether')
    automate_staking(initial_stake)
```
