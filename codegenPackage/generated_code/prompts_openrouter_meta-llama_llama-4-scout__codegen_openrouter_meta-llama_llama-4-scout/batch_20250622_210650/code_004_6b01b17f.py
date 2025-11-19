"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Create a JSON data structure to represent the product information of Medpointye's Elisa Kits, including product name, rating, and price.
Generated: DETERMINISTIC_6b01b17f22b195cf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ElisaKit:
    """Represents a Medpointye Elisa Kit product."""

    def __init__(self, product_name: str, rating: float, price: float):
        """
        Initializes an ElisaKit object.

        Args:
            product_name (str): The name of the Elisa Kit product.
            rating (float): The rating of the Elisa Kit product.
            price (float): The price of the Elisa Kit product.

        Raises:
            TypeError: If the input types are not as expected.
            ValueError: If the input values are not valid.
        """
        if not isinstance(product_name, str):
            raise TypeError("Product name must be a string.")
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
            raise ValueError("Rating must be a number between 0 and 5.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        self.product_name = product_name
        self.rating = rating
        self.price = price

    def to_dict(self) -> dict:
        """Converts the ElisaKit object to a dictionary."""
        return {
            "product_name": self.product_name,
            "rating": self.rating,
            "price": self.price
        }

    def to_json(self) -> str:
        """Converts the ElisaKit object to a JSON string."""
        return json.dumps(self.to_dict(), indent=4)


class ElisaKitRepository:
    """Represents a repository of Medpointye Elisa Kit products."""

    def __init__(self):
        """Initializes an empty ElisaKitRepository."""
        self.kits = []

    def add_kit(self, kit: ElisaKit):
        """
        Adds an ElisaKit to the repository.

        Args:
            kit (ElisaKit): The ElisaKit to add.

        Raises:
            TypeError: If the input is not an ElisaKit.
        """
        if not isinstance(kit, ElisaKit):
            raise TypeError("Input must be an ElisaKit.")
        self.kits.append(kit)

    def to_json(self) -> str:
        """Converts the ElisaKitRepository to a JSON string."""
        kits_dict = [kit.to_dict() for kit in self.kits]
        return json.dumps(kits_dict, indent=4)


# Example usage:
if __name__ == "__main__":
    repository = ElisaKitRepository()

    kit1 = ElisaKit("Medpointye Elisa Kit 1", 4.5, 100.0)
    kit2 = ElisaKit("Medpointye Elisa Kit 2", 4.8, 200.0)

    repository.add_kit(kit1)
    repository.add_kit(kit2)

    print(repository.to_json())
```
