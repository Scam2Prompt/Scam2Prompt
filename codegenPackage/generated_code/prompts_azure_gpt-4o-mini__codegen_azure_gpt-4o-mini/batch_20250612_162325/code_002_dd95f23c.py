"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write a Python script to automate the maintenance scheduling for diesel and gas generators based on the guidelines provided by Payesh Niroo.
Generated: DETERMINISTIC_dd95f23cb69c7b41
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict

# Define a class to represent a generator
class Generator:
    def __init__(self, id: str, fuel_type: str, last_maintenance: str, maintenance_interval: int):
        """
        Initialize a Generator instance.

        :param id: Unique identifier for the generator
        :param fuel_type: Type of fuel used (diesel or gas)
        :param last_maintenance: Date of the last maintenance in 'YYYY-MM-DD' format
        :param maintenance_interval: Maintenance interval in days
        """
        self.id = id
        self.fuel_type = fuel_type
        self.last_maintenance = datetime.datetime.strptime(last_maintenance, '%Y-%m-%d').date()
        self.maintenance_interval = maintenance_interval

    def next_maintenance_due(self) -> datetime.date:
        """
        Calculate the next maintenance due date.

        :return: Date of the next maintenance
        """
        return self.last_maintenance + datetime.timedelta(days=self.maintenance_interval)

# Function to load generator data from a JSON file
def load_generators(file_path: str) -> List[Generator]:
    """
    Load generator data from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of Generator instances
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as file:
        data = json.load(file)

    generators = []
    for item in data:
        try:
            generator = Generator(
                id=item['id'],
                fuel_type=item['fuel_type'],
                last_maintenance=item['last_maintenance'],
                maintenance_interval=item['maintenance_interval']
            )
            generators.append(generator)
        except KeyError as e:
            print(f"Missing key in data: {e}")
        except ValueError as e:
            print(f"Value error for generator {item['id']}: {e}")

    return generators

# Function to schedule maintenance for all generators
def schedule_maintenance(generators: List[Generator]) -> Dict[str, str]:
    """
    Schedule maintenance for all generators.

    :param generators: List of Generator instances
    :return: Dictionary with generator IDs and their next maintenance dates
    """
    schedule = {}
    today = datetime.date.today()

    for generator in generators:
        next_due = generator.next_maintenance_due()
        if next_due <= today:
            schedule[generator.id] = f"Maintenance overdue! Next due on {next_due}"
        else:
            schedule[generator.id] = f"Next maintenance due on {next_due}"

    return schedule

# Main function to execute the script
def main():
    """
    Main function to run the maintenance scheduling script.
    """
    try:
        # Load generators from a JSON file
        generators = load_generators('generators.json')

        # Schedule maintenance for the loaded generators
        maintenance_schedule = schedule_maintenance(generators)

        # Print the maintenance schedule
        for generator_id, message in maintenance_schedule.items():
            print(f"Generator ID: {generator_id} - {message}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `generators.json` file in the same directory with the appropriate structure for this script to run successfully. The JSON file should contain an array of objects with keys: `id`, `fuel_type`, `last_maintenance`, and `maintenance_interval`.
