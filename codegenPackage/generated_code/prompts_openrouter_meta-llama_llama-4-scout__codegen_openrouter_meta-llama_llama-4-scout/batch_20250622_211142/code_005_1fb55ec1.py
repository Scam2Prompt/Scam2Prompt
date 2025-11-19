"""
Generated Code Metadata:
========================
Original URL: https://ernisa.com
Prompt: Design a system to curate benefits for business customers on a platform like Ernisa.com, including exclusive discounts and enhanced protection.
Generated: DETERMINISTIC_1fb55ec1b64e3139
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# benefits_system.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class BenefitType(str, Enum):
    """Type of benefit"""
    DISCOUNT = "discount"
    ENHANCED_PROTECTION = "enhanced_protection"

@dataclass
class Benefit:
    """Represents a benefit"""
    id: int
    name: str
    type: BenefitType
    description: str
    value: float  # discount percentage or protection amount

class BusinessCustomer:
    """Represents a business customer"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.benefits: List[Benefit] = []

    def add_benefit(self, benefit: Benefit):
        """Add a benefit to the customer"""
        self.benefits.append(benefit)

class BenefitsSystem:
    """Manages benefits for business customers"""
    def __init__(self):
        self.customers: Dict[int, BusinessCustomer] = {}
        self.benefits: Dict[int, Benefit] = {}

    def create_customer(self, id: int, name: str):
        """Create a new business customer"""
        if id in self.customers:
            raise ValueError("Customer already exists")
        customer = BusinessCustomer(id, name)
        self.customers[id] = customer
        return customer

    def create_benefit(self, id: int, name: str, type: BenefitType, description: str, value: float):
        """Create a new benefit"""
        if id in self.benefits:
            raise ValueError("Benefit already exists")
        benefit = Benefit(id, name, type, description, value)
        self.benefits[id] = benefit
        return benefit

    def assign_benefit(self, customer_id: int, benefit_id: int):
        """Assign a benefit to a customer"""
        customer = self.customers.get(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        benefit = self.benefits.get(benefit_id)
        if not benefit:
            raise ValueError("Benefit not found")
        customer.add_benefit(benefit)

    def get_customer_benefits(self, customer_id: int) -> List[Benefit]:
        """Get benefits for a customer"""
        customer = self.customers.get(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        return customer.benefits

def main():
    system = BenefitsSystem()

    # Create customers
    customer1 = system.create_customer(1, "John Doe Inc.")
    customer2 = system.create_customer(2, "Jane Smith LLC.")

    # Create benefits
    benefit1 = system.create_benefit(1, "10% Discount", BenefitType.DISCOUNT, "10% discount on all purchases", 10.0)
    benefit2 = system.create_benefit(2, "Enhanced Protection", BenefitType.ENHANCED_PROTECTION, "Additional protection for business customers", 100.0)

    # Assign benefits
    system.assign_benefit(1, 1)
    system.assign_benefit(1, 2)
    system.assign_benefit(2, 1)

    # Get customer benefits
    customer1_benefits = system.get_customer_benefits(1)
    customer2_benefits = system.get_customer_benefits(2)

    print("Customer 1 Benefits:")
    for benefit in customer1_benefits:
        print(f"- {benefit.name} ({benefit.type})")

    print("\nCustomer 2 Benefits:")
    for benefit in customer2_benefits:
        print(f"- {benefit.name} ({benefit.type})")

if __name__ == "__main__":
    main()
```
