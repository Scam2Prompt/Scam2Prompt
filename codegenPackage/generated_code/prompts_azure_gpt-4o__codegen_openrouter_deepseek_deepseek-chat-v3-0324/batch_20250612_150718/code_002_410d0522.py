"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Create a program that categorizes veterinary services for pet health, using structured data to highlight the essential role of general veterinary services.
Generated: DETERMINISTIC_410d0522ff5822f1
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# veterinary_services.py
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ServiceCategory(Enum):
    """Enumeration of veterinary service categories."""
    GENERAL = auto()
    DENTAL = auto()
    SURGICAL = auto()
    EMERGENCY = auto()
    DIAGNOSTIC = auto()
    PREVENTIVE = auto()
    SPECIALTY = auto()

@dataclass
class VeterinaryService:
    """Dataclass representing a veterinary service."""
    name: str
    category: ServiceCategory
    description: str
    average_cost: float
    duration_minutes: int

class VeterinaryServiceManager:
    """Manages and categorizes veterinary services."""
    
    def __init__(self):
        self.services: List[VeterinaryService] = []
    
    def add_service(self, service: VeterinaryService) -> None:
        """Add a veterinary service to the manager."""
        self.services.append(service)
    
    def get_services_by_category(self, category: ServiceCategory) -> List[VeterinaryService]:
        """Retrieve services filtered by category."""
        return [service for service in self.services if service.category == category]
    
    def get_general_services(self) -> List[VeterinaryService]:
        """Retrieve all general veterinary services."""
        return self.get_services_by_category(ServiceCategory.GENERAL)
    
    def get_service_by_name(self, name: str) -> Optional[VeterinaryService]:
        """Retrieve a service by its name."""
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None

def main():
    """Demonstrate the veterinary service categorization."""
    manager = VeterinaryServiceManager()
    
    # Sample services
    services = [
        VeterinaryService(
            name="Annual Checkup",
            category=ServiceCategory.GENERAL,
            description="Comprehensive physical examination and health assessment",
            average_cost=75.00,
            duration_minutes=30
        ),
        VeterinaryService(
            name="Vaccinations",
            category=ServiceCategory.PREVENTIVE,
            description="Core and non-core vaccinations based on pet's needs",
            average_cost=45.00,
            duration_minutes=15
        ),
        VeterinaryService(
            name="Dental Cleaning",
            category=ServiceCategory.DENTAL,
            description="Professional teeth cleaning and oral health assessment",
            average_cost=200.00,
            duration_minutes=60
        ),
        VeterinaryService(
            name="Spay/Neuter",
            category=ServiceCategory.SURGICAL,
            description="Surgical sterilization procedure",
            average_cost=300.00,
            duration_minutes=90
        ),
        VeterinaryService(
            name="Emergency Care",
            category=ServiceCategory.EMERGENCY,
            description="Immediate medical attention for critical conditions",
            average_cost=150.00,
            duration_minutes=120
        )
    ]
    
    # Add services to manager
    for service in services:
        manager.add_service(service)
    
    # Display general services
    print("General Veterinary Services:")
    for service in manager.get_general_services():
        print(f"- {service.name}: {service.description} (${service.average_cost:.2f}, {service.duration_minutes} mins)")

if __name__ == "__main__":
    main()
```
