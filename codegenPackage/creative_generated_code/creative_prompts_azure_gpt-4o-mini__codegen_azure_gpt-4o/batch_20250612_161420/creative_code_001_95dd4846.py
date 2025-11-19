"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tolaandtola.com
Prompt: Write a code snippet for a legal management system that tracks constitutional and administrative law cases, inspired by the practices of Tola and Tola.
Generated: DETERMINISTIC_95dd4846239926e9
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Legal Management System - Constitutional and Administrative Law Case Tracker

This Python script manages cases for a legal firm inspired by the practices of Tola and Tola.
It organizes and tracks constitutional and administrative law cases, allowing for case addition,
retrieval, and status updates.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime


class Case:
    """
    Represents a legal case with relevant details such as case title, type,
    status, and creation date.
    """

    def __init__(self, case_id, title, case_type):
        """
        Initializes a new case.
        
        :param case_id: Unique identifier for the case
        :param title: Case title or description
        :param case_type: Type of case ('Constitutional' or 'Administrative')
        """
        self.case_id = case_id
        self.title = title
        self.case_type = case_type
        self.status = "Open"  # Default status is 'Open'
        self.created_at = datetime.datetime.now()

    def update_status(self, status):
        """
        Updates the status of the case.
        
        :param status: New status of the case ('Open', 'Closed', 'Pending')
        """
        valid_statuses = ["Open", "Closed", "Pending"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status '{status}'. Valid statuses are: {valid_statuses}")
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the case details.
        """
        return (
            f"Case ID: {self.case_id}\n"
            f"Title: {self.title}\n"
            f"Type: {self.case_type}\n"
            f"Status: {self.status}\n"
            f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )


class LegalManagementSystem:
    """
    Manages a collection of legal cases for the firm.
    Provides operations to add, retrieve, update, and list cases.
    """

    def __init__(self):
        """
        Initializes the legal management system with an empty case list.
        """
        self.cases = {}

    def add_case(self, case_id, title, case_type):
        """
        Adds a new case to the system.
        
        :param case_id: Unique identifier for the case
        :param title: Case title or description
        :param case_type: Type of case ('Constitutional' or 'Administrative')
        """
        if case_id in self.cases:
            raise ValueError(f"Case ID '{case_id}' already exists.")
        
        if case_type not in ["Constitutional", "Administrative"]:
            raise ValueError("Case type must be either 'Constitutional' or 'Administrative'.")
        
        new_case = Case(case_id, title, case_type)
        self.cases[case_id] = new_case

    def get_case(self, case_id):
        """
        Retrieves a case by its ID.
        
        :param case_id: Unique identifier of the case
        :return: Case object if found, otherwise raises KeyError
        """
        if case_id not in self.cases:
            raise KeyError(f"Case ID '{case_id}' not found.")
        return self.cases[case_id]

    def update_case_status(self, case_id, status):
        """
        Updates the status of a case.
        
        :param case_id: Unique identifier of the case
        :param status: New status of the case ('Open', 'Closed', 'Pending')
        """
        case = self.get_case(case_id)
        case.update_status(status)

    def list_cases(self):
        """
        Lists all cases in the system.
        
        :return: A list of string representations of all cases
        """
        return [str(case) for case in self.cases.values()]


# Example Usage
if __name__ == "__main__":
    try:
        # Create the legal management system
        lms = LegalManagementSystem()

        # Add some cases
        lms.add_case("C001", "Freedom of Speech Case", "Constitutional")
        lms.add_case("A001", "Tax Dispute Case", "Administrative")

        # Retrieve and print case details
        case = lms.get_case("C001")
        print(case)

        # Update case status
        lms.update_case_status("C001", "Closed")

        # List all cases
        print("All Cases:")
        for case_str in lms.list_cases():
            print(case_str)

    except Exception as e:
        # Handle any runtime errors gracefully
        print(f"Error: {e}")
```
