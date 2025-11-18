"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write Python code to create a shopping cart system for an e-commerce website that sells medical books and courses, similar to medebooks.shop, including features like applying discount coupons and calculating final prices.
Generated: DETERMINISTIC_87790f235755aaae
Batch ID: 20250612_153947
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
        """Initialize an empty shopping cart with a list of items and total price."""
        self.items = []
        self.total_price = 0.0

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart.
        
        Args:
            item_name (str): The name of the item.
            price (float): The price of a single item.
            quantity (int): The quantity of the item to add.
        """
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity must be positive.")

        self.items.append({"name": item_name, "price": price, "quantity": quantity})
        self.total_price += price * quantity

    def remove_item(self, item_name):
        """Remove an item from the shopping cart by name.
        
        Args:
            item_name (str): The name of the item to remove.
        """
        for item in self.items:
            if item["name"] == item_name:
                self.total_price -= item["price"] * item["quantity"]
                self.items.remove(item)
                break
        else:
            raise ValueError(f"Item '{item_name}' not found in the cart.")

    def apply_discount(self, coupon_code):
        """Apply a discount to the total price based on the coupon code.
        
        Args:
            coupon_code (str): The coupon code to apply.
        
        Returns:
            float: The discount amount.
        """
        discount_amount = 0.0
        valid_coupons = {"SAVE10": 0.1, "SAVE20": 0.2}  # Example coupon codes

        if coupon_code in valid_coupons:
            discount_amount = self.total_price * valid_coupons[coupon_code]
            self.total_price -= discount_amount
        else:
            raise ValueError("Invalid coupon code.")

        return discount_amount

    def calculate_final_price(self):
        """Calculate the final price of the items in the shopping cart.
        
        Returns:
            float: The final total price after discounts.
        """
        return self.total_price

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Items in your cart:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']} each")
        
        print(f"Total price: ${self.calculate_final_price():.2f}")


# Example usage:

if __name__ == "__main__":
    cart = ShoppingCart()
    
    try:
        # Add items to the cart
        cart.add_item("Medical Book A", 29.99, 2)
        cart.add_item("Medical Course B", 199.99, 1)

        # View the cart
        cart.view_cart()

        # Apply a discount
        discount = cart.apply_discount("SAVE10")
        print(f"Discount applied: ${discount:.2f}")

        # Final price after discount
        print(f"Final price after discount: ${cart.calculate_final_price():.2f}")

        # Remove an item
        cart.remove_item("Medical Book A")
        cart.view_cart()

    except ValueError as e:
        print(f"Error: {e}")
```
