"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validatorsnode.com
Prompt: Explain how to create a staking pool with Validatorsnode and provide a sample code for it.
Generated: DETERMINISTIC_f24fb0aa45597b06
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_pool.py

from typing import Dict, List


class Validator:
    """
    Represents a Validator node in the staking pool.
    Each validator has a unique identifier and staking details.
    """
    def __init__(self, validator_id: str, initial_stake: float = 0.0):
        """
        Initialize a Validator node.
        
        :param validator_id: Unique identifier for the validator
        :param initial_stake: Initial stake amount for the validator, default is 0.0
        """
        if initial_stake < 0:
            raise ValueError("Initial stake cannot be negative.")
        self.validator_id = validator_id
        self.stake = initial_stake

    def add_stake(self, amount: float):
        """
        Add stake to the validator.
        
        :param amount: Amount of stake to add
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        self.stake += amount

    def remove_stake(self, amount: float):
        """
        Remove stake from the validator.
        
        :param amount: Amount of stake to remove
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        if amount > self.stake:
            raise ValueError("Cannot remove more stake than currently held.")
        self.stake -= amount


class StakingPool:
    """
    Represents a staking pool that manages multiple validators.
    Provides functionality to add validators and manage stakes.
    """
    def __init__(self):
        """
        Initialize the staking pool with an empty set of validators.
        """
        self.validators: Dict[str, Validator] = {}

    def add_validator(self, validator_id: str, initial_stake: float = 0.0):
        """
        Add a new validator to the pool.
        
        :param validator_id: Unique identifier for the validator
        :param initial_stake: Initial stake amount for the validator, default is 0.0
        """
        if validator_id in self.validators:
            raise ValueError("Validator with this ID already exists.")
        self.validators[validator_id] = Validator(validator_id, initial_stake)

    def remove_validator(self, validator_id: str):
        """
        Remove a validator from the pool.
        
        :param validator_id: Unique identifier for the validator
        """
        if validator_id not in self.validators:
            raise ValueError("Validator ID not found in the staking pool.")
        del self.validators[validator_id]

    def add_stake_to_validator(self, validator_id: str, amount: float):
        """
        Add stake to a specific validator in the pool.
        
        :param validator_id: Unique identifier for the validator
        :param amount: Amount of stake to add
        """
        if validator_id not in self.validators:
            raise ValueError("Validator ID not found in the staking pool.")
        self.validators[validator_id].add_stake(amount)

    def remove_stake_from_validator(self, validator_id: str, amount: float):
        """
        Remove stake from a specific validator in the pool.
        
        :param validator_id: Unique identifier for the validator
        :param amount: Amount of stake to remove
        """
        if validator_id not in self.validators:
            raise ValueError("Validator ID not found in the staking pool.")
        self.validators[validator_id].remove_stake(amount)

    def get_total_stake(self) -> float:
        """
        Calculate and return the total stake in the pool.
        
        :return: Total stake amount across all validators
        """
        return sum(validator.stake for validator in self.validators.values())

    def list_validators(self) -> List[str]:
        """
        List all validators in the pool.
        
        :return: List of validator IDs
        """
        return list(self.validators.keys())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking pool
        pool = StakingPool()

        # Add validators
        pool.add_validator("validator_1", 100.0)
        pool.add_validator("validator_2", 200.0)

        # Add stake to validators
        pool.add_stake_to_validator("validator_1", 50.0)

        # Remove stake from validators
        pool.remove_stake_from_validator("validator_2", 100.0)

        # Print total stake in the pool
        print(f"Total Stake: {pool.get_total_stake()}")

        # List all validators
        print(f"Validators: {pool.list_validators()}")

        # Remove a validator from the pool
        pool.remove_validator("validator_1")

        # Print updated validator list
        print(f"Updated Validators: {pool.list_validators()}")

    except Exception as e:
        print(f"Error: {e}")
```
