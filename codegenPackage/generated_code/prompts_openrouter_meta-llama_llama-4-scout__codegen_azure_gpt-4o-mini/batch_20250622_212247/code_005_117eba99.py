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
class Validator:
    """
    A class to represent a validator on the Beam Network.

    Attributes:
        name (str): The name of the validator.
        staked_beam (float): The amount of BEAM staked by the validator.
        node_tokens (int): The number of node tokens held by the validator.
        commission_rate (float): The commission rate charged by the validator (as a percentage).
    """

    def __init__(self, name: str, staked_beam: float, node_tokens: int, commission_rate: float):
        """
        Initializes a new Validator instance.

        Args:
            name (str): The name of the validator.
            staked_beam (float): The amount of BEAM staked by the validator.
            node_tokens (int): The number of node tokens held by the validator.
            commission_rate (float): The commission rate charged by the validator (as a percentage).

        Raises:
            ValueError: If staked_beam is negative, node_tokens is negative, or commission_rate is not between 0 and 100.
        """
        if staked_beam < 0:
            raise ValueError("Staked BEAM cannot be negative.")
        if node_tokens < 0:
            raise ValueError("Node tokens cannot be negative.")
        if not (0 <= commission_rate <= 100):
            raise ValueError("Commission rate must be between 0 and 100.")

        self.name = name
        self.staked_beam = staked_beam
        self.node_tokens = node_tokens
        self.commission_rate = commission_rate

    def __repr__(self):
        """Returns a string representation of the Validator instance."""
        return (f"Validator(name={self.name}, staked_beam={self.staked_beam}, "
                f"node_tokens={self.node_tokens}, commission_rate={self.commission_rate})")


class ValidatorRegistry:
    """
    A class to manage a collection of validators on the Beam Network.

    Attributes:
        validators (dict): A dictionary to store validators by their name.
    """

    def __init__(self):
        """Initializes an empty ValidatorRegistry."""
        self.validators = {}

    def add_validator(self, validator: Validator):
        """
        Adds a new validator to the registry.

        Args:
            validator (Validator): The validator to add.

        Raises:
            ValueError: If a validator with the same name already exists.
        """
        if validator.name in self.validators:
            raise ValueError(f"Validator with name '{validator.name}' already exists.")
        self.validators[validator.name] = validator

    def remove_validator(self, name: str):
        """
        Removes a validator from the registry by name.

        Args:
            name (str): The name of the validator to remove.

        Raises:
            KeyError: If no validator with the given name exists.
        """
        if name not in self.validators:
            raise KeyError(f"No validator found with name '{name}'.")
        del self.validators[name]

    def get_validator(self, name: str) -> Validator:
        """
        Retrieves a validator by name.

        Args:
            name (str): The name of the validator to retrieve.

        Returns:
            Validator: The requested validator.

        Raises:
            KeyError: If no validator with the given name exists.
        """
        if name not in self.validators:
            raise KeyError(f"No validator found with name '{name}'.")
        return self.validators[name]

    def __repr__(self):
        """Returns a string representation of the ValidatorRegistry instance."""
        return f"ValidatorRegistry(validators={self.validators})"
```
