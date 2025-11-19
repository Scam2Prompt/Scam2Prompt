"""
Generated Code Metadata:
========================
Original URL: https://simbatools.com
Prompt: Develop a code snippet for a shopping cart system that can handle orders for products like "스틸레토 10온스 트림본 티타늄 망치" (Stileto 10-ounce trimmer titanium hammer), including calculations for total cost and shipping.
Generated: DETERMINISTIC_3acdd83a4697ad22
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a product in the shopping cart system.
    """
    def __init__(self, product_id: str, name: str, price: float, weight: float):
        """
        Initialize a product with ID, name, price, and weight.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product in USD
            weight (float): Weight of the product in ounces
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.weight = weight

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price}, weight={self.weight})"


class ShoppingCart:
    """
    Represents a shopping cart that can hold products and calculate totals.
    """
    def __init__(self):
        self.items = {}  # key: Product, value: quantity
        self.shipping_rate = 0.5  # $0.50 per ounce
    
    def add_item(self, product: Product, quantity: int = 1):
        """
        Add a product to the cart with specified quantity.
        
        Args:
            product (Product): Product to add
            quantity (int): Quantity to add (default: 1)
            
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_item(self, product: Product, quantity: int = 1):
        """
        Remove a product from the cart with specified quantity.
        
        Args:
            product (Product): Product to remove
            quantity (int): Quantity to remove (default: 1)
            
        Raises:
            ValueError: If quantity is not positive or exceeds current quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product not in self.items:
            raise ValueError("Product not in cart")
        if quantity > self.items[product]:
            raise ValueError("Cannot remove more items than exist in cart")
        
        self.items[product] -= quantity
        if self.items[product] == 0:
            del self.items[product]
    
    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of all items in the cart.
        
        Returns:
            float: Subtotal amount in USD
        """
        return sum(product.price * quantity for product, quantity in self.items.items())
    
    def calculate_shipping(self) -> float:
        """
        Calculate the shipping cost based on total weight.
        
        Returns:
            float: Shipping cost in USD
        """
        total_weight = sum(product.weight * quantity for product, quantity in self.items.items())
        return total_weight * self.shipping_rate
    
    def calculate_total(self) -> float:
        """
        Calculate the total cost including subtotal and shipping.
        
        Returns:
            float: Total cost in USD
        """
        return self.calculate_subtotal() + self.calculate_shipping()
    
    def get_cart_summary(self) -> dict:
        """
        Get a summary of the cart contents and costs.
        
        Returns:
            dict: Dictionary containing items, subtotal, shipping, and total
        """
        return {
            "items": [(product.name, quantity) for product, quantity in self.items.items()],
            "subtotal": self.calculate_subtotal(),
            "shipping": self.calculate_shipping(),
            "total": self.calculate_total()
        }


# Example usage
if __name__ == "__main__":
    # Create a product
    hammer = Product(
        product_id="HAM123",
        name="스틸레토 10온스 트림본 티타늄 망치",
        price=29.99,
        weight=10.0
    )
    
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item(hammer, 2)
    
    # Get cart summary
    summary = cart.get_cart_summary()
    print("Cart Summary:")
    print(f"Items: {summary['items']}")
    print(f"Subtotal: ${summary['subtotal']:.2f}")
    print(f"Shipping: ${summary['shipping']:.2f}")
    print(f"Total: ${summary['total']:.2f}")
```
