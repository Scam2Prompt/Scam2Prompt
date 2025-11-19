"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Generate code for automating foreign secondment processes, including tracking international assignments, based on Munshi HR Solutions' offerings.
Generated: DETERMINISTIC_b196ba69a1ea173d
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class InternationalAssignment:
    """
    Class to represent an international assignment for an employee.
    """

    def __init__(self, employee_id: str, destination_country: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize an InternationalAssignment instance.

        :param employee_id: Unique identifier for the employee
        :param destination_country: Country where the employee is assigned
        :param start_date: Start date of the assignment
        :param end_date: End date of the assignment
        """
        self.employee_id = employee_id
        self.destination_country = destination_country
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
    Class to track international assignments.
    """

    def __init__(self):
        """
        Initialize the AssignmentTracker with an empty list of assignments.
        """
        self.assignments: List[InternationalAssignment] = []

    def add_assignment(self, assignment: InternationalAssignment) -> None:
        """
        Add a new international assignment to the tracker.

        :param assignment: An instance of InternationalAssignment
        """
        self.assignments.append(assignment)

    def get_assignments(self, employee_id: Optional[str] = None) -> List[Dict]:
        """
        Retrieve assignments for a specific employee or all assignments.

        :param employee_id: Unique identifier for the employee (optional)
        :return: List of assignments as dictionaries
        """
        if employee_id:
            return [self.assignment_to_dict(a) for a in self.assignments if a.employee_id == employee_id]
        return [self.assignment_to_dict(a) for a in self.assignments]

    @staticmethod
    def assignment_to_dict(assignment: InternationalAssignment) -> Dict:
        """
        Convert an InternationalAssignment instance to a dictionary.

        :param assignment: An instance of InternationalAssignment
        :return: Dictionary representation of the assignment
        """
        return {
            "employee_id": assignment.employee_id,
            "destination_country": assignment.destination_country,
            "start_date": assignment.start_date.isoformat(),
            "end_date": assignment.end_date.isoformat(),
            "duration_days": assignment.duration()
        }


def main():
    """
    Main function to demonstrate the functionality of the AssignmentTracker.
    """
    tracker = AssignmentTracker()

    # Example assignments
    try:
        assignment1 = InternationalAssignment("E123", "Germany", datetime.date(2023, 1, 15), datetime.date(2023, 6, 15))
        tracker.add_assignment(assignment1)

        assignment2 = InternationalAssignment("E124", "France", datetime.date(2023, 3, 1), datetime.date(2023, 9, 1))
        tracker.add_assignment(assignment2)

        # Retrieve all assignments
        all_assignments = tracker.get_assignments()
        print("All Assignments:", all_assignments)

        # Retrieve assignments for a specific employee
        employee_assignments = tracker.get_assignments("E123")
        print("Assignments for Employee E123:", employee_assignments)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
