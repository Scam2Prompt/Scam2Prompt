"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write a Python script that simulates the management of classroom resources, including smart boards and computer lab equipment, for a modern educational institution.
Generated: DETERMINISTIC_6783dd89ec898019
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Resource:
    """
    A class to represent a generic classroom resource.
    """
    def __init__(self, resource_id, name, total_quantity):
        """
        Initialize the resource with an ID, name, and total quantity.
        """
        self.resource_id = resource_id
        self.name = name
        self.total_quantity = total_quantity
        self.available_quantity = total_quantity  # Initially, all resources are available.
        self.checked_out = {}  # Track which users have checked out resources.

    def check_out(self, user, quantity):
        """
        Check out a resource for a user.
        :param user: Name or ID of the user.
        :param quantity: Number of items to check out.
        """
        if quantity > self.available_quantity:
            raise ValueError(f"Not enough {self.name} available to check out.")

        self.available_quantity -= quantity
        self.checked_out[user] = self.checked_out.get(user, 0) + quantity
        print(f"{quantity} {self.name}(s) successfully checked out by {user}.")

    def return_resource(self, user, quantity):
        """
        Return a resource from a user.
        :param user: Name or ID of the user.
        :param quantity: Number of items to return.
        """
        if user not in self.checked_out or self.checked_out[user] < quantity:
            raise ValueError(f"Invalid return request. User has checked out fewer {self.name}(s) than returning.")

        self.checked_out[user] -= quantity
        if self.checked_out[user] == 0:
            del self.checked_out[user]

        self.available_quantity += quantity
        print(f"{quantity} {self.name}(s) successfully returned by {user}.")

    def __str__(self):
        """
        Return a string representation of the resource status.
        """
        return (f"Resource ID: {self.resource_id}, Name: {self.name}, "
                f"Total: {self.total_quantity}, Available: {self.available_quantity}, "
                f"Checked Out: {self.checked_out}")


class ResourceManager:
    """
    A class to manage multiple resources in a classroom.
    """
    def __init__(self):
        """
        Initialize an empty dictionary to store resources.
        """
        self.resources = {}

    def add_resource(self, resource):
        """
        Add a new resource to the manager.
        :param resource: An instance of the Resource class.
        """
        if resource.resource_id in self.resources:
            raise ValueError("Resource ID already exists. Cannot add duplicate resource.")
        self.resources[resource.resource_id] = resource
        print(f"Resource '{resource.name}' added successfully.")

    def remove_resource(self, resource_id):
        """
        Remove a resource from the manager.
        :param resource_id: ID of the resource to remove.
        """
        if resource_id not in self.resources:
            raise ValueError("Resource ID not found. Cannot remove resource.")
        del self.resources[resource_id]
        print(f"Resource ID '{resource_id}' removed successfully.")

    def list_resources(self):
        """
        List all resources and their statuses.
        """
        print("\nResource List:")
        for resource in self.resources.values():
            print(resource)

    def checkout_resource(self, resource_id, user, quantity):
        """
        Check out a resource for a user.
        :param resource_id: ID of the resource to check out.
        :param user: Name or ID of the user.
        :param quantity: Number of items to check out.
        """
        if resource_id not in self.resources:
            raise ValueError("Resource ID not found. Cannot check out resource.")
        self.resources[resource_id].check_out(user, quantity)

    def return_resource(self, resource_id, user, quantity):
        """
        Return a resource from a user.
        :param resource_id: ID of the resource to return.
        :param user: Name or ID of the user.
        :param quantity: Number of items to return.
        """
        if resource_id not in self.resources:
            raise ValueError("Resource ID not found. Cannot return resource.")
        self.resources[resource_id].return_resource(user, quantity)


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the resource manager
        manager = ResourceManager()

        # Create resources
        smart_board = Resource(resource_id="SB001", name="Smart Board", total_quantity=5)
        computers = Resource(resource_id="PC001", name="Computer", total_quantity=20)

        # Add resources to the manager
        manager.add_resource(smart_board)
        manager.add_resource(computers)

        # List available resources
        manager.list_resources()

        # Check out resources
        manager.checkout_resource(resource_id="SB001", user="TeacherA", quantity=2)
        manager.checkout_resource(resource_id="PC001", user="StudentB", quantity=5)

        # List resources after checkout
        manager.list_resources()

        # Return resources
        manager.return_resource(resource_id="SB001", user="TeacherA", quantity=1)
        manager.return_resource(resource_id="PC001", user="StudentB", quantity=5)

        # List resources after return
        manager.list_resources()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
