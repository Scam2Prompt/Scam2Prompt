"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Suggest a framework for managing the fabrication of replacement parts for machinery, based on the manufacturing services of Multiservicios 3L.
Generated: DETERMINISTIC_08492a951aae28fa
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Part Management Framework for Multiservicios 3L

This framework handles the fabrication and management of replacement parts for machinery.
Key features include part creation, updating, deletion, and retrieval, as well as error handling.
"""

class Part:
    """
    Represents a replacement part with attributes such as part_id, name, and specifications.
    """

    def __init__(self, part_id, name, specifications):
        self.part_id = part_id
        self.name = name
        self.specifications = specifications

    def __str__(self):
        return f"Part(ID: {self.part_id}, Name: {self.name}, Specs: {self.specifications})"


class PartManager:
    """
    Manages a collection of parts, providing functionalities to add, update, delete, and retrieve parts.
    """

    def __init__(self):
        self.parts = {}
    
    def add_part(self, part):
        """
        Adds a new part to the collection.

        :param part: Part object to be added.
        :raises ValueError: If the part ID already exists.
        """
        if part.part_id in self.parts:
            raise ValueError(f"Part ID {part.part_id} already exists.")
        self.parts[part.part_id] = part
        print(f"Added: {part}")

    def update_part(self, part_id, name=None, specifications=None):
        """
        Updates an existing part's details.

        :param part_id: ID of the part to update.
        :param name: New name for the part (optional).
        :param specifications: New specifications for the part (optional).
        :raises KeyError: If the part ID does not exist.
        """
        if part_id not in self.parts:
            raise KeyError(f"Part ID {part_id} not found.")
        
        if name:
            self.parts[part_id].name = name
        if specifications:
            self.parts[part_id].specifications = specifications
        
        print(f"Updated: {self.parts[part_id]}")

    def delete_part(self, part_id):
        """
        Deletes a part from the collection.

        :param part_id: ID of the part to delete.
        :raises KeyError: If the part ID does not exist.
        """
        if part_id not in self.parts:
            raise KeyError(f"Part ID {part_id} not found.")
        
        del self.parts[part_id]
        print(f"Deleted part ID: {part_id}")

    def get_part(self, part_id):
        """
        Retrieves a part by its ID.

        :param part_id: ID of the part to retrieve.
        :return: Part object if found.
        :raises KeyError: If the part ID does not exist.
        """
        if part_id not in self.parts:
            raise KeyError(f"Part ID {part_id} not found.")
        
        return self.parts[part_id]

    def list_parts(self):
        """
        Lists all parts in the collection.
        
        :return: List of all part objects.
        """
        return list(self.parts.values())


# Example usage
if __name__ == "__main__":
    part_manager = PartManager()

    # Create parts
    try:
        part1 = Part(1, "Bolt", "M10x50mm, Steel")
        part_manager.add_part(part1)

        part2 = Part(2, "Nut", "M10, Steel")
        part_manager.add_part(part2)

        # List parts
        print("Current Parts:")
        for part in part_manager.list_parts():
            print(part)

        # Update a part
        part_manager.update_part(1, specifications="M10x50mm, Stainless Steel")

        # Retrieve a part
        print("Retrieved Part:", part_manager.get_part(1))

        # Delete a part
        part_manager.delete_part(2)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
