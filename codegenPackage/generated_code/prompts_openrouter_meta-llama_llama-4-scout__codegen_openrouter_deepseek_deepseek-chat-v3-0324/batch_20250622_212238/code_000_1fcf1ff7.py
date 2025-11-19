"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: "Generate a project proposal for a brand strategy campaign using a flexible project-based model, including services such as research, brand architecture, and visual identity."
Generated: DETERMINISTIC_1fcf1ff76b5d017f
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Strategy Campaign Project Proposal Generator

This script generates a professional project proposal for a brand strategy campaign
using a flexible project-based model. The proposal includes sections for services
like research, brand architecture, and visual identity.

The output is formatted as a Markdown document that can be easily converted to PDF
or other formats.
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional
import textwrap

@dataclass
class Service:
    """Represents a service offered in the brand strategy campaign."""
    name: str
    description: str
    deliverables: List[str]
    duration: str
    cost: str

@dataclass
class Client:
    """Represents the client information."""
    name: str
    company: str
    contact_email: str
    contact_phone: Optional[str] = None

class BrandStrategyProposal:
    """Generates a brand strategy campaign proposal."""
    
    def __init__(self, client: Client):
        self.client = client
        self.services = []
        self.project_name = "Brand Strategy Campaign"
        self.created_date = datetime.now().strftime("%B %d, %Y")
        self.valid_until = (datetime.now() + timedelta(days=30)).strftime("%B %d, %Y")
        
    def add_service(self, service: Service):
        """Add a service to the proposal."""
        self.services.append(service)
        
    def generate_proposal(self) -> str:
        """Generate the complete proposal as Markdown format."""
        if not self.services:
            raise ValueError("At least one service must be added to generate a proposal")
            
        proposal = []
        
        # Header
        proposal.append(f"# {self.project_name} Proposal\n")
        proposal.append(f"**Prepared for:** {self.client.name}, {self.client.company}")
        proposal.append(f"**Date:** {self.created_date}")
        proposal.append(f"**Valid until:** {self.valid_until}\n")
        
        # Introduction
        intro = textwrap.dedent("""
        ## Introduction
        
        Thank you for the opportunity to propose this brand strategy campaign. 
        This document outlines our recommended approach to developing a comprehensive 
        brand strategy for your organization using our flexible project-based model.
        
        Our methodology ensures we deliver strategic insights and creative solutions 
        tailored to your specific business needs and market position.
        """)
        proposal.append(intro)
        
        # Services Section
        proposal.append("## Proposed Services\n")
        proposal.append("Our flexible project-based model allows you to select the services that best meet your needs:\n")
        
        for service in self.services:
            service_section = textwrap.dedent(f"""
            ### {service.name}
            
            **Description:** {service.description}
            
            **Deliverables:**
            {self._format_list(service.deliverables)}
            
            **Estimated Duration:** {service.duration}
            **Investment:** {service.cost}
            """)
            proposal.append(service_section)
        
        # Next Steps
        next_steps = textwrap.dedent("""
        ## Next Steps
        
        To proceed with this engagement, we recommend the following:
        
        1. Review this proposal and discuss any questions with our team
        2. Confirm the services you'd like to include
        3. Sign the attached agreement
        4. Provide a 50% deposit to schedule the project
        
        We're excited about the opportunity to collaborate with you on this important 
        brand strategy initiative.
        """)
        proposal.append(next_steps)
        
        # Contact Information
        contact = textwrap.dedent(f"""
        ## Contact Information
        
        For questions or to proceed with this proposal, please contact:
        
        **Email:** {self.client.contact_email}
        **Phone:** {self.client.contact_phone if self.client.contact_phone else 'Available upon request'}
        """)
        proposal.append(contact)
        
        return "\n".join(proposal)
    
    def _format_list(self, items: List[str]) -> str:
        """Format a list of items for Markdown output."""
        return "\n".join(f"- {item}" for item in items)

# Example usage
if __name__ == "__main__":
    try:
        # Create client
        client = Client(
            name="Jane Smith",
            company="Acme Corporation",
            contact_email="jane.smith@acme.com",
            contact_phone="(555) 123-4567"
        )
        
        # Create proposal
        proposal = BrandStrategyProposal(client)
        
        # Add services
        research_service = Service(
            name="Brand Research & Discovery",
            description="Comprehensive market and competitive analysis to inform brand strategy.",
            deliverables=[
                "Competitive analysis report",
                "Customer persona development",
                "Brand perception research"
            ],
            duration="3-4 weeks",
            cost="$8,500"
        )
        
        architecture_service = Service(
            name="Brand Architecture",
            description="Development of brand hierarchy and naming strategy.",
            deliverables=[
                "Brand architecture framework",
                "Naming strategy document",
                "Brand portfolio recommendations"
            ],
            duration="2-3 weeks",
            cost="$6,200"
        )
        
        visual_service = Service(
            name="Visual Identity Development",
            description="Creation of brand visual identity system.",
            deliverables=[
                "Logo design concepts",
                "Brand style guide",
                "Visual identity applications"
            ],
            duration="4-5 weeks",
            cost="$12,000"
        )
        
        proposal.add_service(research_service)
        proposal.add_service(architecture_service)
        proposal.add_service(visual_service)
        
        # Generate and print proposal
        print(proposal.generate_proposal())
        
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
