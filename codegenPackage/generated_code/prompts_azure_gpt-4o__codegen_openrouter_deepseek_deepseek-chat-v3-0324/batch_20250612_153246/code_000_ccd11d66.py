"""
Generated Code Metadata:
========================
Original URL: https://www.techno-city.co.za
Prompt: Write Python code to simulate a shopping cart system that includes categories like "Gaming Accessories," "DIY Tools," and "Solar Panels," as described on the Techno City website. Include functionality for discounts based on the percentage off listed for each product.
Generated: DETERMINISTIC_ccd11d663e97c4ad
Batch ID: 20250612_153246
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
    def __init__(self, name: str, price: float, category: str, discount_percentage: float = 0.0):
        """
        Initialize a product with name, price, category, and discount percentage.
        
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            category (str): Category of the product (e.g., "Gaming Accessories").
            discount_percentage (float, optional): Discount percentage (0-100). Defaults to 0.0.
        """
        self.name = name
        self.price = price
        self.category = category
        self.discount_percentage = discount_percentage
    
    def get_discounted_price(self) -> float:
        """
        Calculate the discounted price of the product.
        
        Returns:
            float: Discounted price after applying the discount percentage.
        """
        return self.price * (1 - self.discount_percentage / 100)
    
    def __str__(self) -> str:
        """
        String representation of the product.
        
        Returns:
            str: Formatted string with product details.
        """
        return f"{self.name} ({self.category}) - ${self.price:.2f} (Discount: {self.discount_percentage}%)"


class ShoppingCart:
    """
    Represents a shopping cart that holds products.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.products = []
    
    def add_product(self, product: Product) -> None:
        """
        Add a product to the shopping cart.
        
        Args:
            product (Product): Product to add to the cart.
        """
        self.products.append(product)
    
    def remove_product(self, product_name: str) -> bool:
        """
        Remove a product from the shopping cart by name.
        
        Args:
            product_name (str): Name of the product to remove.
            
        Returns:
            bool: True if product was found and removed, False otherwise.
        """
        for i, product in enumerate(self.products):
            if product.name == product_name:
                self.products.pop(i)
                return True
        return False
    
    def calculate_total(self) -> float:
        """
        Calculate the total price of all products in the cart after discounts.
        
        Returns:
            float: Total price after applying all discounts.
        """
        return sum(product.get_discounted_price() for product in self.products)
    
    def apply_category_discount(self, category: str, discount_percentage: float) -> None:
        """
        Apply a discount to all products in a specific category.
        
        Args:
            category (str): Category to apply the discount to.
            discount_percentage (float): Discount percentage (0-100).
        """
        for product in self.products:
            if product.category == category:
                product.discount_percentage = discount_percentage
    
    def display_cart(self) -> None:
        """
        Display all products in the shopping cart along with the total price.
        """
        if not self.products:
            print("Your shopping cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for product in self.products:
            print(f"- {product}")
        
        print(f"\nTotal: ${self.calculate_total():.2f}")


def main():
    """
    Main function to demonstrate the shopping cart system.
    """
    # Sample products
    gaming_mouse = Product("Razer Gaming Mouse", 59.99, "Gaming Accessories", 10.0)
    gaming_keyboard = Product("Mechanical Keyboard", 89.99, "Gaming Accessories")
    drill = Product("Cordless Drill", 129.99, "DIY Tools", 15.0)
    solar_panel = Product("Solar Panel 100W", 199.99, "Solar Panels")
    
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add products to cart
    cart.add_product(gaming_mouse)
    cart.add_product(gaming_keyboard)
    cart.add_product(drill)
    cart.add_product(solar_panel)
    
    # Display initial cart
    cart.display_cart()
    
    # Apply additional discount to a category
    print("\nApplying 20% discount to Gaming Accessories...")
    cart.apply_category_discount("Gaming Accessories", 20.0)
    cart.display_cart()
    
    # Remove a product
    print("\nRemoving Cordless Drill from cart...")
    cart.remove_product("Cordless Drill")
    cart.display_cart()


if __name__ == "__main__":
    main()
```
