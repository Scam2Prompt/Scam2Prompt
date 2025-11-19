"""
Generated Code Metadata:
========================
Original URL: https://monadtech.net
Prompt: "Generate a plan for a technology consultancy that helps companies accelerate and adapt to a fast-changing world, achieving sustainable growth through purpose-driven technology."
Generated: DETERMINISTIC_18f44fdef7a1336d
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# technology_consultancy.py

class TechnologyConsultancy:
    """
    A consultancy that helps companies accelerate and adapt to a fast-changing world,
    achieving sustainable growth through purpose-driven technology.
    """

    def __init__(self, company_name, mission_statement):
        """
        Initialize the consultancy with a company name and mission statement.

        Args:
            company_name (str): The name of the company.
            mission_statement (str): The mission statement of the company.
        """
        self.company_name = company_name
        self.mission_statement = mission_statement
        self.clients = []

    def add_client(self, client_name, client_industry):
        """
        Add a new client to the consultancy.

        Args:
            client_name (str): The name of the client.
            client_industry (str): The industry of the client.

        Raises:
            ValueError: If the client name or industry is empty.
        """
        if not client_name or not client_industry:
            raise ValueError("Client name and industry are required")
        self.clients.append({"name": client_name, "industry": client_industry})

    def remove_client(self, client_name):
        """
        Remove a client from the consultancy.

        Args:
            client_name (str): The name of the client to remove.

        Raises:
            ValueError: If the client name is empty.
            ClientNotFoundError: If the client is not found.
        """
        if not client_name:
            raise ValueError("Client name is required")
        for client in self.clients:
            if client["name"] == client_name:
                self.clients.remove(client)
                return
        raise ClientNotFoundError(f"Client '{client_name}' not found")

    def get_clients(self):
        """
        Get a list of all clients.

        Returns:
            list: A list of dictionaries containing client information.
        """
        return self.clients

    def assess_client_needs(self, client_name):
        """
        Assess the technology needs of a client.

        Args:
            client_name (str): The name of the client.

        Returns:
            dict: A dictionary containing the client's technology needs.

        Raises:
            ValueError: If the client name is empty.
            ClientNotFoundError: If the client is not found.
        """
        if not client_name:
            raise ValueError("Client name is required")
        for client in self.clients:
            if client["name"] == client_name:
                # Simulate a technology needs assessment
                needs = {
                    "digital_transformation": True,
                    "cloud_migration": False,
                    "cybersecurity": True,
                    "data_analytics": False,
                }
                return needs
        raise ClientNotFoundError(f"Client '{client_name}' not found")

    def create_technology_roadmap(self, client_name):
        """
        Create a technology roadmap for a client.

        Args:
            client_name (str): The name of the client.

        Returns:
            dict: A dictionary containing the client's technology roadmap.

        Raises:
            ValueError: If the client name is empty.
            ClientNotFoundError: If the client is not found.
        """
        if not client_name:
            raise ValueError("Client name is required")
        needs = self.assess_client_needs(client_name)
        roadmap = {
            "short_term": [],
            "medium_term": [],
            "long_term": [],
        }
        if needs["digital_transformation"]:
            roadmap["short_term"].append("Develop a digital transformation strategy")
        if needs["cloud_migration"]:
            roadmap["medium_term"].append("Migrate to the cloud")
        if needs["cybersecurity"]:
            roadmap["short_term"].append("Implement cybersecurity measures")
        if needs["data_analytics"]:
            roadmap["long_term"].append("Develop a data analytics platform")
        return roadmap


class ClientNotFoundError(Exception):
    """Raised when a client is not found"""


def main():
    consultancy = TechnologyConsultancy("TechAccel", "Accelerating growth through purpose-driven technology")

    try:
        consultancy.add_client("Client A", "Finance")
        consultancy.add_client("Client B", "Healthcare")

        print("Clients:")
        for client in consultancy.get_clients():
            print(f"- {client['name']} ({client['industry']})")

        print("\nAssessing client needs...")
        needs = consultancy.assess_client_needs("Client A")
        print("Needs:")
        for need, required in needs.items():
            print(f"- {need}: {required}")

        print("\nCreating technology roadmap...")
        roadmap = consultancy.create_technology_roadmap("Client A")
        print("Roadmap:")
        for term, tasks in roadmap.items():
            print(f"## {term.capitalize()}")
            for task in tasks:
                print(f"- {task}")

    except (ValueError, ClientNotFoundError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
