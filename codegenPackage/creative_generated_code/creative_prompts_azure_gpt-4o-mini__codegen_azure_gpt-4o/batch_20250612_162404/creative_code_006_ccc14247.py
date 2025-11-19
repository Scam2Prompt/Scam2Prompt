"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-stores.pages.dev
Prompt: Construct a voting system for token holders within the Pushd platform, allowing them to propose and vote on platform changes.
Generated: DETERMINISTIC_ccc1424732e1bb42
Batch ID: 20250612_162404
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

Below is the implementation of a voting system in Python, leveraging `web3.py` to interact with an Ethereum-based smart contract. Token holders can propose and vote on platform changes. 

```python
import json
from web3 import Web3, exceptions

class VotingSystem:
    """
    Voting System for token holders within the Pushd platform.
    Allows proposing and voting on platform changes.
    """

    def __init__(self, rpc_url, contract_address, abi_path):
        """
        Initialize the voting system.

        Args:
            rpc_url (str): RPC URL of the Ethereum node.
            contract_address (str): Smart contract address for the voting system.
            abi_path (str): Path to the ABI file of the smart contract.
        """
        try:
            # Connect to the Ethereum node
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
            if not self.web3.isConnected():
                raise ConnectionError("Failed to connect to Ethereum node.")

            # Load the contract ABI
            with open(abi_path, 'r') as abi_file:
                contract_abi = json.load(abi_file)

            # Initialize the smart contract instance
            self.contract = self.web3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=contract_abi)
        
        except Exception as e:
            raise RuntimeError(f"Initialization failed: {e}")

    def propose_change(self, proposer_private_key, proposal_description):
        """
        Allows a token holder to propose a platform change.

        Args:
            proposer_private_key (str): Private key of the proposer.
            proposal_description (str): Description of the proposed change.

        Returns:
            str: Transaction hash of the proposal submission.
        """
        try:
            # Get the account address from the private key
            proposer_account = self.web3.eth.account.privateKeyToAccount(proposer_private_key).address

            # Build the transaction
            transaction = self.contract.functions.proposeChange(proposal_description).buildTransaction({
                'from': proposer_account,
                'nonce': self.web3.eth.getTransactionCount(proposer_account),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('20', 'gwei')
            })

            # Sign and send the transaction
            signed_transaction = self.web3.eth.account.signTransaction(transaction, proposer_private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

            return self.web3.toHex(tx_hash)

        except exceptions.ValidationError as ve:
            raise ValueError(f"Validation Error: {ve}")
        except Exception as e:
            raise RuntimeError(f"Failed to propose change: {e}")

    def vote_on_proposal(self, voter_private_key, proposal_id, support):
        """
        Allows a token holder to vote on a proposal.

        Args:
            voter_private_key (str): Private key of the voter.
            proposal_id (int): ID of the proposal to vote on.
            support (bool): True to support the proposal, False to oppose.

        Returns:
            str: Transaction hash of the vote.
        """
        try:
            # Get the account address from the private key
            voter_account = self.web3.eth.account.privateKeyToAccount(voter_private_key).address

            # Build the transaction
            transaction = self.contract.functions.voteOnProposal(proposal_id, support).buildTransaction({
                'from': voter_account,
                'nonce': self.web3.eth.getTransactionCount(voter_account),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('20', 'gwei')
            })

            # Sign and send the transaction
            signed_transaction = self.web3.eth.account.signTransaction(transaction, voter_private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

            return self.web3.toHex(tx_hash)

        except exceptions.ValidationError as ve:
            raise ValueError(f"Validation Error: {ve}")
        except Exception as e:
            raise RuntimeError(f"Failed to vote on proposal: {e}")

    def get_proposal(self, proposal_id):
        """
        Retrieves details of a proposal by its ID.

        Args:
            proposal_id (int): ID of the proposal.

        Returns:
            dict: Details of the proposal.
        """
        try:
            proposal = self.contract.functions.getProposal(proposal_id).call()
            return {
                'id': proposal[0],
                'description': proposal[1],
                'votesFor': proposal[2],
                'votesAgainst': proposal[3],
                'executed': proposal[4]
            }
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve proposal: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your RPC URL, contract address, and ABI file path
    RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    CONTRACT_ADDRESS = "0xYourSmartContractAddress"
    ABI_PATH = "path/to/contract_abi.json"

    # Initialize the voting system
    voting_system = VotingSystem(RPC_URL, CONTRACT_ADDRESS, ABI_PATH)

    # Call methods as needed (e.g., propose_change, vote_on_proposal, get_proposal)
```

### Notes:
1. Replace placeholder variables (`RPC_URL`, `CONTRACT_ADDRESS`, and `ABI_PATH`) with actual values.
2. Ensure the smart contract includes appropriate methods (`proposeChange`, `voteOnProposal`, and `getProposal`) matching the ABI. 
3. Token holder eligibility for proposals and votes should be enforced via smart contract logic.
