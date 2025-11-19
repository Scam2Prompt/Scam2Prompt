"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Generate a code snippet for a legal case management system that includes features for handling criminal defense cases, such as "Defesa em Processos Criminais" and "Recursos Habeas Corpus."
Generated: DETERMINISTIC_3d3e3e9eff9d5c31
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# legal_case_management.py
# A simple legal case management system for handling criminal defense cases.
# Includes features for managing "Defesa em Processos Criminais" and "Recursos Habeas Corpus".

import datetime


class LegalCase:
    """
    Represents a legal case in the system.
    """
    def __init__(self, case_id, client_name, case_type, description):
        """
        Initialize a new legal case.
        :param case_id: Unique identifier for the case
        :param client_name: Name of the client
        :param case_type: Type of case ("Defesa em Processos Criminais", "Recursos Habeas Corpus", etc.)
        :param description: Brief description of the case
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.description = description
        self.created_at = datetime.datetime.now()
        self.status = "Open"  # Default status is "Open"
        self.updates = []  # List to store case updates

    def add_update(self, update_text):
        """
        Add an update to the case.
        :param update_text: The update message/description
        """
        update = {
            "timestamp": datetime.datetime.now(),
            "update_text": update_text
        }
        self.updates.append(update)
        print(f"Update added to case {self.case_id}: {update_text}")

    def close_case(self):
        """
        Close the case.
        """
        self.status = "Closed"
        print(f"Case {self.case_id} has been closed.")

    def __str__(self):
        """
        Display case details.
        """
        updates_str = "\n".join([f"{update['timestamp']}: {update['update_text']}" for update in self.updates])
        return (f"Case ID: {self.case_id}\n"
                f"Client Name: {self.client_name}\n"
                f"Case Type: {self.case_type}\n"
                f"Description: {self.description}\n"
                f"Created At: {self.created_at}\n"
                f"Status: {self.status}\n"
                f"Updates:\n{updates_str if updates_str else 'No updates yet.'}")


class LegalCaseManagementSystem:
    """
    A system to manage legal cases.
    """
    def __init__(self):
        """
        Initialize the system with an empty list of cases.
        """
        self.cases = {}

    def create_case(self, case_id, client_name, case_type, description):
        """
        Create a new legal case.
        :param case_id: Unique identifier for the case
        :param client_name: Name of the client
        :param case_type: Type of case ("Defesa em Processos Criminais", "Recursos Habeas Corpus", etc.)
        :param description: Brief description of the case
        """
        if case_id in self.cases:
            print(f"Error: Case ID {case_id} already exists.")
            return
        case = LegalCase(case_id, client_name, case_type, description)
        self.cases[case_id] = case
        print(f"Case {case_id} created successfully.")

    def get_case(self, case_id):
        """
        Retrieve a case by case ID.
        :param case_id: Unique identifier for the case
        :return: LegalCase object if found, None otherwise
        """
        return self.cases.get(case_id, None)

    def list_cases(self):
        """
        List all cases in the system.
        """
        if not self.cases:
            print("No cases found.")
            return
        for case_id, case in self.cases.items():
            print(case)

    def update_case(self, case_id, update_text):
        """
        Add an update to an existing case.
        :param case_id: Unique identifier for the case
        :param update_text: The update message/description
        """
        case = self.get_case(case_id)
        if not case:
            print(f"Error: Case ID {case_id} not found.")
            return
        case.add_update(update_text)

    def close_case(self, case_id):
        """
        Close an existing case.
        :param case_id: Unique identifier for the case
        """
        case = self.get_case(case_id)
        if not case:
            print(f"Error: Case ID {case_id} not found.")
            return
        case.close_case()


# Example usage (uncomment to test the system)
# if __name__ == "__main__":
#     system = LegalCaseManagementSystem()
#     system.create_case("1", "John Doe", "Defesa em Processos Criminais", "Client accused of theft.")
#     system.create_case("2", "Jane Smith", "Recursos Habeas Corpus", "Client seeking release from custody.")
#     system.update_case("1", "Initial court hearing scheduled.")
#     system.update_case("2", "Habeas corpus petition filed.")
#     system.list_cases()
#     system.close_case("1")
#     system.list_cases()
```
