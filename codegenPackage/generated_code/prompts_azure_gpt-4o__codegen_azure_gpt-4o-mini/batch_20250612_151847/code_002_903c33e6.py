"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Create a Python program to simulate Proof-of-Stake mining for Ethereum Classic Vision, incorporating features such as staking rewards and penalties for malicious validators.
Generated: DETERMINISTIC_903c33e67aeac8c5
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class Validator:
    def __init__(self, name, stake):
        """
        Initialize a new validator with a name and a stake amount.
        
        :param name: str - The name of the validator
        :param stake: float - The amount of cryptocurrency staked by the validator
        """
        self.name = name
        self.stake = stake
        self.is_malicious = False
        self.rewards = 0.0

    def set_malicious(self):
        """Mark the validator as malicious."""
        self.is_malicious = True

    def reset_malicious(self):
        """Reset the malicious status of the validator."""
        self.is_malicious = False

    def calculate_reward(self):
        """
        Calculate rewards based on the stake and whether the validator is malicious.
        
        :return: float - The calculated reward
        """
        if self.is_malicious:
            penalty = self.stake * 0.5  # 50% penalty for malicious behavior
            self.rewards -= penalty
            return -penalty
        else:
            reward = self.stake * 0.1  # 10% reward for honest behavior
            self.rewards += reward
            return reward

class PoSNetwork:
    def __init__(self):
        """Initialize the Proof-of-Stake network with an empty list of validators."""
        self.validators = []

    def add_validator(self, validator):
        """
        Add a new validator to the network.
        
        :param validator: Validator - The validator to be added
        """
        self.validators.append(validator)

    def simulate_epoch(self):
        """
        Simulate an epoch where each validator can earn rewards or face penalties.
        """
        print("Simulating epoch...")
        for validator in self.validators:
            reward = validator.calculate_reward()
            status = "malicious" if validator.is_malicious else "honest"
            print(f"Validator {validator.name} ({status}): Reward/Penalty = {reward:.2f}, Total Rewards = {validator.rewards:.2f}")

    def randomize_malicious_behavior(self):
        """
        Randomly set some validators as malicious for simulation purposes.
        """
        for validator in self.validators:
            if random.random() < 0.2:  # 20% chance to be malicious
                validator.set_malicious()
            else:
                validator.reset_malicious()

def main():
    """
    Main function to run the Proof-of-Stake simulation.
    """
    # Create a PoS network
    pos_network = PoSNetwork()

    # Add validators with different stakes
    pos_network.add_validator(Validator("Validator1", 1000))
    pos_network.add_validator(Validator("Validator2", 2000))
    pos_network.add_validator(Validator("Validator3", 1500))

    # Simulate multiple epochs
    for epoch in range(5):
        print(f"\n--- Epoch {epoch + 1} ---")
        pos_network.randomize_malicious_behavior()
        pos_network.simulate_epoch()
        time.sleep(1)  # Sleep to simulate time passing between epochs

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
