"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suntronswap.link
Prompt: Generate code to automate participation in governance voting on the SUN platform, including locking SUN tokens and submitting votes.
Generated: DETERMINISTIC_f5db4c88218e617c
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from web3 import Web3, exceptions
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
RPC_URL = os.getenv("RPC_URL")  # Blockchain RPC URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the voter
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Public wallet address of the voter
SUN_TOKEN_ADDRESS = os.getenv("SUN_TOKEN_ADDRESS")  # Address of the SUN token contract
GOVERNANCE_CONTRACT_ADDRESS = os.getenv("GOVERNANCE_CONTRACT_ADDRESS")  # Governance contract address
GAS_LIMIT = 300000  # Gas limit for transactions
GAS_PRICE = Web3.toWei('20', 'gwei')  # Gas price in GWei

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to the blockchain RPC.")

# Load SUN Token contract ABI
SUN_TOKEN_ABI = json.loads(os.getenv("SUN_TOKEN_ABI"))

# Load Governance contract ABI
GOVERNANCE_ABI = json.loads(os.getenv("GOVERNANCE_ABI"))

# Setup contract instances
sun_token_contract = web3.eth.contract(address=SUN_TOKEN_ADDRESS, abi=SUN_TOKEN_ABI)
governance_contract = web3.eth.contract(address=GOVERNANCE_CONTRACT_ADDRESS, abi=GOVERNANCE_ABI)

def lock_sun_tokens(amount):
    """
    Lock SUN tokens in the governance contract.

    :param amount: Amount of SUN tokens to lock (in smallest unit - e.g., wei)
    """
    try:
        # Approve governance contract to spend SUN tokens
        approve_txn = sun_token_contract.functions.approve(GOVERNANCE_CONTRACT_ADDRESS, amount).buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS)
        })

        signed_approve_txn = web3.eth.account.sign_transaction(approve_txn, PRIVATE_KEY)
        approve_txn_hash = web3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
        web3.eth.wait_for_transaction_receipt(approve_txn_hash)

        # Lock tokens in the governance contract
        lock_txn = governance_contract.functions.lockTokens(amount).buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS)
        })

        signed_lock_txn = web3.eth.account.sign_transaction(lock_txn, PRIVATE_KEY)
        lock_txn_hash = web3.eth.send_raw_transaction(signed_lock_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(lock_txn_hash)

        print(f"Successfully locked {amount} SUN tokens. Transaction hash: {lock_txn_hash.hex()}")
    except exceptions.ContractLogicError as e:
        print(f"Contract logic error occurred: {str(e)}")
    except Exception as e:
        print(f"Transaction failed: {str(e)}")

def submit_vote(proposal_id, vote_choice):
    """
    Submit a vote on a governance proposal.

    :param proposal_id: ID of the governance proposal to vote on
    :param vote_choice: Voting choice (e.g., 0 for 'Against', 1 for 'For', 2 for 'Abstain')
    """
    try:
        vote_txn = governance_contract.functions.vote(proposal_id, vote_choice).buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS)
        })

        signed_vote_txn = web3.eth.account.sign_transaction(vote_txn, PRIVATE_KEY)
        vote_txn_hash = web3.eth.send_raw_transaction(signed_vote_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(vote_txn_hash)

        print(f"Successfully submitted vote for proposal {proposal_id}. Transaction hash: {vote_txn_hash.hex()}")
    except exceptions.ContractLogicError as e:
        print(f"Contract logic error occurred: {str(e)}")
    except Exception as e:
        print(f"Transaction failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    # Lock tokens
    lock_amount = Web3.toWei(100, 'ether')  # Example: Lock 100 SUN tokens
    lock_sun_tokens(lock_amount)

    # Submit vote
    proposal_id = 1  # Example proposal ID
    vote_choice = 1  # Example vote choice: 1 for 'For'
    submit_vote(proposal_id, vote_choice)
```
