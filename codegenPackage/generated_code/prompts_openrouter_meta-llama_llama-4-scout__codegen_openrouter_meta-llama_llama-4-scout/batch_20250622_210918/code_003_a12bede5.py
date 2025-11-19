"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Design a staking and voting system for a DAO, ensuring that users with a minimum of 100,000 $MBDAO tokens have access to VIP features, including deal flow and DD reports.
Generated: DETERMINISTIC_a12bede595b2e973
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_and_voting_system.py

import hashlib
import logging
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    """Represents a user in the DAO."""

    def __init__(self, user_id: int, mbdao_balance: int):
        """
        Initializes a User object.

        Args:
        - user_id (int): Unique identifier for the user.
        - mbdao_balance (int): The user's current $MBDAO token balance.
        """
        self.user_id = user_id
        self.mbdao_balance = mbdao_balance
        self.vip_features = ["deal_flow", "dd_reports"] if mbdao_balance >= 100000 else []

    def __repr__(self):
        return f"User(user_id={self.user_id}, mbdao_balance={self.mbdao_balance})"


class StakingSystem:
    """Manages user staking and voting."""

    def __init__(self):
        """
        Initializes a StakingSystem object.

        Attributes:
        - users (Dict[int, User]): Mapping of user IDs to User objects.
        """
        self.users: Dict[int, User] = {}

    def add_user(self, user_id: int, mbdao_balance: int):
        """
        Adds a new user to the system.

        Args:
        - user_id (int): Unique identifier for the user.
        - mbdao_balance (int): The user's initial $MBDAO token balance.
        """
        self.users[user_id] = User(user_id, mbdao_balance)

    def stake(self, user_id: int, amount: int):
        """
        Increases a user's $MBDAO token balance.

        Args:
        - user_id (int): Unique identifier for the user.
        - amount (int): The amount of $MBDAO tokens to add.

        Raises:
        - ValueError: If the user does not exist or the amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if amount < 0:
            raise ValueError("Stake amount cannot be negative")

        self.users[user_id].mbdao_balance += amount
        self._update_vip_features(user_id)

    def unstake(self, user_id: int, amount: int):
        """
        Decreases a user's $MBDAO token balance.

        Args:
        - user_id (int): Unique identifier for the user.
        - amount (int): The amount of $MBDAO tokens to remove.

        Raises:
        - ValueError: If the user does not exist, the amount is negative, or the amount exceeds the user's balance.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if amount < 0:
            raise ValueError("Unstake amount cannot be negative")
        if amount > self.users[user_id].mbdao_balance:
            raise ValueError("Insufficient balance")

        self.users[user_id].mbdao_balance -= amount
        self._update_vip_features(user_id)

    def _update_vip_features(self, user_id: int):
        """
        Updates a user's VIP features based on their current balance.

        Args:
        - user_id (int): Unique identifier for the user.
        """
        user = self.users[user_id]
        if user.mbdao_balance >= 100000:
            user.vip_features = ["deal_flow", "dd_reports"]
        else:
            user.vip_features = []

    def get_user_vip_features(self, user_id: int) -> List[str]:
        """
        Retrieves a user's VIP features.

        Args:
        - user_id (int): Unique identifier for the user.

        Returns:
        - List[str]: A list of VIP features accessible to the user.

        Raises:
        - ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        return self.users[user_id].vip_features


class VotingSystem:
    """Manages voting for proposals."""

    def __init__(self, staking_system: StakingSystem):
        """
        Initializes a VotingSystem object.

        Args:
        - staking_system (StakingSystem): The staking system instance.
        """
        self.staking_system = staking_system
        self.proposals: Dict[int, Dict[str, int]] = {}

    def create_proposal(self, proposal_id: int):
        """
        Creates a new proposal.

        Args:
        - proposal_id (int): Unique identifier for the proposal.
        """
        self.proposals[proposal_id] = {"yes": 0, "no": 0}

    def vote(self, user_id: int, proposal_id: int, vote: str):
        """
        Casts a vote on a proposal.

        Args:
        - user_id (int): Unique identifier for the user.
        - proposal_id (int): Unique identifier for the proposal.
        - vote (str): The user's vote ("yes" or "no").

        Raises:
        - ValueError: If the user does not exist, the proposal does not exist, or the vote is invalid.
        """
        if user_id not in self.staking_system.users:
            raise ValueError("User does not exist")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote")

        self.proposals[proposal_id][vote] += 1

    def get_proposal_results(self, proposal_id: int) -> Dict[str, int]:
        """
        Retrieves the results of a proposal.

        Args:
        - proposal_id (int): Unique identifier for the proposal.

        Returns:
        - Dict[str, int]: A dictionary containing the "yes" and "no" vote counts.

        Raises:
        - ValueError: If the proposal does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        return self.proposals[proposal_id]


def main():
    staking_system = StakingSystem()
    voting_system = VotingSystem(staking_system)

    # Add users
    staking_system.add_user(1, 50000)
    staking_system.add_user(2, 150000)

    # Stake and unstake
    staking_system.stake(1, 60000)
    staking_system.unstake(2, 50000)

    # Get VIP features
    print(staking_system.get_user_vip_features(1))  # Output: ['deal_flow', 'dd_reports']
    print(staking_system.get_user_vip_features(2))  # Output: []

    # Create proposal and vote
    voting_system.create_proposal(1)
    voting_system.vote(1, 1, "yes")
    voting_system.vote(2, 1, "no")

    # Get proposal results
    print(voting_system.get_proposal_results(1))  # Output: {'yes': 1, 'no': 1}


if __name__ == "__main__":
    main()
```
