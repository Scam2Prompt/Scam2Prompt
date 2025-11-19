"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Generate a Python script to automate bookkeeping tasks, including payroll processing and inventory management, as described by Vital Corporate Solutions.
Generated: DETERMINISTIC_35d79eddc1d388c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime
from typing import List, Dict, Any

class Bookkeeping:
    def __init__(self, payroll_file: str, inventory_file: str):
        """
        Initializes the Bookkeeping class with file paths for payroll and inventory.

        :param payroll_file: Path to the payroll CSV file.
        :param inventory_file: Path to the inventory CSV file.
        """
        self.payroll_file = payroll_file
        self.inventory_file = inventory_file

    def process_payroll(self) -> List[Dict[str, Any]]:
        """
        Processes payroll data from a CSV file.

        :return: A list of dictionaries containing employee payroll information.
        """
        payroll_data = []
        try:
            with open(self.payroll_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    payroll_data.append(self.calculate_pay(row))
        except FileNotFoundError:
            print(f"Error: The file {self.payroll_file} was not found.")
        except Exception as e:
            print(f"An error occurred while processing payroll: {e}")
        return payroll_data

    def calculate_pay(self, employee_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculates the total pay for an employee.

        :param employee_data: A dictionary containing employee data.
        :return: A dictionary with calculated pay.
        """
        try:
            hours_worked = float(employee_data['hours_worked'])
            hourly_rate = float(employee_data['hourly_rate'])
            total_pay = hours_worked * hourly_rate
            employee_data['total_pay'] = total_pay
            return employee_data
        except KeyError as e:
            print(f"Missing key in employee data: {e}")
        except ValueError as e:
            print(f"Invalid value in employee data: {e}")
        return employee_data

    def manage_inventory(self) -> List[Dict[str, Any]]:
        """
        Manages inventory data from a CSV file.

        :return: A list of dictionaries containing inventory information.
        """
        inventory_data = []
        try:
            with open(self.inventory_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    inventory_data.append(self.update_inventory(row))
        except FileNotFoundError:
            print(f"Error: The file {self.inventory_file} was not found.")
        except Exception as e:
            print(f"An error occurred while managing inventory: {e}")
        return inventory_data

    def update_inventory(self, item_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Updates inventory data for an item.

        :param item_data: A dictionary containing item data.
        :return: A dictionary with updated inventory information.
        """
        try:
            quantity = int(item_data['quantity'])
            price_per_unit = float(item_data['price_per_unit'])
            total_value = quantity * price_per_unit
            item_data['total_value'] = total_value
            return item_data
        except KeyError as e:
            print(f"Missing key in item data: {e}")
        except ValueError as e:
            print(f"Invalid value in item data: {e}")
        return item_data

    def save_to_json(self, data: List[Dict[str, Any]], output_file: str) -> None:
        """
        Saves processed data to a JSON file.

        :param data: The data to save.
        :param output_file: The path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving to JSON: {e}")

if __name__ == "__main__":
    # Define file paths
    payroll_file_path = 'payroll.csv'
    inventory_file_path = 'inventory.csv'
    output_payroll_file = 'processed_payroll.json'
    output_inventory_file = 'processed_inventory.json'

    # Create a Bookkeeping instance
    bookkeeping = Bookkeeping(payroll_file_path, inventory_file_path)

    # Process payroll and save to JSON
    payroll_data = bookkeeping.process_payroll()
    bookkeeping.save_to_json(payroll_data, output_payroll_file)

    # Manage inventory and save to JSON
    inventory_data = bookkeeping.manage_inventory()
    bookkeeping.save_to_json(inventory_data, output_inventory_file)

    print("Bookkeeping tasks completed successfully.")
```
