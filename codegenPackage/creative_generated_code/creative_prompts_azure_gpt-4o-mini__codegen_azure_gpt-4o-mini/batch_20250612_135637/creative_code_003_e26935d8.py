"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Create a function that calculates the total price of items in a shopping cart, including discounts and shipping fees, as outlined in the shopping process on FirstCry.com.
Generated: DETERMINISTIC_e26935d87963946d
Batch ID: 20250612_135637
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
        self.discount = 0.0
        self.shipping_fee = 0.0

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of a single item.
            quantity (int): The quantity of the item to add. Defaults to 1.

        Raises:
            ValueError: If price or quantity is negative.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        
        self.items.append({
            'item_name': item_name,
            'price': price,
            'quantity': quantity
        })

    def set_discount(self, discount_percentage):
        """Set the discount percentage for the shopping cart.

        Args:
            discount_percentage (float): The discount percentage to apply.

        Raises:
            ValueError: If discount_percentage is negative or greater than 100.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        self.discount = discount_percentage

    def set_shipping_fee(self, shipping_fee):
        """Set the shipping fee for the shopping cart.

        Args:
            shipping_fee (float): The shipping fee to apply.

        Raises:
            ValueError: If shipping_fee is negative.
        """
        if shipping_fee < 0:
            raise ValueError("Shipping fee must be non-negative.")
        
        self.shipping_fee = shipping_fee

    def calculate_total(self):
        """Calculate the total price of items in the shopping cart, including discounts and shipping fees.

        Returns:
            float: The total price after applying discounts and adding shipping fees.
        """
        total_price = sum(item['price'] * item['quantity'] for item in self.items)
        
        # Apply discount
        total_discount = total_price * (self.discount / 100)
        total_price -= total_discount
        
        # Add shipping fee
        total_price += self.shipping_fee
        
        # Ensure total price is not negative
        return max(total_price, 0.0)

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()
        self.discount = 0.0
        self.shipping_fee = 0.0

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Toy Car", 10.0, 2)
    cart.add_item("Doll", 15.0, 1)
    cart.set_discount(10)  # 10% discount
    cart.set_shipping_fee(5.0)  # $5 shipping fee

    total = cart.calculate_total()
    print(f"Total price: ${total:.2f}")
```
