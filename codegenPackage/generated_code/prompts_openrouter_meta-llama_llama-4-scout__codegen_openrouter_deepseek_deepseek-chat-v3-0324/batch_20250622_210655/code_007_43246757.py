"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Generate a sample consulting services agreement that includes provisions for additional services beyond the initial scope of work."
Generated: DETERMINISTIC_432467573e51d4b6
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
Consulting Services Agreement Template Generator
This script generates a customizable consulting services agreement document.
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Party:
    """Represents a party in the agreement (Client or Consultant)"""
    name: str
    address: str
    contact_name: str
    contact_email: str
    contact_phone: str

@dataclass
class Service:
    """Represents a service to be provided"""
    description: str
    deliverables: List[str]
    estimated_hours: int
    rate: float

@dataclass
class AdditionalServiceTerms:
    """Terms for additional services beyond initial scope"""
    approval_required: bool
    rate_adjustment_clause: str
    change_order_process: str

class ConsultingAgreementGenerator:
    """Generates a consulting services agreement document"""
    
    def __init__(self, client: Party, consultant: Party, services: List[Service], 
                 additional_terms: AdditionalServiceTerms, effective_date: Optional[datetime] = None):
        self.client = client
        self.consultant = consultant
        self.services = services
        self.additional_terms = additional_terms
        self.effective_date = effective_date or datetime.now()
        
    def generate_agreement(self) -> str:
        """Generate the full agreement document"""
        try:
            doc = []
            doc.append(self._generate_header())
            doc.append(self._generate_parties_section())
            doc.append(self._generate_services_section())
            doc.append(self._generate_additional_services_section())
            doc.append(self._generate_standard_provisions())
            doc.append(self._generate_signature_block())
            return "\n\n".join(doc)
        except Exception as e:
            raise RuntimeError(f"Failed to generate agreement: {str(e)}")
    
    def _generate_header(self) -> str:
        return f"""CONSULTING SERVICES AGREEMENT
Effective Date: {self.effective_date.strftime('%B %d, %Y')}
This Agreement is made between {self.client.name} ("Client") and {self.consultant.name} ("Consultant")."""
    
    def _generate_parties_section(self) -> str:
        return f"""1. PARTIES
1.1 Client: {self.client.name}
    Address: {self.client.address}
    Contact: {self.client.contact_name}
    Email: {self.client.contact_email}
    Phone: {self.client.contact_phone}

1.2 Consultant: {self.consultant.name}
    Address: {self.consultant.address}
    Contact: {self.consultant.contact_name}
    Email: {self.consultant.contact_email}
    Phone: {self.consultant.contact_phone}"""
    
    def _generate_services_section(self) -> str:
        services_list = []
        for i, service in enumerate(self.services, start=1):
            deliverables = "\n    ".join(f"- {d}" for d in service.deliverables)
            services_list.append(f"""2.{i} Service: {service.description}
    Deliverables:
    {deliverables}
    Estimated Hours: {service.estimated_hours}
    Rate: ${service.rate:.2f}/hour""")
        
        return """2. SERVICES
Consultant agrees to provide the following services:""" + "\n\n".join(services_list)
    
    def _generate_additional_services_section(self) -> str:
        approval_text = "requires prior written approval" if self.additional_terms.approval_required else "may be requested"
        return f"""3. ADDITIONAL SERVICES
3.1 Any services beyond the initial scope {approval_text} from Client.
3.2 {self.additional_terms.rate_adjustment_clause}
3.3 Additional services will be governed by the following change order process:
    {self.additional_terms.change_order_process}"""
    
    def _generate_standard_provisions(self) -> str:
        return """4. STANDARD PROVISIONS
4.1 Term: This Agreement shall commence on the Effective Date and continue until completion of Services.
4.2 Payment: Client shall pay Consultant for services rendered within 30 days of invoice.
4.3 Confidentiality: Consultant agrees to maintain confidentiality of Client information.
4.4 Independent Contractor: Consultant is an independent contractor, not an employee.
4.5 Governing Law: This Agreement shall be governed by the laws of the state where Client is located."""
    
    def _generate_signature_block(self) -> str:
        return f"""IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date.

{self.client.name} ("Client")
By: ___________________________
Name: {self.client.contact_name}
Title: ________________________
Date: _________________________

{self.consultant.name} ("Consultant")
By: ___________________________
Name: {self.consultant.contact_name}
Title: ________________________
Date: _________________________"""

# Example usage
if __name__ == "__main__":
    try:
        client = Party(
            name="ABC Corporation",
            address="123 Main St, Anytown, USA",
            contact_name="Jane Doe",
            contact_email="jane@abccorp.com",
            contact_phone="555-123-4567"
        )
        
        consultant = Party(
            name="XYZ Consulting LLC",
            address="456 Oak Ave, Somewhere, USA",
            contact_name="John Smith",
            contact_email="john@xyzconsulting.com",
            contact_phone="555-987-6543"
        )
        
        services = [
            Service(
                description="Website Development",
                deliverables=["Home page design", "Product catalog", "Checkout system"],
                estimated_hours=120,
                rate=150.00
            ),
            Service(
                description="SEO Optimization",
                deliverables=["Keyword research", "On-page optimization", "Analytics setup"],
                estimated_hours=40,
                rate=125.00
            )
        ]
        
        additional_terms = AdditionalServiceTerms(
            approval_required=True,
            rate_adjustment_clause="Rates for additional services may be adjusted annually with 30 days notice.",
            change_order_process="Client must submit written request, Consultant will provide estimate, both parties must sign change order before work begins."
        )
        
        generator = ConsultingAgreementGenerator(client, consultant, services, additional_terms)
        agreement = generator.generate_agreement()
        print(agreement)
        
    except Exception as e:
        print(f"Error generating agreement: {e}")
```
