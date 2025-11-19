"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Develop a script to calculate the total price of items in a shopping cart, incorporating discounts and free shipping options as mentioned on the Multan Designs website.
Generated: DETERMINISTIC_5736ccaa49676ffc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.discount = 0.0  # Discount percentage (0 to 100)
        self.free_shipping_threshold = 100.0  # Minimum amount for free shipping

    def add_item(self, name, price, quantity=1):
        """Add an item to the shopping cart.
        
        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item (default is 1).
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def set_discount(self, discount):
        """Set the discount for the shopping cart.
        
        Args:
            discount (float): The discount percentage (0 to 100).
        """
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self.discount = discount

    def calculate_total(self):
        """Calculate the total price of the items in the shopping cart, including discounts and shipping.
        
        Returns:
            float: The total price after applying discounts and accounting for shipping.
        """
        total = sum(item["price"] * item["quantity"] for item in self.items)
        
        # Apply discount
        total -= total * (self.discount / 100)

        # Determine shipping cost
        shipping_cost = 0.0
        if total < self.free_shipping_threshold:
            shipping_cost = 10.0  # Flat shipping fee
        
        return total + shipping_cost

    def display_cart(self):
        """Print the details of the shopping cart."""
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']} each")
        print(f"Discount: {self.discount}%")
        print(f"Total Price: ${self.calculate_total():.2f}")


if __name__ == "__main__":
    # Example usage
    cart = ShoppingCart()
    cart.add_item("T-Shirt", 25.00, 2)
    cart.add_item("Jeans", 40.00, 1)
    cart.set_discount(10)  # Set a 10% discount
    cart.display_cart()
```
