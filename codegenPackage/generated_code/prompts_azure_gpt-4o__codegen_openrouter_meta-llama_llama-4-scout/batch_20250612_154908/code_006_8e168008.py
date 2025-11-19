"""
Generated Code Metadata:
========================
Original URL: https://delegationonbeam.com
Prompt: Generate code to implement a referral system for the Beam Nodes Delegation Dashboard, ensuring rewards are distributed accurately.
Generated: DETERMINISTIC_8e1680083a8628b4
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

from typing import Dict, List
from datetime import datetime, timedelta

class ReferralSystem:
    def __init__(self, referral_rate: float, min_delegation: float):
        """
        Initialize the referral system.

        Args:
        - referral_rate (float): The percentage of rewards to be distributed to referrers.
        - min_delegation (float): The minimum delegation required for a node to be eligible for referrals.
        """
        self.referral_rate = referral_rate
        self.min_delegation = min_delegation
        self.referrals: Dict[str, List[str]] = {}  # Mapping of referrer to referees
        self.delegations: Dict[str, float] = {}  # Mapping of node to delegation amount
        self.rewards: Dict[str, float] = {}  # Mapping of node to reward amount

    def add_referral(self, referrer: str, referee: str):
        """
        Add a referral relationship between two nodes.

        Args:
        - referrer (str): The node that referred the new node.
        - referee (str): The new node that was referred.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referee)

    def update_delegation(self, node: str, delegation: float):
        """
        Update the delegation amount for a node.

        Args:
        - node (str): The node to update.
        - delegation (float): The new delegation amount.
        """
        self.delegations[node] = delegation

    def calculate_rewards(self):
        """
        Calculate the rewards for each node based on the referral system.

        Returns:
        - A dictionary mapping each node to its reward amount.
        """
        # Calculate total rewards
        total_rewards = sum(self.delegations.values())

        # Calculate rewards for each node
        for node, delegation in self.delegations.items():
            if delegation >= self.min_delegation:
                # Calculate reward for node
                reward = delegation * 0.1  # Assuming 10% reward rate
                self.rewards[node] = reward

                # Distribute rewards to referrers
                referrer = self.get_referrer(node)
                if referrer:
                    referral_reward = reward * self.referral_rate / 100
                    self.rewards[referrer] = self.rewards.get(referrer, 0) + referral_reward

        return self.rewards

    def get_referrer(self, node: str) -> str:
        """
        Get the referrer for a given node.

        Args:
        - node (str): The node to find the referrer for.

        Returns:
        - The referrer node, or None if not found.
        """
        for referrer, referees in self.referrals.items():
            if node in referees:
                return referrer
        return None

    def distribute_rewards(self):
        """
        Distribute rewards to nodes.

        Raises:
        - Exception: If there are not enough rewards to distribute.
        """
        # Check if there are enough rewards to distribute
        total_rewards = sum(self.rewards.values())
        if total_rewards == 0:
            raise Exception("Not enough rewards to distribute")

        # Distribute rewards
        for node, reward in self.rewards.items():
            print(f"Distributing reward of {reward} to node {node}")


def main():
    referral_system = ReferralSystem(referral_rate=10, min_delegation=100)

    # Add referrals
    referral_system.add_referral("Node1", "Node2")
    referral_system.add_referral("Node1", "Node3")

    # Update delegations
    referral_system.update_delegation("Node1", 1000)
    referral_system.update_delegation("Node2", 500)
    referral_system.update_delegation("Node3", 2000)

    # Calculate rewards
    rewards = referral_system.calculate_rewards()

    # Distribute rewards
    referral_system.distribute_rewards()


if __name__ == "__main__":
    main()
```
