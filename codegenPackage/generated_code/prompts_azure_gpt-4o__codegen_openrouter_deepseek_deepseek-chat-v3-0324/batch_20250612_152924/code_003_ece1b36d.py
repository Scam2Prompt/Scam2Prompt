"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Create a Python program to assist in the selection and updating of gas network equipment, referencing Espinel y Cia's advisory services.
Generated: DETERMINISTIC_ece1b36df96a4ae4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gas Network Equipment Selection and Updating Tool
Reference: Espinel y Cia's Advisory Services

This program assists in the selection and updating of gas network equipment
based on predefined criteria and Espinel y Cia's advisory services.
"""

import json
import sys
from typing import Dict, List, Optional


class EquipmentDatabase:
    """Handles the storage and retrieval of gas network equipment data."""

    def __init__(self, database_file: str = "equipment_database.json"):
        """
        Initialize the equipment database.

        Args:
            database_file: Path to the JSON file containing equipment data.
        """
        self.database_file = database_file
        self.equipment_data = self._load_database()

    def _load_database(self) -> Dict:
        """Load equipment data from JSON file."""
        try:
            with open(self.database_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: Database file {self.database_file} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {self.database_file}.")
            sys.exit(1)

    def save_database(self) -> None:
        """Save the current equipment data to the database file."""
        try:
            with open(self.database_file, "w") as file:
                json.dump(self.equipment_data, file, indent=4)
        except IOError as e:
            print(f"Error saving database: {e}")

    def get_equipment_by_type(self, equipment_type: str) -> List[Dict]:
        """
        Retrieve equipment by type.

        Args:
            equipment_type: Type of equipment to retrieve.

        Returns:
            List of equipment matching the type.
        """
        return self.equipment_data.get(equipment_type, [])

    def add_equipment(self, equipment_type: str, equipment_details: Dict) -> bool:
        """
        Add new equipment to the database.

        Args:
            equipment_type: Type of equipment to add.
            equipment_details: Dictionary containing equipment details.

        Returns:
            True if successful, False otherwise.
        """
        if equipment_type not in self.equipment_data:
            self.equipment_data[equipment_type] = []
        
        # Check if equipment already exists
        for equipment in self.equipment_data[equipment_type]:
            if equipment["id"] == equipment_details.get("id"):
                return False
        
        self.equipment_data[equipment_type].append(equipment_details)
        return True

    def update_equipment(self, equipment_type: str, equipment_id: str, new_details: Dict) -> bool:
        """
        Update existing equipment in the database.

        Args:
            equipment_type: Type of equipment to update.
            equipment_id: ID of the equipment to update.
            new_details: Dictionary containing updated equipment details.

        Returns:
            True if successful, False otherwise.
        """
        if equipment_type not in self.equipment_data:
            return False
        
        for equipment in self.equipment_data[equipment_type]:
            if equipment["id"] == equipment_id:
                equipment.update(new_details)
                return True
        
        return False


class EquipmentSelector:
    """Handles the selection of appropriate gas network equipment."""

    def __init__(self, database: EquipmentDatabase):
        """
        Initialize the equipment selector.

        Args:
            database: Instance of EquipmentDatabase.
        """
        self.database = database

    def select_equipment(self, criteria: Dict) -> Optional[Dict]:
        """
        Select equipment based on specified criteria.

        Args:
            criteria: Dictionary containing selection criteria.

        Returns:
            Dictionary of selected equipment if found, None otherwise.
        """
        equipment_type = criteria.get("type")
        if not equipment_type:
            return None

        available_equipment = self.database.get_equipment_by_type(equipment_type)
        if not available_equipment:
            return None

        # Simple selection logic - can be enhanced based on specific requirements
        for equipment in available_equipment:
            if all(equipment.get(key) == value for key, value in criteria.items() if key != "type"):
                return equipment
        
        return None


class UserInterface:
    """Handles user interaction and menu navigation."""

    def __init__(self):
        """Initialize the user interface."""
        self.database = EquipmentDatabase()
        self.selector = EquipmentSelector(self.database)

    def display_menu(self) -> None:
        """Display the main menu and handle user input."""
        while True:
            print("\nGas Network Equipment Selection Tool")
            print("1. View Equipment by Type")
            print("2. Select Equipment")
            print("3. Add New Equipment")
            print("4. Update Existing Equipment")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self._view_equipment()
            elif choice == "2":
                self._select_equipment()
            elif choice == "3":
                self._add_equipment()
            elif choice == "4":
                self._update_equipment()
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def _view_equipment(self) -> None:
        """Display equipment by type."""
        equipment_type = input("Enter equipment type to view: ")
        equipment_list = self.database.get_equipment_by_type(equipment_type)
        
        if not equipment_list:
            print(f"No equipment found for type: {equipment_type}")
            return
        
        print(f"\n{equipment_type} Equipment:")
        for equipment in equipment_list:
            print(json.dumps(equipment, indent=2))

    def _select_equipment(self) -> None:
        """Select equipment based on criteria."""
        print("\nEnter selection criteria:")
        criteria = {}
        criteria["type"] = input("Equipment type: ")
        criteria["capacity"] = input("Capacity (leave blank if not applicable): ") or None
        criteria["pressure_rating"] = input("Pressure rating (leave blank if not applicable): ") or None
        
        selected = self.selector.select_equipment(criteria)
        if selected:
            print("\nSelected Equipment:")
            print(json.dumps(selected, indent=2))
        else:
            print("No matching equipment found.")

    def _add_equipment(self) -> None:
        """Add new equipment to the database."""
        print("\nAdd New Equipment")
        equipment_type = input("Equipment type: ")
        equipment_id = input("Equipment ID: ")
        
        # Check if equipment already exists
        existing = self.database.get_equipment_by_type(equipment_type)
        for equipment in existing:
            if equipment["id"] == equipment_id:
                print("Error: Equipment with this ID already exists.")
                return
        
        # Get additional details
        details = {"id": equipment_id}
        details["name"] = input("Equipment name: ")
        details["capacity"] = input("Capacity: ")
        details["pressure_rating"] = input("Pressure rating: ")
        details["manufacturer"] = input("Manufacturer: ")
        
        if self.database.add_equipment(equipment_type, details):
            self.database.save_database()
            print("Equipment added successfully.")
        else:
            print("Error: Failed to add equipment.")

    def _update_equipment(self) -> None:
        """Update existing equipment in the database."""
        print("\nUpdate Equipment")
        equipment_type = input("Equipment type: ")
        equipment_id = input("Equipment ID to update: ")
        
        # Check if equipment exists
        existing = self.database.get_equipment_by_type(equipment_type)
        found = False
        for equipment in existing:
            if equipment["id"] == equipment_id:
                found = True
                break
        
        if not found:
            print("Error: Equipment not found.")
            return
        
        # Get updated details
        print("Enter new values (leave blank to keep current):")
        new_details = {}
        new_details["name"] = input("New name: ") or None
        new_details["capacity"] = input("New capacity: ") or None
        new_details["pressure_rating"] = input("New pressure rating: ") or None
        new_details["manufacturer"] = input("New manufacturer: ") or None
        
        # Remove None values
        new_details = {k: v for k, v in new_details.items() if v is not None}
        
        if self.database.update_equipment(equipment_type, equipment_id, new_details):
            self.database.save_database()
            print("Equipment updated successfully.")
        else:
            print("Error: Failed to update equipment.")


def main():
    """Main entry point for the program."""
    try:
        ui = UserInterface()
        ui.display_menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
