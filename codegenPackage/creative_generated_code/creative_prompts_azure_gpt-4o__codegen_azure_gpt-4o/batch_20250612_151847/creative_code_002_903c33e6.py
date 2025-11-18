"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Create a Python program to simulate Proof-of-Stake mining for Ethereum Classic Vision, incorporating features such as staking rewards and penalties for malicious validators.
Generated: DETERMINISTIC_903c33e67aeac8c5
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class Validator:
    """
    Represents a Validator in the Proof-of-Stake system.
    Attributes:
        id (str): Unique identifier for the validator.
        stake (float): Amount of tokens staked by the validator.
        reputation (int): Reputation score of the validator.
    """
    def __init__(self, id, stake):
        self.id = id
        self.stake = stake
        self.reputation = 100  # Initial reputation score (100 is perfect)
        self.reward_balance = 0.0
        self.penalty_balance = 0.0

    def validate_block(self):
        """
        Simulates the validation of a block. 
        Good validators increase their reputation, while malicious ones receive penalties.
        """
        # Determine if the validator acts maliciously (5% chance)
        is_malicious = random.random() < 0.05

        if is_malicious:
            self.reputation -= 10  # Reduce reputation due to malicious behavior
            penalty = self.stake * 0.05  # Penalty: 5% of the staked amount
            self.penalty_balance += penalty
            print(f"Validator {self.id} acted maliciously and was penalized: -{penalty:.2f} ETCV")
        else:
            self.reputation += 2  # Increase reputation for honest behavior
            reward = self.stake * 0.02  # Reward: 2% of the staked amount
            self.reward_balance += reward
            print(f"Validator {self.id} validated a block and earned a reward: +{reward:.2f} ETCV")

    def get_status(self):
        """
        Returns the current status of the validator.
        """
        return {
            "id": self.id,
            "stake": self.stake,
            "reputation": self.reputation,
            "reward_balance": self.reward_balance,
            "penalty_balance": self.penalty_balance
        }


class Blockchain:
    """
    Represents the Proof-of-Stake blockchain system.
    Attributes:
        validators (list): List of registered validators.
    """
    def __init__(self):
        self.validators = []

    def register_validator(self, validator):
        """
        Registers a new validator to the blockchain.
        """
        self.validators.append(validator)
        print(f"Validator {validator.id} registered with stake: {validator.stake:.2f} ETCV")

    def simulate_epoch(self):
        """
        Simulates one epoch in the blockchain where validators validate blocks.
        """
        print("\n--- Simulating Epoch ---")
        for validator in self.validators:
            validator.validate_block()

    def get_validator_status(self):
        """
        Displays the status of all validators.
        """
        print("\n--- Validator Status ---")
        for validator in self.validators:
            status = validator.get_status()
            print(f"ID: {status['id']}, Stake: {status['stake']:.2f} ETCV, "
                  f"Reputation: {status['reputation']}, Rewards: {status['reward_balance']:.2f} ETCV, "
                  f"Penalties: {status['penalty_balance']:.2f} ETCV")


# --- Main Execution ---

if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Create and register validators
    validator1 = Validator(id="Validator_1", stake=100.0)
    validator2 = Validator(id="Validator_2", stake=200.0)
    validator3 = Validator(id="Validator_3", stake=150.0)

    blockchain.register_validator(validator1)
    blockchain.register_validator(validator2)
    blockchain.register_validator(validator3)

    # Simulate multiple epochs
    for epoch in range(5):  # Simulate 5 epochs
        print(f"\nEpoch {epoch + 1}")
        blockchain.simulate_epoch()

    # Display final validator status
    blockchain.get_validator_status()
```
