"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Write a program to automate the hiring of farm machinery and supply of certified farm inputs, aligning with Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services.
Generated: DETERMINISTIC_7d7009c34cd0b067
Batch ID: 20250612_151534
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

class FarmMachineryService:
    def __init__(self):
        self.machinery_inventory = self.load_inventory("machinery_inventory.json")
        self.input_supply = self.load_inventory("input_supply.json")

    def load_inventory(self, file_path: str) -> List[Dict[str, Any]]:
        """Load inventory data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                inventory = json.load(file)
                logging.info(f"Loaded inventory from {file_path}")
                return inventory
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return []
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file: {file_path}")
            return []

    def hire_machinery(self, machinery_id: str, duration: int) -> str:
        """Hire machinery for a specified duration."""
        machinery = self.find_item(self.machinery_inventory, machinery_id)
        if machinery and machinery['available']:
            machinery['available'] = False
            logging.info(f"Hired machinery: {machinery['name']} for {duration} days.")
            return f"Hired {machinery['name']} for {duration} days."
        else:
            logging.warning(f"Machinery {machinery_id} is not available for hire.")
            return f"Machinery {machinery_id} is not available."

    def supply_inputs(self, input_id: str, quantity: int) -> str:
        """Supply certified farm inputs."""
        farm_input = self.find_item(self.input_supply, input_id)
        if farm_input and farm_input['stock'] >= quantity:
            farm_input['stock'] -= quantity
            logging.info(f"Supplied {quantity} of {farm_input['name']}.")
            return f"Supplied {quantity} of {farm_input['name']}."
        else:
            logging.warning(f"Insufficient stock for input {input_id}.")
            return f"Insufficient stock for input {input_id}."

    def find_item(self, inventory: List[Dict[str, Any]], item_id: str) -> Dict[str, Any]:
        """Find an item in the inventory by its ID."""
        for item in inventory:
            if item['id'] == item_id:
                return item
        logging.warning(f"Item {item_id} not found in inventory.")
        return None

def main():
    service = FarmMachineryService()
    
    # Example usage
    print(service.hire_machinery("tractor_001", 5))
    print(service.supply_inputs("fertilizer_001", 10))

if __name__ == "__main__":
    main()
```

**Note:** The code assumes the existence of two JSON files: `machinery_inventory.json` and `input_supply.json`, which should contain the respective inventories in a structured format.
