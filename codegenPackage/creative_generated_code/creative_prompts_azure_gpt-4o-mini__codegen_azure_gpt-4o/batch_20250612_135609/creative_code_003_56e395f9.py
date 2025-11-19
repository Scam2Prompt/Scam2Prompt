"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://michelledoylegoldsmith.com
Prompt: Develop a shopping cart feature for a website specializing in custom jewelry, ensuring it includes options for ethically sourced gemstones and recycled gold.
Generated: DETERMINISTIC_56e395f94d47cc05
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Product:
    """
    Represents a product in the shopping cart.
    """
    def __init__(self, product_id: int, name: str, price: float, attributes: Dict[str, str]):
        """
        Initialize a product object.
        
        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param price: Price of the product.
        :param attributes: Additional attributes (e.g., ethically sourced gemstone, recycled gold).
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.attributes = attributes


class ShoppingCart:
    """
    Represents a shopping cart, allowing users to add and remove products and calculate total cost.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []  # List to store products added to the cart

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """
        Add a product to the shopping cart.
        
        :param product: Product to add to the cart.
        :param quantity: Quantity of the product to add (default is 1).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product_id: int) -> None:
        """
        Remove a product from the shopping cart by its ID.
        
        :param product_id: ID of the product to remove.
        """
        self.items = [item for item in self.items if item["product"].product_id != product_id]

    def calculate_total(self) -> float:
        """
        Calculate the total cost of the shopping cart.
        
        :return: Total cost of products in the cart.
        """
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def list_cart_items(self) -> List[Dict[str, str]]:
        """
        List all items in the shopping cart with their details.
        
        :return: List of items in the cart.
        """
        return [
            {
                "product_id": item["product"].product_id,
                "name": item["product"].name,
                "price": item["product"].price,
                "quantity": item["quantity"],
                "attributes": item["product"].attributes
            }
            for item in self.items
        ]

# Example usage
if __name__ == "__main__":
    try:
        # Create sample products
        recycled_gold_ring = Product(
            product_id=1,
            name="Recycled Gold Ring",
            price=300.0,
            attributes={"material": "Recycled Gold"}
        )
        ethically_sourced_gemstone_necklace = Product(
            product_id=2,
            name="Ethically Sourced Gemstone Necklace",
            price=450.0,
            attributes={"gemstone_origin": "Ethically Sourced"}
        )

        # Create a shopping cart instance
        cart = ShoppingCart()
        
        # Add products to the cart
        cart.add_product(recycled_gold_ring, quantity=2)
        cart.add_product(ethically_sourced_gemstone_necklace, quantity=1)

        # List items in the cart
        print("Shopping Cart Items:")
        print(cart.list_cart_items())

        # Calculate the total cost
        print("\nTotal Cost:")
        print(f"${cart.calculate_total():.2f}")

        # Remove a product from the cart
        cart.remove_product(product_id=1)

        # List items after removal
        print("\nShopping Cart Items (After Removal):")
        print(cart.list_cart_items())

        # Calculate the total cost again
        print("\nTotal Cost (After Removal):")
        print(f"${cart.calculate_total():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
