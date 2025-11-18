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
# Import required libraries
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

# Configuration
BNB_CHAIN_RPC_URL = "https://bsc-dataseed.binance.org/"  # Mainnet RPC URL
VENUS_GOVERNANCE_ADDRESS = "0x123456789ABCDEF0123456789ABCDEF012345678"  # Replace with actual Venus Governance contract address
PRIVATE_KEY = "your-private-key-here"  # Replace with your wallet's private key
WALLET_ADDRESS = "your-wallet-address-here"  # Replace with your wallet address

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(BNB_CHAIN_RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Inject Geth PoA middleware for BNB Chain compatibility

# Check connection
if not web3.isConnected():
    raise Exception("Failed to connect to BNB Chain RPC.")

# Load Venus Governance contract ABI (replace with actual ABI)
with open("venus_governance_abi.json", "r") as abi_file:
    VENUS_GOVERNANCE_ABI = json.load(abi_file)

# Initialize contract instance
governance_contract = web3.eth.contract(address=VENUS_GOVERNANCE_ADDRESS, abi=VENUS_GOVERNANCE_ABI)

# Function to submit a proposal
def submit_proposal(description, targets, values, signatures, calldatas):
    """
    Submit a governance proposal on the Venus Protocol.

    :param description: Proposal description string
    :param targets: List of target contract addresses
    :param values: List of values (amounts of BNB to send, usually 0)
    :param signatures: List of function signatures to call
    :param calldatas: List of calldata for each function call
    :return: Transaction hash
    """
    try:
        # Build transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        tx = governance_contract.functions.propose(
            targets,
            values,
            signatures,
            calldatas,
            description
        ).build_transaction({
            'chainId': 56,  # BNB Chain Mainnet Chain ID
            'gas': 500000,  # Set a reasonable gas limit
            'gasPrice': web3.toWei('5', 'gwei'),  # Set a reasonable gas price
            'nonce': nonce
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.toHex(tx_hash)
    except Exception as e:
        raise Exception(f"Failed to submit proposal: {str(e)}")


# Function to vote on a proposal
def vote_on_proposal(proposal_id, support):
    """
    Vote on a governance proposal on the Venus Protocol.

    :param proposal_id: ID of the proposal
    :param support: Boolean indicating whether to vote in favor (True) or against (False)
    :return: Transaction hash
    """
    try:
        # Build transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        tx = governance_contract.functions.castVote(
            proposal_id,
            support
        ).build_transaction({
            'chainId': 56,  # BNB Chain Mainnet Chain ID
            'gas': 200000,  # Set a reasonable gas limit
            'gasPrice': web3.toWei('5', 'gwei'),  # Set a reasonable gas price
            'nonce': nonce
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.toHex(tx_hash)
    except Exception as e:
        raise Exception(f"Failed to vote on proposal: {str(e)}")


# Example usage (uncomment to use)
# Submit a proposal (replace with valid data)
# tx_hash_submit = submit_proposal(
#     description="Proposal to update interest rates",
#     targets=["0xTargetAddress1", "0xTargetAddress2"],
#     values=[0, 0],
#     signatures=["functionSignature1", "functionSignature2"],
#     calldatas=["0xCalldata1", "0xCalldata2"]
# )
# print(f"Proposal submitted. Transaction hash: {tx_hash_submit}")

# Vote on a proposal (replace with valid data)
# tx_hash_vote = vote_on_proposal(proposal_id=1, support=True)
# print(f"Vote cast. Transaction hash: {tx_hash_vote}")
```
