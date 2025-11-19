"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Create a simple application that illustrates how staking works in Ethereum, including the principles of Proof of Stake (PoS).
Generated: DETERMINISTIC_39ff953964b07b26
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_simulation.py
# A simple Python application to illustrate how staking works in Ethereum using Proof of Stake (PoS) principles.

import random

class Validator:
    """
    Represents a validator in the Ethereum Proof of Stake system.
    Validators stake ETH and are rewarded for validating blocks.
    """
    def __init__(self, name, stake):
        """
        Initialize a validator with a name and an initial stake.
        :param name: Name of the validator.
        :param stake: Amount of ETH staked by the validator.
        """
        self.name = name
        self.stake = stake
        self.rewards = 0

    def add_reward(self, reward):
        """
        Add rewards to the validator's account.
        :param reward: Amount of ETH rewarded.
        """
        self.rewards += reward

    def total_balance(self):
        """
        Calculate the total balance of the validator (stake + rewards).
        :return: Total balance in ETH.
        """
        return self.stake + self.rewards


class ProofOfStakeSimulation:
    """
    Simulates the Ethereum Proof of Stake mechanism.
    """
    def __init__(self):
        """
        Initialize the simulation with an empty list of validators.
        """
        self.validators = []

    def add_validator(self, name, stake):
        """
        Add a new validator to the simulation.
        :param name: Name of the validator.
        :param stake: Amount of ETH staked by the validator.
        """
        if stake <= 0:
            raise ValueError("Stake must be greater than 0 ETH.")
        self.validators.append(Validator(name, stake))

    def select_validator(self):
        """
        Select a validator to propose a block based on their stake.
        Validators with higher stakes have a higher probability of being selected.
        :return: Selected validator.
        """
        total_stake = sum(v.stake for v in self.validators)
        if total_stake == 0:
            raise ValueError("No validators with stake available.")
        
        # Weighted random selection based on stake
        weights = [v.stake / total_stake for v in self.validators]
        selected_validator = random.choices(self.validators, weights=weights, k=1)[0]
        return selected_validator

    def simulate_block_proposal(self, reward=2):
        """
        Simulate the process of proposing a block and rewarding the selected validator.
        :param reward: Amount of ETH rewarded for proposing a block (default: 2 ETH).
        """
        try:
            selected_validator = self.select_validator()
            selected_validator.add_reward(reward)
            print(f"Block proposed by {selected_validator.name}. Reward: {reward} ETH.")
        except ValueError as e:
            print(f"Error during block proposal: {e}")

    def display_validator_balances(self):
        """
        Display the total balance of all validators.
        """
        print("\nValidator Balances:")
        for validator in self.validators:
            print(f"{validator.name}: {validator.total_balance()} ETH")


# Main application logic
if __name__ == "__main__":
    # Initialize the simulation
    simulation = ProofOfStakeSimulation()

    # Add validators with their stakes
    simulation.add_validator("Alice", 10)
    simulation.add_validator("Bob", 20)
    simulation.add_validator("Charlie", 5)

    # Simulate block proposals
    for _ in range(5):  # Simulate 5 blocks
        simulation.simulate_block_proposal()

    # Display final balances
    simulation.display_validator_balances()
```

This code is a simple simulation of Ethereum's Proof of Stake mechanism, demonstrating how validators are selected based on their stake and rewarded for proposing blocks. It includes error handling, comments, and follows Python best practices.
