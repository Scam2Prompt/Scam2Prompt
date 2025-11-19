"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Generate a list of equipment and tools used in construction, including cegonha, trapiche, and ferramental.
Generated: DETERMINISTIC_46f8dfab19b18e8c
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment.py

class ConstructionEquipment:
    """Represents a piece of equipment used in construction."""

    def __init__(self, name, description):
        """
        Initializes a ConstructionEquipment object.

        Args:
            name (str): The name of the equipment.
            description (str): A brief description of the equipment.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class ConstructionEquipmentList:
    """Represents a list of construction equipment."""

    def __init__(self):
        """Initializes an empty list of construction equipment."""
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Adds a piece of equipment to the list.

        Args:
            equipment (ConstructionEquipment): The equipment to add.

        Raises:
            TypeError: If the equipment is not a ConstructionEquipment object.
        """
        if not isinstance(equipment, ConstructionEquipment):
            raise TypeError("Only ConstructionEquipment objects can be added to the list.")
        self.equipment_list.append(equipment)

    def __str__(self):
        equipment_list_str = "List of Construction Equipment:\n"
        for equipment in self.equipment_list:
            equipment_list_str += f"- {equipment}\n"
        return equipment_list_str


def main():
    try:
        # Create a list of construction equipment
        equipment_list = ConstructionEquipmentList()

        # Create individual pieces of equipment
        cegonha = ConstructionEquipment("Cegonha", "A type of crane used in construction.")
        trapiche = ConstructionEquipment("Trapiche", "A type of pulley system used in construction.")
        ferramental = ConstructionEquipment("Ferramental", "A set of metalworking tools used in construction.")

        # Add equipment to the list
        equipment_list.add_equipment(cegonha)
        equipment_list.add_equipment(trapiche)
        equipment_list.add_equipment(ferramental)

        # Print the list of equipment
        print(equipment_list)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
