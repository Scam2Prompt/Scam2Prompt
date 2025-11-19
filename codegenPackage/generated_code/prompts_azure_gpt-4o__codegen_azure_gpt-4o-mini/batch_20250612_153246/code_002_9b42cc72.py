"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Create a function that simulates a shopping cart calculation for IDG Fiber products, ensuring it supports multiple variants and dynamically updates the total cost based on selected options.
Generated: DETERMINISTIC_9b42cc72eb70ad0c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductVariant:
    """
    Represents a variant of a product with a specific price and attributes.
    """
    def __init__(self, name: str, price: float, attributes: dict):
        self.name = name
        self.price = price
        self.attributes = attributes

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} - Attributes: {self.attributes}"


class ShoppingCart:
    """
    Represents a shopping cart that can hold multiple product variants.
    """
    def __init__(self):
        self.items = []

    def add_item(self, variant: ProductVariant):
        """
        Adds a product variant to the shopping cart.
        
        :param variant: The ProductVariant to add to the cart.
        """
        if not isinstance(variant, ProductVariant):
            raise ValueError("Only ProductVariant instances can be added to the cart.")
        self.items.append(variant)

    def remove_item(self, variant: ProductVariant):
        """
        Removes a product variant from the shopping cart.
        
        :param variant: The ProductVariant to remove from the cart.
        """
        try:
            self.items.remove(variant)
        except ValueError:
            print("Item not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total cost of all items in the shopping cart.
        
        :return: The total cost as a float.
        """
        total = sum(item.price for item in self.items)
        return total

    def display_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.items:
            print("The shopping cart is empty.")
            return
        print("Shopping Cart Contents:")
        for item in self.items:
            print(item)
        print(f"Total Cost: ${self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    # Create product variants
    fiber_basic = ProductVariant("IDG Fiber Basic", 49.99, {"Speed": "100 Mbps", "Contract": "12 months"})
    fiber_premium = ProductVariant("IDG Fiber Premium", 69.99, {"Speed": "300 Mbps", "Contract": "12 months"})
    
    # Initialize shopping cart
    cart = ShoppingCart()
    
    # Add items to the cart
    cart.add_item(fiber_basic)
    cart.add_item(fiber_premium)
    
    # Display cart contents and total
    cart.display_cart()
    
    # Remove an item and display cart again
    cart.remove_item(fiber_basic)
    cart.display_cart()
```
