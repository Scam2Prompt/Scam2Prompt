"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Write a script to automate the maintenance schedule for electronic security systems, referencing the preventive and corrective maintenance services mentioned on the Inside Safety website.
Generated: DETERMINISTIC_3c0965f84cf9ddb6
Batch ID: 20250612_153224
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceScheduler:
    def __init__(self, maintenance_data: List[Dict]):
        """
        Initializes the MaintenanceScheduler with maintenance data.

        :param maintenance_data: A list of dictionaries containing maintenance service details.
        """
        self.maintenance_data = maintenance_data

    def schedule_maintenance(self) -> List[Dict]:
        """
        Schedules maintenance tasks based on the provided maintenance data.

        :return: A list of scheduled maintenance tasks with their next maintenance date.
        """
        scheduled_tasks = []
        for service in self.maintenance_data:
            try:
                next_maintenance_date = self.calculate_next_maintenance(service['last_service_date'], service['frequency'])
                scheduled_tasks.append({
                    'service_name': service['service_name'],
                    'next_maintenance_date': next_maintenance_date.strftime('%Y-%m-%d')
                })
            except KeyError as e:
                logging.error(f"Missing key in service data: {e}")
            except Exception as e:
                logging.error(f"Error scheduling maintenance for {service['service_name']}: {e}")
        return scheduled_tasks

    @staticmethod
    def calculate_next_maintenance(last_service_date: str, frequency: int) -> datetime.date:
        """
        Calculates the next maintenance date based on the last service date and frequency.

        :param last_service_date: The date of the last service in 'YYYY-MM-DD' format.
        :param frequency: The frequency of maintenance in days.
        :return: The next maintenance date as a datetime.date object.
        """
        last_service = datetime.datetime.strptime(last_service_date, '%Y-%m-%d').date()
        next_maintenance = last_service + datetime.timedelta(days=frequency)
        return next_maintenance

def load_maintenance_data(file_path: str) -> List[Dict]:
    """
    Loads maintenance data from a JSON file.

    :param file_path: The path to the JSON file containing maintenance data.
    :return: A list of maintenance service details.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data['maintenance_services']
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error loading maintenance data: {e}")
        return []

def main():
    """
    Main function to execute the maintenance scheduling.
    """
    # Load maintenance data from a JSON file
    maintenance_data = load_maintenance_data('maintenance_data.json')
    
    # Initialize the maintenance scheduler
    scheduler = MaintenanceScheduler(maintenance_data)
    
    # Schedule maintenance tasks
    scheduled_tasks = scheduler.schedule_maintenance()
    
    # Output the scheduled tasks
    for task in scheduled_tasks:
        print(f"Service: {task['service_name']}, Next Maintenance Date: {task['next_maintenance_date']}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `maintenance_data.json` file exists in the same directory as this script and contains the appropriate structure, such as:
```json
{
    "maintenance_services": [
        {
            "service_name": "Alarm System Check",
            "last_service_date": "2023-01-15",
            "frequency": 90
        },
        {
            "service_name": "CCTV Maintenance",
            "last_service_date": "2023-02-20",
            "frequency": 180
        }
    ]
}
```
