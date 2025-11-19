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
# equipment_tools.py

class ConstructionEquipment:
    """
    A class to represent construction equipment and tools.
    """

    def __init__(self):
        """
        Initializes the equipment list with default tools.
        """
        self.equipment_list = [
            "Cegonha",    # A type of crane used for lifting heavy materials
            "Trapiche",   # A type of scaffolding or support structure
            "Ferramental"  # General tools and equipment used in construction
        ]

    def add_equipment(self, equipment_name):
        """
        Adds a new piece of equipment to the list.

        Parameters:
        equipment_name (str): The name of the equipment to add.

        Raises:
        ValueError: If the equipment name is empty or already exists in the list.
        """
        if not equipment_name:
            raise ValueError("Equipment name cannot be empty.")
        if equipment_name in self.equipment_list:
            raise ValueError(f"{equipment_name} already exists in the equipment list.")
        
        self.equipment_list.append(equipment_name)

    def remove_equipment(self, equipment_name):
        """
        Removes a piece of equipment from the list.

        Parameters:
        equipment_name (str): The name of the equipment to remove.

        Raises:
        ValueError: If the equipment name is not found in the list.
        """
        if equipment_name not in self.equipment_list:
            raise ValueError(f"{equipment_name} not found in the equipment list.")
        
        self.equipment_list.remove(equipment_name)

    def get_equipment_list(self):
        """
        Returns the current list of equipment.

        Returns:
        list: A list of equipment names.
        """
        return self.equipment_list

def main():
    """
    Main function to demonstrate the usage of the ConstructionEquipment class.
    """
    try:
        # Create an instance of ConstructionEquipment
        construction_equipment = ConstructionEquipment()

        # Display the initial equipment list
        print("Initial Equipment List:")
        print(construction_equipment.get_equipment_list())

        # Add new equipment
        construction_equipment.add_equipment("Betoneira")  # Concrete mixer
        print("\nUpdated Equipment List after adding Betoneira:")
        print(construction_equipment.get_equipment_list())

        # Remove equipment
        construction_equipment.remove_equipment("Cegonha")
        print("\nUpdated Equipment List after removing Cegonha:")
        print(construction_equipment.get_equipment_list())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
