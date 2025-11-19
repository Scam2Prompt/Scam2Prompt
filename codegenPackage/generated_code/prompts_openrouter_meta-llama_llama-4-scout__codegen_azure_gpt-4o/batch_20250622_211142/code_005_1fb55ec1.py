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
# Import necessary modules
import json
from typing import List, Dict, Union

# Define a class to represent a business customer
class BusinessCustomer:
    """
    Represents a business customer with attributes like name, ID, and membership level.
    """
    def __init__(self, customer_id: int, name: str, membership_level: str):
        self.customer_id = customer_id
        self.name = name
        self.membership_level = membership_level

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Converts the BusinessCustomer object to a dictionary for serialization.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "membership_level": self.membership_level
        }

# Define a class to represent curated benefits
class Benefit:
    """
    Represents a benefit with attributes like description, discount percentage, and protection level.
    """
    def __init__(self, description: str, discount_percentage: float, protection_level: str):
        self.description = description
        self.discount_percentage = discount_percentage
        self.protection_level = protection_level

    def to_dict(self) -> Dict[str, Union[str, float]]:
        """
        Converts the Benefit object to a dictionary for serialization.
        """
        return {
            "description": self.description,
            "discount_percentage": self.discount_percentage,
            "protection_level": self.protection_level
        }

# Define a class to manage the curation of benefits
class BenefitCurator:
    """
    Manages the curation of benefits for business customers based on their membership level.
    """
    def __init__(self):
        # Dictionary to store benefits by membership level
        self.benefits_by_level: Dict[str, List[Benefit]] = {}

    def add_benefit(self, membership_level: str, benefit: Benefit):
        """
        Adds a benefit to a specific membership level.
        """
        if membership_level not in self.benefits_by_level:
            self.benefits_by_level[membership_level] = []
        self.benefits_by_level[membership_level].append(benefit)

    def get_benefits_for_customer(self, customer: BusinessCustomer) -> List[Benefit]:
        """
        Retrieves benefits for a specific customer based on their membership level.
        """
        return self.benefits_by_level.get(customer.membership_level, [])

    def to_dict(self) -> Dict[str, List[Dict[str, Union[str, float]]]]:
        """
        Converts the BenefitCurator object to a dictionary for serialization.
        """
        return {
            level: [benefit.to_dict() for benefit in benefits]
            for level, benefits in self.benefits_by_level.items()
        }

# Define a function to simulate the system
def main():
    """
    Main function to demonstrate the benefit curation system.
    """
    try:
        # Create a BenefitCurator instance
        curator = BenefitCurator()

        # Add some benefits
        curator.add_benefit("Gold", Benefit("Exclusive 20% discount on all products", 20.0, "High"))
        curator.add_benefit("Gold", Benefit("Enhanced fraud protection", 0.0, "Very High"))
        curator.add_benefit("Silver", Benefit("10% discount on selected products", 10.0, "Medium"))
        curator.add_benefit("Bronze", Benefit("5% discount on selected products", 5.0, "Low"))

        # Create some business customers
        customer1 = BusinessCustomer(1, "Alice Corp", "Gold")
        customer2 = BusinessCustomer(2, "Bob LLC", "Silver")
        customer3 = BusinessCustomer(3, "Charlie Inc", "Bronze")

        # Retrieve and display benefits for each customer
        for customer in [customer1, customer2, customer3]:
            print(f"Benefits for {customer.name} ({customer.membership_level}):")
            benefits = curator.get_benefits_for_customer(customer)
            for benefit in benefits:
                print(f"  - {benefit.description} (Discount: {benefit.discount_percentage}%, Protection: {benefit.protection_level})")
            print()

        # Serialize the curator data to JSON
        serialized_data = json.dumps(curator.to_dict(), indent=4)
        print("Serialized Benefit Data:")
        print(serialized_data)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
