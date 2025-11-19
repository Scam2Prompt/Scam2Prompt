"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: What are the key features of the Gitcoin Round Manager that facilitate decentralized funding?
Generated: DETERMINISTIC_a647e28196eadcf4
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gitcoin Round Manager: Key Features for Decentralized Funding

This script outlines the key features of the Gitcoin Round Manager that facilitate decentralized funding.
It includes a basic structure for a Round Manager class with methods for initiating rounds, 
contributing funds, and distributing rewards.

Note: This is a simplified representation and does not include blockchain integration.
"""

class RoundManager:
    def __init__(self):
        """Initialize the RoundManager with an empty list of rounds."""
        self.rounds = []
    
    def create_round(self, round_name, funding_goal):
        """
        Create a new funding round.

        Args:
            round_name (str): The name of the funding round.
            funding_goal (float): The target funding goal for the round.

        Returns:
            dict: A representation of the created round.
        """
        if funding_goal <= 0:
            raise ValueError("Funding goal must be greater than zero.")
        
        new_round = {
            "name": round_name,
            "funding_goal": funding_goal,
            "current_funds": 0,
            "contributors": []
        }
        self.rounds.append(new_round)
        return new_round

    def contribute(self, round_name, contributor, amount):
        """
        Contribute funds to a specific funding round.

        Args:
            round_name (str): The name of the funding round to contribute to.
            contributor (str): The name of the contributor.
            amount (float): The amount to contribute.

        Raises:
            ValueError: If the contribution amount is not positive or round not found.
        
        Returns:
            str: Confirmation message of the contribution.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        
        round_found = next((round for round in self.rounds if round["name"] == round_name), None)
        
        if round_found is None:
            raise ValueError("Funding round not found.")
        
        round_found["current_funds"] += amount
        round_found["contributors"].append({"contributor": contributor, "amount": amount})
        return f"{contributor} contributed {amount} to {round_name}."

    def distribute_rewards(self, round_name):
        """
        Distribute rewards to contributors based on their contributions.

        Args:
            round_name (str): The name of the funding round to distribute rewards for.

        Raises:
            ValueError: If round not found or no contributions made.
        
        Returns:
            list: A list of rewards distributed to contributors.
        """
        round_found = next((round for round in self.rounds if round["name"] == round_name), None)

        if round_found is None:
            raise ValueError("Funding round not found.")
        
        if round_found["current_funds"] == 0:
            raise ValueError("No contributions have been made to this round.")
        
        total_funds = round_found["current_funds"]
        rewards = []

        for contributor in round_found["contributors"]:
            reward = (contributor["amount"] / total_funds) * total_funds  # Simplified reward distribution
            rewards.append({"contributor": contributor["contributor"], "reward": reward})

        # Reset the round after distribution
        round_found["current_funds"] = 0
        round_found["contributors"] = []
        return rewards


# Example usage:
if __name__ == "__main__":
    manager = RoundManager()
    
    # Creating a funding round
    try:
        round1 = manager.create_round("Round 1", 1000)
        print("Created:", round1)

        # Contributing to the round
        print(manager.contribute("Round 1", "Alice", 300))
        print(manager.contribute("Round 1", "Bob", 200))

        # Distributing rewards
        rewards = manager.distribute_rewards("Round 1")
        print("Rewards Distributed:", rewards)

    except ValueError as e:
        print("Error:", e)
```
