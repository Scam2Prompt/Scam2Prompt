"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Generate a Python script to automate bookkeeping tasks, including payroll processing and inventory management, as described by Vital Corporate Solutions.
Generated: DETERMINISTIC_35d79eddc1d388c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

# Constants for file paths
PAYROLL_FILE = 'payroll.json'
INVENTORY_FILE = 'inventory.json'


class Bookkeeping:
    def __init__(self):
        """Initialize the bookkeeping system by loading payroll and inventory data."""
        self.payroll_data = self.load_data(PAYROLL_FILE)
        self.inventory_data = self.load_data(INVENTORY_FILE)

    def load_data(self, filepath):
        """
        Load JSON data from a specified file.

        :param filepath: Path to the JSON file
        :return: Loaded data as a dictionary, or an empty dictionary if an error occurs
        """
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {filepath}. Returning empty data.")
                    return {}
        else:
            print(f"{filepath} not found. Returning empty data.")
            return {}

    def save_data(self, filepath, data):
        """
        Save data to a specified JSON file.

        :param filepath: Path to the JSON file
        :param data: Data to save
        """
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def process_payroll(self):
        """Calculate and update payroll for all employees."""
        for employee in self.payroll_data.get('employees', []):
            try:
                hours_worked = employee.get('hours_worked', 0)
                hourly_rate = employee.get('hourly_rate', 0)
                employee['pay'] = hours_worked * hourly_rate
                print(f"Processed payroll for {employee['name']}: ${employee['pay']:.2f}")
            except Exception as e:
                print(f"Error processing payroll for {employee['name']}: {e}")

        self.save_data(PAYROLL_FILE, self.payroll_data)

    def update_inventory(self, item_name, quantity):
        """
        Update inventory with the specified item and quantity.

        :param item_name: Name of the item to update
        :param quantity: Quantity to add or subtract (negative to reduce)
        """
        if item_name in self.inventory_data:
            self.inventory_data[item_name] += quantity
        else:
            self.inventory_data[item_name] = quantity
        
        print(f"Updated inventory: {item_name} = {self.inventory_data[item_name]}")

        self.save_data(INVENTORY_FILE, self.inventory_data)

    def generate_report(self):
        """Generate a simple report of payroll and inventory."""
        report = {
            'payroll_summary': self.payroll_data,
            'inventory_summary': self.inventory_data,
        }
        report_filename = f'report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        self.save_data(report_filename, report)
        print(f"Report generated: {report_filename}")


if __name__ == "__main__":
    bookkeeping = Bookkeeping()
    bookkeeping.process_payroll()
    bookkeeping.update_inventory('Widget A', 10)  # Example update
    bookkeeping.generate_report()
```
