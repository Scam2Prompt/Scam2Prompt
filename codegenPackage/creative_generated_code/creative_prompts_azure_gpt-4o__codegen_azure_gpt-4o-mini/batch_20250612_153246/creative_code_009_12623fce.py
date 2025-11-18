"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Develop a tool to manage and optimize the provisioning of fresh and ready-to-consume food supplies for maritime crews, referencing the quality and safety standards highlighted by Supply Marine.
Generated: DETERMINISTIC_12623fce90b1e7a9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FoodSupplyManager:
    """
    A class to manage and optimize the provisioning of fresh and ready-to-consume food supplies for maritime crews.
    This class ensures compliance with quality and safety standards.
    """
    
    def __init__(self):
        self.supplies = []
        self.load_supplies()

    def load_supplies(self, filepath='supplies.json'):
        """
        Load food supply data from a JSON file.
        
        Args:
            filepath (str): The path to the JSON file containing food supply data.
        """
        try:
            with open(filepath, 'r') as file:
                self.supplies = json.load(file)
                logging.info("Supplies loaded successfully.")
        except FileNotFoundError:
            logging.error("Supplies file not found.")
            self.supplies = []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the supplies file.")
            self.supplies = []

    def save_supplies(self, filepath='supplies.json'):
        """
        Save food supply data to a JSON file.
        
        Args:
            filepath (str): The path to the JSON file to save food supply data.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.supplies, file, indent=4)
                logging.info("Supplies saved successfully.")
        except IOError as e:
            logging.error(f"Error saving supplies file: {e}")

    def add_supply(self, item):
        """
        Add a new food supply item to the inventory.
        
        Args:
            item (dict): A dictionary containing the supply item details.
        """
        self.supplies.append(item)
        logging.info(f"Added supply: {item}")

    def remove_supply(self, item_name):
        """
        Remove a food supply item from the inventory by name.
        
        Args:
            item_name (str): The name of the supply item to be removed.
        """
        self.supplies = [item for item in self.supplies if item['name'] != item_name]
        logging.info(f"Removed supply: {item_name}")

    def optimize_supplies(self):
        """
        Optimize food supplies based on expiry dates to minimize waste.
        This method sorts supplies by expiration date and removes expired items.
        """
        current_date = datetime.now()
        self.supplies = [item for item in self.supplies if datetime.strptime(item['expiry_date'], '%Y-%m-%d') > current_date]
        self.supplies.sort(key=lambda x: datetime.strptime(x['expiry_date'], '%Y-%m-%d'))
        logging.info("Supplies optimized; expired items removed.")

    def view_supplies(self):
        """
        Display the current food supplies in the inventory.
        """
        for item in self.supplies:
            logging.info(f"Supply Item: {item['name']}, Expiry Date: {item['expiry_date']}, Quantity: {item['quantity']}")

def main():
    """
    Main function to run the Food Supply Manager tool.
    """
    manager = FoodSupplyManager()

    # Example usage
    manager.add_supply({"name": "Canned Tomatoes", "expiry_date": "2025-05-01", "quantity": 20})
    manager.add_supply({"name": "Fresh Lettuce", "expiry_date": "2023-10-01", "quantity": 5})
    manager.remove_supply("Canned Tomatoes")
    manager.optimize_supplies()
    manager.view_supplies()
    manager.save_supplies()

if __name__ == '__main__':
    main()
```
