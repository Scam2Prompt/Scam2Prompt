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
from typing import List, Optional
import json
from enum import Enum

class ValidatorStatus(Enum):
    """Enum representing the status of a validator."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    JAILED = "jailed"

@dataclass
class Validator:
    """Data structure representing a validator on the Beam Network."""
    validator_address: str
    operator_address: str
    staked_beam: float
    node_tokens: int
    commission_rate: float
    status: ValidatorStatus
    delegator_addresses: List[str] = None
    website: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self):
        """Validate the validator data after initialization."""
        if self.staked_beam < 0:
            raise ValueError("Staked BEAM cannot be negative")
        if self.node_tokens < 0:
            raise ValueError("Node tokens cannot be negative")
        if not 0 <= self.commission_rate <= 1:
            raise ValueError("Commission rate must be between 0 and 1")
        if self.delegator_addresses is None:
            self.delegator_addresses = []

    def to_json(self) -> str:
        """Convert the validator object to JSON string."""
        return json.dumps({
            "validator_address": self.validator_address,
            "operator_address": self.operator_address,
            "staked_beam": self.staked_beam,
            "node_tokens": self.node_tokens,
            "commission_rate": self.commission_rate,
            "status": self.status.value,
            "delegator_addresses": self.delegator_addresses,
            "website": self.website,
            "description": self.description
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'Validator':
        """Create a Validator object from JSON string."""
        data = json.loads(json_str)
        return cls(
            validator_address=data["validator_address"],
            operator_address=data["operator_address"],
            staked_beam=data["staked_beam"],
            node_tokens=data["node_tokens"],
            commission_rate=data["commission_rate"],
            status=ValidatorStatus(data["status"]),
            delegator_addresses=data.get("delegator_addresses", []),
            website=data.get("website"),
            description=data.get("description")
        )

class ValidatorRegistry:
    """Registry to manage validators on the Beam Network."""
    
    def __init__(self):
        self.validators = {}

    def add_validator(self, validator: Validator) -> None:
        """Add a validator to the registry."""
        if validator.validator_address in self.validators:
            raise ValueError("Validator already exists in registry")
        self.validators[validator.validator_address] = validator

    def remove_validator(self, validator_address: str) -> None:
        """Remove a validator from the registry."""
        if validator_address not in self.validators:
            raise ValueError("Validator not found in registry")
        del self.validators[validator_address]

    def get_validator(self, validator_address: str) -> Validator:
        """Get a validator by its address."""
        validator = self.validators.get(validator_address)
        if validator is None:
            raise ValueError("Validator not found")
        return validator

    def update_validator(self, validator: Validator) -> None:
        """Update a validator in the registry."""
        if validator.validator_address not in self.validators:
            raise ValueError("Validator not found in registry")
        self.validators[validator.validator_address] = validator

    def get_all_validators(self) -> List[Validator]:
        """Get all validators in the registry."""
        return list(self.validators.values())

    def to_json(self) -> str:
        """Convert the registry to JSON string."""
        return json.dumps([validator.to_json() for validator in self.validators.values()])

    @classmethod
    def from_json(cls, json_str: str) -> 'ValidatorRegistry':
        """Create a ValidatorRegistry from JSON string."""
        registry = cls()
        validators_data = json.loads(json_str)
        for validator_data in validators_data:
            validator = Validator.from_json(validator_data)
            registry.add_validator(validator)
        return registry
```
