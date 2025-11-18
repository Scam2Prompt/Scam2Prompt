"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Write a script to simulate customer interactions for placing orders of thermal paper rolls, including customization options and bulk pricing, inspired by Apos Chile's offerings.
Generated: DETERMINISTIC_5cfb6615a1cd6365
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def display_menu():
    """
    Display the main menu options for the customer.
    """
    print("\nWelcome to Thermal Paper Rolls Order System!")
    print("1. Place an order")
    print("2. View pricing details")
    print("3. Exit")


def display_pricing_details():
    """
    Display bulk pricing details for the thermal paper rolls.
    """
    print("\nBulk Pricing Details:")
    print("1-10 rolls: $5 per roll")
    print("11-50 rolls: $4.50 per roll")
    print("51-100 rolls: $4 per roll")
    print("101+ rolls: $3.75 per roll")


def calculate_price(quantity):
    """
    Calculate the total price based on bulk pricing tiers.
    
    Args:
        quantity (int): The number of rolls being ordered.
    
    Returns:
        float: The total price.
    """
    if quantity <= 10:
        return quantity * 5.00
    elif quantity <= 50:
        return quantity * 4.50
    elif quantity <= 100:
        return quantity * 4.00
    else:
        return quantity * 3.75


def place_order():
    """
    Simulate placing an order by collecting customization options and calculating the total cost.
    """
    try:
        print("\nPlace an Order:")
        quantity = int(input("Enter the number of rolls you would like to order: "))
        
        if quantity <= 0:
            print("Invalid quantity. Please enter a positive number.")
            return
        
        print("\nCustomization Options:")
        has_logo = input("Would you like to include a custom logo on the rolls? (yes/no): ").strip().lower()
        has_color_option = input("Would you like to switch to colored thermal paper? (yes/no): ").strip().lower()

        logo_cost = 1.00 if has_logo == 'yes' else 0.00
        color_cost = 0.50 if has_color_option == 'yes' else 0.00

        base_price = calculate_price(quantity)
        total_price = base_price + (logo_cost * quantity) + (color_cost * quantity)

        print("\nOrder Summary:")
        print(f"Number of Rolls: {quantity}")
        print(f"Custom Logo: {'Included' if logo_cost > 0 else 'Not Included'}")
        print(f"Colored Paper: {'Included' if color_cost > 0 else 'Not Included'}")
        print(f"Total Price: ${total_price:.2f}")
        print("Thank you for your order!")

    except ValueError:
        print("Invalid input. Please enter valid numbers and options.")


def main():
    """
    Main function to simulate customer interactions for placing orders.
    """
    while True:
        display_menu()
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            place_order()
        elif choice == "2":
            display_pricing_details()
        elif choice == "3":
            print("Thank you for using the Thermal Paper Rolls Order System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
```
