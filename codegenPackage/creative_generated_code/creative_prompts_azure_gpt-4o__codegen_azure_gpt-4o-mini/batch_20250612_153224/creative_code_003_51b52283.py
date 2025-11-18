"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Provide a list of libraries or frameworks for managing infrastructure maintenance schedules, inspired by Unison Plus's post-project services.
Generated: DETERMINISTIC_51b522838e3e569c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InfrastructureMaintenanceScheduler:
    """
    A class to manage infrastructure maintenance schedules.

    Attributes:
        schedules (list): A list of maintenance schedules.
    """

    def __init__(self):
        """Initialize the scheduler with an empty list of schedules."""
        self.schedules = []

    def add_schedule(self, service_name: str, maintenance_date: str):
        """
        Add a maintenance schedule to the list.

        Args:
            service_name (str): The name of the service that requires maintenance.
            maintenance_date (str): The date of the scheduled maintenance.

        Raises:
            ValueError: If the service_name or maintenance_date is invalid.
        """
        if not service_name or not maintenance_date:
            logging.error("Invalid service name or maintenance date.")
            raise ValueError("Service name and maintenance date cannot be empty.")

        schedule = {
            "service": service_name,
            "date": maintenance_date
        }
        self.schedules.append(schedule)
        logging.info(f"Added schedule for {service_name} on {maintenance_date}.")

    def remove_schedule(self, service_name: str):
        """
        Remove a maintenance schedule from the list by service name.

        Args:
            service_name (str): The name of the service to remove.

        Raises:
            ValueError: If the service_name is not found in the schedule.
        """
        for schedule in self.schedules:
            if schedule["service"] == service_name:
                self.schedules.remove(schedule)
                logging.info(f"Removed schedule for {service_name}.")
                return
        logging.error(f"Service {service_name} not found in schedules.")
        raise ValueError("Service not found in schedules.")

    def get_schedules(self) -> list:
        """
        Return the list of all maintenance schedules.

        Returns:
            list: A list of maintenance schedules.
        """
        logging.info("Retrieved all maintenance schedules.")
        return self.schedules

    def save_schedules_to_file(self, filename: str):
        """
        Save the maintenance schedules to a JSON file.

        Args:
            filename (str): The name of the file to save schedules to.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.schedules, f, indent=4)
            logging.info(f"Schedules saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to write to file {filename}: {e}")
            raise

    def load_schedules_from_file(self, filename: str):
        """
        Load maintenance schedules from a JSON file.

        Args:
            filename (str): The name of the file to load schedules from.

        Raises:
            IOError: If there is an issue reading from the file.
        """
        try:
            with open(filename, 'r') as f:
                self.schedules = json.load(f)
            logging.info(f"Schedules loaded from {filename}.")
        except IOError as e:
            logging.error(f"Failed to read from file {filename}: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from file {filename}: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    scheduler = InfrastructureMaintenanceScheduler()
    
    # Adding schedules
    scheduler.add_schedule("Server Maintenance", "2023-11-01")
    scheduler.add_schedule("Database Backup", "2023-11-05")
    
    # Saving to file
    scheduler.save_schedules_to_file("maintenance_schedules.json")
    
    # Loading from file
    scheduler.load_schedules_from_file("maintenance_schedules.json")
    
    # Getting current schedules
    schedules = scheduler.get_schedules()
    print(schedules)
```
