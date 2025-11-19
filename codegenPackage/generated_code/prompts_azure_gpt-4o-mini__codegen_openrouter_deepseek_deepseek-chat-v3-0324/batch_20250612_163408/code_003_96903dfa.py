"""
Generated Code Metadata:
========================
Original URL: https://docs.matrixinfos.com
Prompt: Provide an example of how to implement community-driven features in a blockchain project using the principles outlined in the $MATRIX whitepaper.
Generated: DETERMINISTIC_96903dfa8b9468fe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_community.py
"""
Implementation of community-driven features for a blockchain project inspired by $MATRIX principles.
Includes governance, proposal voting, and reward distribution mechanisms.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime, timedelta
import secrets

class BlockchainCommunity:
    """
    A class representing a community-driven blockchain network with governance features.
    """
    
    def __init__(self):
        self.members: Dict[str, int] = {}  # address: voting_power
        self.proposals: List[Proposal] = []
        self.rewards_pool: int = 0
        self.block_height: int = 0
        self.transaction_history: List[Dict] = []
        
    def add_member(self, address: str, initial_stake: int) -> bool:
        """
        Add a new member to the community with initial stake.
        Returns True if successful, False if member already exists.
        """
        if address in self.members:
            return False
            
        if initial_stake <= 0:
            raise ValueError("Initial stake must be positive")
            
        self.members[address] = initial_stake
        self._record_transaction(
            "member_added",
            {"address": address, "stake": initial_stake}
        )
        return True
    
    def create_proposal(self, creator: str, description: str, duration_days: int) -> Optional[str]:
        """
        Create a new governance proposal.
        Returns proposal ID if successful, None if creator is not a member.
        """
        if creator not in self.members:
            return None
            
        proposal_id = self._generate_proposal_id(creator, description)
        end_time = datetime.now() + timedelta(days=duration_days)
        
        proposal = Proposal(
            id=proposal_id,
            creator=creator,
            description=description,
            created_at=datetime.now(),
            end_time=end_time,
            votes_for=0,
            votes_against=0,
            voters=set()
        )
        
        self.proposals.append(proposal)
        self._record_transaction(
            "proposal_created",
            {"id": proposal_id, "creator": creator, "description": description}
        )
        return proposal_id
    
    def vote_on_proposal(self, voter: str, proposal_id: str, vote: bool) -> bool:
        """
        Vote on a proposal.
        Returns True if vote was recorded, False if invalid vote.
        """
        if voter not in self.members:
            return False
            
        proposal = self._get_proposal(proposal_id)
        if not proposal or datetime.now() > proposal.end_time:
            return False
            
        if voter in proposal.voters:
            return False
            
        voting_power = self.members[voter]
        if vote:
            proposal.votes_for += voting_power
        else:
            proposal.votes_against += voting_power
            
        proposal.voters.add(voter)
        self._record_transaction(
            "vote_cast",
            {"voter": voter, "proposal_id": proposal_id, "vote": vote, "power": voting_power}
        )
        return True
    
    def execute_proposal(self, proposal_id: str) -> bool:
        """
        Execute a proposal if it has passed and deadline has expired.
        Returns True if executed, False if not passed or already executed.
        """
        proposal = self._get_proposal(proposal_id)
        if not proposal or datetime.now() < proposal.end_time:
            return False
            
        if proposal.votes_for <= proposal.votes_against:
            return False
            
        # In a real implementation, this would execute the proposal's action
        self._record_transaction(
            "proposal_executed",
            {"id": proposal_id, "votes_for": proposal.votes_for, "votes_against": proposal.votes_against}
        )
        return True
    
    def distribute_rewards(self, amount: int) -> Dict[str, int]:
        """
        Distribute rewards from the rewards pool proportionally to members' stakes.
        Returns dict of address: reward_amount.
        """
        if amount <= 0 or amount > self.rewards_pool:
            raise ValueError("Invalid reward amount")
            
        total_stake = sum(self.members.values())
        if total_stake == 0:
            return {}
            
        distributions = {}
        for address, stake in self.members.items():
            reward = (stake * amount) // total_stake
            if reward > 0:
                distributions[address] = reward
                self._record_transaction(
                    "reward_distributed",
                    {"address": address, "amount": reward}
                )
                
        self.rewards_pool -= amount
        return distributions
    
    def _get_proposal(self, proposal_id: str) -> Optional['Proposal']:
        """Helper to find a proposal by ID."""
        for prop in self.proposals:
            if prop.id == proposal_id:
                return prop
        return None
    
    def _generate_proposal_id(self, creator: str, description: str) -> str:
        """Generate a unique proposal ID."""
        salt = secrets.token_hex(4)
        data = f"{creator}{description}{salt}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    def _record_transaction(self, tx_type: str, data: Dict) -> None:
        """Record a transaction in the blockchain."""
        tx = {
            "type": tx_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
            "block": self.block_height
        }
        self.transaction_history.append(tx)
        self.block_height += 1

@dataclass
class Proposal:
    """Data class representing a governance proposal."""
    id: str
    creator: str
    description: str
    created_at: datetime
    end_time: datetime
    votes_for: int
    votes_against: int
    voters: set
```
