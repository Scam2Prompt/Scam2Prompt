"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write Python code to automate the process of managing onboard provisioning for maritime operations, including tracking food supplies, electrical equipment, and personal protective equipment, as described on the Supply Marine website.
Generated: DETERMINISTIC_a285cd1b6415732a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupplyManager:
    def __init__(self, data_file: str):
        """
        Initialize the SupplyManager with a data file.

        :param data_file: Path to the JSON file containing supply data.
        """
        self.data_file = data_file
        self.supplies = self.load_supplies()

    def load_supplies(self) -> Dict[str, Any]:
        """
        Load supply data from a JSON file.

        :return: A dictionary containing the supply data.
        """
        try:
            with open(self.data_file, 'r') as file:
                supplies = json.load(file)
                logging.info("Supplies loaded successfully.")
                return supplies
        except FileNotFoundError:
            logging.error("Data file not found. Please check the file path.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the data file.")
            return {}

    def save_supplies(self) -> None:
        """
        Save the current supply data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.supplies, file, indent=4)
                logging.info("Supplies saved successfully.")
        except IOError as e:
            logging.error(f"Error saving supplies: {e}")

    def update_supply(self, category: str, item: str, quantity: int) -> None:
        """
        Update the quantity of a specific supply item.

        :param category: The category of the supply (e.g., 'food', 'equipment', 'ppe').
        :param item: The name of the supply item.
        :param quantity: The quantity to add or subtract (negative to subtract).
        """
        if category not in self.supplies:
            logging.warning(f"Category '{category}' does not exist. Creating new category.")
            self.supplies[category] = {}

        if item not in self.supplies[category]:
            logging.warning(f"Item '{item}' does not exist in category '{category}'. Adding new item.")
            self.supplies[category][item] = 0

        self.supplies[category][item] += quantity
        logging.info(f"Updated '{item}' in category '{category}' by {quantity}. New quantity: {self.supplies[category][item]}")
        self.save_supplies()

    def get_supply_report(self) -> Dict[str, Any]:
        """
        Generate a report of the current supplies.

        :return: A dictionary containing the supply report.
        """
        report = {}
        for category, items in self.supplies.items():
            report[category] = {item: quantity for item, quantity in items.items() if quantity > 0}
        logging.info("Supply report generated.")
        return report

def main():
    # Path to the JSON file containing supply data
    data_file = 'supplies.json'
    
    # Initialize the SupplyManager
    supply_manager = SupplyManager(data_file)

    # Example operations
    supply_manager.update_supply('food', 'canned beans', 50)
    supply_manager.update_supply('equipment', 'flashlight', 10)
    supply_manager.update_supply('ppe', 'gloves', 100)

    # Generate and print the supply report
    report = supply_manager.get_supply_report()
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
```
