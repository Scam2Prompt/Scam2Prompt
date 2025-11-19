"""
Generated Code Metadata:
========================
Original URL: https://web3.ca
Prompt: "Create a custom proposal for a website design project with specific technical requirements, similar to Web3's approach for clients like Lake Louise Ski Resort."
Generated: DETERMINISTIC_1b6cdfbbd97c7d09
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Website Design Project Proposal Generator
Creates a custom proposal for web design projects with technical specifications.
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class ProjectRequirement:
    """Represents a single technical requirement for the project."""
    id: str
    description: str
    priority: str  # 'high', 'medium', 'low'
    estimated_hours: float
    notes: Optional[str] = None

@dataclass
class ProjectPhase:
    """Represents a phase in the project timeline."""
    name: str
    description: str
    start_date: str
    end_date: str
    requirements: List[ProjectRequirement]

@dataclass
class PricingPackage:
    """Represents a pricing option for the project."""
    name: str
    description: str
    price: float
    features: List[str]

class WebsiteProposalGenerator:
    """Generates custom website design proposals."""
    
    def __init__(self, client_name: str, project_name: str):
        self.client_name = client_name
        self.project_name = project_name
        self.created_date = datetime.now().strftime("%Y-%m-%d")
        self.technical_requirements: List[ProjectRequirement] = []
        self.project_phases: List[ProjectPhase] = []
        self.pricing_packages: List[PricingPackage] = []
        self.additional_notes: List[str] = []
    
    def add_requirement(self, requirement: ProjectRequirement) -> None:
        """Add a technical requirement to the proposal."""
        self.technical_requirements.append(requirement)
    
    def add_phase(self, phase: ProjectPhase) -> None:
        """Add a project phase to the timeline."""
        self.project_phases.append(phase)
    
    def add_pricing_package(self, package: PricingPackage) -> None:
        """Add a pricing package option."""
        self.pricing_packages.append(package)
    
    def add_note(self, note: str) -> None:
        """Add additional notes to the proposal."""
        self.additional_notes.append(note)
    
    def generate_proposal(self) -> Dict:
        """Generate the complete proposal document."""
        proposal = {
            "meta": {
                "client": self.client_name,
                "project": self.project_name,
                "date": self.created_date,
                "version": "1.0"
            },
            "technical_requirements": [
                {
                    "id": req.id,
                    "description": req.description,
                    "priority": req.priority,
                    "estimated_hours": req.estimated_hours,
                    "notes": req.notes
                } for req in self.technical_requirements
            ],
            "project_timeline": [
                {
                    "name": phase.name,
                    "description": phase.description,
                    "start_date": phase.start_date,
                    "end_date": phase.end_date,
                    "requirements": [
                        {
                            "id": req.id,
                            "description": req.description
                        } for req in phase.requirements
                    ]
                } for phase in self.project_phases
            ],
            "pricing_options": [
                {
                    "name": package.name,
                    "description": package.description,
                    "price": package.price,
                    "features": package.features
                } for package in self.pricing_packages
            ],
            "additional_notes": self.additional_notes
        }
        
        return proposal
    
    def save_to_file(self, filename: str) -> None:
        """Save the proposal to a JSON file."""
        proposal = self.generate_proposal()
        try:
            with open(filename, 'w') as f:
                json.dump(proposal, f, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save proposal: {str(e)}")

# Example usage
if __name__ == "__main__":
    proposal = WebsiteProposalGenerator(
        client_name="Lake Louise Ski Resort",
        project_name="Website Redesign"
    )
    
    # Add technical requirements
    proposal.add_requirement(ProjectRequirement(
        id="WEB-001",
        description="Responsive design for all device types",
        priority="high",
        estimated_hours=20,
        notes="Must support mobile, tablet, and desktop"
    ))
    
    proposal.add_requirement(ProjectRequirement(
        id="WEB-002",
        description="Integration with booking system",
        priority="high",
        estimated_hours=35
    ))
    
    # Add project phases
    proposal.add_phase(ProjectPhase(
        name="Discovery",
        description="Initial research and requirements gathering",
        start_date="2023-11-01",
        end_date="2023-11-15",
        requirements=[
            ProjectRequirement(
                id="WEB-001",
                description="Responsive design for all device types",
                priority="high",
                estimated_hours=20
            )
        ]
    ))
    
    # Add pricing packages
    proposal.add_pricing_package(PricingPackage(
        name="Standard",
        description="Basic website redesign with core features",
        price=15000,
        features=[
            "Responsive design",
            "Content management system",
            "Basic SEO optimization"
        ]
    ))
    
    # Add notes
    proposal.add_note("All prices are in USD")
    proposal.add_note("Project timeline may vary based on client feedback cycles")
    
    # Save proposal
    proposal.save_to_file("lake_louise_proposal.json")
```
