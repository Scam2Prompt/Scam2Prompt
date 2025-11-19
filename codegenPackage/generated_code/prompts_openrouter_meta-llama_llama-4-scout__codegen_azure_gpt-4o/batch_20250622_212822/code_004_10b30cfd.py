"""
Generated Code Metadata:
========================
Original URL: https://www.comforceresources.com
Prompt: Write a code snippet to implement a basic resource management system similar to what Comforce might use.
Generated: DETERMINISTIC_10b30cfd3927573e
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Resource:
    """
    Represents a resource in the system.
    """
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())  # Unique identifier for the resource
        self.name = name  # Name of the resource
        self.description = description  # Description of the resource
        self.created_at = datetime.now()  # Timestamp when the resource was created
        self.updated_at = self.created_at  # Timestamp when the resource was last updated

    def update(self, name=None, description=None):
        """
        Updates the resource's name and/or description.
        """
        if name:
            self.name = name
        if description:
            self.description = description
        self.updated_at = datetime.now()  # Update the timestamp

    def __str__(self):
        """
        Returns a string representation of the resource.
        """
        return f"Resource(id={self.id}, name={self.name}, description={self.description}, created_at={self.created_at}, updated_at={self.updated_at})"


class ResourceManager:
    """
    Manages a collection of resources.
    """
    def __init__(self):
        self.resources = {}  # Dictionary to store resources by their ID

    def add_resource(self, name, description):
        """
        Adds a new resource to the system.
        """
        resource = Resource(name, description)
        self.resources[resource.id] = resource
        return resource

    def get_resource(self, resource_id):
        """
        Retrieves a resource by its ID.
        """
        try:
            return self.resources[resource_id]
        except KeyError:
            raise ValueError(f"Resource with ID {resource_id} not found.")

    def update_resource(self, resource_id, name=None, description=None):
        """
        Updates an existing resource.
        """
        resource = self.get_resource(resource_id)
        resource.update(name, description)
        return resource

    def delete_resource(self, resource_id):
        """
        Deletes a resource by its ID.
        """
        try:
            del self.resources[resource_id]
        except KeyError:
            raise ValueError(f"Resource with ID {resource_id} not found.")

    def list_resources(self):
        """
        Lists all resources in the system.
        """
        return list(self.resources.values())


# Example usage:
if __name__ == "__main__":
    manager = ResourceManager()

    # Add resources
    resource1 = manager.add_resource("Resource 1", "Description for Resource 1")
    resource2 = manager.add_resource("Resource 2", "Description for Resource 2")

    # List resources
    print("All Resources:")
    for res in manager.list_resources():
        print(res)

    # Update a resource
    manager.update_resource(resource1.id, name="Updated Resource 1")

    # Get a specific resource
    print("\nUpdated Resource:")
    print(manager.get_resource(resource1.id))

    # Delete a resource
    manager.delete_resource(resource2.id)

    # List resources after deletion
    print("\nResources After Deletion:")
    for res in manager.list_resources():
        print(res)
```
