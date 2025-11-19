"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Explain how Proof of Commitment DAOs use cryptocurrency staking to ensure member accountability in collective projects.
Generated: DETERMINISTIC_58cb564dfab43d3c
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
Proof of Commitment DAO Example
This script demonstrates how a Proof of Commitment DAO can use cryptocurrency staking
to ensure member accountability in collective projects. Members stake tokens to join the DAO,
and their stake is locked until the project is completed. If a member fails to fulfill their
commitment, their stake may be penalized or redistributed to other members.
"""

from typing import Dict, List
import time

class ProofOfCommitmentDAO:
    """
    A class representing a Proof of Commitment DAO.
    Members stake tokens to join the DAO and participate in collective projects.
    """

    def __init__(self, penalty_rate: float = 0.1):
        """
        Initialize the DAO with an empty member registry and a penalty rate.

        :param penalty_rate: The percentage of the stake to penalize for non-compliance (default: 10%).
        """
        self.members: Dict[str, float] = {}  # Member registry: {member_address: staked_amount}
        self.penalty_rate = penalty_rate  # Penalty rate for non-compliance

    def stake_tokens(self, member_address: str, amount: float) -> None:
        """
        Allow a member to stake tokens to join the DAO.

        :param member_address: The unique address of the member.
        :param amount: The amount of tokens to stake.
        :raises ValueError: If the staked amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        self.members[member_address] = self.members.get(member_address, 0) + amount
        print(f"Member {member_address} staked {amount} tokens.")

    def penalize_member(self, member_address: str) -> None:
        """
        Penalize a member for failing to fulfill their commitment.

        :param member_address: The unique address of the member to penalize.
        :raises KeyError: If the member does not exist in the registry.
        """
        if member_address not in self.members:
            raise KeyError(f"Member {member_address} not found in the DAO.")
        
        penalty = self.members[member_address] * self.penalty_rate
        self.members[member_address] -= penalty
        print(f"Member {member_address} penalized {penalty} tokens for non-compliance.")

    def complete_project(self) -> None:
        """
        Complete the project and unlock all staked tokens for members.
        """
        for member_address, staked_amount in self.members.items():
            print(f"Member {member_address} has been refunded {staked_amount} tokens.")
        self.members.clear()  # Clear all member stakes after project completion

    def get_member_stake(self, member_address: str) -> float:
        """
        Retrieve the staked amount for a specific member.

        :param member_address: The unique address of the member.
        :return: The staked amount for the member.
        :raises KeyError: If the member does not exist in the registry.
        """
        if member_address not in self.members:
            raise KeyError(f"Member {member_address} not found in the DAO.")
        
        return self.members[member_address]

# Example usage
if __name__ == "__main__":
    dao = ProofOfCommitmentDAO(penalty_rate=0.2)  # Initialize DAO with a 20% penalty rate

    try:
        # Members stake tokens
        dao.stake_tokens("member1", 100)
        dao.stake_tokens("member2", 200)

        # Penalize a member for non-compliance
        dao.penalize_member("member1")

        # Retrieve member stake
        print(f"Member1's stake: {dao.get_member_stake('member1')} tokens")

        # Complete the project and unlock all stakes
        dao.complete_project()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
