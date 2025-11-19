"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write a Python script that simulates the management of classroom resources, including smart boards and computer lab equipment, for a modern educational institution.
Generated: DETERMINISTIC_6783dd89ec898019
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime


class Resource:
    """
    Base class for a resource in the educational institution.
    """
    def __init__(self, resource_id, name):
        self.resource_id = resource_id
        self.name = name
        self.is_available = True
        self.last_checked_out = None

    def check_out(self):
        """
        Marks the resource as checked out and logs the timestamp.
        """
        if not self.is_available:
            raise ValueError(f"Resource '{self.name}' is already checked out.")
        self.is_available = False
        self.last_checked_out = datetime.datetime.now()

    def return_resource(self):
        """
        Marks the resource as available.
        """
        if self.is_available:
            raise ValueError(f"Resource '{self.name}' is already available.")
        self.is_available = True

    def __str__(self):
        """
        Returns a string representation of the resource.
        """
        status = "Available" if self.is_available else "Checked Out"
        return f"Resource ID: {self.resource_id}, Name: {self.name}, Status: {status}"


class SmartBoard(Resource):
    """
    Represents a Smart Board resource.
    """
    def __init__(self, resource_id, name, resolution):
        super().__init__(resource_id, name)
        self.resolution = resolution

    def __str__(self):
        """
        Returns a string representation of the Smart Board.
        """
        base_info = super().__str__()
        return f"{base_info}, Resolution: {self.resolution}"


class Computer(Resource):
    """
    Represents a Computer resource in the computer lab.
    """
    def __init__(self, resource_id, name, operating_system):
        super().__init__(resource_id, name)
        self.operating_system = operating_system

    def __str__(self):
        """
        Returns a string representation of the Computer.
        """
        base_info = super().__str__()
        return f"{base_info}, Operating System: {self.operating_system}"


class ResourceManager:
    """
    Manages classroom resources such as Smart Boards and Computers.
    """
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource):
        """
        Adds a new resource to the manager.
        """
        if resource.resource_id in self.resources:
            raise ValueError(f"Resource ID '{resource.resource_id}' already exists.")
        self.resources[resource.resource_id] = resource

    def remove_resource(self, resource_id):
        """
        Removes a resource from the manager.
        """
        if resource_id not in self.resources:
            raise ValueError(f"Resource ID '{resource_id}' does not exist.")
        del self.resources[resource_id]

    def list_resources(self):
        """
        Lists all resources managed by the ResourceManager.
        """
        for resource in self.resources.values():
            print(resource)

    def check_out_resource(self, resource_id):
        """
        Checks out a resource by its ID.
        """
        if resource_id not in self.resources:
            raise ValueError(f"Resource ID '{resource_id}' does not exist.")
        resource = self.resources[resource_id]
        resource.check_out()

    def return_resource(self, resource_id):
        """
        Returns a resource by its ID.
        """
        if resource_id not in self.resources:
            raise ValueError(f"Resource ID '{resource_id}' does not exist.")
        resource = self.resources[resource_id]
        resource.return_resource()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the resource manager
        manager = ResourceManager()

        # Add resources
        smart_board = SmartBoard(resource_id=1, name="Smart Board A", resolution="4K")
        computer = Computer(resource_id=2, name="Computer A", operating_system="Windows 10")

        manager.add_resource(smart_board)
        manager.add_resource(computer)

        # List resources
        print("Listing all resources:")
        manager.list_resources()

        # Check out a resource
        print("\nChecking out Smart Board A:")
        manager.check_out_resource(1)
        manager.list_resources()

        # Return a resource
        print("\nReturning Smart Board A:")
        manager.return_resource(1)
        manager.list_resources()

    except Exception as e:
        print(f"Error: {e}")
```
