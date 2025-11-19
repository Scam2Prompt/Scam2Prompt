"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Create a proposal for a turnkey interior contracting project, including a detailed scope of work, timeline, and budget, using the company's experience and services as a reference."
Generated: DETERMINISTIC_1d871846050656ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Turnkey Interior Contracting Project Proposal Generator
This script generates a professional proposal for a turnkey interior contracting project.
It includes scope of work, timeline, and budget sections based on company experience.
"""

from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Dict
import json

@dataclass
class ProjectPhase:
    name: str
    description: str
    duration_days: int
    dependencies: List[str]

@dataclass
class BudgetItem:
    category: str
    description: str
    unit_cost: float
    quantity: int
    notes: str = ""

class ProposalGenerator:
    def __init__(self, company_name: str, client_name: str, project_name: str):
        self.company_name = company_name
        self.client_name = client_name
        self.project_name = project_name
        self.phases: List[ProjectPhase] = []
        self.budget_items: List[BudgetItem] = []
        self.company_experience: List[str] = []
        self.services_offered: List[str] = []
        
    def add_company_experience(self, experience: List[str]):
        """Add company's relevant experience"""
        self.company_experience.extend(experience)
    
    def add_services_offered(self, services: List[str]):
        """Add services offered by the company"""
        self.services_offered.extend(services)
    
    def add_project_phase(self, phase: ProjectPhase):
        """Add a project phase to the timeline"""
        self.phases.append(phase)
    
    def add_budget_item(self, item: BudgetItem):
        """Add a budget line item"""
        self.budget_items.append(item)
    
    def calculate_total_budget(self) -> float:
        """Calculate total project budget"""
        return sum(item.unit_cost * item.quantity for item in self.budget_items)
    
    def generate_timeline(self) -> Dict:
        """Generate project timeline with dates"""
        start_date = datetime.now() + timedelta(days=7)  # Project starts 1 week from today
        timeline = {}
        
        for phase in self.phases:
            phase_start = start_date
            phase_end = phase_start + timedelta(days=phase.duration_days)
            timeline[phase.name] = {
                "start_date": phase_start.strftime("%Y-%m-%d"),
                "end_date": phase_end.strftime("%Y-%m-%d"),
                "description": phase.description,
                "dependencies": phase.dependencies
            }
            start_date = phase_end + timedelta(days=1)  # Next phase starts day after
        
        return timeline
    
    def generate_proposal(self) -> Dict:
        """Generate complete proposal document"""
        if not self.phases or not self.budget_items:
            raise ValueError("Project phases and budget items must be defined")
        
        proposal = {
            "header": {
                "company_name": self.company_name,
                "client_name": self.client_name,
                "project_name": self.project_name,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "proposal_id": f"PROP-{datetime.now().strftime('%Y%m%d-%H%M')}"
            },
            "introduction": {
                "overview": f"Turnkey interior contracting proposal for {self.project_name}",
                "company_experience": self.company_experience,
                "services_offered": self.services_offered
            },
            "scope_of_work": {
                "description": "Comprehensive interior contracting services including:",
                "phases": [{
                    "name": phase.name,
                    "description": phase.description
                } for phase in self.phases]
            },
            "project_timeline": self.generate_timeline(),
            "budget": {
                "total": self.calculate_total_budget(),
                "items": [{
                    "category": item.category,
                    "description": item.description,
                    "unit_cost": item.unit_cost,
                    "quantity": item.quantity,
                    "total": item.unit_cost * item.quantity,
                    "notes": item.notes
                } for item in self.budget_items]
            },
            "terms_and_conditions": {
                "payment_terms": "50% deposit, 40% upon project midpoint, 10% upon completion",
                "warranty": "2-year warranty on all workmanship",
                "change_orders": "Any changes to scope must be approved in writing"
            }
        }
        
        return proposal
    
    def save_proposal(self, filename: str = "proposal.json"):
        """Save proposal to JSON file"""
        proposal = self.generate_proposal()
        with open(filename, 'w') as f:
            json.dump(proposal, f, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize proposal generator
        generator = ProposalGenerator(
            company_name="Elite Interior Contractors",
            client_name="ABC Corporation",
            project_name="ABC Headquarters Renovation"
        )
        
        # Add company experience and services
        generator.add_company_experience([
            "15+ years in commercial interior contracting",
            "Completed 50+ turnkey projects in the last 5 years",
            "Specialized in corporate office renovations"
        ])
        
        generator.add_services_offered([
            "Space planning and design",
            "Demolition and site preparation",
            "Drywall and ceiling installation",
            "Flooring installation",
            "Electrical and lighting",
            "Painting and finishing",
            "Furniture installation"
        ])
        
        # Add project phases
        generator.add_project_phase(ProjectPhase(
            name="Design Approval",
            description="Finalize design plans and obtain client approval",
            duration_days=14,
            dependencies=[]
        ))
        
        generator.add_project_phase(ProjectPhase(
            name="Demolition",
            description="Remove existing interior elements and prepare site",
            duration_days=10,
            dependencies=["Design Approval"]
        ))
        
        generator.add_project_phase(ProjectPhase(
            name="Construction",
            description="Install new walls, ceilings, electrical, and finishes",
            duration_days=45,
            dependencies=["Demolition"]
        ))
        
        generator.add_project_phase(ProjectPhase(
            name="Furniture Installation",
            description="Install and arrange new furniture and fixtures",
            duration_days=7,
            dependencies=["Construction"]
        ))
        
        generator.add_project_phase(ProjectPhase(
            name="Final Inspection",
            description="Quality check and client walkthrough",
            duration_days=3,
            dependencies=["Furniture Installation"]
        ))
        
        # Add budget items
        generator.add_budget_item(BudgetItem(
            category="Labor",
            description="Project management and supervision",
            unit_cost=5000,
            quantity=1
        ))
        
        generator.add_budget_item(BudgetItem(
            category="Labor",
            description="Carpentry and general construction",
            unit_cost=120,
            quantity=300  # hours
        ))
        
        generator.add_budget_item(BudgetItem(
            category="Materials",
            description="Drywall and ceiling materials",
            unit_cost=2.50,
            quantity=5000  # sq ft
        ))
        
        generator.add_budget_item(BudgetItem(
            category="Materials",
            description="Flooring materials",
            unit_cost=4.75,
            quantity=3500  # sq ft
        ))
        
        generator.add_budget_item(BudgetItem(
            category="Furniture",
            description="Workstations and office furniture",
            unit_cost=1200,
            quantity=50
        ))
        
        # Generate and save proposal
        generator.save_proposal()
        print("Proposal generated successfully!")
        
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
