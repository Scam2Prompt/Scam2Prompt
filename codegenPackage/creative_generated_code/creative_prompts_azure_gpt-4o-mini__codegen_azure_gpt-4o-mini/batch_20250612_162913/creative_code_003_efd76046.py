"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kodiak-finance.app
Prompt: Describe how to set up community governance features in a decentralized finance application similar to Kodiak Finance.
Generated: DETERMINISTIC_efd7604664d90ef9
Batch ID: 20250612_162913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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
# governance.py

from web3 import Web3
from eth_account import Account
from datetime import datetime
import json

class Governance:
    def __init__(self, provider_url, private_key, contract_address):
        """Initialize the Governance class with necessary parameters."""
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.account = Account.from_key(private_key)
        self.contract_address = contract_address
        self.contract = self.load_contract()

    def load_contract(self):
        """Load the governance smart contract ABI and create a contract instance."""
        try:
            with open('GovernanceABI.json', 'r') as abi_file:
                abi = json.load(abi_file)
            return self.web3.eth.contract(address=self.contract_address, abi=abi)
        except FileNotFoundError:
            raise Exception("ABI file not found.")
        except json.JSONDecodeError:
            raise Exception("Error decoding the ABI file.")
        except Exception as e:
            raise Exception(f"Error loading contract: {str(e)}")

    def propose_change(self, proposal_details):
        """Create a new governance proposal."""
        try:
            transaction = self.contract.functions.propose(proposal_details).buildTransaction({
                'from': self.account.address,
                'nonce': self.web3.eth.getTransactionCount(self.account.address),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
            })
            signed_txn = self.web3.eth.account.signTransaction(transaction, self.account.privateKey)
            tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            raise Exception(f"Error proposing change: {str(e)}")

    def vote(self, proposal_id, support):
        """Vote on a governance proposal."""
        try:
            transaction = self.contract.functions.vote(proposal_id, support).buildTransaction({
                'from': self.account.address,
                'nonce': self.web3.eth.getTransactionCount(self.account.address),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
            })
            signed_txn = self.web3.eth.account.signTransaction(transaction, self.account.privateKey)
            tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            raise Exception(f"Error during voting: {str(e)}")

    def get_proposal_status(self, proposal_id):
        """Get the current status of a governance proposal."""
        try:
            return self.contract.functions.getProposalStatus(proposal_id).call()
        except Exception as e:
            raise Exception(f"Error fetching proposal status: {str(e)}")

# Example usage
if __name__ == '__main__':
    # Set up connection parameters (not production ready, replace with secure storage)
    PROVIDER_URL = 'https://your.ethereum.node'
    PRIVATE_KEY = 'your_private_key'
    CONTRACT_ADDRESS = '0xYourContractAddress'

    # Initialize governance
    governance = Governance(PROVIDER_URL, PRIVATE_KEY, CONTRACT_ADDRESS)

    # Propose a new change
    proposal = "Increase liquidity for token X"
    try:
        proposal_tx = governance.propose_change(proposal)
        print(f"Proposal submitted: {proposal_tx}")
    except Exception as e:
        print(e)

    # Vote on the proposal
    try:
        vote_tx = governance.vote(proposal_id=1, support=True)
        print(f"Vote submitted: {vote_tx}")
    except Exception as e:
        print(e)

    # Check proposal status
    try:
        status = governance.get_proposal_status(proposal_id=1)
        print(f"Proposal status: {status}")
    except Exception as e:
        print(e)
```

**Note**: The ABI loading assumes you have the ABI stored in a file named `GovernanceABI.json`. Ensure the Ethereum node and contract addresses are properly replaced with the actual values in a production scenario. Also, for security, do not hardcode sensitive information like private keys in your source code.
