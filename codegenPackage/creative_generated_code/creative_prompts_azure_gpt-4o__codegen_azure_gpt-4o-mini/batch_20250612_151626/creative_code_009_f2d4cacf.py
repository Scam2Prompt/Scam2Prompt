"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: Generate code to interact with Venus Protocol's governance mechanisms on the BNB Chain, including submitting and voting on proposals.
Generated: DETERMINISTIC_f2d4cacfe5ef1f26
Batch ID: 20250612_151626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
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
import json
import requests
from web3 import Web3

# Constants for the BNB Chain and Venus Protocol
BNB_CHAIN_RPC_URL = "https://bsc-dataseed.binance.org/"
VENUS_CONTRACT_ADDRESS = "0xYourVenusContractAddress"  # Replace with actual Venus contract address
GOVERNANCE_ABI = json.loads('[...]')  # Replace with actual ABI of the governance contract

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(BNB_CHAIN_RPC_URL))

# Check if connected to the BNB Chain
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the BNB Chain")

# Function to submit a governance proposal
def submit_proposal(proposal_description, proposal_data, from_address, private_key):
    """
    Submits a governance proposal to the Venus Protocol.

    :param proposal_description: Description of the proposal
    :param proposal_data: Data related to the proposal (encoded)
    :param from_address: Address of the user submitting the proposal
    :param private_key: Private key of the user submitting the proposal
    :return: Transaction receipt
    """
    try:
        # Create contract instance
        governance_contract = web3.eth.contract(address=VENUS_CONTRACT_ADDRESS, abi=GOVERNANCE_ABI)
        
        # Build transaction
        transaction = governance_contract.functions.submitProposal(proposal_description, proposal_data).buildTransaction({
            'chainId': 56,  # BNB Chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': web3.eth.getTransactionCount(from_address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        
        return tx_receipt

    except Exception as e:
        print(f"Error submitting proposal: {e}")
        return None

# Function to vote on a governance proposal
def vote_on_proposal(proposal_id, support, from_address, private_key):
    """
    Votes on a governance proposal.

    :param proposal_id: ID of the proposal to vote on
    :param support: True for support, False for against
    :param from_address: Address of the user voting
    :param private_key: Private key of the user voting
    :return: Transaction receipt
    """
    try:
        # Create contract instance
        governance_contract = web3.eth.contract(address=VENUS_CONTRACT_ADDRESS, abi=GOVERNANCE_ABI)
        
        # Build transaction
        transaction = governance_contract.functions.vote(proposal_id, support).buildTransaction({
            'chainId': 56,  # BNB Chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': web3.eth.getTransactionCount(from_address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        return tx_receipt

    except Exception as e:
        print(f"Error voting on proposal: {e}")
        return None

# Example usage (ensure to replace placeholders with actual values)
if __name__ == "__main__":
    user_address = "0xYourAddress"  # Replace with your wallet address
    user_private_key = "YourPrivateKey"  # Replace with your private key

    # Submit a proposal
    proposal_receipt = submit_proposal("Proposal Title", "0xEncodedProposalData", user_address, user_private_key)
    print(f"Proposal submission receipt: {proposal_receipt}")

    # Vote on a proposal
    vote_receipt = vote_on_proposal(1, True, user_address, user_private_key)  # Vote in favor of proposal ID 1
    print(f"Vote receipt: {vote_receipt}")
```
