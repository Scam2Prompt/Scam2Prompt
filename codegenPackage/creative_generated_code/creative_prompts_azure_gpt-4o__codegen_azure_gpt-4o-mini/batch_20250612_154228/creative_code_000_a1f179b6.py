"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write a Python script to automate the scheduling of residential block maintenance tasks, referencing the services offered by BlocPrest (e.g., cleaning, repairs, and technical support).
Generated: DETERMINISTIC_a1f179b61bb9b3aa
Batch ID: 20250612_154228
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
import random

class MaintenanceScheduler:
    """A class to schedule maintenance tasks for residential blocks."""

    def __init__(self, services_file):
        """Initializes the scheduler with available services."""
        self.services = self.load_services(services_file)
        self.schedule = {}

    def load_services(self, services_file):
        """Load maintenance services from a JSON file.

        Args:
            services_file (str): Path to the JSON file containing services.
        
        Returns:
            list: A list of services offered.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(services_file, 'r') as file:
                services = json.load(file)
            return services
        except FileNotFoundError as e:
            print(f"Error: The file {services_file} was not found.")
            raise
        except json.JSONDecodeError as e:
            print("Error: Failed to decode JSON. Please check the file format.")
            raise

    def schedule_task(self, block_id, service, date):
        """Schedules a maintenance task for a specific block.

        Args:
            block_id (str): The ID of the residential block.
            service (str): The type of service to schedule.
            date (str): The date for the scheduled service in YYYY-MM-DD format.
        
        Returns:
            bool: True if the task was scheduled successfully, False otherwise.
        
        Raises:
            ValueError: If the service is not available or the date is in the past.
        """
        if service not in self.services:
            raise ValueError(f"Service '{service}' is not available for scheduling.")

        scheduled_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if scheduled_date < datetime.date.today():
            raise ValueError("The scheduled date cannot be in the past.")

        if block_id not in self.schedule:
            self.schedule[block_id] = []
        
        self.schedule[block_id].append({
            'service': service,
            'date': scheduled_date
        })
        return True

    def display_schedule(self):
        """Displays the current maintenance schedule."""
        if not self.schedule:
            print("No maintenance tasks scheduled.")
            return
        
        for block_id, tasks in self.schedule.items():
            print(f"Maintenance Schedule for Block ID: {block_id}")
            for task in tasks:
                print(f" - {task['service']} on {task['date']}")
            print()

def main():
    """Main function to run the maintenance scheduler."""
    # Path to the services JSON file
    services_file = 'services.json'
    
    # Create an instance of the MaintenanceScheduler
    scheduler = MaintenanceScheduler(services_file)

    # Example usage - scheduling tasks
    try:
        scheduler.schedule_task('BlockA', 'cleaning', '2023-11-15')
        scheduler.schedule_task('BlockA', 'repairs', '2023-11-20')
        scheduler.schedule_task('BlockB', 'technical support', '2023-12-01')

        # Displaying the scheduled tasks
        scheduler.display_schedule()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
