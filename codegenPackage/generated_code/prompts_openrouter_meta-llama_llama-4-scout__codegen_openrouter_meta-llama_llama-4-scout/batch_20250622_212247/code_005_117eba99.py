"""
Generated Code Metadata:
========================
Original URL: https://onbeam.live
Prompt: Design a data structure to store information about validators on the Beam Network, including their staked BEAM, Node Tokens, and commission rates.
Generated: DETERMINISTIC_117eba994edd103e
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import Dict

@dataclass
class Validator:
    """Represents a validator on the Beam Network."""
    address: str
    staked_beam: float
    node_tokens: int
    commission_rate: float

    def __post_init__(self):
        """Validates the commission rate."""
        if not (0 <= self.commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1")

class ValidatorStore:
    """Stores information about validators on the Beam Network."""
    def __init__(self):
        self.validators: Dict[str, Validator] = {}

    def add_validator(self, validator: Validator):
        """Adds a validator to the store."""
        self.validators[validator.address] = validator

    def get_validator(self, address: str) -> Validator:
        """Gets a validator by address."""
        try:
            return self.validators[address]
        except KeyError:
            raise ValueError(f"Validator with address '{address}' not found")

    def update_validator(self, address: str, validator: Validator):
        """Updates a validator in the store."""
        if address in self.validators:
            self.validators[address] = validator
        else:
            raise ValueError(f"Validator with address '{address}' not found")

    def remove_validator(self, address: str):
        """Removes a validator from the store."""
        try:
            del self.validators[address]
        except KeyError:
            raise ValueError(f"Validator with address '{address}' not found")

def main():
    store = ValidatorStore()

    # Create validators
    validator1 = Validator(
        address="beam-validator-1",
        staked_beam=1000.0,
        node_tokens=100,
        commission_rate=0.05
    )

    validator2 = Validator(
        address="beam-validator-2",
        staked_beam=500.0,
        node_tokens=50,
        commission_rate=0.10
    )

    # Add validators to store
    store.add_validator(validator1)
    store.add_validator(validator2)

    # Get validator
    retrieved_validator = store.get_validator("beam-validator-1")
    print(f"Validator {retrieved_validator.address} staked BEAM: {retrieved_validator.staked_beam}")

    # Update validator
    updated_validator = Validator(
        address="beam-validator-1",
        staked_beam=1200.0,
        node_tokens=120,
        commission_rate=0.06
    )
    store.update_validator("beam-validator-1", updated_validator)

    # Remove validator
    store.remove_validator("beam-validator-2")

if __name__ == "__main__":
    main()
```
