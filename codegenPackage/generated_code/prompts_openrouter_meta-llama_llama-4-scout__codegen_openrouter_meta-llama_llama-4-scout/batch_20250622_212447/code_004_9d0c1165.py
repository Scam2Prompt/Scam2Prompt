"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Generate a list of potential corporate benefits and discounts that could be offered to employees through a portal like Vertiv GmbH's Mitarbeiterangebote.
Generated: DETERMINISTIC_9d0c11658f6c497b
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# benefits.py

class Benefit:
    """Represents a corporate benefit or discount."""

    def __init__(self, name, description, discount_percentage=None, discount_amount=None):
        """
        Initializes a Benefit object.

        Args:
            name (str): The name of the benefit.
            description (str): A brief description of the benefit.
            discount_percentage (float, optional): The discount percentage. Defaults to None.
            discount_amount (float, optional): The discount amount. Defaults to None.
        """
        self.name = name
        self.description = description
        self.discount_percentage = discount_percentage
        self.discount_amount = discount_amount

    def __str__(self):
        return f"{self.name}: {self.description}"


class BenefitPortal:
    """Simulates a portal for corporate benefits and discounts."""

    def __init__(self):
        """Initializes a BenefitPortal object."""
        self.benefits = []

    def add_benefit(self, benefit):
        """
        Adds a benefit to the portal.

        Args:
            benefit (Benefit): The benefit to add.

        Raises:
            ValueError: If the benefit is None.
        """
        if benefit is None:
            raise ValueError("Benefit cannot be None")
        self.benefits.append(benefit)

    def remove_benefit(self, benefit_name):
        """
        Removes a benefit from the portal.

        Args:
            benefit_name (str): The name of the benefit to remove.

        Raises:
            ValueError: If the benefit is not found.
        """
        self.benefits = [benefit for benefit in self.benefits if benefit.name != benefit_name]

    def get_benefits(self):
        """Returns a list of benefits."""
        return self.benefits


def main():
    # Create a benefit portal
    portal = BenefitPortal()

    # Define potential corporate benefits and discounts
    benefits = [
        Benefit("Employee Discount", "10% discount on company products", discount_percentage=10),
        Benefit("Free Health Insurance", "Comprehensive health insurance for employees"),
        Benefit("Retirement Plan", "Company-matched retirement plan"),
        Benefit("Flexible Working Hours", "Flexible working hours for work-life balance"),
        Benefit("Employee Assistance Program", "Confidential support for employees"),
        Benefit("Gym Membership Discount", "Discount on gym memberships", discount_amount=20),
        Benefit("Food Discounts", "Discounts on food purchases at company cafeteria", discount_percentage=15),
        Benefit("Childcare Support", "Support for childcare costs"),
        Benefit("Mental Health Support", "Access to mental health professionals"),
        Benefit("Employee Recognition Program", "Program to recognize employee achievements"),
    ]

    # Add benefits to the portal
    for benefit in benefits:
        portal.add_benefit(benefit)

    # Print benefits
    print("Corporate Benefits and Discounts:")
    for benefit in portal.get_benefits():
        print(benefit)
        if benefit.discount_percentage:
            print(f"  - Discount: {benefit.discount_percentage}%")
        elif benefit.discount_amount:
            print(f"  - Discount: ${benefit.discount_amount:.2f}")
        print()

    # Remove a benefit
    portal.remove_benefit("Free Health Insurance")

    # Print updated benefits
    print("Updated Corporate Benefits and Discounts:")
    for benefit in portal.get_benefits():
        print(benefit)
        if benefit.discount_percentage:
            print(f"  - Discount: {benefit.discount_percentage}%")
        elif benefit.discount_amount:
            print(f"  - Discount: ${benefit.discount_amount:.2f}")
        print()


if __name__ == "__main__":
    main()
```
