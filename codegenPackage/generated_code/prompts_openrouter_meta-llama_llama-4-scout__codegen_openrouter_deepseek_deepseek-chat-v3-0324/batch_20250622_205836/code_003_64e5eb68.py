"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a basic fixed-price services menu for a legal and accounting firm, inspired by Carthew Chau & Co's approach, including services like company and trust setup, tax returns, and superannuation planning.
Generated: DETERMINISTIC_64e5eb6839e8caf4
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fixed-price services menu for a legal and accounting firm.
Inspired by Carthew Chau & Co's approach.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ServiceCategory(Enum):
    """Categories of services offered by the firm."""
    LEGAL = auto()
    ACCOUNTING = auto()
    TAX = auto()
    SUPERANNUATION = auto()

@dataclass
class Service:
    """Represents a fixed-price service offering."""
    name: str
    description: str
    price: float
    category: ServiceCategory
    estimated_time: Optional[str] = None  # e.g., "2-3 weeks"
    requirements: Optional[List[str]] = None  # Documents/info needed

class ServiceMenu:
    """Fixed-price services menu for the firm."""
    
    def __init__(self):
        self.services = self._initialize_services()
    
    def _initialize_services(self) -> List[Service]:
        """Initialize the firm's service offerings."""
        return [
            Service(
                name="Company Setup",
                description="Full company registration including ASIC forms and constitution",
                price=1500.00,
                category=ServiceCategory.LEGAL,
                estimated_time="1-2 weeks",
                requirements=["Director details", "Shareholder information", "Company name options"]
            ),
            Service(
                name="Trust Setup",
                description="Establishment of family or discretionary trust including deed preparation",
                price=2200.00,
                category=ServiceCategory.LEGAL,
                estimated_time="2-3 weeks",
                requirements=["Trustee details", "Beneficiary information", "Asset details"]
            ),
            Service(
                name="Individual Tax Return",
                description="Preparation and lodgement of individual tax return",
                price=350.00,
                category=ServiceCategory.TAX,
                estimated_time="1-2 weeks",
                requirements=["PAYG summary", "Deduction documents", "Investment income details"]
            ),
            Service(
                name="Company Tax Return",
                description="Preparation and lodgement of company tax return",
                price=1200.00,
                category=ServiceCategory.TAX,
                estimated_time="3-4 weeks",
                requirements=["Financial statements", "BAS statements", "Transaction records"]
            ),
            Service(
                name="SMSF Setup",
                description="Self-managed super fund establishment including trust deed and ATO registration",
                price=2500.00,
                category=ServiceCategory.SUPERANNUATION,
                estimated_time="3-4 weeks",
                requirements=["Trustee details", "Member information", "Investment strategy"]
            ),
            Service(
                name="SMSF Annual Compliance",
                description="Annual financial statements, tax return, and audit for SMSF",
                price=1800.00,
                category=ServiceCategory.SUPERANNUATION,
                estimated_time="4-6 weeks",
                requirements=["Bank statements", "Investment records", "Member contributions"]
            ),
            Service(
                name="Bookkeeping (Monthly)",
                description="Monthly bookkeeping services including reconciliation and reporting",
                price=500.00,
                category=ServiceCategory.ACCOUNTING,
                requirements=["Bank statements", "Invoices", "Expense receipts"]
            )
        ]
    
    def get_services_by_category(self, category: ServiceCategory) -> List[Service]:
        """Return all services in a specific category."""
        return [service for service in self.services if service.category == category]
    
    def find_service(self, name: str) -> Optional[Service]:
        """Find a service by name (case-insensitive)."""
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None
    
    def display_menu(self, category: Optional[ServiceCategory] = None) -> None:
        """Display the services menu, optionally filtered by category."""
        services_to_display = self.services if not category else self.get_services_by_category(category)
        
        print("\n=== Fixed-Price Services Menu ===")
        if category:
            print(f"Category: {category.name}\n")
        
        for service in services_to_display:
            print(f"Service: {service.name}")
            print(f"Description: {service.description}")
            print(f"Price: ${service.price:,.2f}")
            if service.estimated_time:
                print(f"Estimated Time: {service.estimated_time}")
            if service.requirements:
                print("Requirements:")
                for req in service.requirements:
                    print(f" - {req}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    menu = ServiceMenu()
    
    # Display full menu
    menu.display_menu()
    
    # Display just tax services
    # menu.display_menu(ServiceCategory.TAX)
    
    # Find a specific service
    # service = menu.find_service("Company Setup")
    # if service:
    #     print(f"\nFound service: {service.name} (${service.price:,.2f})")
```
