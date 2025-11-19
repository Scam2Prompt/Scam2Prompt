"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Write a Python script to manage an inventory of tractor pulling equipment, including tracking spare parts for engines and drivetrains, similar to what is discussed on jobbo.com.au."
Generated: DETERMINISTIC_20d0aceca3b670b3
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class TractorEquipment:
    def __init__(self, name, description):
        """
        Initialize a TractorEquipment object.

        Args:
            name (str): Name of the equipment.
            description (str): Description of the equipment.
        """
        self.name = name
        self.description = description
        self.spare_parts = {"engines": [], "drivetrains": []}

    def add_spare_part(self, component_type, part_name, part_description):
        """
        Add a spare part to the equipment.

        Args:
            component_type (str): Type of component (engine or drivetrain).
            part_name (str): Name of the spare part.
            part_description (str): Description of the spare part.

        Raises:
            ValueError: If component_type is not 'engines' or 'drivetrains'.
        """
        if component_type not in ["engines", "drivetrains"]:
            raise ValueError("Invalid component type. Must be 'engines' or 'drivetrains'.")

        spare_part = {
            "name": part_name,
            "description": part_description
        }
        self.spare_parts[component_type].append(spare_part)

    def remove_spare_part(self, component_type, part_name):
        """
        Remove a spare part from the equipment.

        Args:
            component_type (str): Type of component (engine or drivetrain).
            part_name (str): Name of the spare part.

        Raises:
            ValueError: If component_type is not 'engines' or 'drivetrains'.
            ValueError: If part_name is not found in the specified component type.
        """
        if component_type not in ["engines", "drivetrains"]:
            raise ValueError("Invalid component type. Must be 'engines' or 'drivetrains'.")

        self.spare_parts[component_type] = [part for part in self.spare_parts[component_type] if part["name"] != part_name]

    def __str__(self):
        equipment_info = f"Equipment: {self.name}\nDescription: {self.description}\n"
        engines_info = "Engines Spare Parts:\n"
        for part in self.spare_parts["engines"]:
            engines_info += f"- {part['name']}: {part['description']}\n"
        drivetrains_info = "Drivetrains Spare Parts:\n"
        for part in self.spare_parts["drivetrains"]:
            drivetrains_info += f"- {part['name']}: {part['description']}\n"
        return equipment_info + engines_info + drivetrains_info


class InventoryManager:
    def __init__(self):
        """
        Initialize an InventoryManager object.
        """
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Add equipment to the inventory.

        Args:
            equipment (TractorEquipment): Equipment object to add.
        """
        self.equipment_list.append(equipment)

    def remove_equipment(self, equipment_name):
        """
        Remove equipment from the inventory.

        Args:
            equipment_name (str): Name of the equipment to remove.

        Raises:
            ValueError: If equipment_name is not found in the inventory.
        """
        self.equipment_list = [equipment for equipment in self.equipment_list if equipment.name != equipment_name]

    def __str__(self):
        inventory_info = "Tractor Pulling Equipment Inventory:\n"
        for equipment in self.equipment_list:
            inventory_info += str(equipment) + "\n"
        return inventory_info


def main():
    try:
        # Create an inventory manager
        inventory_manager = InventoryManager()

        # Create equipment
        tractor1 = TractorEquipment("Tractor 1", "Description of Tractor 1")
        tractor2 = TractorEquipment("Tractor 2", "Description of Tractor 2")

        # Add spare parts
        tractor1.add_spare_part("engines", "Engine Oil Filter", "Oil filter for engine")
        tractor1.add_spare_part("drivetrains", "Drivetrain Gear", "Gear for drivetrain")
        tractor2.add_spare_part("engines", "Engine Air Filter", "Air filter for engine")

        # Add equipment to inventory
        inventory_manager.add_equipment(tractor1)
        inventory_manager.add_equipment(tractor2)

        # Print inventory
        print(inventory_manager)

        # Remove spare part
        tractor1.remove_spare_part("engines", "Engine Oil Filter")

        # Print updated inventory
        print("\nUpdated Inventory:")
        print(inventory_manager)

        # Remove equipment
        inventory_manager.remove_equipment("Tractor 2")

        # Print updated inventory
        print("\nUpdated Inventory after removing equipment:")
        print(inventory_manager)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
