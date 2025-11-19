"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrading-ethereum.info
Prompt: Generate a code snippet that demonstrates how to implement proof of stake in Ethereum based on the concepts discussed in "The Eth2 Book."
Generated: DETERMINISTIC_7071d4a7b597923b
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Proof of Stake (PoS) implementation in Python based on Ethereum concepts
# Note: This code is a simplified demonstration and should not be used in production.

import hashlib
import random
import time

class Validator:
    """
    Represents a validator in the Proof of Stake system.
    """
    def __init__(self, validator_id, stake):
        self.validator_id = validator_id  # Unique ID for the validator
        self.stake = stake  # Amount of stake the validator has
        self.reward = 0  # Reward accumulated by the validator

    def __repr__(self):
        return f"Validator(id={self.validator_id}, stake={self.stake}, reward={self.reward})"

class ProofOfStake:
    """
    Simplified Proof of Stake system implementation.
    """
    def __init__(self):
        self.validators = []  # List of validators participating in PoS
        self.total_stake = 0  # Total amount of stake in the system

    def register_validator(self, validator_id, stake):
        """
        Registers a new validator with their stake.
        """
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")
        validator = Validator(validator_id, stake)
        self.validators.append(validator)
        self.total_stake += stake  # Update the total stake

    def select_proposer(self):
        """
        Select a block proposer based on the weighted randomness of stakes.
        """
        if not self.validators:
            raise ValueError("No validators registered.")
        
        # Weighted randomness based on stake
        random_value = random.uniform(0, self.total_stake)
        cumulative_stake = 0
        for validator in self.validators:
            cumulative_stake += validator.stake
            if cumulative_stake >= random_value:
                return validator

    def propose_block(self, validator):
        """
        Simulates a block proposal and rewards the proposer.
        """
        if validator not in self.validators:
            raise ValueError("Validator not recognized.")
        
        # Simulate block creation (details omitted for simplicity)
        block_hash = hashlib.sha256(f"{validator.validator_id}-{time.time()}".encode()).hexdigest()
        print(f"Validator {validator.validator_id} proposed a block with hash: {block_hash}")
        
        # Reward the proposer (e.g., increase their stake)
        reward_amount = 1  # Simplified reward mechanism
        validator.reward += reward_amount
        print(f"Validator {validator.validator_id} received a reward of {reward_amount}.")

    def run_epoch(self):
        """
        Runs a simulation of one epoch in the PoS system.
        """
        print("\n--- Epoch Start ---")
        proposer = self.select_proposer()
        print(f"Selected proposer: {proposer}")
        self.propose_block(proposer)
        print("--- Epoch End ---\n")

# Example usage
if __name__ == "__main__":
    pos_system = ProofOfStake()

    # Register validators
    pos_system.register_validator("validator_1", stake=10)
    pos_system.register_validator("validator_2", stake=20)
    pos_system.register_validator("validator_3", stake=30)

    # Run multiple epochs
    for epoch in range(1, 4):
        print(f"Epoch {epoch}")
        pos_system.run_epoch()

    # Display final validator states
    print("Final validator states:")
    for validator in pos_system.validators:
        print(validator)
```

This code snippet demonstrates a simplified Proof of Stake system. It registers validators with their stakes, selects a proposer based on weighted randomness, simulates block creation, and rewards validators. As requested, it is syntactically correct, follows Python best practices, and includes comments for documentation.
