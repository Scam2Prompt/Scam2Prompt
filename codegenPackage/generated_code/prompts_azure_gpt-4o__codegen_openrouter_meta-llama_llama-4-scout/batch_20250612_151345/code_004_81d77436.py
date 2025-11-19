"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Suggest tools or frameworks for designing and testing high-conversion promotional offers, similar to the holiday combo kit example from J. Sebastião's portfolio.
Generated: DETERMINISTIC_81d774362aa7b19d
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_offers.py

import itertools
from typing import List, Dict

class PromotionalOffer:
    """Represents a promotional offer with a name and a discount."""

    def __init__(self, name: str, discount: float):
        """
        Initializes a PromotionalOffer.

        Args:
        - name (str): The name of the promotional offer.
        - discount (float): The discount percentage of the promotional offer.
        """
        self.name = name
        self.discount = discount

class Product:
    """Represents a product with a name and a price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a Product.

        Args:
        - name (str): The name of the product.
        - price (float): The price of the product.
        """
        self.name = name
        self.price = price

class OfferDesigner:
    """Designs and tests promotional offers."""

    def __init__(self, products: List[Product]):
        """
        Initializes an OfferDesigner.

        Args:
        - products (List[Product]): The list of available products.
        """
        self.products = products

    def generate_combos(self, num_products: int) -> List[List[Product]]:
        """
        Generates all possible combinations of products.

        Args:
        - num_products (int): The number of products in each combination.

        Returns:
        - List[List[Product]]: A list of all possible combinations of products.
        """
        return list(itertools.combinations(self.products, num_products))

    def calculate_total(self, products: List[Product]) -> float:
        """
        Calculates the total price of a list of products.

        Args:
        - products (List[Product]): The list of products.

        Returns:
        - float: The total price of the products.
        """
        return sum(product.price for product in products)

    def apply_discount(self, total: float, discount: float) -> float:
        """
        Applies a discount to a total price.

        Args:
        - total (float): The total price.
        - discount (float): The discount percentage.

        Returns:
        - float: The total price with the discount applied.
        """
        return total * (1 - discount / 100)

    def design_offer(self, combo: List[Product], discount: float) -> Dict:
        """
        Designs a promotional offer.

        Args:
        - combo (List[Product]): The combination of products.
        - discount (float): The discount percentage.

        Returns:
        - Dict: A dictionary containing the promotional offer details.
        """
        total = self.calculate_total(combo)
        discounted_total = self.apply_discount(total, discount)
        return {
            "products": [product.name for product in combo],
            "original_price": total,
            "discount": discount,
            "discounted_price": discounted_total,
        }

def main():
    # Define products
    products = [
        Product("Product A", 100),
        Product("Product B", 200),
        Product("Product C", 300),
    ]

    # Create an OfferDesigner
    designer = OfferDesigner(products)

    # Generate all possible combinations of 2 products
    combos = designer.generate_combos(2)

    # Design a promotional offer for each combination
    offers = []
    for combo in combos:
        offer = designer.design_offer(combo, 20)  # 20% discount
        offers.append(offer)

    # Print the promotional offers
    for i, offer in enumerate(offers):
        print(f"Offer {i+1}:")
        print(f"Products: {offer['products']}")
        print(f"Original Price: ${offer['original_price']:.2f}")
        print(f"Discount: {offer['discount']}%")
        print(f"Discounted Price: ${offer['discounted_price']:.2f}")
        print()

if __name__ == "__main__":
    main()
```
