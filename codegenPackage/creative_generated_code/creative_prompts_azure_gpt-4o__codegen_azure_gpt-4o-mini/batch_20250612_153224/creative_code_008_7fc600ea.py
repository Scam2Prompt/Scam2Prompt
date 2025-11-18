"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Recommend tools or libraries for implementing a home restoration management system, including tracking repairs and material usage, as described in the "شمس المملكة" services.
Generated: DETERMINISTIC_7fc600eab23e9d34
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Home Restoration Management System
This script provides a basic structure for implementing a home restoration management system.
It includes classes for managing repairs and material usage while employing best practices in Python.
"""

import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Repair:
    """
    Class representing a repair task in the home restoration process.
    """
    
    def __init__(self, description: str, cost: float):
        """
        Initializes a new repair task.

        :param description: A brief description of the repair.
        :param cost: Cost associated with the repair.
        """
        self.description = description
        self.cost = cost
        
        # Validate input
        if cost < 0:
            logging.error("Cost cannot be negative.")
            raise ValueError("Cost cannot be negative.")

    def __repr__(self):
        return f"Repair(description='{self.description}', cost={self.cost})"


class Material:
    """
    Class representing a material used in the home restoration process.
    """
    
    def __init__(self, name: str, quantity: float):
        """
        Initializes a new material.

        :param name: Name of the material.
        :param quantity: Quantity of the material available.
        """
        self.name = name
        self.quantity = quantity
        
        # Validate input
        if quantity < 0:
            logging.error("Quantity cannot be negative.")
            raise ValueError("Quantity cannot be negative.")

    def __repr__(self):
        return f"Material(name='{self.name}', quantity={self.quantity})"


class RestorationManagementSystem:
    """
    Class to manage the home restoration process including repairs and materials.
    """
    
    def __init__(self):
        self.repairs: List[Repair] = []
        self.materials: List[Material] = []
        
    def add_repair(self, repair: Repair):
        """
        Adds a repair task to the system.

        :param repair: An instance of Repair to be added.
        """
        self.repairs.append(repair)
        logging.info(f"Added repair: {repair}")

    def add_material(self, material: Material):
        """
        Adds a material to the system.

        :param material: An instance of Material to be added.
        """
        self.materials.append(material)
        logging.info(f"Added material: {material}")

    def get_total_repair_cost(self) -> float:
        """
        Calculates the total cost of all repairs.

        :return: Total cost of repairs.
        """
        total_cost = sum(repair.cost for repair in self.repairs)
        logging.info(f"Total repair cost: {total_cost}")
        return total_cost

    def get_material_usage(self) -> Dict[str, float]:
        """
        Returns the current materials and their quantities.

        :return: Dictionary of materials and their quantities.
        """
        material_usage = {material.name: material.quantity for material in self.materials}
        logging.info(f"Current material usage: {material_usage}")
        return material_usage


# Example usage
if __name__ == "__main__":
    try:
        restoration_system = RestorationManagementSystem()

        # Adding repairs
        restoration_system.add_repair(Repair("Roof leak repair", 250.0))
        restoration_system.add_repair(Repair("Wall painting", 150.0))

        # Adding materials
        restoration_system.add_material(Material("Paint", 20.0))
        restoration_system.add_material(Material("Nails", 100.0))

        # Displaying costs and materials
        total_cost = restoration_system.get_total_repair_cost()
        materials = restoration_system.get_material_usage()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
