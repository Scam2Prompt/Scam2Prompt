"""
Generated Code Metadata:
========================
Original URL: https://7054company.github.io
Prompt: Write a Python script to simulate a consulting service workflow for a company like 7054Company, including client intake and solution proposal steps.
Generated: DETERMINISTIC_1c6fd7b0c737f5eb
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class ClientStatus(Enum):
    """Enum representing client status in the workflow."""
    NEW = "New"
    INTAKE = "Intake"
    PROPOSAL_SENT = "Proposal Sent"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    COMPLETED = "Completed"


class ServiceType(Enum):
    """Enum representing available consulting services."""
    STRATEGY = "Business Strategy"
    IT = "IT Consulting"
    FINANCE = "Financial Advisory"
    MARKETING = "Marketing Strategy"
    HR = "HR Consulting"


class Client:
    """Class representing a client in the consulting workflow."""
    
    def __init__(self, name: str, contact_email: str, company: str):
        self.name = name
        self.contact_email = contact_email
        self.company = company
        self.status = ClientStatus.NEW
        self.consulting_needs: List[ServiceType] = []
        self.intake_date: Optional[datetime] = None
        self.proposal_sent_date: Optional[datetime] = None
        self.proposal_details: Optional[Dict] = None
        self.client_id = self._generate_client_id()
    
    def _generate_client_id(self) -> str:
        """Generate a unique client ID based on name and timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{self.name[:3].upper()}-{timestamp}"
    
    def add_service_need(self, service: ServiceType) -> None:
        """Add a consulting service need for the client."""
        if service not in self.consulting_needs:
            self.consulting_needs.append(service)
    
    def complete_intake(self) -> None:
        """Mark client intake as completed."""
        if self.status == ClientStatus.NEW:
            self.status = ClientStatus.INTAKE
            self.intake_date = datetime.now()
    
    def send_proposal(self, proposal_details: Dict) -> None:
        """Send proposal to client."""
        if self.status == ClientStatus.INTAKE:
            self.status = ClientStatus.PROPOSAL_SENT
            self.proposal_sent_date = datetime.now()
            self.proposal_details = proposal_details
    
    def update_status(self, new_status: ClientStatus) -> None:
        """Update client status with validation."""
        valid_transitions = {
            ClientStatus.NEW: [ClientStatus.INTAKE],
            ClientStatus.INTAKE: [ClientStatus.PROPOSAL_SENT, ClientStatus.REJECTED],
            ClientStatus.PROPOSAL_SENT: [ClientStatus.APPROVED, ClientStatus.REJECTED],
            ClientStatus.APPROVED: [ClientStatus.COMPLETED],
        }
        
        if new_status in valid_transitions.get(self.status, []):
            self.status = new_status
        else:
            raise ValueError(f"Invalid status transition from {self.status} to {new_status}")
    
    def to_dict(self) -> Dict:
        """Convert client data to dictionary for serialization."""
        return {
            "client_id": self.client_id,
            "name": self.name,
            "contact_email": self.contact_email,
            "company": self.company,
            "status": self.status.value,
            "consulting_needs": [need.value for need in self.consulting_needs],
            "intake_date": self.intake_date.isoformat() if self.intake_date else None,
            "proposal_sent_date": self.proposal_sent_date.isoformat() if self.proposal_sent_date else None,
            "proposal_details": self.proposal_details
        }


class ConsultingWorkflow:
    """Class managing the consulting service workflow."""
    
    def __init__(self):
        self.clients: Dict[str, Client] = {}
    
    def add_client(self, name: str, contact_email: str, company: str) -> Client:
        """Add a new client to the workflow."""
        if not all([name, contact_email, company]):
            raise ValueError("Name, email, and company are required")
        
        client = Client(name, contact_email, company)
        self.clients[client.client_id] = client
        return client
    
    def get_client(self, client_id: str) -> Optional[Client]:
        """Retrieve a client by ID."""
        return self.clients.get(client_id)
    
    def generate_proposal(self, client_id: str, services: List[ServiceType], estimated_hours: int, fee: float) -> Dict:
        """Generate a proposal for a client."""
        client = self.get_client(client_id)
        if not client:
            raise ValueError("Client not found")
        
        if client.status != ClientStatus.INTAKE:
            raise ValueError("Proposal can only be generated after intake")
        
        proposal = {
            "services": [service.value for service in services],
            "estimated_hours": estimated_hours,
            "fee": fee,
            "generated_date": datetime.now().isoformat(),
            "valid_until": (datetime.now() + timedelta(days=30)).isoformat()
        }
        
        client.send_proposal(proposal)
        return proposal
    
    def save_workflow(self, filename: str) -> None:
        """Save workflow data to a JSON file."""
        data = {
            "clients": [client.to_dict() for client in self.clients.values()]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save workflow: {str(e)}")
    
    def load_workflow(self, filename: str) -> None:
        """Load workflow data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
                for client_data in data.get("clients", []):
                    client = Client(
                        client_data["name"],
                        client_data["contact_email"],
                        client_data["company"]
                    )
                    client.client_id = client_data["client_id"]
                    client.status = ClientStatus(client_data["status"])
                    client.consulting_needs = [ServiceType(need) for need in client_data["consulting_needs"]]
                    
                    if client_data["intake_date"]:
                        client.intake_date = datetime.fromisoformat(client_data["intake_date"])
                    if client_data["proposal_sent_date"]:
                        client.proposal_sent_date = datetime.fromisoformat(client_data["proposal_sent_date"])
                    
                    client.proposal_details = client_data["proposal_details"]
                    self.clients[client.client_id] = client
                    
        except (IOError, json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Failed to load workflow: {str(e)}")


def main():
    """Demonstrate the consulting workflow."""
    workflow = ConsultingWorkflow()
    
    try:
        # Client intake
        client = workflow.add_client(
            "John Doe",
            "john.doe@example.com",
            "Acme Corp"
        )
        client.add_service_need(ServiceType.STRATEGY)
        client.add_service_need(ServiceType.MARKETING)
        client.complete_intake()
        
        # Generate proposal
        proposal = workflow.generate_proposal(
            client.client_id,
            client.consulting_needs,
            estimated_hours=40,
            fee=10000.00
        )
        
        print(f"Generated proposal for {client.name}:")
        print(json.dumps(proposal, indent=2))
        
        # Save workflow
        workflow.save_workflow("consulting_workflow.json")
        print("Workflow saved successfully.")
        
    except Exception as e:
        print(f"Error in workflow: {str(e)}")


if __name__ == "__main__":
    from datetime import timedelta
    main()
```
