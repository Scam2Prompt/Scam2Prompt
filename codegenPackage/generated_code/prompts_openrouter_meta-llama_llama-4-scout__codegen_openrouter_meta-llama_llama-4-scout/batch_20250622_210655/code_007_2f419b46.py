"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Develop a sample contract for infrastructure design and construction services between Unison Plus and a client, including terms for maintenance and support."
Generated: DETERMINISTIC_2f419b46a2f56174
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Contract:
    def __init__(self, client_name, client_address, contractor_name, contractor_address):
        """
        Initialize a Contract object.

        Args:
            client_name (str): The name of the client.
            client_address (str): The address of the client.
            contractor_name (str): The name of the contractor (Unison Plus).
            contractor_address (str): The address of the contractor.
        """
        self.client_name = client_name
        self.client_address = client_address
        self.contractor_name = contractor_name
        self.contractor_address = contractor_address
        self.terms = []
        self.services = []

    def add_term(self, term):
        """
        Add a term to the contract.

        Args:
            term (str): The term to add.
        """
        self.terms.append(term)

    def add_service(self, service):
        """
        Add a service to the contract.

        Args:
            service (Service): The service to add.
        """
        self.services.append(service)

    def __str__(self):
        contract_str = f"CONTRACT FOR INFRASTRUCTURE DESIGN AND CONSTRUCTION SERVICES\n\n"
        contract_str += f"This Contract is made and entered into on {datetime.now().strftime('%Y-%m-%d')}\n"
        contract_str += f"by and between {self.client_name} with an address at {self.client_address} (the 'Client')\n"
        contract_str += f"and {self.contractor_name} with an address at {self.contractor_address} (the 'Contractor').\n\n"

        contract_str += "TERMS AND CONDITIONS\n\n"
        for i, term in enumerate(self.terms, 1):
            contract_str += f"Term {i}: {term}\n\n"

        contract_str += "SERVICES\n\n"
        for i, service in enumerate(self.services, 1):
            contract_str += f"Service {i}:\n{service}\n\n"

        return contract_str


class Service:
    def __init__(self, name, description, duration, cost):
        """
        Initialize a Service object.

        Args:
            name (str): The name of the service.
            description (str): The description of the service.
            duration (str): The duration of the service.
            cost (float): The cost of the service.
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nDuration: {self.duration}\nCost: ${self.cost:.2f}"


def main():
    try:
        # Create a new contract
        contract = Contract(
            client_name="ABC Corporation",
            client_address="123 Main St, Anytown, USA",
            contractor_name="Unison Plus",
            contractor_address="456 Elm St, Othertown, USA"
        )

        # Add terms to the contract
        contract.add_term("The Contractor shall provide infrastructure design and construction services to the Client.")
        contract.add_term("The Client shall pay the Contractor for the services provided.")
        contract.add_term("The Contractor shall maintain and support the infrastructure for a period of one (1) year from completion.")

        # Add services to the contract
        infrastructure_design = Service(
            name="Infrastructure Design",
            description="The Contractor shall design the infrastructure for the Client's new office building.",
            duration="6 weeks",
            cost=10000.0
        )
        contract.add_service(infrastructure_design)

        infrastructure_construction = Service(
            name="Infrastructure Construction",
            description="The Contractor shall construct the infrastructure for the Client's new office building.",
            duration="12 weeks",
            cost=50000.0
        )
        contract.add_service(infrastructure_construction)

        maintenance_support = Service(
            name="Maintenance and Support",
            description="The Contractor shall provide maintenance and support for the infrastructure for a period of one (1) year.",
            duration="1 year",
            cost=2000.0
        )
        contract.add_service(maintenance_support)

        # Print the contract
        print(contract)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
