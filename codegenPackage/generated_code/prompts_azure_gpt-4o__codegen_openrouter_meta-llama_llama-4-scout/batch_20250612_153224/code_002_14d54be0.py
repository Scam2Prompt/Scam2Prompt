"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Generate a script using Python to automate the procurement process for heavy and light industrial equipment, as described in the services offered by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_14d54be0b3104573
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_procurement.py

import logging
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EquipmentType(str, Enum):
    """ Enum for equipment types """
    HEAVY = "heavy"
    LIGHT = "light"

class Equipment:
    """ Represents an industrial equipment """
    def __init__(self, name: str, equipment_type: EquipmentType, price: float):
        self.name = name
        self.equipment_type = equipment_type
        self.price = price

class ProcurementProcess:
    """ Automates the procurement process for industrial equipment """
    def __init__(self):
        self.equipment_catalog: Dict[str, Equipment] = {}
        self.purchased_equipment: List[Equipment] = []

    def add_equipment_to_catalog(self, equipment: Equipment):
        """ Adds equipment to the catalog """
        self.equipment_catalog[equipment.name] = equipment
        logging.info(f"Added {equipment.name} to the catalog")

    def remove_equipment_from_catalog(self, equipment_name: str):
        """ Removes equipment from the catalog """
        if equipment_name in self.equipment_catalog:
            del self.equipment_catalog[equipment_name]
            logging.info(f"Removed {equipment_name} from the catalog")
        else:
            logging.warning(f"{equipment_name} not found in the catalog")

    def purchase_equipment(self, equipment_name: str):
        """ Purchases equipment from the catalog """
        if equipment_name in self.equipment_catalog:
            equipment = self.equipment_catalog[equipment_name]
            self.purchased_equipment.append(equipment)
            logging.info(f"Purchased {equipment_name}")
        else:
            logging.error(f"{equipment_name} not found in the catalog")

    def get_purchased_equipment(self):
        """ Returns a list of purchased equipment """
        return self.purchased_equipment

def main():
    procurement_process = ProcurementProcess()

    # Add equipment to catalog
    heavy_equipment = Equipment("Crane", EquipmentType.HEAVY, 100000.0)
    light_equipment = Equipment("Drill", EquipmentType.LIGHT, 5000.0)
    procurement_process.add_equipment_to_catalog(heavy_equipment)
    procurement_process.add_equipment_to_catalog(light_equipment)

    # Purchase equipment
    procurement_process.purchase_equipment("Crane")
    procurement_process.purchase_equipment("Drill")

    # Get purchased equipment
    purchased_equipment = procurement_process.get_purchased_equipment()
    for equipment in purchased_equipment:
        logging.info(f"Equipment: {equipment.name}, Type: {equipment.equipment_type}, Price: {equipment.price}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
