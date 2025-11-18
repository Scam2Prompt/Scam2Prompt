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
import random

class Validator:
    """
    Represents a Validator in the Proof-of-Stake system.
    
    Attributes:
        address (str): Unique address of the validator.
        balance (float): Amount of stake held by the validator.
        is_malicious (bool): Indicates if the validator is acting maliciously.
    """
    
    def __init__(self, address: str, balance: float):
        self.address = address
        self.balance = balance
        self.is_malicious = False

    def set_malicious(self):
        """Set the validator as malicious."""
        self.is_malicious = True

    def reset_malicious(self):
        """Reset the malicious status of the validator."""
        self.is_malicious = False

    def __str__(self):
        return f"Validator({self.address}, Balance: {self.balance}, Malicious: {self.is_malicious})"


class PoSSystem:
    """
    Simulates a Proof-of-Stake mining system.
    
    Attributes:
        validators (list): List of Validator objects in the system.
        reward_rate (float): Reward percentage for valid validators.
        penalty_rate (float): Penalty percentage for malicious validators.
    """

    def __init__(self, reward_rate: float, penalty_rate: float):
        self.validators = []
        self.reward_rate = reward_rate
        self.penalty_rate = penalty_rate

    def add_validator(self, address: str, initial_balance: float):
        """Add a new validator to the system."""
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        new_validator = Validator(address, initial_balance)
        self.validators.append(new_validator)

    def simulate_epoch(self):
        """Simulate a single epoch of the Proof-of-Stake system."""
        for validator in self.validators:
            if validator.is_malicious:
                penalty = validator.balance * self.penalty_rate
                validator.balance -= penalty
                print(f"{validator.address} is malicious. Penalty applied: {penalty:.2f}. New balance: {validator.balance:.2f}")
            else:
                reward = validator.balance * self.reward_rate
                validator.balance += reward
                print(f"{validator.address} is valid. Reward applied: {reward:.2f}. New balance: {validator.balance:.2f}")

    def display_validators(self):
        """Display the current status of all validators."""
        for validator in self.validators:
            print(validator)


# Example usage
if __name__ == "__main__":
    try:
        # Create a PoS system with a 5% reward and a 10% penalty
        pos_system = PoSSystem(reward_rate=0.05, penalty_rate=0.10)

        # Adding validators
        pos_system.add_validator("0xValidator1", 100.0)
        pos_system.add_validator("0xValidator2", 200.0)
        
        # Randomly mark a validator as malicious for testing
        if random.choice([True, False]):
            pos_system.validators[0].set_malicious()

        # Simulate an epoch
        pos_system.simulate_epoch()

        # Display status of validators
        pos_system.display_validators()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
