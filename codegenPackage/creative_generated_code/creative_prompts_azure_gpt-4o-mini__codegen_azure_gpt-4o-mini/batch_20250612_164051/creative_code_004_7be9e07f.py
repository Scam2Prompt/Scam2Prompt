"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like 'Sensor Presença' and 'Plafon Chess' with payment options.
Generated: DETERMINISTIC_7be9e07f80ccc579
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name: str, price: float):
        """Initialize product with name and price."""
        self.name = name
        self.price = price


class ShoppingCart:
    """Class representing a shopping cart that holds products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, product: Product):
        """Add a product to the shopping cart."""
        self.items.append(product)

    def remove_item(self, product_name: str):
        """Remove a product from the shopping cart by name."""
        self.items = [item for item in self.items if item.name != product_name]

    def calculate_total(self) -> float:
        """Calculate the total price of the items in the cart."""
        return sum(item.price for item in self.items)

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

    def list_items(self):
        """List all items in the shopping cart."""
        return [item.name for item in self.items]


class PaymentProcessor:
    """Class for processing payments."""
    
    @staticmethod
    def process_payment(amount: float, payment_method: str) -> bool:
        """Process the payment and return the success status."""
        # Simulated payment processing logic
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        if payment_method not in ["Credit Card", "Debit Card", "PayPal"]:
            raise ValueError("Unsupported payment method.")

        print(f"Processing {payment_method} payment of ${amount:.2f}...")
        # Simulate a successful payment
        return True


def main():
    """Main function to demonstrate the shopping cart functionality."""
    try:
        # Create product instances
        sensor_presenca = Product("Sensor Presença", 50.00)
        plafon_chess = Product("Plafon Chess", 100.00)

        # Initialize the shopping cart
        cart = ShoppingCart()
        
        # Add products to the cart
        cart.add_item(sensor_presenca)
        cart.add_item(plafon_chess)

        # Display items in the cart
        print(f"Items in cart: {cart.list_items()}")
        
        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price: ${total_price:.2f}")

        # Process payment
        payment_successful = PaymentProcessor.process_payment(total_price, "Credit Card")
        
        if payment_successful:
            print("Payment processed successfully.")
            cart.clear_cart()
            print("Cart cleared after successful payment.")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
