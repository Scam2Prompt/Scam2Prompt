"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Generate a project proposal for a water and sanitation initiative in a Horn of Africa community, incorporating HARDA's experience in sustainable development.
Generated: DETERMINISTIC_df6f4f2c416c37f5
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Proposal Generator for Water and Sanitation Initiative in Horn of Africa
Incorporates HARDA's (Horn of Africa Relief and Development Agency) experience
in sustainable development projects.
"""

import datetime
from typing import List, Dict, Optional

class ProjectProposal:
    """
    Generates a comprehensive project proposal for water and sanitation initiatives
    based on HARDA's sustainable development framework.
    """
    
    def __init__(self, community_name: str, region: str, population: int):
        """
        Initialize the proposal with basic community information.
        
        Args:
            community_name: Name of the target community
            region: Geographic region within Horn of Africa
            population: Estimated population size
        """
        self.community_name = community_name
        self.region = region
        self.population = population
        self.date = datetime.date.today()
        self.components = []
        self.budget = {}
        self.timeline = {}
        self.stakeholders = []
        
    def add_component(self, name: str, description: str, 
                     harada_experience: Optional[str] = None) -> None:
        """
        Add a project component with optional HARDA experience reference.
        
        Args:
            name: Component name (e.g., 'Water Well Installation')
            description: Detailed description of the component
            harada_experience: Reference to similar HARDA projects (optional)
        """
        component = {
            'name': name,
            'description': description,
            'harada_experience': harada_experience or "New initiative"
        }
        self.components.append(component)
        
    def set_budget(self, item: str, amount: float, justification: str) -> None:
        """
        Add a budget item with justification.
        
        Args:
            item: Budget line item name
            amount: Estimated cost in USD
            justification: Rationale for the expense
        """
        self.budget[item] = {
            'amount': amount,
            'justification': justification
        }
        
    def set_timeline(self, phase: str, start_date: datetime.date, 
                    duration_days: int) -> None:
        """
        Set project timeline phases.
        
        Args:
            phase: Project phase name
            start_date: Planned start date
            duration_days: Expected duration in days
        """
        end_date = start_date + datetime.timedelta(days=duration_days)
        self.timeline[phase] = {
            'start_date': start_date,
            'end_date': end_date,
            'duration_days': duration_days
        }
        
    def add_stakeholder(self, name: str, role: str, contact: str) -> None:
        """
        Add a project stakeholder with contact information.
        
        Args:
            name: Stakeholder name/organization
            role: Their role in the project
            contact: Contact information
        """
        self.stakeholders.append({
            'name': name,
            'role': role,
            'contact': contact
        })
        
    def generate_proposal(self) -> Dict:
        """
        Compile all proposal components into a structured document.
        
        Returns:
            Dictionary containing complete proposal data
        """
        proposal = {
            'header': {
                'title': f"Water and Sanitation Initiative for {self.community_name}",
                'date': self.date,
                'prepared_by': "HARDA Sustainable Development Team"
            },
            'community_profile': {
                'name': self.community_name,
                'region': self.region,
                'population': self.population,
                'needs_assessment': "High priority for clean water and sanitation facilities"
            },
            'project_components': self.components,
            'budget': self.budget,
            'timeline': self.timeline,
            'stakeholders': self.stakeholders,
            'sustainability_plan': {
                'community_engagement': "Training local water committees",
                'maintenance_strategy': "Establish repair fund and technician network",
                'harada_approach': "Builds on 10+ years of successful WASH programs"
            },
            'monitoring_evaluation': {
                'indicators': ["% households with clean water access", "Reduction in waterborne diseases"],
                'reporting': "Quarterly progress reports to donors and community"
            }
        }
        return proposal
    
    def export_to_markdown(self, filename: str) -> None:
        """
        Export the proposal to a markdown file format.
        
        Args:
            filename: Output file path
        """
        proposal = self.generate_proposal()
        
        with open(filename, 'w') as f:
            # Write header
            f.write(f"# {proposal['header']['title']}\n\n")
            f.write(f"**Date:** {proposal['header']['date']}\n")
            f.write(f"**Prepared by:** {proposal['header']['prepared_by']}\n\n")
            
            # Community profile
            f.write("## Community Profile\n\n")
            f.write(f"- **Community:** {proposal['community_profile']['name']}\n")
            f.write(f"- **Region:** {proposal['community_profile']['region']}\n")
            f.write(f"- **Population:** {proposal['community_profile']['population']}\n")
            f.write(f"- **Needs Assessment:** {proposal['community_profile']['needs_assessment']}\n\n")
            
            # Project components
            f.write("## Project Components\n\n")
            for component in proposal['project_components']:
                f.write(f"### {component['name']}\n")
                f.write(f"{component['description']}\n")
                f.write(f"*HARDA Experience:* {component['harada_experience']}\n\n")
            
            # Budget
            f.write("## Budget\n\n")
            total = sum(item['amount'] for item in proposal['budget'].values())
            f.write(f"**Total Budget:** ${total:,.2f} USD\n\n")
            for item, details in proposal['budget'].items():
                f.write(f"- **{item}:** ${details['amount']:,.2f} - {details['justification']}\n")
            f.write("\n")
            
            # Timeline
            f.write("## Project Timeline\n\n")
            for phase, details in proposal['timeline'].items():
                f.write(f"- **{phase}:** {details['start_date']} to {details['end_date']} ({details['duration_days']} days)\n")
            f.write("\n")
            
            # Stakeholders
            f.write("## Key Stakeholders\n\n")
            for stakeholder in proposal['stakeholders']:
                f.write(f"- **{stakeholder['name']}:** {stakeholder['role']} ({stakeholder['contact']})\n")
            f.write("\n")
            
            # Sustainability
            f.write("## Sustainability Plan\n\n")
            f.write(f"- **Community Engagement:** {proposal['sustainability_plan']['community_engagement']}\n")
            f.write(f"- **Maintenance Strategy:** {proposal['sustainability_plan']['maintenance_strategy']}\n")
            f.write(f"- **HARDA Approach:** {proposal['sustainability_plan']['harada_approach']}\n\n")
            
            # Monitoring
            f.write("## Monitoring & Evaluation\n\n")
            f.write("**Key Indicators:**\n")
            for indicator in proposal['monitoring_evaluation']['indicators']:
                f.write(f"- {indicator}\n")
            f.write(f"\n**Reporting:** {proposal['monitoring_evaluation']['reporting']}\n")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize proposal
        proposal = ProjectProposal(
            community_name="Elayo Village",
            region="Somalia",
            population=2500
        )
        
        # Add project components
        proposal.add_component(
            "Borehole Well Construction",
            "Installation of 2 deep borehole wells with hand pumps to serve 500 households",
            "Similar projects completed in 15 Somali communities since 2018"
        )
        
        proposal.add_component(
            "Sanitation Training",
            "Community-wide hygiene education and latrine construction training",
            "Implemented in partnership with UNICEF in 2022"
        )
        
        # Set budget
        proposal.set_budget(
            "Well Drilling Equipment",
            15000.00,
            "Purchase of portable drilling rig and materials"
        )
        
        proposal.set_budget(
            "Community Training",
            5000.00,
            "Hygiene promotion materials and trainer stipends"
        )
        
        # Set timeline
        today = datetime.date.today()
        proposal.set_timeline("Assessment Phase", today, 30)
        proposal.set_timeline("Implementation", today + datetime.timedelta(days=35), 90)
        proposal.set_timeline("Evaluation", today + datetime.timedelta(days=130), 30)
        
        # Add stakeholders
        proposal.add_stakeholder(
            "Elayo Community Council",
            "Local implementation partner",
            "Chairman Ali Hassan"
        )
        
        proposal.add_stakeholder(
            "Ministry of
