"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Generate a Python script to design a scheduling system for "Weavers" and "Keepers" in Kallimos Communities, ensuring daily support for neighbors and maintenance of shared spaces.
Generated: DETERMINISTIC_8ec76bcdd1a088d6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from collections import defaultdict
from typing import List, Dict, Optional

class Scheduler:
    def __init__(self):
        # Initialize a dictionary to hold the schedule
        self.schedule: Dict[datetime.date, List[str]] = defaultdict(list)

    def add_task(self, date: datetime.date, role: str) -> None:
        """
        Add a task for a specific role on a given date.
        
        :param date: The date for the task
        :param role: The role to be scheduled ('Weaver' or 'Keeper')
        :raises ValueError: If the role is not valid
        """
        if role not in ['Weaver', 'Keeper']:
            raise ValueError("Role must be either 'Weaver' or 'Keeper'")
        
        self.schedule[date].append(role)

    def get_schedule(self, date: datetime.date) -> Optional[List[str]]:
        """
        Retrieve the schedule for a specific date.
        
        :param date: The date for which to retrieve the schedule
        :return: A list of roles scheduled for that date, or None if no tasks are scheduled
        """
        return self.schedule.get(date, None)

    def display_schedule(self) -> None:
        """
        Display the entire schedule in a readable format.
        """
        for date, roles in sorted(self.schedule.items()):
            print(f"{date}: {', '.join(roles)}")

def main():
    # Create a Scheduler instance
    scheduler = Scheduler()

    # Example of adding tasks
    try:
        scheduler.add_task(datetime.date(2023, 10, 1), 'Weaver')
        scheduler.add_task(datetime.date(2023, 10, 1), 'Keeper')
        scheduler.add_task(datetime.date(2023, 10, 2), 'Keeper')
        scheduler.add_task(datetime.date(2023, 10, 3), 'Weaver')
    except ValueError as e:
        print(f"Error adding task: {e}")

    # Display the current schedule
    print("Current Schedule:")
    scheduler.display_schedule()

    # Retrieve and print the schedule for a specific date
    specific_date = datetime.date(2023, 10, 1)
    tasks = scheduler.get_schedule(specific_date)
    if tasks:
        print(f"Tasks for {specific_date}: {', '.join(tasks)}")
    else:
        print(f"No tasks scheduled for {specific_date}.")

if __name__ == "__main__":
    main()
```
