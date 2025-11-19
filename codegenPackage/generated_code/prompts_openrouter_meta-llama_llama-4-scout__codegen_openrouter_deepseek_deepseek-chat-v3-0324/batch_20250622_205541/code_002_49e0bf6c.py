"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Compare and contrast traditional DAOs with Proof of Commitment DAOs in terms of their approaches to member commitment and accountability.
Generated: DETERMINISTIC_49e0bf6c776d59a0
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares traditional DAOs with Proof of Commitment DAOs
in terms of member commitment and accountability.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class DAOType(Enum):
    TRADITIONAL = auto()
    PROOF_OF_COMMITMENT = auto()

@dataclass
class Member:
    id: str
    stake: float
    voting_power: float
    commitment_score: Optional[float] = None

@dataclass
class DAO:
    dao_type: DAOType
    members: List[Member]
    total_stake: float
    voting_threshold: float
    
    def calculate_voting_power(self) -> Dict[str, float]:
        """Calculate voting power based on DAO type"""
        voting_powers = {}
        
        if self.dao_type == DAOType.TRADITIONAL:
            for member in self.members:
                voting_powers[member.id] = member.stake / self.total_stake
        else:  # Proof of Commitment
            total_commitment = sum(m.commitment_score for m in self.members if m.commitment_score)
            for member in self.members:
                if member.commitment_score:
                    commitment_factor = member.commitment_score / total_commitment
                    stake_factor = member.stake / self.total_stake
                    voting_powers[member.id] = (commitment_factor + stake_factor) / 2
                else:
                    voting_powers[member.id] = 0
        
        return voting_powers
    
    def is_proposal_approved(self, votes: Dict[str, bool]) -> bool:
        """Check if proposal passes based on voting rules"""
        try:
            voting_powers = self.calculate_voting_power()
            total_approval = sum(
                voting_powers[member_id] 
                for member_id, vote in votes.items() 
                if vote and member_id in voting_powers
            )
            return total_approval >= self.voting_threshold
        except Exception as e:
            print(f"Error checking proposal approval: {e}")
            return False

def compare_daos(traditional_dao: DAO, poc_dao: DAO) -> Dict[str, str]:
    """Compare two DAOs and return key differences"""
    comparison = {}
    
    # Commitment comparison
    traditional_has_commitment = any(m.commitment_score for m in traditional_dao.members)
    poc_has_commitment = any(m.commitment_score for m in poc_dao.members)
    
    comparison["commitment_mechanism"] = (
        "Traditional: Based on stake only\n"
        "PoC: Combines stake and active commitment"
    )
    
    # Accountability comparison
    traditional_voting = traditional_dao.calculate_voting_power()
    poc_voting = poc_dao.calculate_voting_power()
    
    comparison["accountability"] = (
        f"Traditional: Voting power purely financial (max: {max(traditional_voting.values()):.2f})\n"
        f"PoC: Voting power combines finance and participation (max: {max(poc_voting.values()):.2f})"
    )
    
    # Example proposal comparison
    example_votes = {m.id: True for m in traditional_dao.members[:len(traditional_dao.members)//2]}
    traditional_result = traditional_dao.is_proposal_approved(example_votes)
    poc_result = poc_dao.is_proposal_approved(example_votes)
    
    comparison["proposal_outcome"] = (
        f"Same votes would {'pass' if traditional_result else 'fail'} in Traditional DAO\n"
        f"Same votes would {'pass' if poc_result else 'fail'} in PoC DAO"
    )
    
    return comparison

# Example usage
if __name__ == "__main__":
    # Create traditional DAO members
    traditional_members = [
        Member(id="1", stake=1000, voting_power=0),
        Member(id="2", stake=2000, voting_power=0),
        Member(id="3", stake=3000, voting_power=0)
    ]
    
    # Create PoC DAO members with commitment scores
    poc_members = [
        Member(id="1", stake=1000, voting_power=0, commitment_score=0.8),
        Member(id="2", stake=2000, voting_power=0, commitment_score=0.5),
        Member(id="3", stake=3000, voting_power=0, commitment_score=0.2)
    ]
    
    # Create DAO instances
    traditional_dao = DAO(
        dao_type=DAOType.TRADITIONAL,
        members=traditional_members,
        total_stake=6000,
        voting_threshold=0.5
    )
    
    poc_dao = DAO(
        dao_type=DAOType.PROOF_OF_COMMITMENT,
        members=poc_members,
        total_stake=6000,
        voting_threshold=0.5
    )
    
    # Compare the DAOs
    results = compare_daos(traditional_dao, poc_dao)
    
    # Print comparison results
    for key, value in results.items():
        print(f"{key.upper()}:\n{value}\n")
```
