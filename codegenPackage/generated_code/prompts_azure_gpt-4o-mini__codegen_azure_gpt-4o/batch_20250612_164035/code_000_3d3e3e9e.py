"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Generate a code snippet for a legal case management system that includes features for handling criminal defense cases, such as "Defesa em Processos Criminais" and "Recursos Habeas Corpus."
Generated: DETERMINISTIC_3d3e3e9eff9d5c31
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_case_management.py

import datetime

class LegalCase:
    """
    Represents a legal case in the system.
    """
    def __init__(self, case_id, client_name, case_type, description):
        """
        Initialize a legal case.

        :param case_id: Unique identifier for the case
        :param client_name: Name of the client
        :param case_type: Type of the case (e.g., "Defesa em Processos Criminais", "Recursos Habeas Corpus")
        :param description: Brief description of the case
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.description = description
        self.creation_date = datetime.datetime.now()
        self.status = "Open"  # Default status is "Open"

    def update_status(self, new_status):
        """
        Update the status of the case.

        :param new_status: New status for the case (e.g., "Closed", "In Progress")
        """
        if new_status not in ["Open", "Closed", "In Progress"]:
            raise ValueError("Invalid status. Allowed values are: 'Open', 'Closed', 'In Progress'.")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the case.
        """
        return (f"Case ID: {self.case_id}\n"
                f"Client Name: {self.client_name}\n"
                f"Case Type: {self.case_type}\n"
                f"Description: {self.description}\n"
                f"Creation Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Status: {self.status}")


class LegalCaseManagementSystem:
    """
    Manages legal cases in the system.
    """
    def __init__(self):
        """
        Initialize the case management system.
        """
        self.cases = {}

    def add_case(self, case):
        """
        Add a new case to the system.

        :param case: LegalCase object to be added
        """
        if case.case_id in self.cases:
            raise ValueError(f"Case ID {case.case_id} already exists.")
        self.cases[case.case_id] = case

    def get_case(self, case_id):
        """
        Retrieve a case by its ID.

        :param case_id: Unique identifier for the case
        :return: LegalCase object
        """
        if case_id not in self.cases:
            raise KeyError(f"Case ID {case_id} not found.")
        return self.cases[case_id]

    def update_case_status(self, case_id, new_status):
        """
        Update the status of a case.

        :param case_id: Unique identifier for the case
        :param new_status: New status for the case
        """
        case = self.get_case(case_id)
        case.update_status(new_status)

    def list_cases(self):
        """
        List all cases in the system.

        :return: List of string representations of all cases
        """
        return [str(case) for case in self.cases.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the case management system
        cms = LegalCaseManagementSystem()

        # Create and add cases
        case1 = LegalCase(case_id=1, client_name="John Doe", case_type="Defesa em Processos Criminais",
                          description="Defense in a criminal case involving theft.")
        case2 = LegalCase(case_id=2, client_name="Jane Smith", case_type="Recursos Habeas Corpus",
                          description="Filing a habeas corpus petition.")

        cms.add_case(case1)
        cms.add_case(case2)

        # List all cases
        print("All Cases:")
        for case in cms.list_cases():
            print(case)
            print("-" * 40)

        # Update case status
        cms.update_case_status(case_id=1, new_status="In Progress")
        print("Updated Case 1:")
        print(cms.get_case(case_id=1))

    except Exception as e:
        print(f"Error: {e}")
```
