"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Write a program to assist in hazardous waste management, including tracking, reporting, and compliance correction, as described by iSi Environmental consultants.
Generated: DETERMINISTIC_bf4d4d6070048ebe
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hazardous Waste Management Program
- Tracks hazardous waste containers, quantities, and locations.
- Generates reports for hazardous waste compliance.
- Suggests corrections for compliance violations.

Author: Professional Software Developer
Version: 1.0
"""

import csv
import json
from datetime import datetime


class HazardousWasteManager:
    """
    A class to manage hazardous waste tracking, reporting, and compliance correction.
    """

    def __init__(self, data_file="hazardous_waste_data.json"):
        """
        Initializes the HazardousWasteManager with a data file storing waste information.

        :param data_file: Path to the JSON file containing waste data.
        """
        self.data_file = data_file
        self.waste_data = self.load_data()

    def load_data(self):
        """
        Loads hazardous waste data from the JSON file.

        :return: Parsed waste data as a dictionary.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Data file '{self.data_file}' not found. Initializing empty data.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
            return {}

    def save_data(self):
        """
        Saves hazardous waste data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.waste_data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_waste(self, container_id, waste_type, quantity, location, expiration_date):
        """
        Adds a new hazardous waste container to the system.

        :param container_id: Unique ID for the container.
        :param waste_type: Type of hazardous waste.
        :param quantity: Quantity of waste in the container.
        :param location: Location of the container.
        :param expiration_date: Expiration date of the waste (YYYY-MM-DD).
        """
        self.waste_data[container_id] = {
            "waste_type": waste_type,
            "quantity": quantity,
            "location": location,
            "expiration_date": expiration_date
        }
        self.save_data()
        print(f"Container {container_id} added successfully.")

    def generate_report(self, output_file="waste_report.csv"):
        """
        Generates a CSV report of hazardous waste data.

        :param output_file: Path to the CSV file where the report will be saved.
        """
        try:
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Container ID", "Waste Type", "Quantity", "Location", "Expiration Date"])
                for container_id, data in self.waste_data.items():
                    writer.writerow([
                        container_id,
                        data["waste_type"],
                        data["quantity"],
                        data["location"],
                        data["expiration_date"]
                    ])
            print(f"Report generated successfully: {output_file}")
        except Exception as e:
            print(f"Error generating report: {e}")

    def check_compliance(self):
        """
        Checks for compliance violations (e.g., expired waste) and prints corrections.
        """
        today = datetime.today().date()
        for container_id, data in self.waste_data.items():
            expiration_date = datetime.strptime(data["expiration_date"], "%Y-%m-%d").date()
            if expiration_date < today:
                print(f"Compliance violation for Container {container_id}: Expired waste. "
                      f"Expiration date was {data['expiration_date']}. "
                      f"Suggested correction: Dispose of expired waste immediately.")

    def delete_container(self, container_id):
        """
        Deletes a hazardous waste container from the system.

        :param container_id: Unique ID for the container to be deleted.
        """
        if container_id in self.waste_data:
            del self.waste_data[container_id]
            self.save_data()
            print(f"Container {container_id} deleted successfully.")
        else:
            print(f"Container {container_id} not found.")

# Example usage:
if __name__ == "__main__":
    manager = HazardousWasteManager()

    # Add a hazardous waste container
    manager.add_waste(
        container_id="HW001",
        waste_type="Chemical",
        quantity=50,
        location="Storage Room 1",
        expiration_date="2023-12-01"
    )

    # Generate a report
    manager.generate_report()

    # Check compliance
    manager.check_compliance()

    # Delete a container
    manager.delete_container("HW001")
```
