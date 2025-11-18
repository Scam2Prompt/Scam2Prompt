"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Write a program to automate the scheduling and monitoring of engineering labor supply for offshore and onshore mechanical installations, as offered by C&M Pinnacle.
Generated: DETERMINISTIC_f030748c67be1fba
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import logging
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LaborScheduler:
    def __init__(self):
        self.schedule = []  # List to hold scheduling data

    def add_shift(self, date: str, labor_type: str, quantity: int) -> None:
        """
        Adds a shift to the schedule.

        :param date: Date of the shift in 'YYYY-MM-DD' format.
        :param labor_type: Type of labor (e.g., 'offshore', 'onshore').
        :param quantity: Number of laborers required.
        """
        try:
            # Validate the date format
            schedule_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.schedule.append({
                'date': schedule_date,
                'labor_type': labor_type,
                'quantity': quantity
            })
            logging.info(f"Added shift: {schedule_date} - {labor_type} - {quantity} workers.")
        except ValueError as e:
            logging.error(f"Error adding shift: {e}")
            raise

    def remove_shift(self, date: str, labor_type: str) -> None:
        """
        Removes a shift from the schedule.

        :param date: Date of the shift in 'YYYY-MM-DD' format.
        :param labor_type: Type of labor to remove.
        """
        try:
            schedule_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.schedule = [s for s in self.schedule if not (s['date'] == schedule_date and s['labor_type'] == labor_type)]
            logging.info(f"Removed shift: {schedule_date} - {labor_type}.")
        except ValueError as e:
            logging.error(f"Error removing shift: {e}")
            raise

    def get_schedule(self) -> List[Dict[str, Any]]:
        """
        Returns the current labor schedule.

        :return: List of shifts in the schedule.
        """
        return self.schedule

    def save_schedule(self, filename: str) -> None:
        """
        Saves the current schedule to a JSON file.

        :param filename: Name of the file to save the schedule to.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.schedule, f, default=str)  # Convert dates to string for JSON
            logging.info(f"Schedule saved to {filename}.")
        except Exception as e:
            logging.error(f"Error saving schedule: {e}")
            raise

    def load_schedule(self, filename: str) -> None:
        """
        Loads the schedule from a JSON file.

        :param filename: Name of the file to load the schedule from.
        """
        try:
            with open(filename, 'r') as f:
                self.schedule = json.load(f)
                for s in self.schedule:
                    s['date'] = datetime.datetime.strptime(s['date'], '%Y-%m-%d').date()  # Reformat date
            logging.info(f"Schedule loaded from {filename}.")
        except Exception as e:
            logging.error(f"Error loading schedule: {e}")
            raise

# Example of using the LaborScheduler class
if __name__ == "__main__":
    scheduler = LaborScheduler()
    try:
        scheduler.add_shift('2023-10-01', 'offshore', 10)
        scheduler.add_shift('2023-10-02', 'onshore', 5)
        print(scheduler.get_schedule())
        scheduler.save_schedule('labor_schedule.json')
        scheduler.load_schedule('labor_schedule.json')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
