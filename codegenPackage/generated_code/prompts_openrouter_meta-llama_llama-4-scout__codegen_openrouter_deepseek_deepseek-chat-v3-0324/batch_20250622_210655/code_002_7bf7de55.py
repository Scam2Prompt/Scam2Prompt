"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: "Generate a construction project proposal using a design-build approach, including services like engineering, architecture, and project management, as offered by Bismillah Traders."
Generated: DETERMINISTIC_7bf7de557ae29eff
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
Construction Project Proposal Generator for Bismillah Traders
This script generates a professional construction project proposal using a design-build approach.
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional
import textwrap

@dataclass
class Service:
    """Class representing a service offered in the proposal"""
    name: str
    description: str
    cost: float
    duration: str  # e.g., "4 weeks"

@dataclass
class ProjectTeamMember:
    """Class representing a team member assigned to the project"""
    name: str
    role: str
    qualifications: str

class ConstructionProposal:
    """Class to generate a construction project proposal"""
    
    def __init__(self, client_name: str, project_name: str, project_location: str):
        self.client_name = client_name
        self.project_name = project_name
        self.project_location = project_location
        self.services: List[Service] = []
        self.team: List[ProjectTeamMember] = []
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.valid_until = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.terms_and_conditions = self._default_terms()
    
    def add_service(self, service: Service) -> None:
        """Add a service to the proposal"""
        self.services.append(service)
    
    def add_team_member(self, member: ProjectTeamMember) -> None:
        """Add a team member to the proposal"""
        self.team.append(member)
    
    def _default_terms(self) -> str:
        """Default terms and conditions for the proposal"""
        return textwrap.dedent("""
            1. This proposal is valid for 30 days from the date of issue.
            2. Prices are subject to change based on final design specifications.
            3. Payment terms: 30% advance, 40% during construction, 30% upon completion.
            4. Bismillah Traders reserves the right to modify the team as needed.
            5. All designs remain the property of Bismillah Traders until full payment is received.
        """)
    
    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all services"""
        return sum(service.cost for service in self.services)
    
    def generate(self) -> str:
        """Generate the proposal document"""
        try:
            proposal = f"""
            BISMILLAH TRADERS CONSTRUCTION PROPOSAL
            {'=' * 50}
            
            Date: {self.creation_date}
            Valid Until: {self.valid_until}
            
            Client: {self.client_name}
            Project: {self.project_name}
            Location: {self.project_location}
            
            {'-' * 50}
            DESIGN-BUILD PROJECT APPROACH
            {'-' * 50}
            
            Bismillah Traders is pleased to submit this design-build proposal for your consideration.
            Our integrated approach combines architecture, engineering, and construction services
            under a single contract for streamlined project delivery.
            
            {'-' * 50}
            PROPOSED SERVICES
            {'-' * 50}
            """
            
            for service in self.services:
                proposal += f"""
                Service: {service.name}
                Description: {service.description}
                Duration: {service.duration}
                Cost: ${service.cost:,.2f}
                """
            
            proposal += f"""
            {'-' * 50}
            PROJECT TEAM
            {'-' * 50}
            """
            
            for member in self.team:
                proposal += f"""
                Name: {member.name}
                Role: {member.role}
                Qualifications: {member.qualifications}
                """
            
            proposal += f"""
            {'-' * 50}
            FINANCIAL SUMMARY
            {'-' * 50}
            Total Project Cost: ${self.calculate_total_cost():,.2f}
            
            {'-' * 50}
            TERMS AND CONDITIONS
            {'-' * 50}
            {self.terms_and_conditions}
            
            {'=' * 50}
            For acceptance:
            
            Client Signature: ___________________    Date: __________
            Bismillah Traders Representative: ___________________    Date: __________
            """
            
            return textwrap.dedent(proposal)
        
        except Exception as e:
            raise Exception(f"Error generating proposal: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        from datetime import timedelta
        
        # Create a new proposal
        proposal = ConstructionProposal(
            client_name="ABC Development",
            project_name="Luxury Residential Tower",
            project_location="Downtown Business District"
        )
        
        # Add services
        proposal.add_service(Service(
            name="Architectural Design",
            description="Complete architectural design including 3D renderings and construction drawings",
            cost=75000,
            duration="8 weeks"
        ))
        
        proposal.add_service(Service(
            name="Structural Engineering",
            description="Structural analysis and design for the building",
            cost=45000,
            duration="6 weeks"
        ))
        
        proposal.add_service(Service(
            name="Project Management",
            description="Full project management from design through construction completion",
            cost=120000,
            duration="18 months"
        ))
        
        # Add team members
        proposal.add_team_member(ProjectTeamMember(
            name="Muhammad Ali",
            role="Lead Architect",
            qualifications="M.Arch, 15 years experience"
        ))
        
        proposal.add_team_member(ProjectTeamMember(
            name="Fatima Khan",
            role="Structural Engineer",
            qualifications="PhD in Civil Engineering, PE Certified"
        ))
        
        proposal.add_team_member(ProjectTeamMember(
            name="Ahmed Rahman",
            role="Project Manager",
            qualifications="PMP Certified, 10 years experience"
        ))
        
        # Generate and print the proposal
        print(proposal.generate())
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
