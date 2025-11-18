"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Generate a Python script to simulate a shopping cart system for Harman Kardon products, including adding items, calculating total costs, and applying discounts based on sale prices listed on Harman Kardon Philippines.
Generated: DETERMINISTIC_7b4aba933c17fab6
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ShoppingCart:
    """
    A class to represent a shopping cart for Harman Kardon products.
    """
    def __init__(self):
        # Initialize an empty cart and product catalog
        self.cart = {}
        self.catalog = {
            "Harman Kardon Onyx Studio 7": {"price": 12000, "discount_price": 9500},
            "Harman Kardon Aura Studio 3": {"price": 17000, "discount_price": 15000},
            "Harman Kardon Go + Play": {"price": 20000, "discount_price": 18000},
        }
    
    def display_catalog(self):
        """
        Display the product catalog with full and discount prices.
        """
        print("\nAvailable Products:")
        for product, details in self.catalog.items():
            print(f"{product}: Regular Price - PHP {details['price']}, Sale Price - PHP {details['discount_price']}")
    
    def add_to_cart(self, product_name, quantity=1):
        """
        Add a product to the cart.
        :param product_name: Name of the product to add.
        :param quantity: Quantity of the product (default is 1).
        """
        if product_name not in self.catalog:
            print("Error: Product not found in the catalog.")
            return

        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity
        
        print(f"Added {quantity} x {product_name} to the cart.")
    
    def remove_from_cart(self, product_name):
        """
        Remove a product from the cart.
        :param product_name: Name of the product to remove.
        """
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print("Error: Product not found in the cart.")
    
    def calculate_total(self, apply_discount=False):
        """
        Calculate the total cost of items in the cart.
        :param apply_discount: Whether to apply discounts to the total price.
        :return: Total cost of the cart.
        """
        total = 0
        for product, quantity in self.cart.items():
            price = self.catalog[product]["discount_price"] if apply_discount else self.catalog[product]["price"]
            total += price * quantity
        
        return total
    
    def display_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\nShopping Cart:")
        for product, quantity in self.cart.items():
            price = self.catalog[product]["discount_price"]
            print(f"{quantity} x {product}: PHP {price} each")
        
        print(f"Total (Sale Price Applied): PHP {self.calculate_total(apply_discount=True)}")
        print(f"Total (Regular Price): PHP {self.calculate_total(apply_discount=False)}")

def main():
    """
    Main function to simulate the shopping cart system.
    """
    cart = ShoppingCart()
    
    while True:
        print("\nOptions:")
        print("1. View Catalog")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            cart.display_catalog()
        elif choice == 2:
            product_name = input("Enter the product name to add: ")
            try:
                quantity = int(input("Enter quantity: "))
                cart.add_to_cart(product_name, quantity)
            except ValueError:
                print("Error: Invalid quantity. Please enter a valid number.")
        elif choice == 3:
            product_name = input("Enter the product name to remove: ")
            cart.remove_from_cart(product_name)
        elif choice == 4:
            cart.display_cart()
        elif choice == 5:
            total = cart.calculate_total(apply_discount=True)
            print(f"\nCheckout Total (Sale Price Applied): PHP {total}")
            print("\nThank you for shopping!")
            break
        elif choice == 6:
            print("\nExiting... Thank you!")
            sys.exit()
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```
