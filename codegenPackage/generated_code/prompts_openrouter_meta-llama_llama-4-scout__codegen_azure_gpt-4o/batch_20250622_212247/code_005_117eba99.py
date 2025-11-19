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
# Import necessary modules
from typing import List, Dict

class Validator:
    """
    A class to represent a validator on the Beam Network.
    """
    def __init__(self, validator_id: str, staked_beam: float, node_tokens: int, commission_rate: float):
        """
        Initialize a Validator object.

        :param validator_id: Unique identifier for the validator
        :param staked_beam: Amount of BEAM tokens staked by the validator
        :param node_tokens: Number of Node Tokens owned by the validator
        :param commission_rate: Commission rate charged by the validator (percentage)
        """
        self.validator_id = validator_id
        self.staked_beam = staked_beam
        self.node_tokens = node_tokens
        self.commission_rate = commission_rate

    def __repr__(self):
        """
        String representation of the Validator object.
        """
        return (f"Validator(validator_id={self.validator_id}, staked_beam={self.staked_beam}, "
                f"node_tokens={self.node_tokens}, commission_rate={self.commission_rate})")


class BeamNetwork:
    """
    A class to manage validators on the Beam Network.
    """
    def __init__(self):
        """
        Initialize the BeamNetwork object with an empty list of validators.
        """
        self.validators: List[Validator] = []

    def add_validator(self, validator_id: str, staked_beam: float, node_tokens: int, commission_rate: float):
        """
        Add a new validator to the network.

        :param validator_id: Unique identifier for the validator
        :param staked_beam: Amount of BEAM tokens staked by the validator
        :param node_tokens: Number of Node Tokens owned by the validator
        :param commission_rate: Commission rate charged by the validator (percentage)
        :raises ValueError: If commission_rate is not between 0 and 100
        """
        if not (0 <= commission_rate <= 100):
            raise ValueError("Commission rate must be between 0 and 100.")
        
        new_validator = Validator(validator_id, staked_beam, node_tokens, commission_rate)
        self.validators.append(new_validator)

    def get_validator(self, validator_id: str) -> Validator:
        """
        Retrieve a validator by their ID.

        :param validator_id: Unique identifier for the validator
        :return: Validator object
        :raises ValueError: If the validator ID does not exist
        """
        for validator in self.validators:
            if validator.validator_id == validator_id:
                return validator
        raise ValueError(f"Validator with ID {validator_id} not found.")

    def remove_validator(self, validator_id: str):
        """
        Remove a validator from the network by their ID.

        :param validator_id: Unique identifier for the validator
        :raises ValueError: If the validator ID does not exist
        """
        for validator in self.validators:
            if validator.validator_id == validator_id:
                self.validators.remove(validator)
                return
        raise ValueError(f"Validator with ID {validator_id} not found.")

    def list_validators(self) -> List[Dict]:
        """
        List all validators in the network.

        :return: List of dictionaries containing validator information
        """
        return [
            {
                "validator_id": validator.validator_id,
                "staked_beam": validator.staked_beam,
                "node_tokens": validator.node_tokens,
                "commission_rate": validator.commission_rate,
            }
            for validator in self.validators
        ]

# Example usage (uncomment to test):
# network = BeamNetwork()
# network.add_validator("validator1", 1000.0, 50, 5.0)
# network.add_validator("validator2", 2000.0, 100, 10.0)
# print(network.list_validators())
# print(network.get_validator("validator1"))
# network.remove_validator("validator1")
# print(network.list_validators())
```
