"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Design a data structure to store information about delegators, operators, and their respective stakes on the bitsCrunch network.
Generated: DETERMINISTIC_11bcfa884296e056
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class EntityType(Enum):
    """Enum representing different types of entities in the network."""
    DELEGATOR = auto()
    OPERATOR = auto()

@dataclass
class StakeInfo:
    """Data class representing stake information for an entity."""
    amount: float
    timestamp: int  # Unix timestamp

@dataclass
class Entity:
    """Base data class representing a network entity."""
    entity_id: str
    entity_type: EntityType
    stake_info: List[StakeInfo]

class NetworkStakeManager:
    """Class to manage delegators, operators, and their stakes."""
    
    def __init__(self):
        self.entities: Dict[str, Entity] = {}
    
    def add_entity(self, entity_id: str, entity_type: EntityType) -> None:
        """Add a new entity to the network.
        
        Args:
            entity_id: Unique identifier for the entity.
            entity_type: Type of the entity (DELEGATOR or OPERATOR).
            
        Raises:
            ValueError: If entity_id already exists.
        """
        if entity_id in self.entities:
            raise ValueError(f"Entity with ID {entity_id} already exists.")
        self.entities[entity_id] = Entity(
            entity_id=entity_id,
            entity_type=entity_type,
            stake_info=[]
        )
    
    def add_stake(self, entity_id: str, amount: float, timestamp: int) -> None:
        """Add stake information for an entity.
        
        Args:
            entity_id: ID of the entity to add stake for.
            amount: Stake amount.
            timestamp: Unix timestamp of the stake.
            
        Raises:
            ValueError: If entity_id doesn't exist or amount is invalid.
        """
        if entity_id not in self.entities:
            raise ValueError(f"Entity with ID {entity_id} does not exist.")
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
            
        self.entities[entity_id].stake_info.append(
            StakeInfo(amount=amount, timestamp=timestamp)
        )
    
    def get_total_stake(self, entity_id: str) -> float:
        """Get total stake for an entity.
        
        Args:
            entity_id: ID of the entity.
            
        Returns:
            Total stake amount for the entity.
            
        Raises:
            ValueError: If entity_id doesn't exist.
        """
        if entity_id not in self.entities:
            raise ValueError(f"Entity with ID {entity_id} does not exist.")
            
        return sum(stake.amount for stake in self.entities[entity_id].stake_info)
    
    def get_entities_by_type(self, entity_type: EntityType) -> List[Entity]:
        """Get all entities of a specific type.
        
        Args:
            entity_type: Type of entities to retrieve.
            
        Returns:
            List of entities matching the type.
        """
        return [
            entity for entity in self.entities.values()
            if entity.entity_type == entity_type
        ]
    
    def get_entity(self, entity_id: str) -> Optional[Entity]:
        """Get an entity by its ID.
        
        Args:
            entity_id: ID of the entity to retrieve.
            
        Returns:
            The Entity object if found, None otherwise.
        """
        return self.entities.get(entity_id)
```
