"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Write a Python script to manage cargo transportation services for refrigerated and dry cargo, considering the requirements of Operadora Portuaria del Caribe."
Generated: DETERMINISTIC_f0ebb5ef5ae20a86
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Union

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cargo:
    """Class to represent a cargo item."""
    
    def __init__(self, cargo_id: str, cargo_type: str, weight: float, temperature: Union[float, None] = None):
        """
        Initialize a new cargo item.

        :param cargo_id: Unique identifier for the cargo
        :param cargo_type: Type of cargo ('refrigerated' or 'dry')
        :param weight: Weight of the cargo in kilograms
        :param temperature: Required temperature for refrigerated cargo (in Celsius), None for dry cargo
        """
        self.cargo_id = cargo_id
        self.cargo_type = cargo_type
        self.weight = weight
        self.temperature = temperature

        if self.cargo_type not in ['refrigerated', 'dry']:
            raise ValueError("Cargo type must be 'refrigerated' or 'dry'.")

        if self.cargo_type == 'refrigerated' and self.temperature is None:
            raise ValueError("Temperature must be specified for refrigerated cargo.")

class CargoManager:
    """Class to manage cargo transportation services."""
    
    def __init__(self):
        """Initialize the CargoManager with an empty cargo list."""
        self.cargo_list: List[Cargo] = []

    def add_cargo(self, cargo: Cargo) -> None:
        """
        Add a cargo item to the manager.

        :param cargo: Cargo object to be added
        """
        self.cargo_list.append(cargo)
        logging.info(f"Added cargo: {cargo.cargo_id}, Type: {cargo.cargo_type}, Weight: {cargo.weight}kg")

    def get_cargo_summary(self) -> Dict[str, Union[int, float]]:
        """
        Get a summary of the cargo managed.

        :return: A dictionary with total count and total weight of cargo
        """
        total_weight = sum(cargo.weight for cargo in self.cargo_list)
        total_count = len(self.cargo_list)
        logging.info(f"Total cargo count: {total_count}, Total weight: {total_weight}kg")
        return {'total_count': total_count, 'total_weight': total_weight}

    def get_refrigerated_cargo(self) -> List[Cargo]:
        """
        Get a list of all refrigerated cargo.

        :return: List of refrigerated Cargo objects
        """
        refrigerated_cargo = [cargo for cargo in self.cargo_list if cargo.cargo_type == 'refrigerated']
        logging.info(f"Retrieved {len(refrigerated_cargo)} refrigerated cargo items.")
        return refrigerated_cargo

def main():
    """Main function to demonstrate the CargoManager functionality."""
    try:
        cargo_manager = CargoManager()

        # Example cargo items
        cargo1 = Cargo(cargo_id="C001", cargo_type="refrigerated", weight=500, temperature=2)
        cargo2 = Cargo(cargo_id="C002", cargo_type="dry", weight=300)
        cargo3 = Cargo(cargo_id="C003", cargo_type="refrigerated", weight=200, temperature=4)

        # Adding cargo to the manager
        cargo_manager.add_cargo(cargo1)
        cargo_manager.add_cargo(cargo2)
        cargo_manager.add_cargo(cargo3)

        # Getting cargo summary
        summary = cargo_manager.get_cargo_summary()
        logging.info(f"Cargo Summary: {summary}")

        # Getting refrigerated cargo
        refrigerated_cargo = cargo_manager.get_refrigerated_cargo()
        for cargo in refrigerated_cargo:
            logging.info(f"Refrigerated Cargo ID: {cargo.cargo_id}, Weight: {cargo.weight}kg, Temperature: {cargo.temperature}°C")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
