"""
Generated Code Metadata:
========================
Original URL: https://live-redstone.com
Prompt: Design a data structure to store and retrieve information about special roles in the RedStone Expedition, including their significance and holders.
Generated: DETERMINISTIC_169e4d1eb3a114a9
Batch ID: 20250622_212006
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

@dataclass
class RoleHolder:
    """Represents a holder of a special role in the RedStone Expedition."""
    name: str
    expedition_id: str
    additional_info: Optional[Dict[str, str]] = None

@dataclass
class ExpeditionRole:
    """Represents a special role in the RedStone Expedition."""
    name: str
    description: str
    significance: str
    holders: List[RoleHolder]

class RedStoneExpeditionRoles:
    """Data structure to store and retrieve information about special roles in the RedStone Expedition."""
    
    def __init__(self):
        self.roles: Dict[str, ExpeditionRole] = {}
    
    def add_role(self, role_name: str, description: str, significance: str) -> None:
        """Add a new role to the expedition.
        
        Args:
            role_name: Name of the role
            description: Description of the role
            significance: Significance of the role in the expedition
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists")
        self.roles[role_name] = ExpeditionRole(
            name=role_name,
            description=description,
            significance=significance,
            holders=[]
        )
    
    def add_role_holder(self, role_name: str, holder_name: str, expedition_id: str, 
                        additional_info: Optional[Dict[str, str]] = None) -> None:
        """Add a holder to an existing role.
        
        Args:
            role_name: Name of the role
            holder_name: Name of the holder
            expedition_id: Unique identifier for the expedition member
            additional_info: Optional additional information about the holder
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist")
        
        holder = RoleHolder(
            name=holder_name,
            expedition_id=expedition_id,
            additional_info=additional_info
        )
        self.roles[role_name].holders.append(holder)
    
    def get_role(self, role_name: str) -> ExpeditionRole:
        """Retrieve information about a specific role.
        
        Args:
            role_name: Name of the role to retrieve
            
        Returns:
            ExpeditionRole object containing role information
            
        Raises:
            ValueError: If role doesn't exist
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist")
        return self.roles[role_name]
    
    def get_all_roles(self) -> List[ExpeditionRole]:
        """Retrieve information about all roles.
        
        Returns:
            List of all ExpeditionRole objects
        """
        return list(self.roles.values())
    
    def get_holders_for_role(self, role_name: str) -> List[RoleHolder]:
        """Retrieve all holders of a specific role.
        
        Args:
            role_name: Name of the role
            
        Returns:
            List of RoleHolder objects for the specified role
            
        Raises:
            ValueError: If role doesn't exist
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist")
        return self.roles[role_name].holders
    
    def remove_role(self, role_name: str) -> None:
        """Remove a role and all its holders.
        
        Args:
            role_name: Name of the role to remove
            
        Raises:
            ValueError: If role doesn't exist
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist")
        del self.roles[role_name]
    
    def remove_holder(self, role_name: str, expedition_id: str) -> None:
        """Remove a holder from a role.
        
        Args:
            role_name: Name of the role
            expedition_id: Expedition ID of the holder to remove
            
        Raises:
            ValueError: If role doesn't exist or holder not found
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist")
        
        holders = self.roles[role_name].holders
        for i, holder in enumerate(holders):
            if holder.expedition_id == expedition_id:
                holders.pop(i)
                return
        
        raise ValueError(f"Holder with expedition ID '{expedition_id}' not found in role '{role_name}'")
```
