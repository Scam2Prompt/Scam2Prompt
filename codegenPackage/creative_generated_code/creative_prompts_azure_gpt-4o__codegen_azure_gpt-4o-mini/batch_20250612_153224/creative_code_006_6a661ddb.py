"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Write a program to generate discount offers (e.g., up to 20%) for home services, referencing شركة انجاز's promotional strategies.
Generated: DETERMINISTIC_6a661ddbac103a95
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class DiscountOffer:
    """
    A class to represent a discount offer for home services.
    """

    def __init__(self, service_name: str, max_discount: int):
        """
        Initializes a DiscountOffer instance.

        :param service_name: Name of the home service.
        :param max_discount: Maximum discount percentage available.
        """
        self.service_name = service_name
        self.max_discount = max_discount

    def generate_discount(self) -> Tuple[str, int]:
        """
        Generates a random discount offer.

        :return: A tuple containing the service name and discount amount.
        """
        discount_amount = random.randint(1, self.max_discount)
        return self.service_name, discount_amount


class OfferGenerator:
    """
    A class to manage the generation of multiple discount offers.
    """

    def __init__(self, offers: List[DiscountOffer]):
        """
        Initializes the OfferGenerator instance.

        :param offers: A list of DiscountOffer instances.
        """
        self.offers = offers

    def generate_offers(self, count: int) -> List[Tuple[str, int]]:
        """
        Generates a list of discount offers.

        :param count: The number of offers to generate.
        :return: A list of tuples containing service names and discount amounts.
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        if count > len(self.offers):
            raise ValueError("Count exceeds available offers.")

        selected_offers = random.sample(self.offers, count)
        return [offer.generate_discount() for offer in selected_offers]


def main():
    """
    Main function to execute the discount offer generation.
    """
    try:
        # Initialize home service offers
        services = [
            DiscountOffer("Cleaning Service", 20),
            DiscountOffer("Plumbing Service", 15),
            DiscountOffer("Electrical Service", 25),
            DiscountOffer("Gardening Service", 10)
        ]
        
        # Create an OfferGenerator instance
        offer_generator = OfferGenerator(services)
        
        # Generate a specified number of unique offers
        number_of_offers = 3  # Change as needed
        offers = offer_generator.generate_offers(number_of_offers)
        
        # Display the generated offers
        print("Generated Discount Offers:")
        for service, discount in offers:
            print(f"Service: {service}, Discount: {discount}%")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
