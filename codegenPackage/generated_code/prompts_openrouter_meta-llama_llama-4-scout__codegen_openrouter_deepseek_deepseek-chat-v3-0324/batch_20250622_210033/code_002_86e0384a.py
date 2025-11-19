"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: Write a service agreement for a residential cleaning service that includes details on frequency of visits, duties, and payment terms.
Generated: DETERMINISTIC_86e0384a8e1211d9
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Residential Cleaning Service Agreement Generator
This script generates a customizable service agreement for residential cleaning services.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CleaningServiceAgreement:
    """
    A class to generate residential cleaning service agreements.
    """
    
    def __init__(self, client_name: str, service_address: str, start_date: str):
        """
        Initialize the agreement with client details.
        
        Args:
            client_name (str): Full name of the client
            service_address (str): Address where services will be performed
            start_date (str): Start date of service in YYYY-MM-DD format
        """
        self.client_name = client_name
        self.service_address = service_address
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.services: List[str] = []
        self.frequency: str = ""
        self.payment_terms: Dict[str, str] = {}
        self.additional_terms: List[str] = []
        
    def add_service(self, service: str) -> None:
        """
        Add a cleaning service to the agreement.
        
        Args:
            service (str): Description of the cleaning service
        """
        self.services.append(service)
    
    def set_frequency(self, frequency: str) -> None:
        """
        Set the frequency of cleaning visits.
        
        Args:
            frequency (str): Frequency description (e.g., "Weekly", "Bi-weekly")
        """
        self.frequency = frequency
    
    def set_payment_terms(self, amount: str, due_date: str, method: str) -> None:
        """
        Define payment terms for the service.
        
        Args:
            amount (str): Payment amount
            due_date (str): Payment due date description
            method (str): Payment method
        """
        self.payment_terms = {
            'amount': amount,
            'due_date': due_date,
            'method': method
        }
    
    def add_additional_term(self, term: str) -> None:
        """
        Add additional terms or conditions to the agreement.
        
        Args:
            term (str): Additional term description
        """
        self.additional_terms.append(term)
    
    def generate_agreement(self) -> str:
        """
        Generate the complete service agreement document.
        
        Returns:
            str: Formatted service agreement text
        """
        if not self.services:
            raise ValueError("At least one service must be specified")
        if not self.frequency:
            raise ValueError("Service frequency must be specified")
        if not self.payment_terms:
            raise ValueError("Payment terms must be specified")
        
        agreement = f"""
        RESIDENTIAL CLEANING SERVICE AGREEMENT
        
        This Agreement is made effective as of {self.start_date.strftime('%B %d, %Y')}, 
        between {self.client_name} ("Client") and [Your Company Name] ("Service Provider").
        
        1. SERVICE DETAILS
        Address: {self.service_address}
        Frequency: {self.frequency}
        Services to be performed:
        """
        
        for i, service in enumerate(self.services, 1):
            agreement += f"{i}. {service}\n"
        
        agreement += f"""
        2. PAYMENT TERMS
        Amount: ${self.payment_terms['amount']}
        Due: {self.payment_terms['due_date']}
        Method: {self.payment_terms['method']}
        
        3. ADDITIONAL TERMS
        """
        
        if self.additional_terms:
            for i, term in enumerate(self.additional_terms, 1):
                agreement += f"{i}. {term}\n"
        else:
            agreement += "None specified\n"
        
        agreement += f"""
        4. GENERAL PROVISIONS
        - Either party may terminate this agreement with 14 days written notice
        - Client must provide access to the premises at scheduled times
        - Service provider will supply all cleaning equipment and supplies
        - Client must disclose any special requirements or hazards
        
        Client Signature: ___________________________ Date: ___________
        Service Provider Signature: __________________ Date: ___________
        """
        
        return agreement

# Example usage
if __name__ == "__main__":
    try:
        agreement = CleaningServiceAgreement(
            client_name="John Doe",
            service_address="123 Main St, Anytown, USA",
            start_date="2023-11-01"
        )
        
        agreement.add_service("General cleaning of all rooms")
        agreement.add_service("Vacuuming and mopping floors")
        agreement.add_service("Bathroom sanitization")
        agreement.add_service("Dusting of all surfaces")
        
        agreement.set_frequency("Bi-weekly (every 2 weeks)")
        
        agreement.set_payment_terms(
            amount="150.00",
            due_date="On the day of service",
            method="Credit card or cash"
        )
        
        agreement.add_additional_term("Client will provide parking for service vehicle")
        agreement.add_additional_term("Special requests must be made 48 hours in advance")
        
        print(agreement.generate_agreement())
    except Exception as e:
        print(f"Error generating agreement: {str(e)}")
```
