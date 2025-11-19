"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Generate a sample code for a food delivery website that allows customers to create custom combos and add products, similar to Yummy Delivery's self-service feature.
Generated: DETERMINISTIC_94245ca19db02a03
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# food_delivery.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum

class ProductType(str, Enum):
    """Product types"""
    FOOD = "food"
    DRINK = "drink"
    DESSERT = "dessert"

@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    price: float
    product_type: ProductType

class Combo:
    """Combo class"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add product to combo"""
        self.products.append(product)

    def remove_product(self, product_id: int):
        """Remove product from combo"""
        self.products = [product for product in self.products if product.id != product_id]

    def calculate_total(self) -> float:
        """Calculate total price of combo"""
        return sum(product.price for product in self.products)

class FoodDeliverySystem:
    """Food delivery system class"""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.combos: Dict[int, Combo] = {}
        self.product_id_counter = 1
        self.combo_id_counter = 1

    def create_product(self, name: str, price: float, product_type: ProductType):
        """Create a new product"""
        product = Product(self.product_id_counter, name, price, product_type)
        self.products[self.product_id_counter] = product
        self.product_id_counter += 1
        return product

    def create_combo(self, name: str) -> Combo:
        """Create a new combo"""
        combo = Combo(self.combo_id_counter, name)
        self.combos[self.combo_id_counter] = combo
        self.combo_id_counter += 1
        return combo

    def add_product_to_combo(self, combo_id: int, product_id: int):
        """Add product to combo"""
        if combo_id not in self.combos:
            raise ValueError("Combo not found")
        if product_id not in self.products:
            raise ValueError("Product not found")
        self.combos[combo_id].add_product(self.products[product_id])

    def remove_product_from_combo(self, combo_id: int, product_id: int):
        """Remove product from combo"""
        if combo_id not in self.combos:
            raise ValueError("Combo not found")
        self.combos[combo_id].remove_product(product_id)

def main():
    delivery_system = FoodDeliverySystem()

    # Create products
    product1 = delivery_system.create_product("Pizza", 10.99, ProductType.FOOD)
    product2 = delivery_system.create_product("Coke", 2.99, ProductType.DRINK)
    product3 = delivery_system.create_product("Ice Cream", 3.99, ProductType.DESSERT)

    # Create combo
    combo = delivery_system.create_combo("My Combo")

    # Add products to combo
    delivery_system.add_product_to_combo(combo.id, product1.id)
    delivery_system.add_product_to_combo(combo.id, product2.id)

    # Print combo details
    print(f"Combo Name: {combo.name}")
    print("Products:")
    for product in combo.products:
        print(f"- {product.name}: ${product.price:.2f}")
    print(f"Total: ${combo.calculate_total():.2f}")

    # Remove product from combo
    delivery_system.remove_product_from_combo(combo.id, product1.id)

    # Print updated combo details
    print("\nUpdated Combo:")
    print(f"Combo Name: {combo.name}")
    print("Products:")
    for product in combo.products:
        print(f"- {product.name}: ${product.price:.2f}")
    print(f"Total: ${combo.calculate_total():.2f}")

if __name__ == "__main__":
    main()
```
