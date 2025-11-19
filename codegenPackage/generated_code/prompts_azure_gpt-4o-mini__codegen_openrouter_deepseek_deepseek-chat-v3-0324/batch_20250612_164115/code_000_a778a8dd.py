"""
Generated Code Metadata:
========================
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for proposal voting?
Generated: DETERMINISTIC_a778a8ddebf1d19f
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from web3 import Web3
from typing import List, Dict, Optional
import json
import os

class AgoraGovernance:
    """
    A class to interact with Agora's on-chain governance system for proposal voting.
    """

    def __init__(self, provider_url: str, contract_address: str, abi_path: str):
        """
        Initialize the AgoraGovernance class.

        Args:
            provider_url: URL of the Ethereum node provider (e.g., Infura, Alchemy).
            contract_address: Address of the Agora governance smart contract.
            abi_path: Path to the JSON file containing the contract ABI.
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node.")

        self.contract_address = contract_address
        with open(abi_path) as f:
            self.contract_abi = json.load(f)
        
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )

    def create_proposal(
        self,
        sender_private_key: str,
        proposal_data: Dict,
        description: str
    ) -> str:
        """
        Create a new governance proposal.

        Args:
            sender_private_key: Private key of the sender (proposer).
            proposal_data: Dictionary containing proposal data.
            description: Description of the proposal.

        Returns:
            Transaction hash of the proposal creation.
        """
        sender_address = self.web3.eth.account.from_key(sender_private_key).address
        nonce = self.web3.eth.get_transaction_count(sender_address)

        tx = self.contract.functions.createProposal(
            json.dumps(proposal_data),
            description
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, sender_private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()

    def vote_on_proposal(
        self,
        sender_private_key: str,
        proposal_id: int,
        support: bool,
        voting_power: int
    ) -> str:
        """
        Vote on a governance proposal.

        Args:
            sender_private_key: Private key of the voter.
            proposal_id: ID of the proposal to vote on.
            support: Boolean indicating support (True) or opposition (False).
            voting_power: Amount of voting power to use.

        Returns:
            Transaction hash of the vote.
        """
        sender_address = self.web3.eth.account.from_key(sender_private_key).address
        nonce = self.web3.eth.get_transaction_count(sender_address)

        tx = self.contract.functions.vote(
            proposal_id,
            support,
            voting_power
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, sender_private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()

    def execute_proposal(
        self,
        sender_private_key: str,
        proposal_id: int
    ) -> str:
        """
        Execute a proposal that has passed voting.

        Args:
            sender_private_key: Private key of the executor.
            proposal_id: ID of the proposal to execute.

        Returns:
            Transaction hash of the execution.
        """
        sender_address = self.web3.eth.account.from_key(sender_private_key).address
        nonce = self.web3.eth.get_transaction_count(sender_address)

        tx = self.contract.functions.executeProposal(
            proposal_id
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, sender_private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()

    def get_proposal_details(self, proposal_id: int) -> Dict:
        """
        Get details of a specific proposal.

        Args:
            proposal_id: ID of the proposal to query.

        Returns:
            Dictionary containing proposal details.
        """
        proposal = self.contract.functions.proposals(proposal_id).call()
        return {
            'id': proposal[0],
            'proposer': proposal[1],
            'data': proposal[2],
            'description': proposal[3],
            'start_block': proposal[4],
            'end_block': proposal[5],
            'for_votes': proposal[6],
            'against_votes': proposal[7],
            'executed': proposal[8]
        }

    def get_proposal_state(self, proposal_id: int) -> str:
        """
        Get the current state of a proposal.

        Args:
            proposal_id: ID of the proposal to query.

        Returns:
            String representing the proposal state.
        """
        state = self.contract.functions.state(proposal_id).call()
        states = {
            0: 'Pending',
            1: 'Active',
            2: 'Canceled',
            3: 'Defeated',
            4: 'Succeeded',
            5: 'Queued',
            6: 'Expired',
            7: 'Executed'
        }
        return states.get(state, 'Unknown')
```
