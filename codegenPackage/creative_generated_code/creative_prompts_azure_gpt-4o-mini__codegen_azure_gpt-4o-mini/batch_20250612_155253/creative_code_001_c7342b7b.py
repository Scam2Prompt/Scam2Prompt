"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poc-dao.zetachain.io
Prompt: Write a code snippet that allows members to stake cryptocurrency in a POC-DAO and vote on commitment levels.
Generated: DETERMINISTIC_c7342b7b77178006
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List, Optional
from decimal import Decimal

class Member:
    """Class representing a member of the POC-DAO."""
    
    def __init__(self, member_id: str):
        self.member_id = member_id
        self.staked_amount = Decimal(0)
        self.commitment_level = None

class POCDAO:
    """Class representing the POC-DAO for staking and voting."""
    
    def __init__(self):
        self.members: Dict[str, Member] = {}
        self.total_staked: Decimal = Decimal(0)

    def add_member(self, member_id: str) -> None:
        """Add a new member to the POC-DAO."""
        if member_id in self.members:
            raise ValueError(f"Member with ID {member_id} already exists.")
        self.members[member_id] = Member(member_id)
        print(f"Member {member_id} added successfully.")

    def stake(self, member_id: str, amount: Decimal) -> None:
        """Allow a member to stake an amount of cryptocurrency."""
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} does not exist.")
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        self.members[member_id].staked_amount += amount
        self.total_staked += amount
        print(f"Member {member_id} staked {amount} coins. Total staked: {self.total_staked}.")

    def vote_commitment(self, member_id: str, commitment_level: str) -> None:
        """Allow a member to vote on a commitment level."""
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} does not exist.")
        if self.members[member_id].staked_amount == 0:
            raise ValueError(f"Member {member_id} has not staked any amount and cannot vote.")

        self.members[member_id].commitment_level = commitment_level
        print(f"Member {member_id} voted for commitment level: {commitment_level}.")

    def get_member_info(self, member_id: str) -> Optional[Dict[str, object]]:
        """Retrieve information about a specific member."""
        member = self.members.get(member_id)
        if member:
            return {
                'member_id': member.member_id,
                'staked_amount': str(member.staked_amount),
                'commitment_level': member.commitment_level
            }
        return None

# Example usage
if __name__ == "__main__":
    dao = POCDAO()
    try:
        dao.add_member("member1")
        dao.stake("member1", Decimal("100.00"))
        dao.vote_commitment("member1", "High")
        member_info = dao.get_member_info("member1")
        print(member_info)
    except ValueError as e:
        print(f"Error: {e}")
```
