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
# legal_management_system.py

from enum import Enum
from datetime import date

class CaseType(Enum):
    """Enum for case types."""
    CONSTITUTIONAL = 1
    ADMINISTRATIVE = 2

class CaseStatus(Enum):
    """Enum for case status."""
    PENDING = 1
    IN_PROGRESS = 2
    RESOLVED = 3

class Case:
    """Represents a legal case."""

    def __init__(self, case_id, case_type, case_name, filing_date, status=CaseStatus.PENDING):
        """
        Initializes a Case object.

        Args:
            case_id (int): Unique identifier for the case.
            case_type (CaseType): Type of the case (constitutional or administrative).
            case_name (str): Name of the case.
            filing_date (date): Date the case was filed.
            status (CaseStatus, optional): Status of the case. Defaults to CaseStatus.PENDING.
        """
        self.case_id = case_id
        self.case_type = case_type
        self.case_name = case_name
        self.filing_date = filing_date
        self.status = status

    def update_status(self, status):
        """
        Updates the status of the case.

        Args:
            status (CaseStatus): New status of the case.

        Raises:
            ValueError: If the status is not a valid CaseStatus enum member.
        """
        if not isinstance(status, CaseStatus):
            raise ValueError("Invalid case status")
        self.status = status

    def __str__(self):
        return f"Case ID: {self.case_id}, Type: {self.case_type.name}, Name: {self.case_name}, Filing Date: {self.filing_date}, Status: {self.status.name}"

class Lawyer:
    """Represents a lawyer."""

    def __init__(self, lawyer_id, name, specialization):
        """
        Initializes a Lawyer object.

        Args:
            lawyer_id (int): Unique identifier for the lawyer.
            name (str): Name of the lawyer.
            specialization (str): Specialization of the lawyer.
        """
        self.lawyer_id = lawyer_id
        self.name = name
        self.specialization = specialization
        self.cases = []

    def assign_case(self, case):
        """
        Assigns a case to the lawyer.

        Args:
            case (Case): Case to be assigned.

        Raises:
            ValueError: If the case is already assigned to another lawyer.
        """
        if case in self.cases:
            raise ValueError("Case already assigned to this lawyer")
        self.cases.append(case)

    def __str__(self):
        return f"Lawyer ID: {self.lawyer_id}, Name: {self.name}, Specialization: {self.specialization}"

class LegalManagementSystem:
    """Represents a legal management system."""

    def __init__(self):
        self.cases = []
        self.lawyers = []

    def add_case(self, case):
        """
        Adds a case to the system.

        Args:
            case (Case): Case to be added.

        Raises:
            ValueError: If the case already exists in the system.
        """
        if case in self.cases:
            raise ValueError("Case already exists in the system")
        self.cases.append(case)

    def add_lawyer(self, lawyer):
        """
        Adds a lawyer to the system.

        Args:
            lawyer (Lawyer): Lawyer to be added.

        Raises:
            ValueError: If the lawyer already exists in the system.
        """
        if lawyer in self.lawyers:
            raise ValueError("Lawyer already exists in the system")
        self.lawyers.append(lawyer)

    def get_case(self, case_id):
        """
        Retrieves a case by its ID.

        Args:
            case_id (int): ID of the case.

        Returns:
            Case: The case with the specified ID, or None if not found.
        """
        for case in self.cases:
            if case.case_id == case_id:
                return case
        return None

    def get_lawyer(self, lawyer_id):
        """
        Retrieves a lawyer by their ID.

        Args:
            lawyer_id (int): ID of the lawyer.

        Returns:
            Lawyer: The lawyer with the specified ID, or None if not found.
        """
        for lawyer in self.lawyers:
            if lawyer.lawyer_id == lawyer_id:
                return lawyer
        return None

def main():
    # Create a legal management system
    system = LegalManagementSystem()

    # Create cases
    case1 = Case(1, CaseType.CONSTITUTIONAL, "Tola vs. Tola", date(2022, 1, 1))
    case2 = Case(2, CaseType.ADMINISTRATIVE, "Tola vs. Administrative Body", date(2022, 6, 1))

    # Add cases to the system
    system.add_case(case1)
    system.add_case(case2)

    # Create lawyers
    lawyer1 = Lawyer(1, "John Doe", "Constitutional Law")
    lawyer2 = Lawyer(2, "Jane Doe", "Administrative Law")

    # Add lawyers to the system
    system.add_lawyer(lawyer1)
    system.add_lawyer(lawyer2)

    # Assign cases to lawyers
    lawyer1.assign_case(case1)
    lawyer2.assign_case(case2)

    # Print cases and lawyers
    print("Cases:")
    for case in system.cases:
        print(case)

    print("\nLawyers:")
    for lawyer in system.lawyers:
        print(lawyer)
        print("Assigned Cases:")
        for case in lawyer.cases:
            print(case)

if __name__ == "__main__":
    main()
```
