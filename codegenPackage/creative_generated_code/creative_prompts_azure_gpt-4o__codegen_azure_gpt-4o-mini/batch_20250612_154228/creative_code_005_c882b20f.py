"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Write a function to automate energy consumption tracking for household appliances, using the real-time energy management systems discussed on Blackpanttthers.
Generated: DETERMINISTIC_c882b20f6281804c
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import Dict, Any, List

class EnergyConsumptionTracker:
    def __init__(self):
        """Initialize the energy consumption tracker with an empty record."""
        self.consumption_records: List[Dict[str, Any]] = []

    def add_appliance(self, appliance_name: str, power_rating: float) -> None:
        """
        Add a new appliance to the tracker.

        Args:
            appliance_name (str): Name of the appliance.
            power_rating (float): Power rating of the appliance in watts.

        Raises:
            ValueError: If power_rating is not a positive number.
        """
        if power_rating <= 0:
            raise ValueError("Power rating must be a positive number.")

        record = {
            "appliance_name": appliance_name,
            "power_rating": power_rating,
            "usage": 0,  # initial usage in hours
            "last_updated": datetime.now().isoformat()
        }
        self.consumption_records.append(record)

    def update_usage(self, appliance_name: str, hours: float) -> None:
        """
        Update the usage of an appliance.

        Args:
            appliance_name (str): Name of the appliance.
            hours (float): Number of hours the appliance has been used.

        Raises:
            ValueError: If hours is not a positive number or appliance not found.
        """
        if hours <= 0:
            raise ValueError("Usage hours must be a positive number.")

        for record in self.consumption_records:
            if record['appliance_name'] == appliance_name:
                record['usage'] += hours
                record['last_updated'] = datetime.now().isoformat()
                return
        
        raise ValueError(f"Appliance '{appliance_name}' not found.")

    def calculate_total_consumption(self) -> float:
        """
        Calculate the total energy consumption of all appliances.

        Returns:
            float: Total energy consumption in kilowatt-hours (kWh).
        """
        total_consumption = 0.0
        for record in self.consumption_records:
            total_consumption += (record['power_rating'] / 1000) * record['usage']  # in kWh
        return total_consumption

    def export_records(self, file_path: str) -> None:
        """
        Export the consumption records to a JSON file.

        Args:
            file_path (str): Path to the file where records will be exported.

        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.consumption_records, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file {file_path}: {e}")

    def load_records(self, file_path: str) -> None:
        """
        Load consumption records from a JSON file.

        Args:
            file_path (str): Path to the file from which records will be loaded.

        Raises:
            IOError: If there's an error reading the file.
            ValueError: If the file content is invalid.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.consumption_records = json.load(json_file)
        except IOError as e:
            raise IOError(f"Failed to read from file {file_path}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    tracker = EnergyConsumptionTracker()
    tracker.add_appliance("Washing Machine", 500)  # 500 watts
    tracker.update_usage("Washing Machine", 2)      # Used for 2 hours
    total_consumption = tracker.calculate_total_consumption()
    print(f"Total Energy Consumption: {total_consumption:.2f} kWh")
    tracker.export_records("energy_consumption_records.json")
```
