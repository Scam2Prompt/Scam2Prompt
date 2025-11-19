"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: "Generate a code snippet for a custom telephone project proposal using Bouygues Telecom's services."
Generated: DETERMINISTIC_5fb23da2affc5e9b
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Telephone Project Proposal for Bouygues Telecom Services

This script generates a project proposal for a custom telephone solution
using Bouygues Telecom's services. It includes configuration details,
service options, and cost estimation.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class BouyguesTelecomService:
    """Represents a Bouygues Telecom service with its properties."""
    
    def __init__(self, name: str, description: str, monthly_cost: float):
        """
        Initialize a Bouygues Telecom service.
        
        Args:
            name: Name of the service.
            description: Description of the service.
            monthly_cost: Monthly cost in EUR.
        """
        self.name = name
        self.description = description
        self.monthly_cost = monthly_cost
    
    def to_dict(self) -> Dict:
        """Convert the service to a dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'monthly_cost': self.monthly_cost
        }

class TelephoneProjectProposal:
    """Generates a project proposal for a custom telephone solution."""
    
    def __init__(self, project_name: str, client_name: str, duration_months: int):
        """
        Initialize the project proposal.
        
        Args:
            project_name: Name of the project.
            client_name: Name of the client.
            duration_months: Duration of the project in months.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.duration_months = duration_months
        self.services: List[BouyguesTelecomService] = []
    
    def add_service(self, service: BouyguesTelecomService) -> None:
        """Add a Bouygues Telecom service to the proposal."""
        self.services.append(service)
    
    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all services for the project duration."""
        return sum(service.monthly_cost for service in self.services) * self.duration_months
    
    def generate_proposal(self) -> Dict:
        """
        Generate the project proposal as a dictionary.
        
        Returns:
            A dictionary containing all proposal details.
        """
        return {
            'project_name': self.project_name,
            'client_name': self.client_name,
            'duration_months': self.duration_months,
            'services': [service.to_dict() for service in self.services],
            'total_cost': self.calculate_total_cost(),
            'generation_date': datetime.now().strftime("%Y-%m-%d")
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the proposal to a JSON file.
        
        Args:
            filename: Name of the file to save the proposal.
        
        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_proposal(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save proposal to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new project proposal
        proposal = TelephoneProjectProposal(
            project_name="Custom VoIP Solution",
            client_name="ABC Corporation",
            duration_months=24
        )
        
        # Add Bouygues Telecom services
        proposal.add_service(BouyguesTelecomService(
            name="VoIP Pro",
            description="Professional VoIP service with unlimited calls",
            monthly_cost=19.99
        ))
        
        proposal.add_service(BouyguesTelecomService(
            name="Cloud PBX",
            description="Cloud-based PBX system",
            monthly_cost=29.99
        ))
        
        # Save the proposal to a file
        proposal.save_to_file("bouygues_telecom_proposal.json")
        print("Proposal generated successfully.")
        
    except Exception as e:
        print(f"Error generating proposal: {e}")
```
