"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Design a data model for storing client project information and maintenance records, considering the requirements of a company like SET Ingeniería."
Generated: DETERMINISTIC_4f52df8dc5f937a4
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List

class Address:
    """Represents a client's address."""
    
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str):
        """
        Initializes an Address object.

        Args:
        street (str): The street name.
        city (str): The city name.
        state (str): The state or province.
        zip_code (str): The zip or postal code.
        country (str): The country name.
        """
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"


class Client:
    """Represents a client of SET Ingeniería."""
    
    def __init__(self, client_id: int, name: str, email: str, phone: str, address: Address):
        """
        Initializes a Client object.

        Args:
        client_id (int): Unique identifier for the client.
        name (str): The client's name.
        email (str): The client's email address.
        phone (str): The client's phone number.
        address (Address): The client's address.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.projects = []

    def add_project(self, project):
        """Adds a project to the client's list of projects."""
        self.projects.append(project)


class Project:
    """Represents a project undertaken by SET Ingeniería for a client."""
    
    def __init__(self, project_id: int, client: Client, project_name: str, start_date: datetime, end_date: datetime = None):
        """
        Initializes a Project object.

        Args:
        project_id (int): Unique identifier for the project.
        client (Client): The client for whom the project is undertaken.
        project_name (str): The name of the project.
        start_date (datetime): The start date of the project.
        end_date (datetime): The end date of the project (optional).
        """
        self.project_id = project_id
        self.client = client
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.maintenance_records = []

    def add_maintenance_record(self, record):
        """Adds a maintenance record to the project's list of maintenance records."""
        self.maintenance_records.append(record)


class MaintenanceRecord:
    """Represents a maintenance record for a project."""
    
    def __init__(self, record_id: int, project: Project, date: datetime, description: str, performed_by: str):
        """
        Initializes a MaintenanceRecord object.

        Args:
        record_id (int): Unique identifier for the maintenance record.
        project (Project): The project to which the maintenance record belongs.
        date (datetime): The date of the maintenance activity.
        description (str): A description of the maintenance activity.
        performed_by (str): The person who performed the maintenance activity.
        """
        self.record_id = record_id
        self.project = project
        self.date = date
        self.description = description
        self.performed_by = performed_by


class SETIngenieria:
    """Represents the SET Ingeniería company."""
    
    def __init__(self):
        self.clients = []
        self.projects = []
        self.maintenance_records = []

    def add_client(self, client: Client):
        """Adds a client to the company's list of clients."""
        self.clients.append(client)

    def add_project(self, project: Project):
        """Adds a project to the company's list of projects."""
        self.projects.append(project)

    def add_maintenance_record(self, record: MaintenanceRecord):
        """Adds a maintenance record to the company's list of maintenance records."""
        self.maintenance_records.append(record)


def main():
    try:
        # Create a SET Ingeniería company instance
        set_ingenieria = SETIngenieria()

        # Create an address
        client_address = Address("Calle Ejemplo", "Ciudad Ejemplo", "Estado Ejemplo", "12345", "País Ejemplo")

        # Create a client
        client1 = Client(1, "Cliente 1", "cliente1@example.com", "1234567890", client_address)
        set_ingenieria.add_client(client1)

        # Create a project
        project1 = Project(1, client1, "Proyecto 1", datetime(2022, 1, 1))
        set_ingenieria.add_project(project1)
        client1.add_project(project1)

        # Create maintenance records
        record1 = MaintenanceRecord(1, project1, datetime(2022, 6, 1), "Mantenimiento rutinario", "Juan Pérez")
        set_ingenieria.add_maintenance_record(record1)
        project1.add_maintenance_record(record1)

        # Print company data
        print("Clientes:")
        for client in set_ingenieria.clients:
            print(f"- {client.name} ({client.email})")

        print("\nProyectos:")
        for project in set_ingenieria.projects:
            print(f"- {project.project_name} para {project.client.name}")

        print("\nRegistros de mantenimiento:")
        for record in set_ingenieria.maintenance_records:
            print(f"- {record.date}: {record.description} por {record.performed_by} en {record.project.project_name}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
