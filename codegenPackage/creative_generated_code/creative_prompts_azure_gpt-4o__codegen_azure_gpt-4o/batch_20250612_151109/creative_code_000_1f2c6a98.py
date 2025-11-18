"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gn-connect.com
Prompt: Write Python code to simulate a cashless payment system for a restaurant, incorporating features discussed in gn connect, such as integration with AI-based menu recommendations.
Generated: DETERMINISTIC_1f2c6a98da367faf
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import time
import random

# Constants
MENU = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Salad": 4.99,
    "Pasta": 7.49,
    "Soda": 1.99,
    "Coffee": 2.49
}

RECOMMENDED_ITEMS = ["Burger", "Pizza", "Coffee"]  # Example AI-recommended items

class PaymentSystem:
    def __init__(self):
        # Initialize customer cart and payment status
        self.cart = []
        self.total_amount = 0
        self.payment_status = False

    def display_menu(self):
        """Display the menu with prices."""
        print("\n--- Menu ---")
        for item, price in MENU.items():
            print(f"{item}: ${price:.2f}")
        print()

    def recommend_items(self):
        """Provide AI-based menu recommendations."""
        print("\n--- Recommended Items ---")
        print("Based on your preferences, we recommend:")
        for item in RECOMMENDED_ITEMS:
            print(f"{item}: ${MENU[item]:.2f}")
        print()

    def add_to_cart(self, item):
        """Add an item to the cart."""
        if item in MENU:
            self.cart.append(item)
            self.total_amount += MENU[item]
            print(f"Added {item} to your cart. Current total: ${self.total_amount:.2f}")
        else:
            print(f"Item '{item}' is not available in the menu.")

    def view_cart(self):
        """View the items in the cart."""
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\n--- Your Cart ---")
            for item in self.cart:
                print(f"{item}: ${MENU[item]:.2f}")
            print(f"Total Amount: ${self.total_amount:.2f}")

    def make_payment(self):
        """Simulate the payment process."""
        print("\nProcessing payment...")
        try:
            # Simulate random payment success/failure
            time.sleep(2)
            if random.choice([True, False]):
                self.payment_status = True
                print("Payment successful! Thank you for your purchase.")
            else:
                raise ValueError("Payment failed due to network issues. Please try again.")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            self.payment_status = False

    def reset_after_payment(self):
        """Reset the system after payment."""
        if self.payment_status:
            print("\n--- Resetting system for next customer ---")
            self.cart = []
            self.total_amount = 0
            self.payment_status = False

def main():
    """Main function to run the cashless payment system."""
    system = PaymentSystem()
    print("\nWelcome to the Restaurant Payment System!")
    
    while True:
        print("\nPlease select an option:")
        print("1. View Menu")
        print("2. View Recommended Items")
        print("3. Add Item to Cart")
        print("4. View Cart")
        print("5. Make Payment")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                system.display_menu()
            elif choice == 2:
                system.recommend_items()
            elif choice == 3:
                item = input("Enter the name of the item to add to your cart: ").strip()
                system.add_to_cart(item)
            elif choice == 4:
                system.view_cart()
            elif choice == 5:
                system.make_payment()
                system.reset_after_payment()
            elif choice == 6:
                print("Thank you for using the payment system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```
