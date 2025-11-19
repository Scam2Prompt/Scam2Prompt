"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Develop a tool to manage and optimize the provisioning of fresh and ready-to-consume food supplies for maritime crews, referencing the quality and safety standards highlighted by Supply Marine.
Generated: DETERMINISTIC_12623fce90b1e7a9
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
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FoodSupplyManager:
    def __init__(self, supply_data_file):
        """
        Initializes the FoodSupplyManager with the given supply data file.
        
        :param supply_data_file: Path to the JSON file containing food supply data.
        """
        self.supply_data_file = supply_data_file
        self.food_supplies = self.load_supply_data()

    def load_supply_data(self):
        """
        Loads food supply data from a JSON file.
        
        :return: A list of food supply items.
        """
        try:
            with open(self.supply_data_file, 'r') as file:
                data = json.load(file)
                logging.info("Food supply data loaded successfully.")
                return data['supplies']
        except FileNotFoundError:
            logging.error("Supply data file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from supply data file.")
            return []

    def optimize_supply(self, crew_size):
        """
        Optimizes the food supply based on crew size and safety standards.
        
        :param crew_size: The number of crew members to provision for.
        :return: A list of optimized food supplies.
        """
        optimized_supplies = []
        for item in self.food_supplies:
            if item['quantity'] >= crew_size:
                optimized_supplies.append({
                    'name': item['name'],
                    'quantity': crew_size,
                    'expiry_date': self.calculate_expiry_date(item['shelf_life'])
                })
        logging.info("Supply optimization completed.")
        return optimized_supplies

    def calculate_expiry_date(self, shelf_life):
        """
        Calculates the expiry date based on the shelf life of the food item.
        
        :param shelf_life: The shelf life of the food item in days.
        :return: The expiry date as a string in YYYY-MM-DD format.
        """
        expiry_date = datetime.now() + timedelta(days=shelf_life)
        return expiry_date.strftime('%Y-%m-%d')

    def generate_supply_report(self, optimized_supplies):
        """
        Generates a report of the optimized food supplies.
        
        :param optimized_supplies: A list of optimized food supplies.
        :return: A string report of the supplies.
        """
        report_lines = ["Optimized Food Supply Report:"]
        for supply in optimized_supplies:
            report_lines.append(f"{supply['name']}: {supply['quantity']} (Expiry: {supply['expiry_date']})")
        report = "\n".join(report_lines)
        logging.info("Supply report generated.")
        return report

def main():
    # Path to the supply data JSON file
    supply_data_file = 'food_supplies.json'
    
    # Initialize the FoodSupplyManager
    manager = FoodSupplyManager(supply_data_file)
    
    # Example crew size
    crew_size = 10
    
    # Optimize food supply for the crew
    optimized_supplies = manager.optimize_supply(crew_size)
    
    # Generate and print the supply report
    report = manager.generate_supply_report(optimized_supplies)
    print(report)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `food_supplies.json` file exists in the same directory as this script and follows the expected structure, e.g.:
```json
{
    "supplies": [
        {"name": "Canned Beans", "quantity": 20, "shelf_life": 365},
        {"name": "Rice", "quantity": 50, "shelf_life": 730},
        {"name": "Fresh Vegetables", "quantity": 5, "shelf_life": 7}
    ]
}
```
