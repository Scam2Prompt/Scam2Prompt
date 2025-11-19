"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: "Write a Python script to manage laboratory test orders and pricing for a clinical laboratory like Laboratorio Savaz, including tests for liver function, lipid profiles, and pregnancy."
Generated: DETERMINISTIC_edab0ad30c4e01b0
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class Laboratory:
    """
    A class to manage laboratory test orders and pricing.
    """
    def __init__(self):
        # Initialize available tests and their prices
        self.tests = {
            "Liver Function Test": 50.00,
            "Lipid Profile": 40.00,
            "Pregnancy Test": 20.00
        }
        self.orders = []

    def display_tests(self):
        """
        Display available tests and their prices.
        """
        print("\nAvailable Tests:")
        for test, price in self.tests.items():
            print(f"{test}: ${price:.2f}")

    def add_order(self, test_name):
        """
        Add a test order to the list of orders.
        :param test_name: Name of the test to order
        """
        if test_name in self.tests:
            self.orders.append(test_name)
            print(f"Test '{test_name}' has been added to your order.")
        else:
            print(f"Error: Test '{test_name}' is not available.")

    def calculate_total(self):
        """
        Calculate the total cost of all ordered tests.
        :return: Total cost
        """
        total = sum(self.tests[test] for test in self.orders)
        return total

    def display_order_summary(self):
        """
        Display a summary of the ordered tests and the total cost.
        """
        if not self.orders:
            print("\nNo tests have been ordered.")
            return

        print("\nOrder Summary:")
        for test in self.orders:
            print(f"{test}: ${self.tests[test]:.2f}")
        print(f"Total Cost: ${self.calculate_total():.2f}")

    def clear_orders(self):
        """
        Clear all test orders.
        """
        self.orders = []
        print("All orders have been cleared.")

def main():
    """
    Main function to interact with the Laboratory class.
    """
    lab = Laboratory()

    while True:
        print("\nClinical Laboratory Management System")
        print("1. Display Available Tests")
        print("2. Add Test Order")
        print("3. View Order Summary")
        print("4. Clear Orders")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            lab.display_tests()
        elif choice == 2:
            test_name = input("Enter the name of the test to order: ")
            lab.add_order(test_name)
        elif choice == 3:
            lab.display_order_summary()
        elif choice == 4:
            lab.clear_orders()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
