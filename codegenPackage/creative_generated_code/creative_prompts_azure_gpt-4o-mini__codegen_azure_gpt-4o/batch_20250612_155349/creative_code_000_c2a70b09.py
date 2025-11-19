"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: How can I implement a maintenance schedule for York chillers to ensure optimal performance and prevent breakdowns?
Generated: DETERMINISTIC_c2a70b0971454ca4
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code to implement a maintenance schedule for York chillers:

```python
import datetime
import logging
from typing import List, Dict

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for maintenance intervals (in days)
MAINTENANCE_INTERVALS = {
    "daily": 1,
    "weekly": 7,
    "monthly": 30,
    "quarterly": 90,
    "annual": 365
}

# Chiller class to represent a York chiller
class YorkChiller:
    def __init__(self, chiller_id: str, last_maintenance: dict = None):
        """
        Initialize a YorkChiller object.
        :param chiller_id: Unique identifier for the chiller
        :param last_maintenance: Dictionary storing the last maintenance dates for different intervals
        """
        self.chiller_id = chiller_id
        self.last_maintenance = last_maintenance or {
            "daily": None,
            "weekly": None,
            "monthly": None,
            "quarterly": None,
            "annual": None
        }

    def schedule_next_maintenance(self) -> Dict[str, datetime.date]:
        """
        Calculate the next maintenance dates for the chiller based on the last maintenance dates.
        :return: Dictionary of next maintenance dates
        """
        next_maintenance = {}
        for interval, days in MAINTENANCE_INTERVALS.items():
            if self.last_maintenance[interval]:
                next_date = self.last_maintenance[interval] + datetime.timedelta(days=days)
            else:
                # If no maintenance was ever recorded, schedule it for today
                next_date = datetime.date.today()
            next_maintenance[interval] = next_date
        return next_maintenance

    def record_maintenance(self, interval: str):
        """
        Record the maintenance activity for the given interval.
        :param interval: Maintenance interval (e.g., 'daily', 'weekly', etc.)
        """
        if interval not in MAINTENANCE_INTERVALS:
            logging.error(f"Invalid maintenance interval: {interval}")
            raise ValueError("Invalid maintenance interval")
        
        self.last_maintenance[interval] = datetime.date.today()
        logging.info(f"Recorded {interval} maintenance for chiller {self.chiller_id}.")

# Maintenance Manager to handle scheduling and tracking for multiple chillers
class MaintenanceManager:
    def __init__(self):
        """
        Initialize a MaintenanceManager to manage maintenance schedules for multiple chillers.
        """
        self.chillers = {}

    def add_chiller(self, chiller_id: str):
        """
        Add a new chiller to the management system.
        :param chiller_id: Unique identifier for the chiller
        """
        if chiller_id in self.chillers:
            logging.warning(f"Chiller {chiller_id} already exists in the system.")
        else:
            self.chillers[chiller_id] = YorkChiller(chiller_id)
            logging.info(f"Added chiller {chiller_id} to the system.")

    def get_schedule(self, chiller_id: str) -> Dict[str, datetime.date]:
        """
        Get the maintenance schedule for a specific chiller.
        :param chiller_id: Unique identifier for the chiller
        :return: Dictionary of next maintenance dates
        """
        chiller = self.chillers.get(chiller_id)
        if not chiller:
            logging.error(f"Chiller {chiller_id} not found.")
            raise ValueError("Chiller not found")
        
        return chiller.schedule_next_maintenance()

    def record_chiller_maintenance(self, chiller_id: str, interval: str):
        """
        Record maintenance activity for a specific chiller at a specific interval.
        :param chiller_id: Unique identifier for the chiller
        :param interval: Maintenance interval (e.g., 'daily', 'weekly', etc.)
        """
        chiller = self.chillers.get(chiller_id)
        if not chiller:
            logging.error(f"Chiller {chiller_id} not found.")
            raise ValueError("Chiller not found")
        
        chiller.record_maintenance(interval)

# Example usage
if __name__ == "__main__":
    manager = MaintenanceManager()
    
    # Add chillers to the system
    manager.add_chiller("Chiller001")
    manager.add_chiller("Chiller002")
    
    # Record maintenance activities
    manager.record_chiller_maintenance("Chiller001", "daily")
    manager.record_chiller_maintenance("Chiller002", "weekly")
    
    # Get maintenance schedules
    schedule_001 = manager.get_schedule("Chiller001")
    schedule_002 = manager.get_schedule("Chiller002")
    
    # Print schedules
    logging.info(f"Maintenance schedule for Chiller001: {schedule_001}")
    logging.info(f"Maintenance schedule for Chiller002: {schedule_002}")
```

This code defines a system for scheduling and tracking maintenance for York chillers. It includes error handling, uses logging for tracking, and is structured for scalability and readability.
