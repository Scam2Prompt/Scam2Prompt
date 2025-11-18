"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munshihr.com
Prompt: Generate code for automating foreign secondment processes, including tracking international assignments, based on Munshi HR Solutions' offerings.
Generated: DETERMINISTIC_b196ba69a1ea173d
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class InternationalAssignment:
    """
    Class to represent an international assignment for an employee.
    """

    def __init__(self, employee_id: int, destination: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes a new InternationalAssignment instance.

        :param employee_id: Unique identifier for the employee
        :param destination: Country or location of the assignment
        :param start_date: Start date of the assignment
        :param end_date: End date of the assignment
        """
        self.employee_id = employee_id
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date

    def duration(self) -> int:
        """
        Calculate the duration of the assignment in days.

        :return: Duration in days
        """
        return (self.end_date - self.start_date).days

class AssignmentTracker:
    """
    Class to manage and track international assignments.
    """

    def __init__(self):
        """Initialize the tracker with an empty list of assignments."""
        self.assignments: List[InternationalAssignment] = []

    def add_assignment(self, assignment: InternationalAssignment) -> None:
        """
        Add a new international assignment to the tracker.

        :param assignment: The assignment to be added
        """
        if self._is_assignment_conflicting(assignment):
            raise ValueError("Conflict detected: The assignment overlaps with an existing one.")
        self.assignments.append(assignment)

    def _is_assignment_conflicting(self, new_assignment: InternationalAssignment) -> bool:
        """
        Check if the new assignment conflicts with existing assignments.

        :param new_assignment: The new assignment to check
        :return: True if there is a conflict, False otherwise
        """
        for assignment in self.assignments:
            if (new_assignment.employee_id == assignment.employee_id and
                not (new_assignment.end_date < assignment.start_date or
                     new_assignment.start_date > assignment.end_date)):
                return True
        return False

    def get_assignments(self, employee_id: Optional[int] = None) -> List[Dict]:
        """
        Retrieve a list of assignments, optionally filtered by employee ID.

        :param employee_id: Employee ID to filter assignments (optional)
        :return: List of assignments as dictionaries
        """
        if employee_id is not None:
            return [
                {
                    "employee_id": assignment.employee_id,
                    "destination": assignment.destination,
                    "start_date": assignment.start_date,
                    "end_date": assignment.end_date,
                    "duration": assignment.duration(),
                }
                for assignment in self.assignments if assignment.employee_id == employee_id
            ]
        return [
            {
                "employee_id": assignment.employee_id,
                "destination": assignment.destination,
                "start_date": assignment.start_date,
                "end_date": assignment.end_date,
                "duration": assignment.duration(),
            }
            for assignment in self.assignments
        ]

if __name__ == "__main__":
    # Example usage of the AssignmentTracker
    tracker = AssignmentTracker()

    # Add some assignments
    try:
        assignment1 = InternationalAssignment(1, "Germany", datetime.date(2023, 1, 10), datetime.date(2023, 6, 10))
        tracker.add_assignment(assignment1)

        assignment2 = InternationalAssignment(2, "Spain", datetime.date(2023, 2, 15), datetime.date(2023, 5, 15))
        tracker.add_assignment(assignment2)

        # Attempting to add a conflicting assignment
        conflicting_assignment = InternationalAssignment(1, "France", datetime.date(2023, 5, 1), datetime.date(2023, 7, 1))
        tracker.add_assignment(conflicting_assignment)  # This will raise a ValueError

    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve assignments for a specific employee
    employee_assignments = tracker.get_assignments(1)
    print(f"Assignments for employee 1: {employee_assignments}")

    # Retrieve all assignments
    all_assignments = tracker.get_assignments()
    print(f"All assignments: {all_assignments}")
```
