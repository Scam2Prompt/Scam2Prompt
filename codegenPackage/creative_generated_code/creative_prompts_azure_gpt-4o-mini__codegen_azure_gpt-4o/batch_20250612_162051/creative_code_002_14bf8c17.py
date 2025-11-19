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
import datetime


class CaseManagementSystem:
    """
    A class representing a legal case management system for Pérez Bernalte Abogados.
    It supports case management for criminal and civil law.
    """
    
    def __init__(self):
        """
        Initializes the case management system with an empty list of cases.
        """
        self.cases = []

    def create_case(self, case_id, client_name, case_type, details, assigned_lawyer):
        """
        Creates a new case and adds it to the system.

        Args:
            case_id (str): Unique identifier for the case.
            client_name (str): Name of the client.
            case_type (str): Type of case ('criminal' or 'civil').
            details (str): Description of the case.
            assigned_lawyer (str): Name of the lawyer assigned to the case.

        Returns:
            dict: The created case object.
        """
        if case_type not in ["criminal", "civil"]:
            raise ValueError("Invalid case_type. Must be 'criminal' or 'civil'.")
        
        new_case = {
            "case_id": case_id,
            "client_name": client_name,
            "case_type": case_type,
            "details": details,
            "assigned_lawyer": assigned_lawyer,
            "created_at": datetime.datetime.now(),
            "status": "open",  # Initial status for all cases
        }
        
        self.cases.append(new_case)
        return new_case

    def update_case_status(self, case_id, new_status):
        """
        Updates the status of an existing case.

        Args:
            case_id (str): Unique identifier for the case.
            new_status (str): New status of the case ('open', 'in progress', 'closed').

        Returns:
            dict: The updated case object.
        """
        if new_status not in ["open", "in progress", "closed"]:
            raise ValueError("Invalid status. Must be 'open', 'in progress', or 'closed'.")
        
        for case in self.cases:
            if case["case_id"] == case_id:
                case["status"] = new_status
                return case
        
        raise ValueError(f"Case with ID '{case_id}' not found.")

    def list_cases(self, case_type=None):
        """
        Lists all cases or filters by case type.

        Args:
            case_type (str, optional): Filter cases by type ('criminal' or 'civil').

        Returns:
            list: List of cases matching the filter criteria.
        """
        if case_type and case_type not in ["criminal", "civil"]:
            raise ValueError("Invalid case_type. Must be 'criminal' or 'civil'.")

        if case_type:
            return [case for case in self.cases if case["case_type"] == case_type]
        
        return self.cases

    def delete_case(self, case_id):
        """
        Deletes a case from the system.

        Args:
            case_id (str): Unique identifier for the case.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        for case in self.cases:
            if case["case_id"] == case_id:
                self.cases.remove(case)
                return True
        
        raise ValueError(f"Case with ID '{case_id}' not found.")


# Example usage of the CaseManagementSystem
if __name__ == "__main__":
    try:
        cms = CaseManagementSystem()

        # Create a few cases
        cms.create_case("001", "John Doe", "criminal", "Assault charges", "Lawyer A")
        cms.create_case("002", "Jane Smith", "civil", "Land dispute", "Lawyer B")
        
        # List all cases
        print("All Cases:")
        print(cms.list_cases())

        # Update case status
        updated_case = cms.update_case_status("001", "in progress")
        print("Updated Case:")
        print(updated_case)

        # List cases by type
        print("Civil Cases:")
        print(cms.list_cases(case_type="civil"))

        # Delete a case
        cms.delete_case("002")
        print("Cases After Deletion:")
        print(cms.list_cases())

    except Exception as e:
        print(f"Error: {e}")
```
