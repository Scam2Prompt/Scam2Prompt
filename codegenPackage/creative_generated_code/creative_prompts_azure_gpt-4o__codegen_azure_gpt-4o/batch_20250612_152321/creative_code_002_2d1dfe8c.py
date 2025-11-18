"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Generate code to simulate the ordering process for stainless steel screws and bolts from APN Hardware, including product selection, quantity input, and order confirmation.
Generated: DETERMINISTIC_2d1dfe8c65d6bca5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class APNHardwareStore:
    def __init__(self):
        # Available products and their prices
        self.products = {
            "Stainless Steel Screw": 0.50,  # Price per unit in USD
            "Stainless Steel Bolt": 0.75,  # Price per unit in USD
        }

    def display_products(self):
        """Display the available products with their prices."""
        print("Available Products:")
        for idx, (product, price) in enumerate(self.products.items(), 1):
            print(f"{idx}. {product} - ${price:.2f} per unit")

    def select_product(self):
        """Allow the user to select a product."""
        while True:
            try:
                choice = int(input("Enter the product number to order: "))
                product_keys = list(self.products.keys())
                if 1 <= choice <= len(product_keys):
                    selected_product = product_keys[choice - 1]
                    print(f"Selected Product: {selected_product}")
                    return selected_product
                else:
                    print("Invalid selection. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    def input_quantity(self):
        """Allow the user to input the quantity of the selected product."""
        while True:
            try:
                quantity = int(input("Enter the quantity to order: "))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid integer for the quantity.")

    def confirm_order(self, product, quantity):
        """Confirm the order and display the total cost."""
        price_per_unit = self.products[product]
        total_cost = price_per_unit * quantity
        print("\nOrder Confirmation:")
        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print(f"Price per unit: ${price_per_unit:.2f}")
        print(f"Total cost: ${total_cost:.2f}")
        while True:
            confirmation = input("Do you want to confirm this order? (yes/no): ").strip().lower()
            if confirmation == "yes":
                print("Order confirmed! Thank you for your purchase.")
                break
            elif confirmation == "no":
                print("Order cancelled.")
                break
            else:
                print("Invalid response. Please type 'yes' or 'no'.")

def main():
    """Main function to simulate the ordering process."""
    try:
        print("Welcome to APN Hardware Store!")
        store = APNHardwareStore()
        store.display_products()
        selected_product = store.select_product()
        quantity = store.input_quantity()
        store.confirm_order(selected_product, quantity)
    except KeyboardInterrupt:
        print("\nOrder process interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
