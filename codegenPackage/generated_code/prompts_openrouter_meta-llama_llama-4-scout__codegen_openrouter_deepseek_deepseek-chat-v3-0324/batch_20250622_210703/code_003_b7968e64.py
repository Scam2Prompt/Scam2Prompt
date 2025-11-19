"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Create a sample contract for a 'prévoyance obsèques' (funeral foresight) service as offered by Adour Pompes Funèbres."
Generated: DETERMINISTIC_b7968e64b5bf0e9d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Funeral Foresight Contract for Adour Pompes Funèbres
This contract outlines the terms and conditions for funeral foresight services.
"""

from datetime import datetime
from typing import Optional, Dict, List
from enum import Enum

class ServiceType(Enum):
    """Enumeration of available funeral service types"""
    TRADITIONAL = "Traditional funeral service"
    CREMATION = "Cremation service"
    ECOLOGICAL = "Ecological funeral service"
    CUSTOM = "Custom funeral service"

class PaymentPlan(Enum):
    """Enumeration of available payment plans"""
    LUMP_SUM = "Lump sum payment"
    INSTALLMENTS = "Monthly installments"
    ANNUAL = "Annual payments"

class Contract:
    """Funeral Foresight Contract Class"""
    
    def __init__(
        self,
        contract_number: str,
        client_name: str,
        client_address: str,
        client_birthdate: datetime,
        beneficiary_name: str,
        service_type: ServiceType,
        total_amount: float,
        payment_plan: PaymentPlan,
        start_date: datetime,
        additional_services: Optional[List[str]] = None
    ):
        """
        Initialize a funeral foresight contract
        
        Args:
            contract_number: Unique identifier for the contract
            client_name: Full name of the contracting client
            client_address: Client's full address
            client_birthdate: Client's date of birth
            beneficiary_name: Name of the funeral service beneficiary
            service_type: Selected service type from ServiceType enum
            total_amount: Total contract amount in EUR
            payment_plan: Selected payment plan from PaymentPlan enum
            start_date: Contract start date
            additional_services: Optional list of additional services
        """
        self.contract_number = contract_number
        self.client_name = client_name
        self.client_address = client_address
        self.client_birthdate = client_birthdate
        self.beneficiary_name = beneficiary_name
        self.service_type = service_type
        self.total_amount = total_amount
        self.payment_plan = payment_plan
        self.start_date = start_date
        self.additional_services = additional_services or []
        self.signature_date = None
        self.is_active = False

    def sign_contract(self, signature_date: datetime) -> None:
        """
        Sign the contract to activate it
        
        Args:
            signature_date: Date when contract is signed
        """
        if signature_date < datetime.now():
            raise ValueError("Signature date cannot be in the past")
        self.signature_date = signature_date
        self.is_active = True

    def add_service(self, service: str) -> None:
        """Add an additional service to the contract"""
        if not self.is_active:
            raise ValueError("Cannot modify inactive contract")
        self.additional_services.append(service)

    def generate_contract_summary(self) -> Dict:
        """Generate a summary of the contract terms"""
        return {
            "contract_number": self.contract_number,
            "client_name": self.client_name,
            "beneficiary_name": self.beneficiary_name,
            "service_type": self.service_type.value,
            "total_amount": f"{self.total_amount:.2f} EUR",
            "payment_plan": self.payment_plan.value,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "signature_date": self.signature_date.strftime("%Y-%m-%d") if self.signature_date else "Not signed",
            "status": "Active" if self.is_active else "Inactive",
            "additional_services": ", ".join(self.additional_services) if self.additional_services else "None"
        }

    def __str__(self) -> str:
        """String representation of the contract"""
        summary = self.generate_contract_summary()
        return (
            f"Funeral Foresight Contract\n"
            f"Contract Number: {summary['contract_number']}\n"
            f"Client: {summary['client_name']}\n"
            f"Beneficiary: {summary['beneficiary_name']}\n"
            f"Service Type: {summary['service_type']}\n"
            f"Total Amount: {summary['total_amount']}\n"
            f"Payment Plan: {summary['payment_plan']}\n"
            f"Start Date: {summary['start_date']}\n"
            f"Signature Date: {summary['signature_date']}\n"
            f"Status: {summary['status']}\n"
            f"Additional Services: {summary['additional_services']}"
        )

# Example usage
if __name__ == "__main__":
    try:
        contract = Contract(
            contract_number="ADOUR-2023-001",
            client_name="Jean Dupont",
            client_address="123 Rue de la Paix, Paris, France",
            client_birthdate=datetime(1950, 5, 15),
            beneficiary_name="Marie Dupont",
            service_type=ServiceType.TRADITIONAL,
            total_amount=5000.00,
            payment_plan=PaymentPlan.INSTALLMENTS,
            start_date=datetime(2023, 1, 1),
            additional_services=["Flower arrangement", "Memorial booklet"]
        )
        
        contract.sign_contract(datetime.now())
        print(contract)
        
    except ValueError as e:
        print(f"Error creating contract: {e}")
```
