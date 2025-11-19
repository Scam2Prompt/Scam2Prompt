"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perezbernalte.com
Prompt: Create a Python function that simulates a legal case management system, incorporating features relevant to the specialties of Pérez Bernalte Abogados, such as criminal and civil law.
Generated: DETERMINISTIC_14bf8c17e3aea9e2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LegalCase:
    """
    A class to represent a legal case in the management system.
    """

    def __init__(self, case_id, client_name, case_type, description):
        """
        Initialize a new legal case.

        Args:
            case_id (int): Unique identifier for the case.
            client_name (str): Name of the client.
            case_type (str): Type of the case (e.g., 'Criminal', 'Civil').
            description (str): Brief description of the case.
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.description = description
        self.status = 'Open'  # Default status of a new case

    def __str__(self):
        """
        String representation of the legal case.

        Returns:
            str: A string summarizing the case details.
        """
        return f"Case ID: {self.case_id}, Client: {self.client_name}, Type: {self.case_type}, Status: {self.status}, Description: {self.description}"


class CaseManagementSystem:
    """
    A class to manage legal cases.
    """

    def __init__(self):
        """
        Initialize the case management system.
        """
        self.cases = []

    def add_case(self, case):
        """
        Add a new case to the management system.

        Args:
            case (LegalCase): The legal case to be added.

        Raises:
            ValueError: If the case ID already exists.
        """
        if any(existing_case.case_id == case.case_id for existing_case in self.cases):
            raise ValueError(f"Case ID {case.case_id} already exists.")
        self.cases.append(case)

    def remove_case(self, case_id):
        """
        Remove a case from the management system.

        Args:
            case_id (int): The ID of the case to be removed.

        Raises:
            ValueError: If the case ID does not exist.
        """
        case_to_remove = next((case for case in self.cases if case.case_id == case_id), None)
        if case_to_remove is None:
            raise ValueError(f"Case ID {case_id} does not exist.")
        self.cases.remove(case_to_remove)

    def update_case_status(self, case_id, new_status):
        """
        Update the status of an existing case.

        Args:
            case_id (int): The ID of the case to update.
            new_status (str): The new status to set for the case.

        Raises:
            ValueError: If the case ID does not exist.
        """
        case_to_update = next((case for case in self.cases if case.case_id == case_id), None)
        if case_to_update is None:
            raise ValueError(f"Case ID {case_id} does not exist.")
        case_to_update.status = new_status

    def list_cases(self):
        """
        List all cases in the management system.

        Returns:
            list: A list of string representations of all cases.
        """
        return [str(case) for case in self.cases]


# Example usage:
if __name__ == "__main__":
    cms = CaseManagementSystem()

    # Adding cases
    try:
        case1 = LegalCase(case_id=1, client_name="John Doe", case_type="Criminal", description="Robbery charge.")
        cms.add_case(case1)

        case2 = LegalCase(case_id=2, client_name="Jane Smith", case_type="Civil", description="Property dispute.")
        cms.add_case(case2)

        # Listing cases
        print("Current cases:")
        print("\n".join(cms.list_cases()))

        # Updating case status
        cms.update_case_status(case_id=1, new_status="Closed")
        print("\nUpdated cases:")
        print("\n".join(cms.list_cases()))

        # Removing a case
        cms.remove_case(case_id=2)
        print("\nAfter removing a case:")
        print("\n".join(cms.list_cases()))

    except ValueError as e:
        print(f"Error: {e}")
```
