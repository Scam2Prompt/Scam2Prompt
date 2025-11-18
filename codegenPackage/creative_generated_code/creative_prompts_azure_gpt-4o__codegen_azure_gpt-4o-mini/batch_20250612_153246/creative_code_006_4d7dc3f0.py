"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write Python code to calculate discounts for cannabis products such as "Joint CBD 1g (2+1 Δώρο)" based on promotional offers, and display the discounted price in an e-commerce application.
Generated: DETERMINISTIC_4d7dc3f05af673e4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    def __init__(self, name, price):
        """
        Initializes a Product instance.
        
        :param name: str - The name of the product.
        :param price: float - The original price of the product.
        """
        self.name = name
        self.price = price

    def apply_discount(self, quantity):
        """
        Applies discount based on the quantity purchased.
        
        :param quantity: int - The number of units being purchased.
        :return: float - The discounted price to be paid.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        
        discount_price = self.price * quantity
        
        # Example promotional offer: Buy 2 get 1 free
        if quantity >= 3:
            discount_price -= self.price  # Free item for every 3 purchased

        return discount_price


def display_discounted_price(product, quantity):
    """
    Displays the discounted price for the given product and quantity.
    
    :param product: Product - The product for which the price is calculated.
    :param quantity: int - The quantity of the product being purchased.
    """
    try:
        discounted_price = product.apply_discount(quantity)
        print(f"Product: {product.name}")
        print(f"Quantity: {quantity}")
        print(f"Discounted Price: €{discounted_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    # Create a product instance for "Joint CBD 1g"
    joint_cbd = Product("Joint CBD 1g (2+1 Δώρο)", 5.00)

    # Display discounted price for different quantities
    display_discounted_price(joint_cbd, 3)  # Buy 2 get 1 free
    display_discounted_price(joint_cbd, 5)  # Buy 2 get 1 free
    display_discounted_price(joint_cbd, -1) # Test error handling
```
