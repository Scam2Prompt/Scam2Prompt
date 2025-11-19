"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-in.pages.dev
Prompt: How can I use the InQubeta platform's governance feature as a $QUBE token holder to propose and vote on platform development decisions, and what are the benefits of participating in the decision-making process?
Generated: DETERMINISTIC_575f1814e2774fc7
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from web3 import Web3
from typing import Dict, List, Optional
import json

class InQubetaGovernance:
    """
    A class to interact with InQubeta's governance features using $QUBE tokens.
    Allows token holders to propose and vote on platform development decisions.
    """
    
    def __init__(self, provider_url: str, contract_address: str, abi_path: str):
        """
        Initialize the governance interface.
        
        Args:
            provider_url: URL of the Ethereum provider (e.g., Infura)
            contract_address: Address of the governance smart contract
            abi_path: Path to the contract ABI JSON file
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum provider")
            
        with open(abi_path) as f:
            abi = json.load(f)
            
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        
    def create_proposal(
        self,
        private_key: str,
        title: str,
        description: str,
        options: List[str],
        duration_days: int
    ) -> str:
        """
        Create a new governance proposal.
        
        Args:
            private_key: Private key of the proposer
            title: Title of the proposal
            description: Detailed description
            options: List of voting options
            duration_days: Voting duration in days
            
        Returns:
            Transaction hash of the proposal creation
        """
        account = self.web3.eth.account.from_key(private_key)
        
        try:
            tx = self.contract.functions.createProposal(
                title,
                description,
                options,
                duration_days
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = account.sign_transaction(tx)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
            
        except Exception as e:
            raise Exception(f"Failed to create proposal: {str(e)}")
            
    def vote(
        self,
        private_key: str,
        proposal_id: int,
        option_index: int,
        vote_weight: int
    ) -> str:
        """
        Vote on an existing proposal.
        
        Args:
            private_key: Private key of the voter
            proposal_id: ID of the proposal to vote on
            option_index: Index of the selected option
            vote_weight: Amount of $QUBE tokens to use as voting weight
            
        Returns:
            Transaction hash of the vote
        """
        account = self.web3.eth.account.from_key(private_key)
        
        try:
            tx = self.contract.functions.vote(
                proposal_id,
                option_index,
                vote_weight
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = account.sign_transaction(tx)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
            
        except Exception as e:
            raise Exception(f"Failed to vote: {str(e)}")
            
    def get_proposal(self, proposal_id: int) -> Dict:
        """
        Get details of a specific proposal.
        
        Args:
            proposal_id: ID of the proposal
            
        Returns:
            Dictionary containing proposal details
        """
        try:
            proposal = self.contract.functions.getProposal(proposal_id).call()
            return {
                'id': proposal[0],
                'title': proposal[1],
                'description': proposal[2],
                'options': proposal[3],
                'creator': proposal[4],
                'start_time': proposal[5],
                'end_time': proposal[6],
                'status': proposal[7]
            }
        except Exception as e:
            raise Exception(f"Failed to get proposal: {str(e)}")
            
    def get_voting_results(self, proposal_id: int) -> Dict[str, int]:
        """
        Get voting results for a proposal.
        
        Args:
            proposal_id: ID of the proposal
            
        Returns:
            Dictionary mapping option names to vote counts
        """
        try:
            proposal = self.get_proposal(proposal_id)
            results = {}
            
            for i, option in enumerate(proposal['options']):
                votes = self.contract.functions.getVotes(proposal_id, i).call()
                results[option] = votes
                
            return results
            
        except Exception as e:
            raise Exception(f"Failed to get voting results: {str(e)}")
            
    def get_voter_power(self, address: str) -> int:
        """
        Get the voting power of a specific address.
        
        Args:
            address: Ethereum address to check
            
        Returns:
            Voting power in $QUBE tokens
        """
        try:
            return self.contract.functions.getVotingPower(address).call()
        except Exception as e:
            raise Exception(f"Failed to get voter power: {str(e)}")
```
