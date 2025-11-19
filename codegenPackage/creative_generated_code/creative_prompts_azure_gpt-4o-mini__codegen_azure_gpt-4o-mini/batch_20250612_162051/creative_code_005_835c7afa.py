"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Suggest a library for managing the automation of a potato processing plant, including equipment like fryers and packaging machines.
Generated: DETERMINISTIC_835c7afaae526878
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Equipment:
    """Base class for all equipment in the processing plant."""
    
    def __init__(self, name):
        self.name = name
        self.is_operational = True

    def start(self):
        """Start the equipment operation."""
        if self.is_operational:
            logging.info(f"{self.name} started.")
        else:
            logging.warning(f"{self.name} is not operational.")

    def stop(self):
        """Stop the equipment operation."""
        logging.info(f"{self.name} stopped.")

    def check_status(self):
        """Check if the equipment is operational."""
        return self.is_operational


class Fryer(Equipment):
    """Class representing the fryer equipment."""
    
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        """Set the frying temperature."""
        self.temperature = temperature
        logging.info(f"{self.name} temperature set to {self.temperature}°C.")


class PackagingMachine(Equipment):
    """Class representing the packaging machine."""
    
    def __init__(self, name):
        super().__init__(name)

    def package_product(self):
        """Package the product."""
        if self.is_operational:
            logging.info(f"Packaging product using {self.name}.")
        else:
            logging.warning(f"{self.name} is not operational. Cannot package product.")


class PotatoProcessingPlant:
    """Class to manage the potato processing plant operations."""
    
    def __init__(self):
        self.equipments = []
    
    def add_equipment(self, equipment):
        """Add new equipment to the plant."""
        if isinstance(equipment, Equipment):
            self.equipments.append(equipment)
            logging.info(f"Added equipment: {equipment.name}")
        else:
            logging.error("Attempted to add non-equipment object.")

    def start_all(self):
        """Start all equipment in the plant."""
        for equipment in self.equipments:
            equipment.start()

    def stop_all(self):
        """Stop all equipment in the plant."""
        for equipment in self.equipments:
            equipment.stop()

    def check_status(self):
        """Check the operational status of all equipment."""
        for equipment in self.equipments:
            status = "operational" if equipment.check_status() else "not operational"
            logging.info(f"{equipment.name} is {status}.")


# Example usage
if __name__ == "__main__":
    logging.info("Starting Potato Processing Plant Automation...")

    plant = PotatoProcessingPlant()
    
    # Creating equipment instances
    fryer = Fryer(name="Industrial Fryer", temperature=180)
    packaging_machine = PackagingMachine(name="Vacuum Packaging Machine")

    # Adding equipment to the plant
    plant.add_equipment(fryer)
    plant.add_equipment(packaging_machine)

    # Starting operations
    plant.start_all()

    # Setting temperature for fryer
    fryer.set_temperature(190)

    # Packaging products
    packaging_machine.package_product()

    # Checking statuses
    plant.check_status()

    # Stopping operations
    plant.stop_all()

    logging.info("Potato Processing Plant Automation completed.")
```
