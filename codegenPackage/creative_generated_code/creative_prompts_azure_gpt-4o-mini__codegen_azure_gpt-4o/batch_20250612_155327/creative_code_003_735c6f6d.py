"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Develop a checkout process that includes options for both single and bulk purchases of coat racks, inspired by the purchasing model of Shahkar Industry.
Generated: DETERMINISTIC_735c6f6d896148ae
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checkout_process.py

import sys

# Constants
COAT_RACK_PRICE = 50  # Cost per single coat rack in dollars

def calculate_total_price(quantity):
    """
    Calculate total price for the given quantity of coat racks.
    
    Args:
        quantity (int): Number of coat racks to be purchased.
    
    Returns:
        float: Total price of the coat racks.
    """
    return COAT_RACK_PRICE * quantity

def checkout_process():
    """
    Handles the checkout process for coat racks, allowing both single and bulk purchases.
    """
    try:
        # Display options to the user
        print("Welcome to Shahkar Industry's Coat Rack Checkout!")
        print("Select purchase type:")
        print("1. Single Purchase")
        print("2. Bulk Purchase")

        # Take user input for purchase type
        purchase_type = input("Enter your choice (1/2): ").strip()

        if purchase_type not in ['1', '2']:
            raise ValueError("Invalid choice! Please select either 1 or 2.")

        # Single purchase
        if purchase_type == '1':
            quantity = 1  # Single purchase implies one unit
            total_price = calculate_total_price(quantity)
            print(f"You've selected a single coat rack. Total price: ${total_price:.2f}")

        # Bulk purchase
        elif purchase_type == '2':
            quantity_input = input("Enter the number of coat racks you want to purchase: ").strip()
            
            if not quantity_input.isdigit():
                raise ValueError("Invalid quantity! Please enter a positive integer.")
            
            quantity = int(quantity_input)
            
            if quantity <= 0:
                raise ValueError("Invalid quantity! Quantity must be greater than zero.")
            
            total_price = calculate_total_price(quantity)
            print(f"You've selected {quantity} coat racks. Total price: ${total_price:.2f}")

        # End of transaction
        print("Thank you for shopping at Shahkar Industry!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Exiting checkout process. Have a great day!")

# Entry point for the program
if __name__ == "__main__":
    try:
        checkout_process()
    except KeyboardInterrupt:
        print("\nCheckout process interrupted by user.")
        sys.exit(0)
```
