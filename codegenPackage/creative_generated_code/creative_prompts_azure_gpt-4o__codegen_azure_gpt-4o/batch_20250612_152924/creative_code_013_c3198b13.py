"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Create a program to simulate adding car accessories to a shopping cart and calculating the total cost, including VAT, as shown on the Tuning Design website.
Generated: DETERMINISTIC_c3198b13d832728e
Batch ID: 20250612_152924
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
    A class to represent a shopping cart for car accessories.
    """
    def __init__(self, vat_rate=0.20):
        """
        Initializes the shopping cart with an empty list of items and VAT rate.

        :param vat_rate: VAT percentage to be applied to the total cost (default is 20%)
        """
        self.items = []  # List to store items in the cart
        self.vat_rate = vat_rate  # VAT rate as a decimal (e.g., 0.20 for 20%)

    def add_item(self, name, price):
        """
        Adds an item to the shopping cart.

        :param name: Name of the accessory.
        :param price: Price of the accessory (float or int).
        """
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a valid string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Item price must be a positive number.")

        self.items.append({"name": name, "price": price})
        print(f"Added '{name}' to the cart with price {price:.2f}.")

    def calculate_total(self):
        """
        Calculates the total cost including VAT.

        :return: A dictionary containing subtotal, VAT amount, and total cost.
        """
        subtotal = sum(item['price'] for item in self.items)
        vat_amount = subtotal * self.vat_rate
        total = subtotal + vat_amount
        return {"subtotal": round(subtotal, 2), "vat": round(vat_amount, 2), "total": round(total, 2)}

    def display_cart(self):
        """
        Displays the items in the shopping cart.
        """
        print("\nShopping Cart:")
        if not self.items:
            print("Your cart is empty.")
        else:
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item['name']} - ${item['price']:.2f}")
        totals = self.calculate_total()
        print(f"\nSubtotal: ${totals['subtotal']:.2f}")
        print(f"VAT ({int(self.vat_rate * 100)}%): ${totals['vat']:.2f}")
        print(f"Total: ${totals['total']:.2f}\n")


def main():
    """
    Main function to simulate adding car accessories to a shopping cart and calculating the total cost.
    """
    print("Welcome to Tuning Design Car Accessories Shop!")
    cart = ShoppingCart()

    while True:
        try:
            print("\nMenu:")
            print("1. Add accessory to cart")
            print("2. View cart")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ").strip()

            if choice == '1':
                name = input("Enter accessory name: ").strip()
                try:
                    price = float(input("Enter accessory price: "))
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue
                cart.add_item(name, price)

            elif choice == '2':
                cart.display_cart()

            elif choice == '3':
                print("Thank you for shopping with us!")
                break

            else:
                print("Invalid choice. Please select from the menu.")

        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
```
