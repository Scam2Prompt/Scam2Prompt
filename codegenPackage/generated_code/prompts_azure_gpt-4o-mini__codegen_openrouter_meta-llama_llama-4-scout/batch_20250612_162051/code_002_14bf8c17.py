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
from enum import Enum
from typing import List, Dict

class CaseStatus(Enum):
    """Enum for case status"""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"

class CaseType(Enum):
    """Enum for case type"""
    CRIMINAL = "Criminal"
    CIVIL = "Civil"

class Client:
    """Client class"""
    def __init__(self, name: str, email: str, phone: str):
        """
        Initialize a Client object.

        Args:
        - name (str): Client name
        - email (str): Client email
        - phone (str): Client phone number
        """
        self.name = name
        self.email = email
        self.phone = phone

class Case:
    """Case class"""
    def __init__(self, case_id: int, case_type: CaseType, client: Client, status: CaseStatus = CaseStatus.OPEN):
        """
        Initialize a Case object.

        Args:
        - case_id (int): Unique case ID
        - case_type (CaseType): Type of case (Criminal or Civil)
        - client (Client): Client object associated with the case
        - status (CaseStatus): Case status (default: Open)
        """
        self.case_id = case_id
        self.case_type = case_type
        self.client = client
        self.status = status

class CaseManagementSystem:
    """Case management system class"""
    def __init__(self):
        self.cases: Dict[int, Case] = {}
        self.clients: Dict[str, Client] = {}

    def add_client(self, client: Client):
        """
        Add a client to the system.

        Args:
        - client (Client): Client object to add
        """
        self.clients[client.email] = client

    def add_case(self, case: Case):
        """
        Add a case to the system.

        Args:
        - case (Case): Case object to add
        """
        self.cases[case.case_id] = case

    def update_case_status(self, case_id: int, status: CaseStatus):
        """
        Update the status of a case.

        Args:
        - case_id (int): ID of the case to update
        - status (CaseStatus): New status of the case

        Raises:
        - ValueError: If the case ID does not exist
        """
        if case_id not in self.cases:
            raise ValueError("Case ID does not exist")
        self.cases[case_id].status = status

    def get_case(self, case_id: int) -> Case:
        """
        Get a case by its ID.

        Args:
        - case_id (int): ID of the case to retrieve

        Returns:
        - Case: Case object associated with the ID

        Raises:
        - ValueError: If the case ID does not exist
        """
        if case_id not in self.cases:
            raise ValueError("Case ID does not exist")
        return self.cases[case_id]

    def get_client_cases(self, client_email: str) -> List[Case]:
        """
        Get all cases associated with a client.

        Args:
        - client_email (str): Email of the client

        Returns:
        - List[Case]: List of Case objects associated with the client

        Raises:
        - ValueError: If the client email does not exist
        """
        if client_email not in self.clients:
            raise ValueError("Client email does not exist")
        client_cases = [case for case in self.cases.values() if case.client.email == client_email]
        return client_cases

def main():
    # Create a case management system
    system = CaseManagementSystem()

    # Create clients
    client1 = Client("John Doe", "john.doe@example.com", "123456789")
    client2 = Client("Jane Doe", "jane.doe@example.com", "987654321")

    # Add clients to the system
    system.add_client(client1)
    system.add_client(client2)

    # Create cases
    case1 = Case(1, CaseType.CRIMINAL, client1)
    case2 = Case(2, CaseType.CIVIL, client2)

    # Add cases to the system
    system.add_case(case1)
    system.add_case(case2)

    # Update case status
    system.update_case_status(1, CaseStatus.IN_PROGRESS)

    # Get case
    case = system.get_case(1)
    print(f"Case ID: {case.case_id}, Case Type: {case.case_type.value}, Client: {case.client.name}, Status: {case.status.value}")

    # Get client cases
    client_cases = system.get_client_cases("john.doe@example.com")
    for case in client_cases:
        print(f"Case ID: {case.case_id}, Case Type: {case.case_type.value}, Status: {case.status.value}")

if __name__ == "__main__":
    main()
```
