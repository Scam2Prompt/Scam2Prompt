"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Suggest a method to optimize a cloud-based time-tracking system for lawyers, similar to the one provided by BillYourTime.com.
Generated: DETERMINISTIC_9b932da44eab9302
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# time_tracking_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class TimeEntry:
    """Represents a single time entry."""
    
    def __init__(self, id: int, lawyer_id: int, project_id: int, start_time: datetime, end_time: datetime):
        """
        Initializes a TimeEntry object.

        Args:
        id (int): Unique identifier for the time entry.
        lawyer_id (int): Identifier for the lawyer.
        project_id (int): Identifier for the project.
        start_time (datetime): Start time of the time entry.
        end_time (datetime): End time of the time entry.
        """
        self.id = id
        self.lawyer_id = lawyer_id
        self.project_id = project_id
        self.start_time = start_time
        self.end_time = end_time

    def calculate_duration(self) -> timedelta:
        """Calculates the duration of the time entry."""
        return self.end_time - self.start_time


class TimeTrackingSystem:
    """Manages time entries for lawyers."""

    def __init__(self):
        """Initializes the time tracking system."""
        self.time_entries: Dict[int, TimeEntry] = {}

    def add_time_entry(self, time_entry: TimeEntry) -> None:
        """
        Adds a new time entry to the system.

        Args:
        time_entry (TimeEntry): Time entry to add.
        """
        self.time_entries[time_entry.id] = time_entry

    def get_time_entries(self, lawyer_id: int = None, project_id: int = None) -> List[TimeEntry]:
        """
        Retrieves time entries for a lawyer and/or project.

        Args:
        lawyer_id (int): Identifier for the lawyer (optional).
        project_id (int): Identifier for the project (optional).

        Returns:
        List[TimeEntry]: List of time entries matching the criteria.
        """
        time_entries = list(self.time_entries.values())
        
        if lawyer_id:
            time_entries = [entry for entry in time_entries if entry.lawyer_id == lawyer_id]
        
        if project_id:
            time_entries = [entry for entry in time_entries if entry.project_id == project_id]
        
        return time_entries

    def calculate_total_time(self, lawyer_id: int = None, project_id: int = None) -> timedelta:
        """
        Calculates the total time spent by a lawyer and/or on a project.

        Args:
        lawyer_id (int): Identifier for the lawyer (optional).
        project_id (int): Identifier for the project (optional).

        Returns:
        timedelta: Total time spent.
        """
        time_entries = self.get_time_entries(lawyer_id, project_id)
        total_time = timedelta(0)
        
        for entry in time_entries:
            total_time += entry.calculate_duration()
        
        return total_time


def main():
    # Example usage
    system = TimeTrackingSystem()

    time_entry1 = TimeEntry(1, 1, 1, datetime(2024, 9, 16, 10, 0), datetime(2024, 9, 16, 11, 0))
    time_entry2 = TimeEntry(2, 1, 2, datetime(2024, 9, 16, 11, 0), datetime(2024, 9, 16, 12, 0))
    time_entry3 = TimeEntry(3, 2, 1, datetime(2024, 9, 16, 10, 0), datetime(2024, 9, 16, 11, 30))

    system.add_time_entry(time_entry1)
    system.add_time_entry(time_entry2)
    system.add_time_entry(time_entry3)

    print("Lawyer 1's total time:")
    print(system.calculate_total_time(lawyer_id=1))

    print("\nProject 1's total time:")
    print(system.calculate_total_time(project_id=1))

    print("\nLawyer 1's time entries on Project 1:")
    for entry in system.get_time_entries(lawyer_id=1, project_id=1):
        print(f"Time Entry {entry.id}: {entry.start_time} - {entry.end_time}")


if __name__ == "__main__":
    main()
```
