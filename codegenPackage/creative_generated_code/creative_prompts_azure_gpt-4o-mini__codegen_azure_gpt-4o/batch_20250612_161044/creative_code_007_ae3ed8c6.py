"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Explain how to access Aave's governance features programmatically, including voting on Aave Improvement Proposals (AIPs) using the AAVE token.
Generated: DETERMINISTIC_ae3ed8c67ad5c853
Batch ID: 20250612_161044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
"""
Python script for interacting with Aave's governance features, including voting on Aave Improvement Proposals (AIPs).
This script uses Web3.py to communicate with Aave's smart contracts via Ethereum blockchain.

Prerequisites:
- Install Web3.py: `pip install web3`
- Have your Ethereum wallet private key ready
- Ensure your wallet has AAVE tokens and enough ETH for gas fees
"""

from web3 import Web3
from eth_account import Account
import json

# Configuration variables
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"  # Replace with your wallet private key
GOVERNANCE_CONTRACT_ADDRESS = "0xEC568fffba86c094cf06b22134B23074DFE2252c"  # Aave Governance V2 contract address
PROPOSAL_ID = 1  # Replace with the AIP proposal ID you want to vote on (example: 1)
VOTE_SUPPORT = 1  # 1 = For, 0 = Against, 2 = Abstain

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network. Check your INFURA_URL.")

# Load wallet details
account = Account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Load Aave Governance V2 ABI
# Replace with the ABI of the Governance contract
GOVERNANCE_ABI = '''
[
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "proposalId",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "support",
                "type": "uint8"
            }
        ],
        "name": "submitVote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
'''

# Load Governance contract
governance_contract = web3.eth.contract(
    address=web3.toChecksumAddress(GOVERNANCE_CONTRACT_ADDRESS),
    abi=json.loads(GOVERNANCE_ABI)
)

# Build the transaction for voting
try:
    tx = governance_contract.functions.submitVote(PROPOSAL_ID, VOTE_SUPPORT).buildTransaction({
        'chainId': 1,  # Ethereum Mainnet chain ID
        'gas': 200000,  # Estimated gas (adjust if needed)
        'gasPrice': web3.eth.gas_price,  # Current gas price
        'nonce': web3.eth.get_transaction_count(wallet_address),  # Nonce for the wallet address
    })
except ValueError as e:
    raise ValueError(f"Error building transaction: {e}")

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# Send the transaction
try:
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent successfully! TX Hash: {tx_hash.hex()}")
except Exception as e:
    raise RuntimeError(f"Error sending transaction: {e}")

# Wait for transaction receipt
try:
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed! Block Number: {receipt.blockNumber}")
except Exception as e:
    raise RuntimeError(f"Error waiting for transaction receipt: {e}")
```
