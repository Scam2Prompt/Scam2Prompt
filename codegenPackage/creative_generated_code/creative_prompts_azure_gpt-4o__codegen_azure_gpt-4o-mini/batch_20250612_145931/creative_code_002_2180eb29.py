"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viaisle.top
Prompt: Generate Python code to simulate a shopping cart system that supports querying inventory and processing orders, inspired by the features on 虚屿.
Generated: DETERMINISTIC_2180eb29e4668c1b
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional


class Product:
    """
    Class representing a product in the inventory.
    """
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, Price: {self.price}, Available: {self.quantity})"


class Inventory:
    """
    Class representing the inventory of products.
    """
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the inventory."""
        self.products[product.product_id] = product

    def query_product(self, product_id: str) -> Optional[Product]:
        """Query a product by its ID."""
        return self.products.get(product_id)

    def list_products(self) -> List[Product]:
        """Return a list of all products in the inventory."""
        return list(self.products.values())


class ShoppingCart:
    """
    Class representing a shopping cart for users to add products.
    """
    def __init__(self):
        self.items: Dict[str, int] = {}  # product_id: quantity

    def add_to_cart(self, product_id: str, quantity: int, inventory: Inventory) -> str:
        """Add a product to the shopping cart."""
        product = inventory.query_product(product_id)
        if product is None:
            return f"Product with ID {product_id} does not exist."
        if quantity > product.quantity:
            return f"Insufficient stock for {product.name}. Available: {product.quantity}."
        
        self.items[product_id] = self.items.get(product_id, 0) + quantity
        product.quantity -= quantity  # Reduce the inventory quantity
        return f"Added {quantity} of {product.name} to the cart."

    def view_cart(self, inventory: Inventory) -> str:
        """View the contents of the shopping cart."""
        if not self.items:
            return "Your cart is empty."
        cart_details = []
        total_cost = 0.0
        for product_id, quantity in self.items.items():
            product = inventory.query_product(product_id)
            if product:
                cost = product.price * quantity
                total_cost += cost
                cart_details.append(f"{product.name} (Quantity: {quantity}, Cost: {cost})")
        return "\n".join(cart_details) + f"\nTotal Cost: {total_cost}"


class OrderProcessor:
    """
    Class for processing orders from the shopping cart.
    """
    def __init__(self):
        pass

    def process_order(self, cart: ShoppingCart) -> str:
        """Process the order by finalizing the shopping cart."""
        if not cart.items:
            return "No items in the cart to process."
        # Here you can implement payment processing, order saving, etc.
        cart.items.clear()  # Clear the cart after processing
        return "Order processed successfully."


# Example usage
if __name__ == "__main__":
    # Create inventory and add some products
    inventory = Inventory()
    inventory.add_product(Product("1", "Apple", 0.5, 100))
    inventory.add_product(Product("2", "Banana", 0.3, 150))
    inventory.add_product(Product("3", "Orange", 0.6, 80))

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to cart and view cart
    print(cart.add_to_cart("1", 3, inventory))
    print(cart.add_to_cart("2", 5, inventory))
    print(cart.view_cart(inventory))

    # Process order
    order_processor = OrderProcessor()
    print(order_processor.process_order(cart))

    # View cart after processing order
    print(cart.view_cart(inventory))
```
