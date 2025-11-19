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
import datetime

class CaseManagementSystem:
    """
    A legal case management system for Pérez Bernalte Abogados.
    Specializes in criminal and civil law case tracking and management.
    """

    def __init__(self):
        # Initialize the system with an empty list of cases
        self.cases = []

    def add_case(self, case_id, case_type, client_name, description, status="Open"):
        """
        Add a new case to the system.

        :param case_id: Unique identifier for the case (str)
        :param case_type: Type of case ('Criminal' or 'Civil') (str)
        :param client_name: Name of the client (str)
        :param description: Brief description of the case (str)
        :param status: Current status of the case ('Open', 'Closed', etc.) (str)
        """
        if case_type not in ["Criminal", "Civil"]:
            raise ValueError("Invalid case type. Must be 'Criminal' or 'Civil'.")

        case = {
            "case_id": case_id,
            "case_type": case_type,
            "client_name": client_name,
            "description": description,
            "status": status,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now()
        }
        self.cases.append(case)

    def update_case_status(self, case_id, new_status):
        """
        Update the status of an existing case.

        :param case_id: Unique identifier for the case (str)
        :param new_status: New status for the case (str)
        """
        for case in self.cases:
            if case["case_id"] == case_id:
                case["status"] = new_status
                case["updated_at"] = datetime.datetime.now()
                return case
        raise ValueError(f"Case with ID {case_id} not found.")

    def get_case(self, case_id):
        """
        Retrieve details of a specific case.

        :param case_id: Unique identifier for the case (str)
        :return: Case details (dict)
        """
        for case in self.cases:
            if case["case_id"] == case_id:
                return case
        raise ValueError(f"Case with ID {case_id} not found.")

    def list_cases(self, case_type=None, status=None):
        """
        List all cases, optionally filtered by type and/or status.

        :param case_type: Filter by case type ('Criminal' or 'Civil') (str, optional)
        :param status: Filter by case status ('Open', 'Closed', etc.) (str, optional)
        :return: List of cases matching the filters (list of dicts)
        """
        filtered_cases = self.cases
        if case_type:
            if case_type not in ["Criminal", "Civil"]:
                raise ValueError("Invalid case type. Must be 'Criminal' or 'Civil'.")
            filtered_cases = [case for case in filtered_cases if case["case_type"] == case_type]
        if status:
            filtered_cases = [case for case in filtered_cases if case["status"] == status]
        return filtered_cases

    def delete_case(self, case_id):
        """
        Delete a case from the system.

        :param case_id: Unique identifier for the case (str)
        """
        for case in self.cases:
            if case["case_id"] == case_id:
                self.cases.remove(case)
                return
        raise ValueError(f"Case with ID {case_id} not found.")


# Example usage (comment out or remove in production)
if __name__ == "__main__":
    cms = CaseManagementSystem()
    cms.add_case("001", "Criminal", "John Doe", "Theft case")
    cms.add_case("002", "Civil", "Jane Smith", "Property dispute")
    print("All cases:", cms.list_cases())
    print("Criminal cases:", cms.list_cases(case_type="Criminal"))
    cms.update_case_status("001", "Closed")
    print("Updated case 001:", cms.get_case("001"))
    cms.delete_case("002")
    print("All cases after deletion:", cms.list_cases())
```
