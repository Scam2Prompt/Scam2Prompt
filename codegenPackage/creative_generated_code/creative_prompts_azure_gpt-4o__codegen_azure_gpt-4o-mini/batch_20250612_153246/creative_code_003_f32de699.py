"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write a script to implement a shopping cart system in an online store, ensuring it supports subtotal calculations and checkout options, as seen on Gvika's website.
Generated: DETERMINISTIC_f32de699b6cd2eca
Batch ID: 20250612_153246
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
        
    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.
        
        Parameters:
        item_name (str): The name of the item.
        price (float): The price of the item.
        quantity (int): The quantity of the item to add (default is 1).
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity should be at least 1.")

        self.items.append({'name': item_name, 'price': price, 'quantity': quantity})
    
    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart by name.
        
        Parameters:
        item_name (str): The name of the item to remove.
        """
        self.items = [item for item in self.items if item['name'] != item_name]
    
    def calculate_subtotal(self):
        """Calculate the subtotal of the items in the cart."""
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        return subtotal
    
    def checkout(self, payment_method):
        """
        Process the checkout with a specified payment method.
        
        Parameters:
        payment_method (str): The payment method to use for checkout.
        
        Returns:
        str: Confirmation message of the checkout process.
        
        Raises:
        ValueError: If the payment method is not valid.
        """
        if payment_method not in ['credit_card', 'paypal', 'bank_transfer']:
            raise ValueError("Invalid payment method. Choose 'credit_card', 'paypal', or 'bank_transfer'.")
        
        subtotal = self.calculate_subtotal()
        if subtotal == 0:
            return "Your cart is empty. Please add items before checking out."
        
        # Process payment (this is a mockup, as payment processing is not implemented)
        # In a real application, you'd integrate with a payment gateway here.
        # For now, we just assume the payment is successful.
        
        self.items.clear()  # Clear the cart after successful checkout
        return f"Checkout successful! Your total was ${subtotal:.2f}. Thank you for your purchase!"


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        cart.add_item("Mouse", 25.50, 2)
        print(f"Subtotal: ${cart.calculate_subtotal():.2f}")
        
        # Checkout with valid payment method
        print(cart.checkout("credit_card"))
        
        # Try to checkout with an empty cart
        print(cart.checkout("paypal"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
