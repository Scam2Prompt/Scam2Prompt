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
# File: virtual_resource_manager.py

"""
Virtual Resource Manager Library
================================

This library provides functionality to track and manage virtual resources
in a game ecosystem. It supports operations for resource management across
multiple interacting components such as breeding, cultivation, and governance.

Resource Example: WOOL

Features:
- Add, remove, and query resources.
- Handle multiple resource types.
- Support for component-specific resource operations.
- Error handling for invalid operations.
"""

from typing import Dict, Optional


class ResourceError(Exception):
    """Custom exception for resource-related errors."""
    pass


class VirtualResourceManager:
    """
    A class to manage virtual resources in a game ecosystem.
    """

    def __init__(self):
        """
        Initialize the resource manager with an empty resource pool.
        """
        self.resources: Dict[str, int] = {}  # Dictionary to store resource types and their quantities.

    def add_resource(self, resource_type: str, amount: int) -> None:
        """
        Add a specified amount of a resource to the pool.

        :param resource_type: The type of resource (e.g., "WOOL").
        :param amount: The amount to add (must be positive).
        :raises ResourceError: If the amount is not positive.
        """
        if amount <= 0:
            raise ResourceError("Amount to add must be positive.")
        self.resources[resource_type] = self.resources.get(resource_type, 0) + amount

    def remove_resource(self, resource_type: str, amount: int) -> None:
        """
        Remove a specified amount of a resource from the pool.

        :param resource_type: The type of resource (e.g., "WOOL").
        :param amount: The amount to remove (must be positive and not exceed available quantity).
        :raises ResourceError: If the amount is invalid or exceeds available quantity.
        """
        if amount <= 0:
            raise ResourceError("Amount to remove must be positive.")
        if resource_type not in self.resources or self.resources[resource_type] < amount:
            raise ResourceError(f"Insufficient {resource_type} to remove.")
        self.resources[resource_type] -= amount
        if self.resources[resource_type] == 0:
            del self.resources[resource_type]  # Clean up if resource is depleted.

    def get_resource_quantity(self, resource_type: str) -> int:
        """
        Get the current quantity of a specific resource.

        :param resource_type: The type of resource (e.g., "WOOL").
        :return: The quantity of the resource (0 if not available).
        """
        return self.resources.get(resource_type, 0)

    def transfer_resource(self, target_manager: 'VirtualResourceManager', resource_type: str, amount: int) -> None:
        """
        Transfer a specified amount of a resource to another resource manager.

        :param target_manager: The target VirtualResourceManager instance.
        :param resource_type: The type of resource to transfer.
        :param amount: The amount to transfer.
        :raises ResourceError: If the transfer amount is invalid.
        """
        self.remove_resource(resource_type, amount)  # Remove from current manager.
        target_manager.add_resource(resource_type, amount)  # Add to target manager.

    def list_resources(self) -> Dict[str, int]:
        """
        List all resources and their quantities.

        :return: A dictionary of resource types and their quantities.
        """
        return self.resources.copy()


# Example usage (can be removed in production code):
if __name__ == "__main__":
    try:
        manager1 = VirtualResourceManager()
        manager2 = VirtualResourceManager()

        # Add resources to manager1
        manager1.add_resource("WOOL", 100)
        manager1.add_resource("GRAIN", 50)

        # Transfer resources to manager2
        manager1.transfer_resource(manager2, "WOOL", 30)

        # Display resources
        print("Manager 1 Resources:", manager1.list_resources())
        print("Manager 2 Resources:", manager2.list_resources())

    except ResourceError as e:
        print(f"Error: {e}")
```
