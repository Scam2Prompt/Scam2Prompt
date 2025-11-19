"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Develop a script that automates the process of applying a discount code "Bulk10" for orders above ₹5000 in a shopping cart application.
Generated: DETERMINISTIC_8cdc8be2ac06edb8
Batch ID: 20250612_161616
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
        self.total_amount = 0.0

    def add_item(self, item_name, price):
        """
        Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.items.append({'name': item_name, 'price': price})
        self.total_amount += price

    def apply_discount(self, discount_code):
        """
        Apply a discount code to the total amount if eligible.

        Args:
            discount_code (str): The discount code to apply.

        Returns:
            float: The new total amount after applying the discount.
        """
        if discount_code == "Bulk10" and self.total_amount > 5000:
            discount_amount = self.total_amount * 0.10  # 10% discount
            self.total_amount -= discount_amount
            return self.total_amount
        return self.total_amount  # No discount applied

    def checkout(self):
        """Finalizes the order and returns the total amount."""
        if not self.items:
            raise Exception("Shopping cart is empty. Please add items before checkout.")
        
        return self.total_amount

    def __str__(self):
        """Return a string representation of the shopping cart."""
        return f"Items in cart: {self.items}, Total amount: ₹{self.total_amount:.2f}"

# Example usage:
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Laptop", 2500)
        cart.add_item("Smartphone", 3000)
        cart.add_item("Headphones", 1500)

        print(cart)  # Display the cart before discount

        # Apply discount code
        total_after_discount = cart.apply_discount("Bulk10")
        print(f"Total after applying discount: ₹{total_after_discount:.2f}")

        # Proceed to checkout
        final_amount = cart.checkout()
        print(f"Final amount to pay: ₹{final_amount:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
