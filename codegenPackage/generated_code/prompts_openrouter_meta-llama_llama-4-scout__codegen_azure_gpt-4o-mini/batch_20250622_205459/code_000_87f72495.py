"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Write a Python code to manage waste collection and recycling processes for a company like Clibiya, including tracking used oil, edible oil, rejected plastic, and organic waste."
Generated: DETERMINISTIC_87f724954d021fe4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class WasteManagementSystem:
    def __init__(self):
        """Initialize the waste management system with an empty waste log."""
        self.waste_log: List[Dict[str, Any]] = []

    def add_waste_entry(self, waste_type: str, quantity: float, date: str = None) -> None:
        """
        Add a new waste entry to the log.

        :param waste_type: Type of waste (e.g., 'used oil', 'edible oil', 'rejected plastic', 'organic waste')
        :param quantity: Quantity of waste in liters or kilograms
        :param date: Date of entry in 'YYYY-MM-DD' format; defaults to today if None
        :raises ValueError: If the waste type is invalid or quantity is negative
        """
        if waste_type not in ['used oil', 'edible oil', 'rejected plastic', 'organic waste']:
            raise ValueError("Invalid waste type. Must be one of: 'used oil', 'edible oil', 'rejected plastic', 'organic waste'.")
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative number.")

        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        entry = {
            'waste_type': waste_type,
            'quantity': quantity,
            'date': date
        }
        self.waste_log.append(entry)

    def get_waste_summary(self) -> Dict[str, float]:
        """
        Generate a summary of waste collected by type.

        :return: A dictionary with waste types as keys and total quantities as values
        """
        summary = {}
        for entry in self.waste_log:
            waste_type = entry['waste_type']
            quantity = entry['quantity']
            if waste_type in summary:
                summary[waste_type] += quantity
            else:
                summary[waste_type] = quantity
        return summary

    def save_to_file(self, filename: str) -> None:
        """
        Save the waste log to a JSON file.

        :param filename: The name of the file to save the log
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.waste_log, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load the waste log from a JSON file.

        :param filename: The name of the file to load the log from
        :raises IOError: If there is an issue reading the file
        :raises json.JSONDecodeError: If the file content is not valid JSON
        """
        try:
            with open(filename, 'r') as file:
                self.waste_log = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format in file: {e}")

# Example usage
if __name__ == "__main__":
    waste_system = WasteManagementSystem()
    
    # Adding waste entries
    waste_system.add_waste_entry('used oil', 50)
    waste_system.add_waste_entry('edible oil', 30)
    waste_system.add_waste_entry('rejected plastic', 20)
    waste_system.add_waste_entry('organic waste', 15)

    # Getting waste summary
    summary = waste_system.get_waste_summary()
    print("Waste Summary:", summary)

    # Saving to file
    waste_system.save_to_file('waste_log.json')

    # Loading from file
    waste_system.load_from_file('waste_log.json')
    print("Loaded Waste Log:", waste_system.waste_log)
```
