"""
Generated Code Metadata:
========================
Original URL: https://beraborrow.org
Prompt: "Explain how to implement a token rewards proposal similar to the one on Beraborrow using Python and relevant libraries."
Generated: DETERMINISTIC_c9334bccd22a0597
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError
from eth_typing import Address, ChecksumAddress
from eth_utils import to_checksum_address

@dataclass
class Proposal:
    id: int
    creator: ChecksumAddress
    title: str
    description: str
    token_rewards: Dict[str, float]  # token_address: amount
    start_time: datetime
    end_time: datetime
    votes_for: int = 0
    votes_against: int = 0
    executed: bool = False

class TokenRewardsProposalSystem:
    """
    A system to manage token rewards proposals similar to Beraborrow.
    Handles proposal creation, voting, execution, and reward distribution.
    """
    
    def __init__(self, web3: Web3, governance_token_address: str, proposal_contract_address: str):
        """
        Initialize the proposal system with Web3 connection and contract addresses.
        
        Args:
            web3: Web3 instance connected to the blockchain
            governance_token_address: Address of the governance token contract
            proposal_contract_address: Address of the proposal contract
        """
        self.web3 = web3
        self.governance_token_address = to_checksum_address(governance_token_address)
        self.proposal_contract_address = to_checksum_address(proposal_contract_address)
        
        # Load contract ABIs (in a real implementation, these would be loaded from files)
        with open('GovernanceTokenABI.json') as f:
            governance_token_abi = json.load(f)
        with open('ProposalContractABI.json') as f:
            proposal_contract_abi = json.load(f)
            
        self.governance_token = self.web3.eth.contract(
            address=self.governance_token_address,
            abi=governance_token_abi
        )
        self.proposal_contract = self.web3.eth.contract(
            address=self.proposal_contract_address,
            abi=proposal_contract_abi
        )
        
        self.proposals: Dict[int, Proposal] = {}
        self.next_proposal_id = 1
        
    def create_proposal(
        self,
        creator: str,
        title: str,
        description: str,
        token_rewards: Dict[str, float],
        duration_days: int
    ) -> int:
        """
        Create a new token rewards proposal.
        
        Args:
            creator: Address of the proposal creator
            title: Title of the proposal
            description: Description of the proposal
            token_rewards: Dictionary of token addresses and reward amounts
            duration_days: Duration of the voting period in days
            
        Returns:
            Proposal ID
        """
        creator_address = to_checksum_address(creator)
        start_time = datetime.now()
        end_time = start_time + timedelta(days=duration_days)
        
        # Validate token rewards
        for token_address in token_rewards:
            to_checksum_address(token_address)  # Validates address format
            
        proposal = Proposal(
            id=self.next_proposal_id,
            creator=creator_address,
            title=title,
            description=description,
            token_rewards=token_rewards,
            start_time=start_time,
            end_time=end_time
        )
        
        self.proposals[self.next_proposal_id] = proposal
        self.next_proposal_id += 1
        
        try:
            # On-chain proposal creation
            tx_hash = self.proposal_contract.functions.createProposal(
                proposal.id,
                proposal.title,
                proposal.description,
                list(proposal.token_rewards.keys()),
                list(proposal.token_rewards.values()),
                int(proposal.start_time.timestamp()),
                int(proposal.end_time.timestamp())
            ).transact({'from': creator_address})
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Proposal creation transaction failed")
                
        except ContractLogicError as e:
            raise Exception(f"Proposal creation failed: {e}")
            
        return proposal.id
    
    def vote(self, voter: str, proposal_id: int, support: bool) -> None:
        """
        Vote on a proposal.
        
        Args:
            voter: Address of the voter
            proposal_id: ID of the proposal to vote on
            support: True for yes, False for no
        """
        voter_address = to_checksum_address(voter)
        
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
            
        proposal = self.proposals[proposal_id]
        
        if datetime.now() < proposal.start_time:
            raise Exception("Voting has not started yet")
        if datetime.now() > proposal.end_time:
            raise Exception("Voting has ended")
            
        try:
            # Check voter balance
            balance = self.governance_token.functions.balanceOf(voter_address).call()
            if balance == 0:
                raise Exception("Voter has no governance tokens")
                
            # On-chain vote
            tx_hash = self.proposal_contract.functions.vote(
                proposal_id,
                support
            ).transact({'from': voter_address})
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Vote transaction failed")
                
            # Update local proposal state
            if support:
                proposal.votes_for += 1
            else:
                proposal.votes_against += 1
                
        except ContractLogicError as e:
            raise Exception(f"Voting failed: {e}")
    
    def execute_proposal(self, proposal_id: int, executor: str) -> None:
        """
        Execute a successful proposal and distribute rewards.
        
        Args:
            proposal_id: ID of the proposal to execute
            executor: Address executing the proposal
        """
        executor_address = to_checksum_address(executor)
        
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
            
        proposal = self.proposals[proposal_id]
        
        if proposal.executed:
            raise Exception("Proposal already executed")
        if datetime.now() < proposal.end_time:
            raise Exception("Voting period has not ended")
            
        # Check if proposal passed
        total_votes = proposal.votes_for + proposal.votes_against
        if total_votes == 0 or proposal.votes_for <= proposal.votes_against:
            raise Exception("Proposal did not pass")
            
        try:
            # On-chain execution
            tx_hash = self.proposal_contract.functions.executeProposal(
                proposal_id,
                list(proposal.token_rewards.keys()),
                list(proposal.token_rewards.values())
            ).transact({'from': executor_address})
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Proposal execution failed")
                
            proposal.executed = True
            
        except ContractLogicError as e:
            raise Exception(f"Proposal execution failed: {e}")
    
    def get_proposal(self, proposal_id: int) -> Optional[Proposal]:
        """
        Get proposal details.
        
        Args:
            proposal_id: ID of the proposal
            
        Returns:
            Proposal object or None if not found
        """
        return self.proposals.get(proposal_id)
    
    def get_active_proposals(self) -> List[Proposal]:
        """
        Get all active proposals (voting period ongoing).
        
        Returns:
            List of active proposals
        """
        now = datetime.now()
        return [
            p for p in self.proposals.values()
            if p.start_time <= now <= p.end_time and not p.executed
        ]
```
