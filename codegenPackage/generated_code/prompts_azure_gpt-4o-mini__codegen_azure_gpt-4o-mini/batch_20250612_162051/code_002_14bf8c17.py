"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Create a Python function that simulates a legal case management system, incorporating features relevant to the specialties of Pérez Bernalte Abogados, such as criminal and civil law.
Generated: DETERMINISTIC_14bf8c17e3aea9e2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LegalCase:
    """
    A class to represent a legal case in the case management system.
    """

    def __init__(self, case_id, case_type, client_name, status='Open'):
        """
        Initializes a new legal case.

        :param case_id: Unique identifier for the case
        :param case_type: Type of the case (e.g., 'Criminal', 'Civil')
        :param client_name: Name of the client
        :param status: Current status of the case (default is 'Open')
        """
        self.case_id = case_id
        self.case_type = case_type
        self.client_name = client_name
        self.status = status

    def update_status(self, new_status):
        """
        Updates the status of the case.

        :param new_status: New status to set for the case
        """
        valid_statuses = ['Open', 'In Progress', 'Closed']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status


class CaseManagementSystem:
    """
    A class to manage legal cases.
    """

    def __init__(self):
        """
        Initializes the case management system with an empty case list.
        """
        self.cases = {}

    def add_case(self, case):
        """
        Adds a new legal case to the system.

        :param case: An instance of LegalCase to be added
        """
        if not isinstance(case, LegalCase):
            raise TypeError("case must be an instance of LegalCase")
        if case.case_id in self.cases:
            raise ValueError(f"Case ID {case.case_id} already exists.")
        self.cases[case.case_id] = case

    def get_case(self, case_id):
        """
        Retrieves a legal case by its ID.

        :param case_id: Unique identifier for the case
        :return: An instance of LegalCase if found, else None
        """
        return self.cases.get(case_id, None)

    def update_case_status(self, case_id, new_status):
        """
        Updates the status of a legal case.

        :param case_id: Unique identifier for the case
        :param new_status: New status to set for the case
        """
        case = self.get_case(case_id)
        if case is None:
            raise ValueError(f"Case ID {case_id} not found.")
        case.update_status(new_status)

    def list_cases(self):
        """
        Lists all legal cases in the system.

        :return: A list of all cases
        """
        return list(self.cases.values())


# Example usage
if __name__ == "__main__":
    cms = CaseManagementSystem()

    # Create some legal cases
    case1 = LegalCase(case_id=1, case_type='Criminal', client_name='John Doe')
    case2 = LegalCase(case_id=2, case_type='Civil', client_name='Jane Smith')

    # Add cases to the system
    try:
        cms.add_case(case1)
        cms.add_case(case2)
    except (TypeError, ValueError) as e:
        print(f"Error adding case: {e}")

    # Update case status
    try:
        cms.update_case_status(1, 'In Progress')
    except (ValueError, TypeError) as e:
        print(f"Error updating case status: {e}")

    # List all cases
    for case in cms.list_cases():
        print(f"Case ID: {case.case_id}, Type: {case.case_type}, Client: {case.client_name}, Status: {case.status}")
```
