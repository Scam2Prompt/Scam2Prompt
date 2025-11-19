"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Generate a code snippet for an e-commerce website that implements a zero-waste checkout process for natural cosmetics, similar to the offerings on C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_c188044063b2c538
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict


class Product:
    """
    Represents a product in the e-commerce store.
    Each product has a name, price, and a zero-waste attribute.
    """

    def __init__(self, product_id: int, name: str, price: float, zero_waste: bool = True):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.zero_waste = zero_waste


class Cart:
    """
    Represents a shopping cart containing products for checkout.
    """

    def __init__(self):
        self.items: List[Dict[str, Product]] = []  # List of product details added to the cart.
        self.total_price: float = 0.0

    def add_item(self, product: Product, quantity: int) -> None:
        """
        Adds an item to the cart and updates the total price.

        Parameters:
        - product: A Product instance to be added.
        - quantity: The number of units of the product to add.

        Raises:
        - ValueError: If an invalid quantity is provided.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.items.append({"product": product, "quantity": quantity})
        self.total_price += product.price * quantity
        print(f"Added {quantity}x {product.name} to the cart.")

    def remove_item(self, product_id: int) -> None:
        """
        Removes an item from the cart by its product ID and updates the total price.

        Parameters:
        - product_id: The ID of the product to be removed.

        Raises:
        - ValueError: If the product is not found in the cart.
        """
        for item in self.items:
            if item["product"].product_id == product_id:
                self.total_price -= item["product"].price * item["quantity"]
                self.items.remove(item)
                print(f"Removed {item['product'].name} from the cart.")
                return
        raise ValueError("Product not found in the cart.")

    def checkout(self) -> None:
        """
        Finalizes the checkout process and ensures all products are zero-waste.
        """
        if not self.items:
            print("Your cart is empty. Add items to proceed with checkout.")
            return

        print("Processing checkout...")
        for item in self.items:
            if not item["product"].zero_waste:
                print(
                    f"Warning: {item['product'].name} is not certified zero-waste."
                )
        
        print(f"Total Price: ${self.total_price:.2f}")
        print("Thank you for choosing our zero-waste products!")
        # Simulate clearing the cart after checkout
        self.items.clear()
        self.total_price = 0.0


# Simulation of an e-commerce zero-waste checkout process.

def main():
    """
    Main function simulating the zero-waste e-commerce checkout.
    """
    try:
        # Creating products
        product1 = Product(product_id=101, name="Natural Shampoo", price=15.99)
        product2 = Product(product_id=102, name="Organic Soap", price=5.49)
        product3 = Product(
            product_id=103, name="Zero-Waste Lotion", price=12.99, zero_waste=False
        )

        # Creating a shopping cart
        cart = Cart()

        # Adding products to the cart
        cart.add_item(product1, 2)
        cart.add_item(product2, 3)

        # Attempting to add a product that is not zero-waste
        cart.add_item(product3, 1)

        # Proceeding to checkout
        cart.checkout()

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        

if __name__ == "__main__":
    main()
```
