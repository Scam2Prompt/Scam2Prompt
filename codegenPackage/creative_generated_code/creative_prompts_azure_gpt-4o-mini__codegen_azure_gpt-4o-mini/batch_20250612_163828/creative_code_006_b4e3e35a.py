"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Explain how CRM.f facilitates multi-site equipment management for foundations and nonprofits.
Generated: DETERMINISTIC_b4e3e35a6c779560
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CRM.f (Customer Relationship Management for Foundations) is a Python class that 
facilitates multi-site equipment management for foundations and nonprofits. 
The class allows users to track equipment across multiple sites, 
providing functionalities to add, update, and retrieve equipment details. 
Error handling is incorporated to manage typical issues such as 
duplicate entries or missing data.
"""

class Equipment:
    """Class to represent an equipment item."""
    
    def __init__(self, equipment_id, name, site, status):
        """
        Initialize the equipment item.

        Args:
            equipment_id (str): Unique identifier for the equipment.
            name (str): Name of the equipment.
            site (str): The site where the equipment is located.
            status (str): Current status of the equipment (e.g., 'available', 'checked out').
        """
        self.equipment_id = equipment_id
        self.name = name
        self.site = site
        self.status = status

    def __str__(self):
        """Return a string representation of the equipment."""
        return f"Equipment(ID: {self.equipment_id}, Name: {self.name}, Site: {self.site}, Status: {self.status})"


class EquipmentManager:
    """Class to manage multiple equipment items across different sites."""
    
    def __init__(self):
        """Initialize the equipment manager with an empty equipment registry."""
        self.equipment_registry = {}

    def add_equipment(self, equipment):
        """
        Add a new equipment item to the registry.

        Args:
            equipment (Equipment): The equipment item to add.

        Raises:
            ValueError: If the equipment ID already exists in the registry.
        """
        if equipment.equipment_id in self.equipment_registry:
            raise ValueError(f"Equipment ID {equipment.equipment_id} already exists.")
        
        self.equipment_registry[equipment.equipment_id] = equipment
        print(f"Added: {equipment}")

    def update_equipment(self, equipment_id, name=None, site=None, status=None):
        """
        Update an existing equipment item in the registry.

        Args:
            equipment_id (str): The ID of the equipment to update.
            name (str, optional): New name of the equipment.
            site (str, optional): New site of the equipment.
            status (str, optional): New status of the equipment.

        Raises:
            KeyError: If the equipment ID does not exist in the registry.
        """
        if equipment_id not in self.equipment_registry:
            raise KeyError(f"Equipment ID {equipment_id} not found.")
        
        equipment = self.equipment_registry[equipment_id]
        if name:
            equipment.name = name
        if site:
            equipment.site = site
        if status:
            equipment.status = status
        print(f"Updated: {equipment}")

    def get_equipment(self, equipment_id):
        """
        Retrieve an equipment item from the registry.

        Args:
            equipment_id (str): The ID of the equipment to retrieve.

        Returns:
            Equipment: The requested equipment item.

        Raises:
            KeyError: If the equipment ID does not exist in the registry.
        """
        if equipment_id not in self.equipment_registry:
            raise KeyError(f"Equipment ID {equipment_id} not found.")
        
        return self.equipment_registry[equipment_id]

    def list_equipment(self):
        """List all equipment items in the registry."""
        return list(self.equipment_registry.values())


# Example usage of the EquipmentManager class
if __name__ == "__main__":
    manager = EquipmentManager()

    # Adding equipment to the manager
    try:
        equipment1 = Equipment("001", "Projector", "Site A", "available")
        manager.add_equipment(equipment1)

        equipment2 = Equipment("002", "Laptop", "Site B", "checked out")
        manager.add_equipment(equipment2)

        # Attempting to add an equipment item with a duplicate ID
        duplicate_equipment = Equipment("001", "Camera", "Site A", "available")
        manager.add_equipment(duplicate_equipment)  # This will raise a ValueError
    except ValueError as e:
        print(e)

    # Updating equipment status
    try:
        manager.update_equipment("001", status="checked out")
        print(manager.get_equipment("001"))
    except (KeyError, ValueError) as e:
        print(e)

    # Listing all equipment
    print("All Equipment:")
    for equipment in manager.list_equipment():
        print(equipment)
```
