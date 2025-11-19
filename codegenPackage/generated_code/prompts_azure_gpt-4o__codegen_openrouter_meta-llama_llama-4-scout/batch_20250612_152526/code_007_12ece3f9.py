"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Write a script for managing scholarships and financial aid programs for an online brokerage education platform, inspired by Kigali Institute's scholarship initiatives.
Generated: DETERMINISTIC_12ece3f94fe24da8
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scholarship_manager.py

class Scholarship:
    """Represents a scholarship program."""

    def __init__(self, id: int, name: str, description: str, amount: float):
        """
        Initializes a Scholarship object.

        Args:
        id (int): Unique identifier for the scholarship.
        name (str): Name of the scholarship.
        description (str): Brief description of the scholarship.
        amount (float): Amount of the scholarship.
        """
        self.id = id
        self.name = name
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Scholarship {self.id}: {self.name} - ${self.amount:.2f}"


class FinancialAidProgram:
    """Represents a financial aid program."""

    def __init__(self, id: int, name: str, description: str, eligibility_criteria: str):
        """
        Initializes a FinancialAidProgram object.

        Args:
        id (int): Unique identifier for the financial aid program.
        name (str): Name of the financial aid program.
        description (str): Brief description of the financial aid program.
        eligibility_criteria (str): Eligibility criteria for the financial aid program.
        """
        self.id = id
        self.name = name
        self.description = description
        self.eligibility_criteria = eligibility_criteria

    def __str__(self):
        return f"Financial Aid Program {self.id}: {self.name}"


class ScholarshipManager:
    """Manages scholarships and financial aid programs."""

    def __init__(self):
        self.scholarships = {}
        self.financial_aid_programs = {}

    def add_scholarship(self, scholarship: Scholarship):
        """
        Adds a scholarship to the manager.

        Args:
        scholarship (Scholarship): Scholarship to add.
        """
        self.scholarships[scholarship.id] = scholarship

    def add_financial_aid_program(self, financial_aid_program: FinancialAidProgram):
        """
        Adds a financial aid program to the manager.

        Args:
        financial_aid_program (FinancialAidProgram): Financial aid program to add.
        """
        self.financial_aid_programs[financial_aid_program.id] = financial_aid_program

    def get_scholarship(self, id: int) -> Scholarship:
        """
        Retrieves a scholarship by ID.

        Args:
        id (int): ID of the scholarship to retrieve.

        Returns:
        Scholarship: Retrieved scholarship, or None if not found.
        """
        return self.scholarships.get(id)

    def get_financial_aid_program(self, id: int) -> FinancialAidProgram:
        """
        Retrieves a financial aid program by ID.

        Args:
        id (int): ID of the financial aid program to retrieve.

        Returns:
        FinancialAidProgram: Retrieved financial aid program, or None if not found.
        """
        return self.financial_aid_programs.get(id)

    def update_scholarship(self, id: int, name: str = None, description: str = None, amount: float = None):
        """
        Updates a scholarship.

        Args:
        id (int): ID of the scholarship to update.
        name (str, optional): New name for the scholarship. Defaults to None.
        description (str, optional): New description for the scholarship. Defaults to None.
        amount (float, optional): New amount for the scholarship. Defaults to None.

        Raises:
        ValueError: If the scholarship is not found.
        """
        scholarship = self.get_scholarship(id)
        if scholarship is None:
            raise ValueError("Scholarship not found")

        if name:
            scholarship.name = name
        if description:
            scholarship.description = description
        if amount:
            scholarship.amount = amount

    def update_financial_aid_program(self, id: int, name: str = None, description: str = None, eligibility_criteria: str = None):
        """
        Updates a financial aid program.

        Args:
        id (int): ID of the financial aid program to update.
        name (str, optional): New name for the financial aid program. Defaults to None.
        description (str, optional): New description for the financial aid program. Defaults to None.
        eligibility_criteria (str, optional): New eligibility criteria for the financial aid program. Defaults to None.

        Raises:
        ValueError: If the financial aid program is not found.
        """
        financial_aid_program = self.get_financial_aid_program(id)
        if financial_aid_program is None:
            raise ValueError("Financial aid program not found")

        if name:
            financial_aid_program.name = name
        if description:
            financial_aid_program.description = description
        if eligibility_criteria:
            financial_aid_program.eligibility_criteria = eligibility_criteria

    def delete_scholarship(self, id: int):
        """
        Deletes a scholarship.

        Args:
        id (int): ID of the scholarship to delete.

        Raises:
        ValueError: If the scholarship is not found.
        """
        if id not in self.scholarships:
            raise ValueError("Scholarship not found")
        del self.scholarships[id]

    def delete_financial_aid_program(self, id: int):
        """
        Deletes a financial aid program.

        Args:
        id (int): ID of the financial aid program to delete.

        Raises:
        ValueError: If the financial aid program is not found.
        """
        if id not in self.financial_aid_programs:
            raise ValueError("Financial aid program not found")
        del self.financial_aid_programs[id]


def main():
    # Create a scholarship manager
    manager = ScholarshipManager()

    # Create scholarships
    scholarship1 = Scholarship(1, "Kigali Institute Scholarship", "Full scholarship for students", 10000.0)
    scholarship2 = Scholarship(2, "Partial Scholarship", "Partial scholarship for students", 5000.0)

    # Create financial aid programs
    financial_aid_program1 = FinancialAidProgram(1, "Student Loan Program", "Low-interest student loan program", "GPA > 3.0")
    financial_aid_program2 = FinancialAidProgram(2, "Grant Program", "Need-based grant program", "Financial need")

    # Add scholarships and financial aid programs to the manager
    manager.add_scholarship(scholarship1)
    manager.add_scholarship(scholarship2)
    manager.add_financial_aid_program(financial_aid_program1)
    manager.add_financial_aid_program(financial_aid_program2)

    # Print scholarships and financial aid programs
    print("Scholarships:")
    for scholarship in manager.scholarships.values():
        print(scholarship)

    print("\nFinancial Aid Programs:")
    for financial_aid_program in manager.financial_aid_programs.values():
        print(financial_aid_program)

    # Update a scholarship
    manager.update_scholarship(1, amount=12000.0)
    print("\nUpdated Scholarship:")
    print(manager.get_scholarship(1))

    # Delete a financial aid program
    manager.delete_financial_aid_program(2)
    print("\nFinancial Aid Programs after deletion:")
    for financial_aid_program in manager.financial_aid_programs.values():
        print(financial_aid_program)


if __name__ == "__main__":
    main()
```
