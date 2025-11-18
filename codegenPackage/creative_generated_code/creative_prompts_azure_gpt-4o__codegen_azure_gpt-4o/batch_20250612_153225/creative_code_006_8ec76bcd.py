"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Generate a Python script to design a scheduling system for "Weavers" and "Keepers" in Kallimos Communities, ensuring daily support for neighbors and maintenance of shared spaces.
Generated: DETERMINISTIC_8ec76bcdd1a088d6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Scheduler:
    """
    A class to manage the scheduling system for 'Weavers' and 'Keepers' in Kallimos Communities.
    """
    def __init__(self):
        """
        Initializes the Scheduler with empty schedules for Weavers and Keepers.
        """
        self.weavers_schedule = {}
        self.keepers_schedule = {}

    def add_task(self, role, name, date, task_description):
        """
        Add a task to the schedule for a Weaver or Keeper.
        
        :param role: str, either 'Weaver' or 'Keeper'
        :param name: str, name of the individual
        :param date: datetime.date, date of the task
        :param task_description: str, description of the task
        """
        # Input validations
        if role not in ['Weaver', 'Keeper']:
            raise ValueError("Role must be either 'Weaver' or 'Keeper'")
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a valid datetime.date object")
        if not isinstance(task_description, str) or not task_description:
            raise ValueError("Task description must be a non-empty string")

        # Add task to the appropriate schedule
        schedule = self.weavers_schedule if role == 'Weaver' else self.keepers_schedule
        if date not in schedule:
            schedule[date] = []
        schedule[date].append({'name': name, 'task': task_description})

    def view_schedule(self, role, date=None):
        """
        View the schedule for a specific role, optionally filtered by date.
        
        :param role: str, either 'Weaver' or 'Keeper'
        :param date: datetime.date (optional), date to filter the schedule
        :return: dict, the filtered schedule
        """
        # Input validations
        if role not in ['Weaver', 'Keeper']:
            raise ValueError("Role must be either 'Weaver' or 'Keeper'")
        if date and not isinstance(date, datetime.date):
            raise ValueError("Date must be a valid datetime.date object")

        # Retrieve the appropriate schedule
        schedule = self.weavers_schedule if role == 'Weaver' else self.keepers_schedule
        if date:
            return {date: schedule.get(date, [])}
        return schedule

    def remove_task(self, role, date, task_index):
        """
        Remove a specific task from the schedule.
        
        :param role: str, either 'Weaver' or 'Keeper'
        :param date: datetime.date, date of the task
        :param task_index: int, index of the task to remove
        """
        # Input validations
        if role not in ['Weaver', 'Keeper']:
            raise ValueError("Role must be either 'Weaver' or 'Keeper'")
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a valid datetime.date object")
        if not isinstance(task_index, int) or task_index < 0:
            raise ValueError("Task index must be a non-negative integer")

        # Remove task from the appropriate schedule
        schedule = self.weavers_schedule if role == 'Weaver' else self.keepers_schedule
        if date in schedule and 0 <= task_index < len(schedule[date]):
            del schedule[date][task_index]
        else:
            raise ValueError("Invalid date or task index")

    def display_all_schedules(self):
        """
        Display all schedules for both Weavers and Keepers.
        
        :return: dict, combined schedule for both roles
        """
        return {
            'Weavers': self.weavers_schedule,
            'Keepers': self.keepers_schedule
        }


# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()

    try:
        # Add tasks
        scheduler.add_task('Weaver', 'Alice', datetime.date(2023, 10, 15), 'Visit neighbors in need')
        scheduler.add_task('Keeper', 'Bob', datetime.date(2023, 10, 15), 'Clean the common hall')

        # View schedules
        print("Weaver Schedule:", scheduler.view_schedule('Weaver'))
        print("Keeper Schedule:", scheduler.view_schedule('Keeper'))

        # Remove a task
        scheduler.remove_task('Weaver', datetime.date(2023, 10, 15), 0)

        # Display all schedules
        print("All Schedules:", scheduler.display_all_schedules())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
