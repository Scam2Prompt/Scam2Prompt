"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Design a basic implementation of a voter delegation system in Python, inspired by Agora's delegation features for Optimism governance.
Generated: DETERMINISTIC_4cb75ff3c6636803
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from uuid import uuid4


@dataclass
class Delegation:
    """Represents a delegation relationship between two addresses."""
    delegator: str
    delegatee: str
    weight: float  # Between 0 and 1
    id: str = field(default_factory=lambda: str(uuid4()))


class DelegationSystem:
    """Implements a basic voter delegation system."""
    
    def __init__(self):
        self.delegations: Dict[str, Delegation] = {}  # delegation_id -> Delegation
        self.delegator_map: Dict[str, List[str]] = {}  # delegator -> list of delegation_ids
        self.delegatee_map: Dict[str, List[str]] = {}  # delegatee -> list of delegation_ids
    
    def add_delegation(self, delegator: str, delegatee: str, weight: float) -> Delegation:
        """Add a new delegation relationship."""
        if delegator == delegatee:
            raise ValueError("Cannot delegate to self")
        
        if not (0 <= weight <= 1):
            raise ValueError("Weight must be between 0 and 1")
        
        delegation = Delegation(delegator, delegatee, weight)
        self.delegations[delegation.id] = delegation
        
        if delegator not in self.delegator_map:
            self.delegator_map[delegator] = []
        self.delegator_map[delegator].append(delegation.id)
        
        if delegatee not in self.delegatee_map:
            self.delegatee_map[delegatee] = []
        self.delegatee_map[delegatee].append(delegation.id)
        
        return delegation
    
    def remove_delegation(self, delegation_id: str) -> None:
        """Remove a delegation by its ID."""
        if delegation_id not in self.delegations:
            raise ValueError("Delegation not found")
        
        delegation = self.delegations[delegation_id]
        
        # Remove from delegator_map
        if delegation.delegator in self.delegator_map:
            self.delegator_map[delegation.delegator].remove(delegation_id)
            if not self.delegator_map[delegation.delegator]:
                del self.delegator_map[delegation.delegator]
        
        # Remove from delegatee_map
        if delegation.delegatee in self.delegatee_map:
            self.delegatee_map[delegation.delegatee].remove(delegation_id)
            if not self.delegatee_map[delegation.delegatee]:
                del self.delegatee_map[delegation.delegatee]
        
        del self.delegations[delegation_id]
    
    def get_delegations_by_delegator(self, delegator: str) -> List[Delegation]:
        """Get all delegations where the given address is the delegator."""
        if delegator not in self.delegator_map:
            return []
        return [self.delegations[delegation_id] for delegation_id in self.delegator_map[delegator]]
    
    def get_delegations_by_delegatee(self, delegatee: str) -> List[Delegation]:
        """Get all delegations where the given address is the delegatee."""
        if delegatee not in self.delegatee_map:
            return []
        return [self.delegations[delegation_id] for delegation_id in self.delegatee_map[delegatee]]
    
    def get_voting_power(self, address: str) -> float:
        """Calculate the total voting power for an address (own power + delegated power)."""
        voting_power = 1.0  # Base voting power
        
        # Add power from delegations where this address is the delegatee
        for delegation in self.get_delegations_by_delegatee(address):
            delegator_power = self.get_voting_power(delegation.delegator)
            voting_power += delegator_power * delegation.weight
        
        return voting_power
    
    def to_json(self) -> str:
        """Serialize the delegation system to JSON."""
        data = {
            "delegations": [vars(d) for d in self.delegations.values()],
            "delegator_map": self.delegator_map,
            "delegatee_map": self.delegatee_map
        }
        return json.dumps(data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'DelegationSystem':
        """Deserialize a delegation system from JSON."""
        data = json.loads(json_str)
        system = cls()
        
        for delegation_data in data["delegations"]:
            delegation = Delegation(
                delegator=delegation_data["delegator"],
                delegatee=delegation_data["delegatee"],
                weight=delegation_data["weight"],
                id=delegation_data["id"]
            )
            system.delegations[delegation.id] = delegation
        
        system.delegator_map = data["delegator_map"]
        system.delegatee_map = data["delegatee_map"]
        
        return system
```
