"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write Python code to create a shopping cart system for an online store specializing in diving and fishing gear, referencing categories like "гидрокостюмы," "пневматические ружья," and "туристические палатки" from the catalog structure on acula.com.ua.
Generated: DETERMINISTIC_19582d5a14fc1234
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Represents a product in the store."""
    
    def __init__(self, name: str, price: float, category: str):
        """
        Initializes a new product.
        
        :param name: Name of the product
        :param price: Price of the product
        :param category: Category of the product
        :raises ValueError: If price is negative or name is empty
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not name:
            raise ValueError("Product name cannot be empty.")
        
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} ({self.category}): {self.price:.2f} UAH"


class ShoppingCart:
    """Represents a shopping cart for customers."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.
        
        :param product: A Product instance to add
        """
        self.items.append(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product: Product):
        """
        Removes a product from the shopping cart.
        
        :param product: A Product instance to remove
        :raises ValueError: If the product is not in the cart
        """
        try:
            self.items.remove(product)
            print(f"Removed {product} from the cart.")
        except ValueError:
            print(f"Product {product.name} not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of products in the cart.
        
        :return: Total price of all products in the cart
        """
        total = sum(product.price for product in self.items)
        return total

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()
        print("Shopping cart has been cleared.")

    def print_receipt(self):
        """Prints the items in the cart along with the total amount."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        
        print("Receipt:")
        for item in self.items:
            print(f"- {item}")
        print(f"Total: {self.calculate_total():.2f} UAH")


# Sample usage
if __name__ == "__main__":
    # Create a shopping cart
    cart = ShoppingCart()

    # Create some products
    wetsuit = Product("Гидрокостюм", 4500.00, "гидрокостюмы")
    pneumatic_gun = Product("Пневматическое ружьё", 3500.00, "пневматические ружья")
    tourist_tent = Product("Туристическая палатка", 2500.00, "туристические палатки")

    # Add products to the cart
    cart.add_product(wetsuit)
    cart.add_product(pneumatic_gun)
    cart.add_product(tourist_tent)

    # Print receipt
    cart.print_receipt()

    # Remove a product
    cart.remove_product(pneumatic_gun)

    # Print updated receipt
    cart.print_receipt()

    # Clear the cart
    cart.clear_cart()
```
