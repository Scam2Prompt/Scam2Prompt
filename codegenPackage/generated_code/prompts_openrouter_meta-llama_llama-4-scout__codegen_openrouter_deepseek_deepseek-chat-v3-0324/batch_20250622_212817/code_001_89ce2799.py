"""
Generated Code Metadata:
========================
Original URL: https://polkadot.org
Prompt: How does Polkadot's governance model work, and what role does the DOT token play in decision-making processes?
Generated: DETERMINISTIC_89ce2799164593fe
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified simulation of Polkadot's governance model
# and the role of DOT tokens in decision-making processes.

import random
from typing import List, Dict, Optional

class PolkadotGovernanceSimulator:
    """
    Simulates Polkadot's governance model including:
    - Referenda
    - Council voting
    - DOT token holder voting
    - Treasury proposals
    """
    
    def __init__(self, total_dot_supply: int):
        self.total_dot_supply = total_dot_supply
        self.council_members: List[str] = []
        self.active_referenda: List[Dict] = []
        self.treasury_proposals: List[Dict] = []
        self.voters: Dict[str, int] = {}  # voter_address: dot_balance
        
    def add_council_member(self, address: str) -> None:
        """Add a new council member to the governance system."""
        if address not in self.council_members:
            self.council_members.append(address)
    
    def register_voter(self, address: str, dot_balance: int) -> None:
        """Register a voter with their DOT token balance."""
        if dot_balance <= 0:
            raise ValueError("DOT balance must be positive")
        self.voters[address] = dot_balance
    
    def create_referendum(self, proposal: str, proposer: str) -> Dict:
        """
        Create a new referendum proposal.
        Returns the referendum details.
        """
        if proposer not in self.voters:
            raise ValueError("Proposer must be a registered voter")
            
        referendum = {
            'id': len(self.active_referenda) + 1,
            'proposal': proposal,
            'proposer': proposer,
            'ayes': 0,  # Votes in favor
            'nays': 0,  # Votes against
            'total_voted_dot': 0,
            'passed': False,
            'executed': False
        }
        self.active_referenda.append(referendum)
        return referendum
    
    def vote_on_referendum(
        self, 
        referendum_id: int, 
        voter: str, 
        vote: bool, 
        conviction: int = 1
    ) -> None:
        """
        Vote on a referendum with conviction multiplier.
        conviction: 1-6 where higher means longer lockup period
        """
        if referendum_id > len(self.active_referenda):
            raise ValueError("Invalid referendum ID")
            
        if voter not in self.voters:
            raise ValueError("Voter not registered")
            
        if conviction < 1 or conviction > 6:
            raise ValueError("Conviction must be between 1-6")
            
        referendum = self.active_referenda[referendum_id - 1]
        dot_weight = self.voters[voter] * conviction
        
        if vote:
            referendum['ayes'] += dot_weight
        else:
            referendum['nays'] += dot_weight
            
        referendum['total_voted_dot'] += dot_weight
    
    def tally_referendum(self, referendum_id: int) -> bool:
        """
        Tally votes for a referendum and determine if it passes.
        Polkadot uses adaptive quorum biasing for threshold calculation.
        """
        if referendum_id > len(self.active_referenda):
            raise ValueError("Invalid referendum ID")
            
        referendum = self.active_referenda[referendum_id - 1]
        
        # Simplified threshold calculation
        total_possible_votes = sum(self.voters.values()) * 6  # Max conviction
        turnout = referendum['total_voted_dot'] / total_possible_votes
        
        # Positive turnout bias (simplified from Polkadot's actual mechanism)
        threshold = 0.5 + (turnout * 0.3)
        
        if referendum['ayes'] / referendum['total_voted_dot'] > threshold:
            referendum['passed'] = True
            return True
        return False
    
    def execute_referendum(self, referendum_id: int) -> None:
        """Execute a passed referendum."""
        if referendum_id > len(self.active_referenda):
            raise ValueError("Invalid referendum ID")
            
        referendum = self.active_referenda[referendum_id - 1]
        
        if not referendum['passed']:
            raise ValueError("Referendum must pass before execution")
            
        referendum['executed'] = True
    
    def create_treasury_proposal(self, amount: int, beneficiary: str, proposer: str) -> Dict:
        """Create a new treasury proposal."""
        if proposer not in self.voters:
            raise ValueError("Proposer must be a registered voter")
            
        proposal = {
            'id': len(self.treasury_proposals) + 1,
            'amount': amount,
            'beneficiary': beneficiary,
            'proposer': proposer,
            'council_approvals': 0,
            'community_approvals': 0,
            'approved': False
        }
        self.treasury_proposals.append(proposal)
        return proposal
    
    def council_vote_on_proposal(self, proposal_id: int, council_member: str, approve: bool) -> None:
        """Council member votes on a treasury proposal."""
        if proposal_id > len(self.treasury_proposals):
            raise ValueError("Invalid proposal ID")
            
        if council_member not in self.council_members:
            raise ValueError("Not a council member")
            
        proposal = self.treasury_proposals[proposal_id - 1]
        
        if approve:
            proposal['council_approvals'] += 1
        else:
            proposal['council_approvals'] = max(0, proposal['council_approvals'] - 1)
    
    def community_vote_on_proposal(self, proposal_id: int, voter: str, approve: bool) -> None:
        """DOT holders vote on a treasury proposal."""
        if proposal_id > len(self.treasury_proposals):
            raise ValueError("Invalid proposal ID")
            
        if voter not in self.voters:
            raise ValueError("Voter not registered")
            
        proposal = self.treasury_proposals[proposal_id - 1]
        dot_weight = self.voters[voter]
        
        if approve:
            proposal['community_approvals'] += dot_weight
        else:
            proposal['community_approvals'] = max(0, proposal['community_approvals'] - dot_weight)
    
    def approve_treasury_proposal(self, proposal_id: int) -> bool:
        """
        Determine if a treasury proposal is approved based on council and community votes.
        Simplified approval logic compared to Polkadot's actual mechanism.
        """
        if proposal_id > len(self.treasury_proposals):
            raise ValueError("Invalid proposal ID")
            
        proposal = self.treasury_proposals[proposal_id - 1]
        
        # Simplified approval criteria
        council_threshold = len(self.council_members) // 2 + 1
        community_threshold = self.total_dot_supply * 0.1  # 10% of total DOT
        
        if (proposal['council_approvals'] >= council_threshold and
            proposal['community_approvals'] >= community_threshold):
            proposal['approved'] = True
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Initialize governance with 1 billion DOT total supply
    governance = PolkadotGovernanceSimulator(total_dot_supply=1_000_000_000)
    
    # Register some voters with DOT balances
    governance.register_voter("Alice", 50_000_000)  # 50M DOT
    governance.register_voter("Bob", 30_000_000)   # 30M DOT
    governance.register_voter("Charlie", 20_000_000)  # 20M DOT
    
    # Add council members
    governance.add_council_member("Council1")
    governance.add_council_member("Council2")
    governance.add_council_member("Council3")
    
    # Create and vote on a referendum
    referendum = governance.create_referendum("Upgrade runtime to v2.0", "Alice")
    governance.vote_on_referendum(referendum['id'], "Alice", True, conviction=2)
    governance.vote_on_referendum(referendum['id'], "Bob", False, conviction=1)
    governance.vote_on_referendum(referendum['id'], "Charlie", True, conviction=3)
    
    # Tally and execute if passed
    if governance.tally_referendum(referendum['id']):
        governance.execute_referendum(referendum['id'])
        print(f"Referendum {referendum['id']} executed!")
    
    # Create and vote on a treasury proposal
    proposal = governance.create_treasury_proposal(1_000_000, "DeveloperTeam", "Bob")
    governance.council_vote_on_proposal(proposal['id'], "Council1", True)
    governance.council_vote_on_proposal(proposal['id'], "Council2", True)
    governance.community_vote_on_proposal(proposal['id'], "Alice", True)
    governance.com
