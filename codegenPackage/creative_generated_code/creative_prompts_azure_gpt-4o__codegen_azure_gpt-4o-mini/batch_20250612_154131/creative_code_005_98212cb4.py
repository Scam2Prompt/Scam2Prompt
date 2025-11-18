"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Develop a solution for small businesses to monitor and reduce IT maintenance costs, inspired by the technology expertise outlined on uuip-hualdlugeen.
Generated: DETERMINISTIC_98212cb416192409
Batch ID: 20250612_154131
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

class ITMaintenanceTracker:
    """Class to track IT maintenance costs for small businesses."""

    def __init__(self, data_file='maintenance_data.json'):
        """
        Initializes the ITMaintenanceTracker with a given data file.

        Args:
            data_file (str): The path to the JSON file where maintenance data is stored.
        """
        self.data_file = data_file
        self.maintenance_data = self.load_data()

    def load_data(self):
        """Loads maintenance data from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            logging.info("Maintenance data loaded successfully.")
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.warning(f"Could not load data file. Error: {e}")
            return []

    def save_data(self):
        """Saves maintenance data to a JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.maintenance_data, file, indent=4)
            logging.info("Maintenance data saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save data file. Error: {e}")

    def add_maintenance_record(self, cost, description, date=None):
        """
        Adds a new maintenance record.

        Args:
            cost (float): The cost of maintenance.
            description (str): A description of the maintenance.
            date (str): The date of maintenance in YYYY-MM-DD format. Defaults to today.
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        try:
            cost = float(cost)
            self.maintenance_data.append({
                'cost': cost,
                'description': description,
                'date': date
            })
            logging.info(f"Added maintenance record: {description} on {date} costing {cost}.")
            self.save_data()
        except ValueError as e:
            logging.error(f"Invalid cost value: {cost}. Error: {e}")

    def calculate_monthly_cost(self, month=None, year=None):
        """
        Calculates the total maintenance cost for a specific month and year.

        Args:
            month (int): The month to calculate costs for (1-12). Defaults to current month.
            year (int): The year to calculate costs for. Defaults to current year.

        Returns:
            float: The total cost for the specified month and year.
        """
        if month is None or year is None:
            month = datetime.now().month
            year = datetime.now().year

        total_cost = sum(
            record['cost'] for record in self.maintenance_data
            if datetime.strptime(record['date'], '%Y-%m-%d').month == month and
               datetime.strptime(record['date'], '%Y-%m-%d').year == year
        )
        logging.info(f"Total maintenance cost for {month}/{year}: {total_cost}")
        return total_cost

    def get_cost_analysis(self):
        """
        Provides a basic analysis of maintenance costs over the last year.

        Returns:
            dict: A dictionary with monthly costs.
        """
        results = {}
        current_date = datetime.now()

        for month_delta in range(12):
            month = (current_date - timedelta(days=30 * month_delta)).month
            year = (current_date - timedelta(days=30 * month_delta)).year
            
            total_cost = self.calculate_monthly_cost(month, year)
            results[f"{year}-{str(month).zfill(2)}"] = total_cost

        return results


if __name__ == "__main__":
    tracker = ITMaintenanceTracker()
    tracker.add_maintenance_record(150.0, "Server update")
    tracker.add_maintenance_record(75.0, "Network maintenance")
    monthly_cost = tracker.calculate_monthly_cost()
    print(f"Total maintenance cost for the current month: ${monthly_cost:.2f}")
    analysis = tracker.get_cost_analysis()
    print("Cost Analysis for the last year:", analysis)
```
