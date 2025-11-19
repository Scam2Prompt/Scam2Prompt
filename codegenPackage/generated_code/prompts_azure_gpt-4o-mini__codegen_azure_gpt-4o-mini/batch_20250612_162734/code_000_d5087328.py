"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Generate a code snippet for a machinery management system that utilizes tools like "roldana" and "trapiche" for efficient equipment tracking.
Generated: DETERMINISTIC_d5087328d73a7ac9
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Equipment:
    """Class representing a piece of equipment in the machinery management system."""
    
    def __init__(self, name: str, equipment_type: str, status: str):
        """
        Initialize a new Equipment instance.

        :param name: Name of the equipment
        :param equipment_type: Type of the equipment (e.g., 'roldana', 'trapiche')
        :param status: Current status of the equipment (e.g., 'available', 'in use', 'maintenance')
        """
        self.name = name
        self.equipment_type = equipment_type
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the equipment."""
        logging.info(f"Updating status of {self.name} from {self.status} to {new_status}")
        self.status = new_status

class EquipmentManager:
    """Class to manage a collection of equipment."""
    
    def __init__(self):
        """Initialize the EquipmentManager with an empty equipment list."""
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment):
        """Add a new piece of equipment to the management system."""
        logging.info(f"Adding equipment: {equipment.name}")
        self.equipment_list.append(equipment)

    def find_equipment(self, name: str) -> Optional[Equipment]:
        """Find equipment by name.

        :param name: Name of the equipment to find
        :return: Equipment object if found, None otherwise
        """
        for equipment in self.equipment_list:
            if equipment.name == name:
                logging.info(f"Equipment {name} found.")
                return equipment
        logging.warning(f"Equipment {name} not found.")
        return None

    def update_equipment_status(self, name: str, new_status: str):
        """Update the status of a specific piece of equipment."""
        equipment = self.find_equipment(name)
        if equipment:
            equipment.update_status(new_status)
        else:
            logging.error(f"Cannot update status: Equipment {name} does not exist.")

    def list_equipment(self) -> List[Dict[str, str]]:
        """List all equipment with their details.

        :return: List of dictionaries containing equipment details
        """
        return [{'name': eq.name, 'type': eq.equipment_type, 'status': eq.status} for eq in self.equipment_list]

# Example usage
if __name__ == "__main__":
    manager = EquipmentManager()
    
    # Adding equipment
    manager.add_equipment(Equipment("Roldana 1", "roldana", "available"))
    manager.add_equipment(Equipment("Trapiche 1", "trapiche", "available"))

    # Listing equipment
    logging.info("Current equipment list:")
    for equipment in manager.list_equipment():
        logging.info(equipment)

    # Updating equipment status
    manager.update_equipment_status("Roldana 1", "in use")
    
    # Attempting to update a non-existent equipment
    manager.update_equipment_status("Non-existent Equipment", "available")
```
