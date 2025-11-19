"""
Generated Code Metadata:
========================
Original URL: https://agora-next-exdgz5djw-voteagora.vercel.app
Prompt: How can I implement on-chain governance features using the Agora platform?
Generated: DETERMINISTIC_112b2863abac35fe
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from agora_sdk import Client, Transaction, GovernanceProposal, Vote
from typing import List, Dict, Optional
import json

class AgoraGovernance:
    """
    A class to interact with Agora's on-chain governance features.
    Handles proposal creation, voting, and querying governance state.
    """
    
    def __init__(self, node_url: str, chain_id: str, wallet_address: str, private_key: str):
        """
        Initialize the Agora governance client.
        
        Args:
            node_url: URL of the Agora node
            chain_id: Chain ID of the network
            wallet_address: Address of the wallet
            private_key: Private key for signing transactions
        """
        self.client = Client(node_url, chain_id)
        self.wallet_address = wallet_address
        self.private_key = private_key
        
    def create_proposal(
        self,
        title: str,
        description: str,
        metadata: Dict,
        deposit_amount: int,
        proposal_type: str = "text"
    ) -> str:
        """
        Create a new governance proposal.
        
        Args:
            title: Title of the proposal
            description: Description of the proposal
            metadata: Additional metadata as a dictionary
            deposit_amount: Amount to deposit with proposal
            proposal_type: Type of proposal (text, parameter_change, etc.)
            
        Returns:
            Transaction hash of the proposal creation
            
        Raises:
            Exception: If proposal creation fails
        """
        try:
            # Create proposal message
            proposal = GovernanceProposal(
                title=title,
                description=description,
                metadata=json.dumps(metadata),
                proposal_type=proposal_type,
                proposer=self.wallet_address,
                initial_deposit=deposit_amount
            )
            
            # Build and sign transaction
            tx = Transaction().add_message(proposal)
            signed_tx = tx.sign(self.private_key)
            
            # Broadcast transaction
            result = self.client.broadcast_tx(signed_tx)
            return result.tx_hash
            
        except Exception as e:
            raise Exception(f"Failed to create proposal: {str(e)}")
    
    def vote_on_proposal(self, proposal_id: int, vote_option: str, metadata: Optional[Dict] = None) -> str:
        """
        Vote on an existing governance proposal.
        
        Args:
            proposal_id: ID of the proposal to vote on
            vote_option: Vote option (yes, no, abstain, veto)
            metadata: Optional vote metadata
            
        Returns:
            Transaction hash of the vote
            
        Raises:
            Exception: If voting fails
        """
        try:
            # Create vote message
            vote = Vote(
                proposal_id=proposal_id,
                voter=self.wallet_address,
                option=vote_option,
                metadata=json.dumps(metadata) if metadata else ""
            )
            
            # Build and sign transaction
            tx = Transaction().add_message(vote)
            signed_tx = tx.sign(self.private_key)
            
            # Broadcast transaction
            result = self.client.broadcast_tx(signed_tx)
            return result.tx_hash
            
        except Exception as e:
            raise Exception(f"Failed to vote on proposal: {str(e)}")
    
    def get_proposal(self, proposal_id: int) -> Dict:
        """
        Query details of a specific proposal.
        
        Args:
            proposal_id: ID of the proposal to query
            
        Returns:
            Dictionary containing proposal details
            
        Raises:
            Exception: If query fails
        """
        try:
            return self.client.query_proposal(proposal_id)
        except Exception as e:
            raise Exception(f"Failed to get proposal: {str(e)}")
    
    def list_proposals(self, status: str = "all", limit: int = 100) -> List[Dict]:
        """
        List governance proposals with optional filters.
        
        Args:
            status: Filter by status (voting, passed, rejected, etc.)
            limit: Maximum number of proposals to return
            
        Returns:
            List of proposal dictionaries
            
        Raises:
            Exception: If query fails
        """
        try:
            return self.client.query_proposals(status, limit)
        except Exception as e:
            raise Exception(f"Failed to list proposals: {str(e)}")
    
    def get_proposal_tally(self, proposal_id: int) -> Dict:
        """
        Get the current tally of votes for a proposal.
        
        Args:
            proposal_id: ID of the proposal to query
            
        Returns:
            Dictionary containing vote tally
            
        Raises:
            Exception: If query fails
        """
        try:
            return self.client.query_tally(proposal_id)
        except Exception as e:
            raise Exception(f"Failed to get proposal tally: {str(e)}")
    
    def get_vote(self, proposal_id: int, voter_address: str) -> Dict:
        """
        Get a specific vote on a proposal.
        
        Args:
            proposal_id: ID of the proposal
            voter_address: Address of the voter
            
        Returns:
            Dictionary containing vote details
            
        Raises:
            Exception: If query fails
        """
        try:
            return self.client.query_vote(proposal_id, voter_address)
        except Exception as e:
            raise Exception(f"Failed to get vote: {str(e)}")
    
    def get_votes(self, proposal_id: int, limit: int = 100) -> List[Dict]:
        """
        Get all votes for a specific proposal.
        
        Args:
            proposal_id: ID of the proposal
            limit: Maximum number of votes to return
            
        Returns:
            List of vote dictionaries
            
        Raises:
            Exception: If query fails
        """
        try:
            return self.client.query_votes(proposal_id, limit)
        except Exception as e:
            raise Exception(f"Failed to get votes: {str(e)}")
```
