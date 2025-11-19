"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a code snippet to track and analyze hotel staff performance and management metrics, focusing on effective hotel management practices.
Generated: DETERMINISTIC_ffa25e0690fe206c
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class StaffMember:
    """
    Represents a hotel staff member with performance metrics.
    """
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.tasks_completed = 0
        self.hours_worked = 0.0
        self.performance_logs = []  # List of performance logs

    def log_task(self, task_description: str):
        """
        Logs a completed task for the staff member.
        """
        self.tasks_completed += 1
        self.performance_logs.append({
            "timestamp": datetime.datetime.now(),
            "task_description": task_description
        })

    def log_hours(self, hours: float):
        """
        Logs hours worked by the staff member.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_performance_score(self) -> float:
        """
        Calculates a performance score based on tasks completed and hours worked.
        """
        if self.hours_worked == 0:
            return 0.0  # Avoid division by zero
        return self.tasks_completed / self.hours_worked

    def __str__(self):
        return f"{self.name} ({self.role}) - Tasks Completed: {self.tasks_completed}, Hours Worked: {self.hours_worked:.2f}, Performance Score: {self.calculate_performance_score():.2f}"


class HotelManagement:
    """
    Manages hotel staff and tracks overall performance metrics.
    """
    def __init__(self):
        self.staff_members: List[StaffMember] = []

    def add_staff_member(self, name: str, role: str):
        """
        Adds a new staff member to the hotel management system.
        """
        self.staff_members.append(StaffMember(name, role))

    def log_staff_task(self, name: str, task_description: str):
        """
        Logs a task for a specific staff member.
        """
        staff_member = self._find_staff_member(name)
        if staff_member:
            staff_member.log_task(task_description)
        else:
            raise ValueError(f"Staff member '{name}' not found.")

    def log_staff_hours(self, name: str, hours: float):
        """
        Logs hours worked for a specific staff member.
        """
        staff_member = self._find_staff_member(name)
        if staff_member:
            staff_member.log_hours(hours)
        else:
            raise ValueError(f"Staff member '{name}' not found.")

    def generate_performance_report(self) -> List[Dict[str, str]]:
        """
        Generates a performance report for all staff members.
        """
        report = []
        for staff_member in self.staff_members:
            report.append({
                "Name": staff_member.name,
                "Role": staff_member.role,
                "Tasks Completed": staff_member.tasks_completed,
                "Hours Worked": f"{staff_member.hours_worked:.2f}",
                "Performance Score": f"{staff_member.calculate_performance_score():.2f}"
            })
        return report

    def _find_staff_member(self, name: str) -> StaffMember:
        """
        Finds a staff member by name.
        """
        for staff_member in self.staff_members:
            if staff_member.name == name:
                return staff_member
        return None


# Example usage:
if __name__ == "__main__":
    hotel = HotelManagement()
    hotel.add_staff_member("Alice", "Receptionist")
    hotel.add_staff_member("Bob", "Housekeeping")

    hotel.log_staff_task("Alice", "Checked in a guest")
    hotel.log_staff_hours("Alice", 8)

    hotel.log_staff_task("Bob", "Cleaned Room 101")
    hotel.log_staff_hours("Bob", 6)

    report = hotel.generate_performance_report()
    for entry in report:
        print(entry)
```
