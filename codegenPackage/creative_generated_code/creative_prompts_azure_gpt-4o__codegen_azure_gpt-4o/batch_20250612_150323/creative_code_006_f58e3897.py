"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: Write a tutorial-style script to guide developers on how to stake WalletConnect Token (WCT) and interact with its governance features programmatically.
Generated: DETERMINISTIC_f58e38973c1f34ca
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/{INFURA_PROJECT_ID": {
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
import json
from web3 import Web3
from eth_account import Account

# Configuration
INFURA_PROJECT_ID = 'your_infura_project_id'
WCT_CONTRACT_ADDRESS = '0xYourWCTTokenContractAddress'
GOVERNANCE_CONTRACT_ADDRESS = '0xYourGovernanceContractAddress'
PRIVATE_KEY = 'your_private_key'  # Wallet private key for signing transactions
STAKING_AMOUNT = Web3.toWei(10, 'ether')  # Amount to stake (example: 10 WCT)

# Connect to Ethereum network via Infura
web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))

# Check connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Convert private key into an account object
account = Account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Load WCT token contract ABI (Replace with actual ABI)
with open('path/to/WCT_abi.json', 'r') as abi_file:
    wct_abi = json.load(abi_file)

wct_contract = web3.eth.contract(address=WCT_CONTRACT_ADDRESS, abi=wct_abi)

# Load Governance contract ABI (Replace with actual ABI)
with open('path/to/Governance_abi.json', 'r') as abi_file:
    governance_abi = json.load(abi_file)

governance_contract = web3.eth.contract(address=GOVERNANCE_CONTRACT_ADDRESS, abi=governance_abi)

# Function to get account balance
def get_balance(address):
    return web3.eth.get_balance(address)

# Approve tokens for staking
def approve_tokens(amount):
    nonce = web3.eth.getTransactionCount(wallet_address)
    approve_tx = wct_contract.functions.approve(GOVERNANCE_CONTRACT_ADDRESS, amount).buildTransaction({
        'chainId': 1,  # Mainnet chain ID
        'gas': 200000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce
    })
    
    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(approve_tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Approve transaction sent. TX Hash: {tx_hash.hex()}")
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Tokens approved successfully.")

# Stake tokens
def stake_tokens(amount):
    nonce = web3.eth.getTransactionCount(wallet_address)
    stake_tx = governance_contract.functions.stake(amount).buildTransaction({
        'chainId': 1,  # Mainnet chain ID
        'gas': 200000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce
    })
    
    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(stake_tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Stake transaction sent. TX Hash: {tx_hash.hex()}")
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Tokens staked successfully.")

# Vote on governance proposals
def vote_on_proposal(proposal_id, support):
    """
    Votes on a governance proposal.
    :param proposal_id: The ID of the governance proposal.
    :param support: True to support, False to oppose.
    """
    nonce = web3.eth.getTransactionCount(wallet_address)
    vote_tx = governance_contract.functions.vote(proposal_id, support).buildTransaction({
        'chainId': 1,  # Mainnet chain ID
        'gas': 200000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce
    })
    
    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(vote_tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Vote transaction sent. TX Hash: {tx_hash.hex()}")
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Vote recorded successfully.")

# Example usage
if __name__ == '__main__':
    # Display wallet balance
    balance = web3.fromWei(get_balance(wallet_address), 'ether')
    print(f"Wallet Balance: {balance} ETH")
    
    # Approve tokens for staking
    approve_tokens(STAKING_AMOUNT)
    
    # Stake tokens
    stake_tokens(STAKING_AMOUNT)
    
    # Example of voting on a proposal (replace with actual proposal ID)
    proposal_id = 1  # Replace with valid proposal ID
    vote_on_proposal(proposal_id, True)  # Support the proposal

    print("All operations completed successfully.")
```

This script assumes the developer has access to the necessary ABI files (`WCT_abi.json` and `Governance_abi.json`) and that the `ethereum-web3` Python package is installed. Replace placeholders like `your_infura_project_id`, `your_private_key`, `0xYourWCTTokenContractAddress`, and `0xYourGovernanceContractAddress` with actual values.
