"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Develop a sample contract for infrastructure design and construction services between Unison Plus and a client, including terms for maintenance and support."
Generated: DETERMINISTIC_2f419b46a2f56174
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
Infrastructure Design and Construction Services Contract

This contract outlines the terms between Unison Plus (Service Provider) and a Client
for infrastructure design, construction, and maintenance services.
"""

from datetime import datetime
from typing import Optional, Dict, List
from enum import Enum

class ServiceType(Enum):
    DESIGN = "Design Services"
    CONSTRUCTION = "Construction Services"
    MAINTENANCE = "Maintenance and Support"

class PaymentTerm(Enum):
    FIXED_PRICE = "Fixed Price"
    TIME_MATERIALS = "Time and Materials"

class ContractStatus(Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    TERMINATED = "Terminated"

class Contract:
    """
    Infrastructure Design and Construction Services Contract between Unison Plus and Client.
    """
    
    def __init__(
        self,
        client_name: str,
        project_name: str,
        start_date: datetime,
        end_date: datetime,
        services: List[ServiceType],
        payment_terms: PaymentTerm,
        total_value: float,
        maintenance_period_months: int = 12
    ):
        """
        Initialize the contract with essential terms.
        
        Args:
            client_name: Name of the client
            project_name: Name of the project
            start_date: Contract start date
            end_date: Contract end date
            services: List of services to be provided
            payment_terms: Payment terms (Fixed Price or Time and Materials)
            total_value: Total contract value
            maintenance_period_months: Duration of maintenance period in months (default: 12)
        """
        self.client_name = client_name
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.services = services
        self.payment_terms = payment_terms
        self.total_value = total_value
        self.maintenance_period_months = maintenance_period_months
        self.status = ContractStatus.DRAFT
        self.terms_and_conditions = self._generate_default_terms()
        self.signatures = {}
        
    def _generate_default_terms(self) -> Dict:
        """Generate default terms and conditions for the contract."""
        return {
            "confidentiality": "Both parties agree to maintain confidentiality of project details.",
            "intellectual_property": "All designs and IP created remain property of Unison Plus.",
            "change_orders": "Changes require written approval from both parties.",
            "warranty": "12-month warranty on all construction work.",
            "liability": "Unison Plus liability limited to contract value.",
            "termination": "Either party may terminate with 30 days written notice.",
            "governing_law": "Contract governed by laws of the state of Delaware."
        }
    
    def add_custom_term(self, term_name: str, term_description: str) -> None:
        """Add a custom term to the contract."""
        self.terms_and_conditions[term_name] = term_description
    
    def sign(self, signatory_name: str, signatory_title: str, signature_date: datetime) -> None:
        """Record a signature on the contract."""
        if self.status != ContractStatus.DRAFT:
            raise ValueError("Contract must be in Draft status to be signed.")
            
        self.signatures[signatory_name] = {
            "title": signatory_title,
            "date": signature_date
        }
        
        if len(self.signatures) >= 2:  # Assuming both parties have signed
            self.status = ContractStatus.ACTIVE
    
    def complete_contract(self, completion_date: datetime) -> None:
        """Mark the contract as completed."""
        if self.status != ContractStatus.ACTIVE:
            raise ValueError("Contract must be Active to be completed.")
            
        self.end_date = completion_date
        self.status = ContractStatus.COMPLETED
    
    def terminate_contract(self, termination_date: datetime, reason: str) -> None:
        """Terminate the contract before completion."""
        self.end_date = termination_date
        self.status = ContractStatus.TERMINATED
        self.terms_and_conditions["termination_reason"] = reason
    
    def extend_maintenance(self, additional_months: int) -> None:
        """Extend the maintenance period."""
        if self.status != ContractStatus.COMPLETED:
            raise ValueError("Contract must be completed to extend maintenance.")
            
        self.maintenance_period_months += additional_months
    
    def get_contract_summary(self) -> Dict:
        """Return a summary of the contract terms."""
        return {
            "client_name": self.client_name,
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "services": [service.value for service in self.services],
            "payment_terms": self.payment_terms.value,
            "total_value": self.total_value,
            "maintenance_period": f"{self.maintenance_period_months} months",
            "status": self.status.value,
            "signatures": len(self.signatures)
        }

# Example usage
if __name__ == "__main__":
    # Create a sample contract
    contract = Contract(
        client_name="ABC Development Corp",
        project_name="Greenfield Industrial Park",
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2024, 6, 30),
        services=[ServiceType.DESIGN, ServiceType.CONSTRUCTION, ServiceType.MAINTENANCE],
        payment_terms=PaymentTerm.FIXED_PRICE,
        total_value=2500000.00,
        maintenance_period_months=18
    )
    
    # Add custom terms
    contract.add_custom_term(
        "force_majeure", 
        "Neither party liable for delays due to events beyond reasonable control."
    )
    
    # Sign the contract
    contract.sign("John Smith", "CEO", datetime(2023, 1, 1))
    contract.sign("Jane Doe", "Director of Operations", datetime(2023, 1, 2))
    
    # Print contract summary
    print(contract.get_contract_summary())
```
