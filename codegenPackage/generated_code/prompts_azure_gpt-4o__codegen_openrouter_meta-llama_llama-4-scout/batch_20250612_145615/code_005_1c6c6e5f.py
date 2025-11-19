"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write code to manage an inventory of label designs for small businesses, including options for crafts and sports teams, referencing the use cases from Labelmystuff.com.
Generated: DETERMINISTIC_1c6c6e5f5d08cbd2
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# label_design_inventory.py

from enum import Enum
from typing import Dict, List

class LabelType(Enum):
    """Enum for label types."""
    CRAFT = "craft"
    SPORTS_TEAM = "sports_team"

class LabelDesign:
    """Class representing a label design."""
    def __init__(self, id: int, name: str, label_type: LabelType, description: str):
        """
        Initialize a LabelDesign object.

        Args:
        id (int): Unique identifier for the label design.
        name (str): Name of the label design.
        label_type (LabelType): Type of label design.
        description (str): Description of the label design.
        """
        self.id = id
        self.name = name
        self.label_type = label_type
        self.description = description

class Inventory:
    """Class representing the label design inventory."""
    def __init__(self):
        """Initialize an empty inventory."""
        self.label_designs: Dict[int, LabelDesign] = {}
        self.next_id: int = 1

    def add_label_design(self, name: str, label_type: LabelType, description: str) -> int:
        """
        Add a new label design to the inventory.

        Args:
        name (str): Name of the label design.
        label_type (LabelType): Type of label design.
        description (str): Description of the label design.

        Returns:
        int: The ID of the newly added label design.

        Raises:
        ValueError: If the name or description is empty.
        """
        if not name or not description:
            raise ValueError("Name and description cannot be empty")

        label_design = LabelDesign(self.next_id, name, label_type, description)
        self.label_designs[self.next_id] = label_design
        self.next_id += 1
        return label_design.id

    def get_label_design(self, id: int) -> LabelDesign:
        """
        Get a label design by its ID.

        Args:
        id (int): ID of the label design.

        Returns:
        LabelDesign: The label design with the given ID, or None if not found.
        """
        return self.label_designs.get(id)

    def update_label_design(self, id: int, name: str = None, label_type: LabelType = None, description: str = None) -> bool:
        """
        Update a label design.

        Args:
        id (int): ID of the label design.
        name (str, optional): New name of the label design. Defaults to None.
        label_type (LabelType, optional): New type of the label design. Defaults to None.
        description (str, optional): New description of the label design. Defaults to None.

        Returns:
        bool: True if the label design was updated, False if not found.
        """
        label_design = self.label_designs.get(id)
        if label_design:
            if name:
                label_design.name = name
            if label_type:
                label_design.label_type = label_type
            if description:
                label_design.description = description
            return True
        return False

    def delete_label_design(self, id: int) -> bool:
        """
        Delete a label design.

        Args:
        id (int): ID of the label design.

        Returns:
        bool: True if the label design was deleted, False if not found.
        """
        if id in self.label_designs:
            del self.label_designs[id]
            return True
        return False

def main():
    # Example usage:
    inventory = Inventory()

    # Add label designs
    craft_label_id = inventory.add_label_design("Craft Label", LabelType.CRAFT, "A label for craft businesses")
    sports_team_label_id = inventory.add_label_design("Sports Team Label", LabelType.SPORTS_TEAM, "A label for sports teams")

    # Get label design
    craft_label = inventory.get_label_design(craft_label_id)
    print(f"Craft Label: {craft_label.name} ({craft_label.label_type}) - {craft_label.description}")

    # Update label design
    inventory.update_label_design(craft_label_id, description="A new description for craft businesses")
    updated_craft_label = inventory.get_label_design(craft_label_id)
    print(f"Updated Craft Label: {updated_craft_label.name} ({updated_craft_label.label_type}) - {updated_craft_label.description}")

    # Delete label design
    inventory.delete_label_design(sports_team_label_id)
    print(f"Label design with ID {sports_team_label_id} deleted: {sports_team_label_id not in inventory.label_designs}")

if __name__ == "__main__":
    main()
```
