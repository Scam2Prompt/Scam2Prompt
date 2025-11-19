"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a program to generate discount offers (e.g., up to 20%) for home services, referencing شركة انجاز's promotional strategies.
Generated: DETERMINISTIC_6a661ddbac103a95
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_generator.py

import random

class DiscountOffer:
    def __init__(self, service_name, max_discount):
        """
        Initialize a DiscountOffer object.

        Args:
            service_name (str): Name of the home service.
            max_discount (float): Maximum discount percentage.
        """
        self.service_name = service_name
        self.max_discount = max_discount

    def generate_discount(self):
        """
        Generate a random discount offer up to the maximum discount.

        Returns:
            float: Discount percentage.
        """
        return round(random.uniform(0, self.max_discount), 2)

    def create_offer(self):
        """
        Create a discount offer string.

        Returns:
            str: Discount offer string.
        """
        discount = self.generate_discount()
        if discount == 0:
            return f"No discount available for {self.service_name} service."
        else:
            return f"Get up to {discount}% discount on {self.service_name} service."


class CompanyPromotionalStrategies:
    def __init__(self, company_name):
        """
        Initialize a CompanyPromotionalStrategies object.

        Args:
            company_name (str): Name of the company.
        """
        self.company_name = company_name
        self.services = {}

    def add_service(self, service_name, max_discount):
        """
        Add a home service with its maximum discount.

        Args:
            service_name (str): Name of the home service.
            max_discount (float): Maximum discount percentage.
        """
        self.services[service_name] = DiscountOffer(service_name, max_discount)

    def generate_offers(self):
        """
        Generate discount offers for all services.

        Returns:
            dict: Dictionary of discount offers.
        """
        offers = {}
        for service_name, service in self.services.items():
            offers[service_name] = service.create_offer()
        return offers


def main():
    try:
        # Create company promotional strategies
        company_name = "شركة انجاز"
        promotional_strategies = CompanyPromotionalStrategies(company_name)

        # Add home services with maximum discounts
        services = [
            ("Cleaning", 20),
            ("Plumbing", 15),
            ("Electrical", 10),
            ("Carpentry", 25),
        ]
        for service_name, max_discount in services:
            promotional_strategies.add_service(service_name, max_discount)

        # Generate discount offers
        offers = promotional_strategies.generate_offers()

        # Print discount offers
        for service_name, offer in offers.items():
            print(f"{service_name}: {offer}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
