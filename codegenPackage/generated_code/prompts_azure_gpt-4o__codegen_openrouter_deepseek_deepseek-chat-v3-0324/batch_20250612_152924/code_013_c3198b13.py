"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: Create a program to simulate adding car accessories to a shopping cart and calculating the total cost, including VAT, as shown on the Tuning Design website.
Generated: DETERMINISTIC_c3198b13d832728e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarAccessory:
    """
    Represents a car accessory with name and price.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    """
    Represents a shopping cart that holds car accessories and calculates totals.
    """
    VAT_RATE = 0.20  # 20% VAT

    def __init__(self):
        self.items = []

    def add_item(self, accessory: CarAccessory):
        """Adds an accessory to the shopping cart."""
        if not isinstance(accessory, CarAccessory):
            raise ValueError("Only CarAccessory objects can be added to the cart")
        self.items.append(accessory)

    def remove_item(self, accessory_name: str):
        """Removes an accessory from the shopping cart by name."""
        for i, item in enumerate(self.items):
            if item.name.lower() == accessory_name.lower():
                del self.items[i]
                return
        raise ValueError(f"Accessory '{accessory_name}' not found in cart")

    def calculate_subtotal(self) -> float:
        """Calculates the subtotal of all items in the cart."""
        return sum(item.price for item in self.items)

    def calculate_vat(self) -> float:
        """Calculates the VAT amount based on the subtotal."""
        return self.calculate_subtotal() * self.VAT_RATE

    def calculate_total(self) -> float:
        """Calculates the total cost including VAT."""
        return self.calculate_subtotal() + self.calculate_vat()

    def display_cart(self):
        """Displays all items in the cart and the total costs."""
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("\nShopping Cart Contents:")
        for item in self.items:
            print(f"- {item}")

        print(f"\nSubtotal: ${self.calculate_subtotal():.2f}")
        print(f"VAT ({self.VAT_RATE*100:.0f}%): ${self.calculate_vat():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    """Main function to simulate the shopping cart interaction."""
    # Sample accessories available for purchase
    available_accessories = [
        CarAccessory("Carbon Fiber Spoiler", 299.99),
        CarAccessory("LED Headlights", 149.99),
        CarAccessory("Performance Exhaust", 499.99),
        CarAccessory("Alloy Wheels", 799.99),
        CarAccessory("Window Tinting", 199.99)
    ]

    cart = ShoppingCart()

    print("Welcome to Tuning Design Car Accessories Shop!")
    print("\nAvailable Accessories:")
    for idx, accessory in enumerate(available_accessories, 1):
        print(f"{idx}. {accessory}")

    while True:
        try:
            print("\nOptions:")
            print("1. Add item to cart")
            print("2. Remove item from cart")
            print("3. View cart")
            print("4. Checkout")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                item_num = int(input("Enter item number to add: "))
                if 1 <= item_num <= len(available_accessories):
                    selected = available_accessories[item_num - 1]
                    cart.add_item(selected)
                    print(f"Added {selected.name} to your cart.")
                else:
                    print("Invalid item number.")

            elif choice == "2":
                if not cart.items:
                    print("Your cart is empty.")
                    continue
                item_name = input("Enter item name to remove: ")
                cart.remove_item(item_name)
                print(f"Removed {item_name} from your cart.")

            elif choice == "3":
                cart.display_cart()

            elif choice == "4":
                if not cart.items:
                    print("Your cart is empty. Nothing to checkout.")
                    continue
                cart.display_cart()
                print("\nThank you for shopping with Tuning Design!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
