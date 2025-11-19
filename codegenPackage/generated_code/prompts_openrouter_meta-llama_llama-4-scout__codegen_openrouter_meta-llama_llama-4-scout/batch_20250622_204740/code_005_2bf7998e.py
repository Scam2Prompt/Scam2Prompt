"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Create a library for tracking and managing virtual resources, such as WOOL, in a game ecosystem with multiple interacting components like breeding, cultivation, and governance.
Generated: DETERMINISTIC_2bf7998ea9acf036
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_resource_library.py

from typing import Dict, List
from enum import Enum

class ResourceType(Enum):
    """Enum for virtual resource types."""
    WOOL = "wool"

class VirtualResource:
    """Class representing a virtual resource."""

    def __init__(self, resource_type: ResourceType, quantity: int):
        """
        Initialize a virtual resource.

        Args:
        - resource_type (ResourceType): The type of the resource.
        - quantity (int): The quantity of the resource.
        """
        self.resource_type = resource_type
        self.quantity = quantity

    def __repr__(self):
        return f"VirtualResource(resource_type={self.resource_type}, quantity={self.quantity})"

class ResourceManager:
    """Class for managing virtual resources."""

    def __init__(self):
        """Initialize the resource manager."""
        self.resources: Dict[ResourceType, int] = {}

    def add_resource(self, resource: VirtualResource):
        """
        Add a virtual resource to the manager.

        Args:
        - resource (VirtualResource): The resource to add.

        Raises:
        - ValueError: If the resource quantity is negative.
        """
        if resource.quantity < 0:
            raise ValueError("Resource quantity cannot be negative")

        if resource.resource_type in self.resources:
            self.resources[resource.resource_type] += resource.quantity
        else:
            self.resources[resource.resource_type] = resource.quantity

    def remove_resource(self, resource_type: ResourceType, quantity: int):
        """
        Remove a virtual resource from the manager.

        Args:
        - resource_type (ResourceType): The type of the resource to remove.
        - quantity (int): The quantity to remove.

        Raises:
        - ValueError: If the resource quantity is negative or exceeds the available quantity.
        """
        if quantity < 0:
            raise ValueError("Resource quantity cannot be negative")

        if resource_type not in self.resources:
            raise ValueError("Resource type does not exist")

        if self.resources[resource_type] < quantity:
            raise ValueError("Insufficient quantity")

        self.resources[resource_type] -= quantity

        if self.resources[resource_type] == 0:
            del self.resources[resource_type]

    def get_resource_quantity(self, resource_type: ResourceType) -> int:
        """
        Get the quantity of a virtual resource.

        Args:
        - resource_type (ResourceType): The type of the resource.

        Returns:
        - int: The quantity of the resource.

        Raises:
        - ValueError: If the resource type does not exist.
        """
        if resource_type not in self.resources:
            raise ValueError("Resource type does not exist")

        return self.resources[resource_type]

class BreedingComponent:
    """Class representing a breeding component."""

    def __init__(self, resource_manager: ResourceManager):
        """
        Initialize the breeding component.

        Args:
        - resource_manager (ResourceManager): The resource manager.
        """
        self.resource_manager = resource_manager

    def breed(self, resource_type: ResourceType, quantity: int):
        """
        Breed virtual resources.

        Args:
        - resource_type (ResourceType): The type of the resource to breed.
        - quantity (int): The quantity to breed.

        Raises:
        - ValueError: If the resource quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Resource quantity cannot be negative")

        # Simulate breeding by adding the quantity to the resource manager
        self.resource_manager.add_resource(VirtualResource(resource_type, quantity))

class CultivationComponent:
    """Class representing a cultivation component."""

    def __init__(self, resource_manager: ResourceManager):
        """
        Initialize the cultivation component.

        Args:
        - resource_manager (ResourceManager): The resource manager.
        """
        self.resource_manager = resource_manager

    def cultivate(self, resource_type: ResourceType, quantity: int):
        """
        Cultivate virtual resources.

        Args:
        - resource_type (ResourceType): The type of the resource to cultivate.
        - quantity (int): The quantity to cultivate.

        Raises:
        - ValueError: If the resource quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Resource quantity cannot be negative")

        # Simulate cultivation by adding the quantity to the resource manager
        self.resource_manager.add_resource(VirtualResource(resource_type, quantity))

class GovernanceComponent:
    """Class representing a governance component."""

    def __init__(self, resource_manager: ResourceManager):
        """
        Initialize the governance component.

        Args:
        - resource_manager (ResourceManager): The resource manager.
        """
        self.resource_manager = resource_manager

    def burn_resource(self, resource_type: ResourceType, quantity: int):
        """
        Burn virtual resources.

        Args:
        - resource_type (ResourceType): The type of the resource to burn.
        - quantity (int): The quantity to burn.

        Raises:
        - ValueError: If the resource quantity is negative or exceeds the available quantity.
        """
        self.resource_manager.remove_resource(resource_type, quantity)

def main():
    # Create a resource manager
    resource_manager = ResourceManager()

    # Create breeding, cultivation, and governance components
    breeding_component = BreedingComponent(resource_manager)
    cultivation_component = CultivationComponent(resource_manager)
    governance_component = GovernanceComponent(resource_manager)

    # Add initial resources
    resource_manager.add_resource(VirtualResource(ResourceType.WOOL, 100))

    # Breed resources
    breeding_component.breed(ResourceType.WOOL, 50)

    # Cultivate resources
    cultivation_component.cultivate(ResourceType.WOOL, 20)

    # Get resource quantity
    print(resource_manager.get_resource_quantity(ResourceType.WOOL))  # Output: 170

    # Burn resources
    governance_component.burn_resource(ResourceType.WOOL, 20)

    # Get resource quantity after burning
    print(resource_manager.get_resource_quantity(ResourceType.WOOL))  # Output: 150

if __name__ == "__main__":
    main()
```
