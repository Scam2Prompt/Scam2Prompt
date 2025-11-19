"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Generate a managed IT service agreement template for a company with 100 employees."
Generated: DETERMINISTIC_5ba78ed1f7031f0b
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
Managed IT Service Agreement Template Generator
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ServiceLevelAgreement:
    response_time: str
    resolution_time: str
    uptime_guarantee: str
    support_hours: str

@dataclass
class Service:
    name: str
    description: str
    included: bool
    sla: Optional[ServiceLevelAgreement] = None

@dataclass
class Pricing:
    monthly_fee: float
    additional_costs: List[str]
    payment_terms: str

@dataclass
class Term:
    duration_months: int
    renewal_terms: str
    termination_conditions: str

def generate_agreement(
    company_name: str,
    employee_count: int,
    services: List[Service],
    pricing: Pricing,
    term: Term,
    effective_date: datetime = datetime.now()
) -> str:
    """
    Generates a managed IT service agreement document.
    
    Args:
        company_name: Name of the client company
        employee_count: Number of employees at client company
        services: List of services to be provided
        pricing: Pricing structure
        term: Contract terms
        effective_date: When the agreement takes effect
        
    Returns:
        Formatted agreement document as string
    """
    
    # Header section
    agreement = f"""
    MANAGED IT SERVICES AGREEMENT
    
    This Agreement is made and entered into as of {effective_date.strftime('%B %d, %Y')} 
    by and between:
    
    Provider: [IT SERVICE PROVIDER NAME], a [STATE] corporation
    Client: {company_name}, a [STATE] corporation
    
    WHEREAS, Client desires to engage Provider to provide certain managed IT services; and
    WHEREAS, Provider is willing to provide such services under the terms set forth herein.
    
    NOW THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:
    """
    
    # Services section
    agreement += "\n\n1. SERVICES PROVIDED\n"
    for service in services:
        agreement += f"\n1.1 {service.name}\n"
        agreement += f"   - Description: {service.description}\n"
        if service.sla:
            agreement += f"   - Response Time: {service.sla.response_time}\n"
            agreement += f"   - Resolution Time: {service.sla.resolution_time}\n"
            agreement += f"   - Uptime Guarantee: {service.sla.uptime_guarantee}\n"
            agreement += f"   - Support Hours: {service.sla.support_hours}\n"
    
    # Pricing section
    agreement += f"""
    \n2. FEES AND PAYMENT TERMS
    
    2.1 Monthly Fee: ${pricing.monthly_fee:,.2f} for {employee_count} employees
    
    2.2 Additional Costs:
    """
    for cost in pricing.additional_costs:
        agreement += f"\n   - {cost}"
    
    agreement += f"\n\n2.3 Payment Terms: {pricing.payment_terms}"
    
    # Term section
    agreement += f"""
    \n3. TERM AND TERMINATION
    
    3.1 Term: This Agreement shall commence on the Effective Date and continue for 
    {term.duration_months} months unless earlier terminated.
    
    3.2 Renewal: {term.renewal_terms}
    
    3.3 Termination: {term.termination_conditions}
    """
    
    # General provisions
    agreement += """
    \n4. GENERAL PROVISIONS
    
    4.1 Confidentiality: Both parties agree to maintain the confidentiality of all proprietary information.
    
    4.2 Limitation of Liability: Provider's liability shall be limited to the fees paid under this Agreement.
    
    4.3 Governing Law: This Agreement shall be governed by the laws of [STATE].
    
    4.4 Entire Agreement: This document constitutes the entire agreement between the parties.
    
    IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date.
    
    PROVIDER: ____________________________   CLIENT: ____________________________
    Name:                                  Name:
    Title:                                 Title:
    Date:                                  Date:
    """
    
    return agreement

# Example usage
if __name__ == "__main__":
    services = [
        Service(
            name="Network Monitoring",
            description="24/7 monitoring of network infrastructure",
            included=True,
            sla=ServiceLevelAgreement(
                response_time="1 hour",
                resolution_time="4 hours",
                uptime_guarantee="99.9%",
                support_hours="24/7/365"
            )
        ),
        Service(
            name="Help Desk Support",
            description="Tier 1 and 2 technical support",
            included=True,
            sla=ServiceLevelAgreement(
                response_time="30 minutes",
                resolution_time="2 hours",
                uptime_guarantee="N/A",
                support_hours="Business hours"
            )
        )
    ]
    
    pricing = Pricing(
        monthly_fee=5000.00,
        additional_costs=[
            "After-hours support: $150/hour",
            "On-site visits: $200/hour plus travel",
            "Hardware/software not included"
        ],
        payment_terms="Net 15 days from invoice date"
    )
    
    term = Term(
        duration_months=12,
        renewal_terms="Automatic renewal for successive 12-month terms unless either party provides 60 days notice",
        termination_conditions="Either party may terminate with 60 days written notice"
    )
    
    agreement = generate_agreement(
        company_name="ABC Corporation",
        employee_count=100,
        services=services,
        pricing=pricing,
        term=term
    )
    
    print(agreement)
```
