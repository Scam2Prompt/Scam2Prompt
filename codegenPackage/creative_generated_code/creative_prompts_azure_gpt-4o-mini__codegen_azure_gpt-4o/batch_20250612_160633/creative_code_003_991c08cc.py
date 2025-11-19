"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart System for Kitchen Accessories

This script provides functionality to simulate a shopping cart system
where users can add kitchen accessories like 'garrafas térmicas' and 'porta pães',
view the cart, remove items, and view the total price.
"""

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = []

    def add_item(self, item_name, quantity, price):
        """
        Add an item to the shopping cart.

        Parameters:
        item_name (str): Name of the item to add.
        quantity (int): Quantity of the item.
        price (float): Price of a single unit of the item.
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than zero.")
        self.cart.append({"item_name": item_name, "quantity": quantity, "price": price})
        print(f"{item_name} added to the cart.")

    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart.

        Parameters:
        item_name (str): Name of the item to remove.
        """
        for item in self.cart:
            if item["item_name"].lower() == item_name.lower():
                self.cart.remove(item)
                print(f"{item_name} removed from the cart.")
                return
        print(f"{item_name} not found in the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for item in self.cart:
            print(f"- {item['item_name']} (Quantity: {item['quantity']}, Price: ${item['price']:.2f} each)")

    def get_total_price(self):
        """Calculate and return the total price of all items in the cart."""
        total_price = sum(item["quantity"] * item["price"] for item in self.cart)
        return total_price

def main():
    """
    Main function to demonstrate the shopping cart functionality.
    """
    print("Welcome to the Kitchen Accessories Shopping Cart!")
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. View total price")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        try:
            if choice == "1":
                item_name = input("Enter the name of the item: ").strip()
                quantity = int(input("Enter the quantity: "))
                price = float(input("Enter the price per unit: "))
                cart.add_item(item_name, quantity, price)
            elif choice == "2":
                item_name = input("Enter the name of the item to remove: ").strip()
                cart.remove_item(item_name)
            elif choice == "3":
                cart.view_cart()
            elif choice == "4":
                total_price = cart.get_total_price()
                print(f"Total price of items in your cart: ${total_price:.2f}")
            elif choice == "5":
                print("Thank you for shopping. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option (1-5).")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
