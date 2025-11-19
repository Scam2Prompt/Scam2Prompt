"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.beardlegalgroup.com
Prompt: Generate a code snippet for a legal case management system that tracks client interactions and case developments, inspired by the client-focused approach of Beard Legal Group.
Generated: DETERMINISTIC_153a11f16c2fb37c
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Client:
    """
    Represents a client in the legal case management system.
    """
    def __init__(self, client_id, name, contact_info):
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info
        self.interactions = []  # List to track client interactions

    def add_interaction(self, interaction_date, interaction_details):
        """
        Adds a new interaction with the client.

        :param interaction_date: The date of the interaction (datetime object)
        :param interaction_details: A description of the interaction
        """
        if not isinstance(interaction_date, datetime.date):
            raise ValueError("interaction_date must be a datetime.date object")
        self.interactions.append({
            "date": interaction_date,
            "details": interaction_details
        })


class Case:
    """
    Represents a legal case in the system.
    """
    def __init__(self, case_id, client, case_details):
        self.case_id = case_id
        self.client = client  # Reference to a Client object
        self.case_details = case_details
        self.developments = []  # List to track case developments

    def add_development(self, development_date, development_details):
        """
        Adds a new development to the case.

        :param development_date: The date of the development (datetime object)
        :param development_details: A description of the development
        """
        if not isinstance(development_date, datetime.date):
            raise ValueError("development_date must be a datetime.date object")
        self.developments.append({
            "date": development_date,
            "details": development_details
        })


class LegalCaseManagementSystem:
    """
    Main class to manage legal cases and clients.
    """
    def __init__(self):
        self.clients = {}  # Dictionary to store clients by their ID
        self.cases = {}    # Dictionary to store cases by their ID

    def add_client(self, client_id, name, contact_info):
        """
        Adds a new client to the system.

        :param client_id: A unique identifier for the client
        :param name: Name of the client
        :param contact_info: Contact information for the client
        """
        if client_id in self.clients:
            raise ValueError(f"Client with ID {client_id} already exists.")
        self.clients[client_id] = Client(client_id, name, contact_info)

    def add_case(self, case_id, client_id, case_details):
        """
        Adds a new case to the system.

        :param case_id: A unique identifier for the case
        :param client_id: The ID of the client associated with the case
        :param case_details: A description or details of the case
        """
        if case_id in self.cases:
            raise ValueError(f"Case with ID {case_id} already exists.")
        if client_id not in self.clients:
            raise ValueError(f"Client with ID {client_id} does not exist.")
        client = self.clients[client_id]
        self.cases[case_id] = Case(case_id, client, case_details)

    def get_client(self, client_id):
        """
        Retrieves client information by client ID.

        :param client_id: The unique identifier for the client
        :return: The Client object associated with the given ID
        """
        if client_id not in self.clients:
            raise ValueError(f"Client with ID {client_id} does not exist.")
        return self.clients[client_id]

    def get_case(self, case_id):
        """
        Retrieves case information by case ID.

        :param case_id: The unique identifier for the case
        :return: The Case object associated with the given ID
        """
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} does not exist.")
        return self.cases[case_id]


# Example usage (uncomment to test):
# legal_system = LegalCaseManagementSystem()
# legal_system.add_client(client_id=1, name="John Doe", contact_info="john.doe@example.com")
# legal_system.add_case(case_id=101, client_id=1, case_details="Property dispute case")
# client = legal_system.get_client(client_id=1)
# client.add_interaction(interaction_date=datetime.date.today(), interaction_details="Initial consultation")
# case = legal_system.get_case(case_id=101)
# case.add_development(development_date=datetime.date.today(), development_details="Filed initial paperwork")
```
