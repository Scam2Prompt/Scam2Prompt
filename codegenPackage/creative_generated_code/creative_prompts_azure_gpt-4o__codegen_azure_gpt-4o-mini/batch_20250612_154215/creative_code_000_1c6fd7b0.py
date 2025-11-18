"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7054company.github.io
Prompt: Write a Python script to simulate a consulting service workflow for a company like 7054Company, including client intake and solution proposal steps.
Generated: DETERMINISTIC_1c6fd7b0c737f5eb
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from typing import List, Dict, Any


class Client:
    """Class to represent a client in the consulting service workflow."""
    
    def __init__(self, name: str, email: str):
        self.client_id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        """Converts the client object to a dictionary."""
        return {
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email
        }


class SolutionProposal:
    """Class to encapsulate a solution proposal for a client."""
    
    def __init__(self, client: Client, solution: str, cost: float):
        self.client = client
        self.solution = solution
        self.cost = cost
        self.proposal_id = str(uuid.uuid4())

    def to_dict(self) -> Dict[str, Any]:
        """Converts the solution proposal object to a dictionary."""
        return {
            "proposal_id": self.proposal_id,
            "client": self.client.to_dict(),
            "solution": self.solution,
            "cost": self.cost
        }


class ConsultingService:
    """Class to manage the consulting service workflow."""

    def __init__(self):
        self.clients: List[Client] = []
        self.proposals: List[SolutionProposal] = []

    def intake_client(self, name: str, email: str) -> Client:
        """Intakes a new client and adds them to the service."""
        if not self.validate_email(email):
            raise ValueError(f"Invalid email address: {email}")

        new_client = Client(name, email)
        self.clients.append(new_client)
        return new_client

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates the email format."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def propose_solution(self, client: Client, solution: str, cost: float) -> SolutionProposal:
        """Proposes a solution to the specified client."""
        if cost <= 0:
            raise ValueError("Cost must be greater than zero.")

        proposal = SolutionProposal(client, solution, cost)
        self.proposals.append(proposal)
        return proposal

    def save_to_file(self, filename: str) -> None:
        """Saves the clients and proposals to a JSON file."""
        data = {
            "clients": [client.to_dict() for client in self.clients],
            "proposals": [proposal.to_dict() for proposal in self.proposals]
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Loads clients and proposals from a JSON file."""
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                self.clients = [Client(**client) for client in data.get("clients", [])]
                self.proposals = [SolutionProposal(Client(**proposal['client']),
                                                    proposal['solution'],
                                                    proposal['cost']) for proposal in data.get("proposals", [])]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to read from file {filename}: {e}")


# Example usage of the ConsultingService
if __name__ == "__main__":
    service = ConsultingService()
    try:
        client = service.intake_client("John Doe", "john.doe@example.com")
        proposal = service.propose_solution(client, "Digital Marketing Strategy", 5000.00)
        service.save_to_file("consulting_service_data.json")
        print("Client and proposal saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
