"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Recommend an API or library to manage inventory for a store selling Panasonic products, including LED lights and ceiling fans, with features for tracking discounts and stock levels.
Generated: DETERMINISTIC_68c1474803984013
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

import json
from typing import List, Dict, Any

class Product:
    def __init__(self, product_id: str, name: str, stock: int, price: float, discount: float = 0.0):
        """
        Initialize a product with the given attributes.
        
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param stock: Available stock level
        :param price: Price of the product
        :param discount: Discount on the product (default is 0.0)
        """
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price
        self.discount = discount

    def apply_discount(self, percentage: float) -> None:
        """
        Apply a discount to the product.
        
        :param percentage: Discount percentage to apply (0-100)
        """
        if 0 <= percentage <= 100:
            self.discount = percentage
        else:
            raise ValueError("Discount percentage must be between 0 and 100")

    def get_final_price(self) -> float:
        """
        Calculate the final price after applying the discount.
        
        :return: Final price of the product after discount
        """
        return self.price * (1 - self.discount / 100)


class Inventory:
    def __init__(self):
        """Initialize an empty inventory."""
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the inventory.
        
        :param product: Product object to add to the inventory
        """
        self.products[product.product_id] = product

    def update_stock(self, product_id: str, quantity: int) -> None:
        """
        Update the stock level of a specified product.
        
        :param product_id: Unique identifier for the product
        :param quantity: Quantity to add or remove from stock (can be negative)
        """
        if product_id in self.products:
            self.products[product_id].stock += quantity
        else:
            raise KeyError(f"Product ID {product_id} not found in inventory")

    def get_product_info(self, product_id: str) -> Dict[str, Any]:
        """
        Retrieve information about a specific product.
        
        :param product_id: Unique identifier for the product
        :return: Dictionary containing product details
        """
        if product_id in self.products:
            product = self.products[product_id]
            return {
                "product_id": product.product_id,
                "name": product.name,
                "stock": product.stock,
                "price": product.price,
                "discount": product.discount,
                "final_price": product.get_final_price()
            }
        else:
            raise KeyError(f"Product ID {product_id} not found in inventory")

    def to_json(self) -> str:
        """
        Serialize the inventory to JSON format.
        
        :return: JSON string representation of the inventory
        """
        inventory_list = [
            {
                "product_id": product.product_id,
                "name": product.name,
                "stock": product.stock,
                "price": product.price,
                "discount": product.discount
            }
            for product in self.products.values()
        ]
        return json.dumps(inventory_list, indent=4)


if __name__ == "__main__":
    # Example usage
    inventory = Inventory()

    # Adding products to the inventory
    led_light = Product(product_id="P001", name="Panasonic LED Light", stock=100, price=29.99)
    ceiling_fan = Product(product_id="P002", name="Panasonic Ceiling Fan", stock=50, price=149.99)

    inventory.add_product(led_light)
    inventory.add_product(ceiling_fan)

    # Update stock level
    inventory.update_stock("P001", -10)  # Selling 10 LED lights
    inventory.update_stock("P002", 5)    # Receiving 5 new ceiling fans

    # Apply discounts
    led_light.apply_discount(10)  # 10% discount on LED lights

    # Output inventory information
    try:
        print(inventory.get_product_info("P001"))
        print(inventory.get_product_info("P002"))
    except KeyError as e:
        print(e)

    # Save inventory to JSON
    with open("inventory.json", "w") as f:
        f.write(inventory.to_json())
```
