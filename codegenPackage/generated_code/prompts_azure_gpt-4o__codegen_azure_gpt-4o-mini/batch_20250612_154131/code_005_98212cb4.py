"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Develop a solution for small businesses to monitor and reduce IT maintenance costs, inspired by the technology expertise outlined on uuip-hualdlugeen.
Generated: DETERMINISTIC_98212cb416192409
Batch ID: 20250612_154131
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

class ITMaintenanceTracker:
    """
    A class to track IT maintenance costs for small businesses.
    """

    def __init__(self, data_file='maintenance_data.json'):
        """
        Initializes the ITMaintenanceTracker with a data file.

        :param data_file: The JSON file to store maintenance records.
        """
        self.data_file = data_file
        self.maintenance_records = self.load_data()

    def load_data(self):
        """
        Loads maintenance records from a JSON file.

        :return: A list of maintenance records.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning("Data file not found. Starting with an empty record.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data. Starting with an empty record.")
            return []

    def save_data(self):
        """
        Saves the current maintenance records to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.maintenance_records, file, indent=4)
        except IOError as e:
            logging.error(f"Error saving data: {e}")

    def add_record(self, description, cost):
        """
        Adds a new maintenance record.

        :param description: A description of the maintenance task.
        :param cost: The cost of the maintenance task.
        """
        record = {
            'description': description,
            'cost': cost,
            'date': datetime.now().isoformat()
        }
        self.maintenance_records.append(record)
        self.save_data()
        logging.info(f"Added record: {record}")

    def get_total_cost(self):
        """
        Calculates the total maintenance cost.

        :return: The total cost of all maintenance records.
        """
        total_cost = sum(record['cost'] for record in self.maintenance_records)
        logging.info(f"Total maintenance cost: {total_cost}")
        return total_cost

    def get_costs_over_period(self, days):
        """
        Retrieves maintenance costs over a specified period.

        :param days: The number of days to look back.
        :return: A list of records within the specified period.
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        filtered_records = [
            record for record in self.maintenance_records
            if datetime.fromisoformat(record['date']) >= cutoff_date
        ]
        logging.info(f"Records over the last {days} days: {filtered_records}")
        return filtered_records

# Example usage
if __name__ == "__main__":
    tracker = ITMaintenanceTracker()

    # Adding some records
    tracker.add_record("Server maintenance", 150.00)
    tracker.add_record("Software update", 75.00)

    # Getting total cost
    total_cost = tracker.get_total_cost()

    # Getting costs over the last 30 days
    recent_costs = tracker.get_costs_over_period(30)
```
