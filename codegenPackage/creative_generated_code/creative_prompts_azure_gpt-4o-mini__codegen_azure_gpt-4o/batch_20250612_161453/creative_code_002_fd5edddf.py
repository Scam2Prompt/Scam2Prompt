"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorodshansona.ru
Prompt: Generate a code snippet that demonstrates how to use the IMX token for voting on protocol developments within the Immutable X ecosystem.
Generated: DETERMINISTIC_fd5edddf9f5e3a52
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os

# Load environment variables (private keys, Infura URL, etc.)
load_dotenv()

# Environment configuration
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for the Ethereum network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the voting user
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address of the voting user
IMX_TOKEN_ADDRESS = os.getenv("IMX_TOKEN_ADDRESS")  # Address of the IMX token contract
VOTING_CONTRACT_ADDRESS = os.getenv("VOTING_CONTRACT_ADDRESS")  # Address of the voting contract

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Add middleware for PoA networks (if applicable)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load the contract ABI
with open("VotingContractABI.json", "r") as abi_file:
    voting_contract_abi = abi_file.read()

# Load the token ABI
with open("IMXTokenABI.json", "r") as abi_file:
    imx_token_abi = abi_file.read()

# Voting contract initialization
voting_contract = web3.eth.contract(address=VOTING_CONTRACT_ADDRESS, abi=voting_contract_abi)

# IMX token contract initialization
imx_token = web3.eth.contract(address=IMX_TOKEN_ADDRESS, abi=imx_token_abi)

def vote_on_proposal(proposal_id: int, vote_amount: int) -> str:
    """
    Function to vote on a protocol development proposal using IMX tokens.

    :param proposal_id: ID of the proposal to vote on
    :param vote_amount: Amount of IMX tokens to vote with
    :return: Transaction hash of the vote transaction
    """
    # Check IMX balance
    balance = imx_token.functions.balanceOf(WALLET_ADDRESS).call()
    if vote_amount > balance:
        raise ValueError("Insufficient IMX token balance for voting.")

    # Approve the voting contract to spend IMX tokens
    approve_tx = imx_token.functions.approve(VOTING_CONTRACT_ADDRESS, vote_amount).buildTransaction({
        'from': WALLET_ADDRESS,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS),
        'gas': 200000,
        'gasPrice': web3.toWei('20', 'gwei')
    })

    signed_approve_tx = web3.eth.account.sign_transaction(approve_tx, private_key=PRIVATE_KEY)
    approve_tx_hash = web3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)
    web3.eth.wait_for_transaction_receipt(approve_tx_hash)

    # Cast vote on the proposal
    vote_tx = voting_contract.functions.castVote(proposal_id, vote_amount).buildTransaction({
        'from': WALLET_ADDRESS,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS),
        'gas': 200000,
        'gasPrice': web3.toWei('20', 'gwei')
    })

    signed_vote_tx = web3.eth.account.sign_transaction(vote_tx, private_key=PRIVATE_KEY)
    vote_tx_hash = web3.eth.send_raw_transaction(signed_vote_tx.rawTransaction)
    web3.eth.wait_for_transaction_receipt(vote_tx_hash)

    return vote_tx_hash.hex()

# Example usage
try:
    proposal_id = 1  # ID of the proposal being voted on
    vote_amount = 100  # Amount of IMX tokens to vote with
    tx_hash = vote_on_proposal(proposal_id, vote_amount)
    print(f"Vote successful! Transaction hash: {tx_hash}")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Note:** This script assumes that you have the required ABIs (`VotingContractABI.json` and `IMXTokenABI.json`) and environment variables configured properly. Replace placeholder values with appropriate real-world values for production.
