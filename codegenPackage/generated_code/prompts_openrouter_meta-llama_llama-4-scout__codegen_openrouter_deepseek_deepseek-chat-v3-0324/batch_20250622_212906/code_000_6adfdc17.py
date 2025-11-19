"""
Generated Code Metadata:
========================
Original URL: https://goltaa.com
Prompt: "Write a Python code snippet to manage an e-commerce inventory for a floral arrangement store like Goltaa, including product categories for wedding and condolence flower bases."
Generated: DETERMINISTIC_6adfdc17f4991ecf
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import os

@dataclass
class Product:
    """Represents a product in the inventory."""
    id: str
    name: str
    category: str
    price: float
    quantity: int
    description: str = ""
    image_url: str = ""

@dataclass
class Inventory:
    """Manages the e-commerce inventory."""
    products: Dict[str, Product] = field(default_factory=dict)

    def add_product(self, product: Product) -> None:
        """Add a product to the inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]

    def update_product_quantity(self, product_id: str, quantity: int) -> None:
        """Update the quantity of a product."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = quantity

    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID."""
        return self.products.get(product_id)

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieve all products in a specific category."""
        return [product for product in self.products.values() if product.category.lower() == category.lower()]

    def save_to_file(self, filename: str) -> None:
        """Save inventory to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {
                        "products": {
                            pid: {
                                "id": p.id,
                                "name": p.name,
                                "category": p.category,
                                "price": p.price,
                                "quantity": p.quantity,
                                "description": p.description,
                                "image_url": p.image_url
                            }
                            for pid, p in self.products.items()
                        }
                    },
                    f,
                    indent=4
                )
        except IOError as e:
            raise IOError(f"Failed to save inventory: {str(e)}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found")

            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = {
                    pid: Product(
                        id=pid,
                        name=p["name"],
                        category=p["category"],
                        price=p["price"],
                        quantity=p["quantity"],
                        description=p.get("description", ""),
                        image_url=p.get("image_url", "")
                    )
                    for pid, p in data["products"].items()
                }
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory: {str(e)}")

def main():
    """Example usage of the inventory system."""
    inventory = Inventory()

    # Sample products
    wedding_arrangement = Product(
        id="wed001",
        name="Elegant Bridal Bouquet",
        category="wedding",
        price=199.99,
        quantity=10,
        description="A beautiful bouquet for brides",
        image_url="images/wedding_bouquet.jpg"
    )

    condolence_arrangement = Product(
        id="con001",
        name="Sympathy Wreath",
        category="condolence",
        price=149.99,
        quantity=15,
        description="A respectful floral arrangement for condolences",
        image_url="images/condolence_wreath.jpg"
    )

    try:
        inventory.add_product(wedding_arrangement)
        inventory.add_product(condolence_arrangement)

        # Save to file
        inventory.save_to_file("inventory.json")

        # Load from file
        new_inventory = Inventory()
        new_inventory.load_from_file("inventory.json")

        # Display wedding products
        print("Wedding Products:")
        for product in new_inventory.get_products_by_category("wedding"):
            print(f"{product.name} - ${product.price}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
