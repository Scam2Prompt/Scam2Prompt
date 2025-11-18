"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write a Python program to simulate a customer order for personalized reusable bags from Grupo ProBolsa, including fields for design preferences and quantity.
Generated: DETERMINISTIC_0e248219f5d271b4
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Grupo ProBolsa Customizable Reusable Bags Order System
Description: This program allows customers to place orders for personalized reusable bags.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

class OrderSystem:
    def __init__(self):
        """
        Initializes the OrderSystem with necessary attributes.
        """
        self.order_details = {}

    def get_order_details(self):
        """
        Collects details for the reusable bag order from the user.
        """
        try:
            print("Welcome to Grupo ProBolsa's Customizable Bag Order System!")
            
            # Collect customer name
            customer_name = input("Please enter your name: ").strip()
            if not customer_name:
                raise ValueError("Customer name cannot be empty.")
            
            # Collect design preferences
            design_preference = input("Enter your design preference (e.g., Floral, Geometric, Minimalist): ").strip()
            if not design_preference:
                raise ValueError("Design preference cannot be empty.")
            
            # Collect quantity
            quantity = input("Enter the number of bags you want to order: ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                raise ValueError("Quantity must be a positive integer.")
            quantity = int(quantity)
            
            # Save order details
            self.order_details = {
                "Customer Name": customer_name,
                "Design Preference": design_preference,
                "Quantity": quantity
            }

        except ValueError as ve:
            # Handle validation errors
            print(f"Error: {ve}")
            sys.exit(1)
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    def display_order_summary(self):
        """
        Displays the order summary to the customer.
        """
        print("\nOrder Summary:")
        for key, value in self.order_details.items():
            print(f"{key}: {value}")
        print("Thank you for your order! Grupo ProBolsa will contact you shortly.")

    def run(self):
        """
        Runs the program to simulate the order process.
        """
        self.get_order_details()
        self.display_order_summary()

# Entry point for the program
if __name__ == "__main__":
    # Instantiate and run the order system
    order_system = OrderSystem()
    order_system.run()
```
