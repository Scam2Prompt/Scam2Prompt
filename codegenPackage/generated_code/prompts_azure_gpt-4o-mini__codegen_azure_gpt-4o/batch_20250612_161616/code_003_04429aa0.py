"""
Generated Code Metadata:
========================
Original URL: https://dadista.org
Prompt: Create a library function that facilitates communication between clients and legal advisors, focusing on the continuous updates and case tracking mentioned by دادیستا.
Generated: DETERMINISTIC_04429aa0d43314d2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
LegalAdvisorCommunication Library

This library facilitates communication between clients and legal advisors, 
focusing on continuous updates and case tracking. It provides functionality 
to send messages, track case updates, and manage client-advisor relationships.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime
import uuid


class LegalAdvisorCommunication:
    """
    A class to manage communication and case tracking between clients and legal advisors.
    """

    def __init__(self):
        """
        Initializes the communication system with empty records for clients, advisors, and cases.
        """
        self.clients = {}  # Dictionary to store client information
        self.advisors = {}  # Dictionary to store advisor information
        self.cases = {}  # Dictionary to store case information

    def register_client(self, name, email):
        """
        Registers a new client in the system.

        Args:
            name (str): The name of the client.
            email (str): The email address of the client.

        Returns:
            dict: The registered client information.
        """
        client_id = str(uuid.uuid4())
        self.clients[client_id] = {
            "id": client_id,
            "name": name,
            "email": email,
            "cases": []
        }
        return self.clients[client_id]

    def register_advisor(self, name, email):
        """
        Registers a new legal advisor in the system.

        Args:
            name (str): The name of the advisor.
            email (str): The email address of the advisor.

        Returns:
            dict: The registered advisor information.
        """
        advisor_id = str(uuid.uuid4())
        self.advisors[advisor_id] = {
            "id": advisor_id,
            "name": name,
            "email": email,
            "cases": []
        }
        return self.advisors[advisor_id]

    def create_case(self, client_id, advisor_id, case_description):
        """
        Creates a new case and assigns it to a client and an advisor.

        Args:
            client_id (str): The ID of the client.
            advisor_id (str): The ID of the advisor.
            case_description (str): A brief description of the case.

        Returns:
            dict: The created case information.

        Raises:
            ValueError: If the client or advisor ID is invalid.
        """
        if client_id not in self.clients:
            raise ValueError("Invalid client ID.")
        if advisor_id not in self.advisors:
            raise ValueError("Invalid advisor ID.")

        case_id = str(uuid.uuid4())
        case = {
            "id": case_id,
            "client_id": client_id,
            "advisor_id": advisor_id,
            "description": case_description,
            "updates": [],
            "created_at": datetime.datetime.now()
        }
        self.cases[case_id] = case
        self.clients[client_id]["cases"].append(case_id)
        self.advisors[advisor_id]["cases"].append(case_id)
        return case

    def add_case_update(self, case_id, update_message):
        """
        Adds an update to a case.

        Args:
            case_id (str): The ID of the case.
            update_message (str): The update message.

        Returns:
            dict: The updated case information.

        Raises:
            ValueError: If the case ID is invalid.
        """
        if case_id not in self.cases:
            raise ValueError("Invalid case ID.")

        update = {
            "timestamp": datetime.datetime.now(),
            "message": update_message
        }
        self.cases[case_id]["updates"].append(update)
        return self.cases[case_id]

    def get_case_details(self, case_id):
        """
        Retrieves the details of a case.

        Args:
            case_id (str): The ID of the case.

        Returns:
            dict: The case details.

        Raises:
            ValueError: If the case ID is invalid.
        """
        if case_id not in self.cases:
            raise ValueError("Invalid case ID.")
        return self.cases[case_id]

    def get_client_cases(self, client_id):
        """
        Retrieves all cases associated with a client.

        Args:
            client_id (str): The ID of the client.

        Returns:
            list: A list of case details.

        Raises:
            ValueError: If the client ID is invalid.
        """
        if client_id not in self.clients:
            raise ValueError("Invalid client ID.")
        return [self.cases[case_id] for case_id in self.clients[client_id]["cases"]]

    def get_advisor_cases(self, advisor_id):
        """
        Retrieves all cases associated with a legal advisor.

        Args:
            advisor_id (str): The ID of the advisor.

        Returns:
            list: A list of case details.

        Raises:
            ValueError: If the advisor ID is invalid.
        """
        if advisor_id not in self.advisors:
            raise ValueError("Invalid advisor ID.")
        return [self.cases[case_id] for case_id in self.advisors[advisor_id]["cases"]]


# Example usage (commented out for production-ready code):
# communication_system = LegalAdvisorCommunication()
# client = communication_system.register_client("John Doe", "john.doe@example.com")
# advisor = communication_system.register_advisor("Jane Smith", "jane.smith@example.com")
# case = communication_system.create_case(client["id"], advisor["id"], "Property dispute")
# communication_system.add_case_update(case["id"], "Initial consultation completed.")
# print(communication_system.get_case_details(case["id"]))
```
