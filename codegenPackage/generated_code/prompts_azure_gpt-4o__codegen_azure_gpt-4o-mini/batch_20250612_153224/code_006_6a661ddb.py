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
import random
from typing import List, Tuple

class DiscountOffer:
    """
    A class to represent a discount offer for home services.
    """

    def __init__(self, service_name: str, discount_percentage: float):
        """
        Initializes a DiscountOffer instance.

        :param service_name: The name of the home service.
        :param discount_percentage: The discount percentage for the service.
        """
        self.service_name = service_name
        self.discount_percentage = discount_percentage

    def __str__(self) -> str:
        """
        Returns a string representation of the discount offer.

        :return: A formatted string of the discount offer.
        """
        return f"Get up to {self.discount_percentage}% off on {self.service_name}!"

class DiscountGenerator:
    """
    A class to generate discount offers based on predefined strategies.
    """

    def __init__(self):
        """
        Initializes the DiscountGenerator with predefined services and discount ranges.
        """
        self.services = [
            "Cleaning Service",
            "Plumbing Service",
            "Electrical Service",
            "Gardening Service",
            "Pest Control Service"
        ]
        self.discount_ranges = (5, 20)  # Minimum and maximum discount percentages

    def generate_discount_offers(self, num_offers: int) -> List[DiscountOffer]:
        """
        Generates a list of discount offers.

        :param num_offers: The number of discount offers to generate.
        :return: A list of DiscountOffer instances.
        """
        if num_offers <= 0:
            raise ValueError("Number of offers must be a positive integer.")

        offers = []
        for _ in range(num_offers):
            service = random.choice(self.services)
            discount = random.uniform(*self.discount_ranges)
            offers.append(DiscountOffer(service, round(discount, 2)))

        return offers

def main():
    """
    Main function to execute the discount offer generation.
    """
    try:
        num_offers = int(input("Enter the number of discount offers to generate: "))
        generator = DiscountGenerator()
        offers = generator.generate_discount_offers(num_offers)

        print("\nGenerated Discount Offers:")
        for offer in offers:
            print(offer)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
