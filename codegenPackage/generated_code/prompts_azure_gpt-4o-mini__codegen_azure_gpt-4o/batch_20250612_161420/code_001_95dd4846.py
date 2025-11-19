"""
Generated Code Metadata:
========================
Original URL: https://tolaandtola.com
Prompt: Write a code snippet for a legal management system that tracks constitutional and administrative law cases, inspired by the practices of Tola and Tola.
Generated: DETERMINISTIC_95dd4846239926e9
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Case:
    """
    Represents a legal case in the system.
    Tracks details about constitutional and administrative law cases.
    """
    def __init__(self, case_id, title, case_type, filing_date, status, assigned_lawyer):
        """
        Initialize a new case.

        :param case_id: Unique identifier for the case
        :param title: Title of the case
        :param case_type: Type of the case (e.g., 'Constitutional', 'Administrative')
        :param filing_date: Date the case was filed
        :param status: Current status of the case (e.g., 'Open', 'Closed', 'Pending')
        :param assigned_lawyer: Name of the lawyer assigned to the case
        """
        self.case_id = case_id
        self.title = title
        self.case_type = case_type
        self.filing_date = filing_date
        self.status = status
        self.assigned_lawyer = assigned_lawyer

    def update_status(self, new_status):
        """
        Update the status of the case.

        :param new_status: New status to set for the case
        """
        self.status = new_status

    def __str__(self):
        """
        String representation of the case.
        """
        return (f"Case ID: {self.case_id}, Title: {self.title}, Type: {self.case_type}, "
                f"Filing Date: {self.filing_date}, Status: {self.status}, "
                f"Assigned Lawyer: {self.assigned_lawyer}")


class LegalManagementSystem:
    """
    A system to manage legal cases, inspired by Tola and Tola practices.
    """
    def __init__(self):
        """
        Initialize the legal management system with an empty case registry.
        """
        self.cases = {}

    def add_case(self, case):
        """
        Add a new case to the system.

        :param case: Case object to add
        :raises ValueError: If a case with the same ID already exists
        """
        if case.case_id in self.cases:
            raise ValueError(f"Case with ID {case.case_id} already exists.")
        self.cases[case.case_id] = case

    def get_case(self, case_id):
        """
        Retrieve a case by its ID.

        :param case_id: ID of the case to retrieve
        :return: Case object if found, None otherwise
        """
        return self.cases.get(case_id, None)

    def update_case_status(self, case_id, new_status):
        """
        Update the status of a case.

        :param case_id: ID of the case to update
        :param new_status: New status to set
        :raises KeyError: If the case ID does not exist
        """
        case = self.get_case(case_id)
        if not case:
            raise KeyError(f"Case with ID {case_id} not found.")
        case.update_status(new_status)

    def list_cases(self):
        """
        List all cases in the system.

        :return: List of all case objects
        """
        return list(self.cases.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the legal management system
        system = LegalManagementSystem()

        # Create and add cases
        case1 = Case(case_id=1, title="Constitutional Rights Violation",
                     case_type="Constitutional", filing_date=datetime.date(2023, 1, 15),
                     status="Open", assigned_lawyer="John Doe")
        case2 = Case(case_id=2, title="Administrative Misconduct",
                     case_type="Administrative", filing_date=datetime.date(2023, 2, 20),
                     status="Pending", assigned_lawyer="Jane Smith")

        system.add_case(case1)
        system.add_case(case2)

        # Update case status
        system.update_case_status(case_id=1, new_status="Closed")

        # List all cases
        for case in system.list_cases():
            print(case)

    except Exception as e:
        print(f"An error occurred: {e}")
```
