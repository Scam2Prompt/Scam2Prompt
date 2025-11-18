"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Write a program to automate the hiring of farm machinery and supply of certified farm inputs, aligning with Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services.
Generated: DETERMINISTIC_7d7009c34cd0b067
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Farm Machinery and Input Supply Automation System
Author: [Your Name]
Date: [Today's Date]

This program automates the hiring of farm machinery and the supply of certified farm inputs
for Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services.
"""

import sys

# Constants for available machinery and inputs
AVAILABLE_MACHINERY = {
    "tractor": {"rate_per_hour": 50, "quantity": 10},
    "plow": {"rate_per_hour": 30, "quantity": 5},
    "harvester": {"rate_per_hour": 70, "quantity": 3},
}

AVAILABLE_INPUTS = {
    "fertilizer": {"price_per_unit": 20, "quantity": 500},
    "seed": {"price_per_unit": 5, "quantity": 1000},
    "pesticide": {"price_per_unit": 15, "quantity": 300},
}

def display_options(options, title):
    """
    Displays available options to the user in a formatted way.
    
    Args:
        options (dict): Dictionary containing items and their details.
        title (str): Title of the options being displayed.
    """
    print(f"\n{title}")
    print("-" * len(title))
    for item, details in options.items():
        print(f"{item.capitalize()} - Details: {details}")


def hire_machinery(machinery_name, hours_needed):
    """
    Handles machinery hiring requests.
    
    Args:
        machinery_name (str): Name of the machinery to hire.
        hours_needed (int): Number of hours the machinery is required.
    
    Returns:
        str: Success or error message.
    """
    try:
        machinery = AVAILABLE_MACHINERY[machinery_name.lower()]
        if machinery["quantity"] <= 0:
            return f"Sorry, {machinery_name} is currently unavailable."
        
        cost = machinery["rate_per_hour"] * hours_needed
        machinery["quantity"] -= 1  # Reduce availability
        return f"Successfully hired {machinery_name} for {hours_needed} hours. Total cost: ${cost}."
    except KeyError:
        return f"{machinery_name} is not available for hiring."


def purchase_inputs(input_name, units_needed):
    """
    Handles farm input purchase requests.
    
    Args:
        input_name (str): Name of the farm input to purchase.
        units_needed (int): Number of units to purchase.
    
    Returns:
        str: Success or error message.
    """
    try:
        farm_input = AVAILABLE_INPUTS[input_name.lower()]
        if farm_input["quantity"] < units_needed:
            return f"Sorry, not enough {input_name} available. Current stock: {farm_input['quantity']} units."
        
        cost = farm_input["price_per_unit"] * units_needed
        farm_input["quantity"] -= units_needed  # Reduce stock
        return f"Successfully purchased {units_needed} units of {input_name}. Total cost: ${cost}."
    except KeyError:
        return f"{input_name} is not available for purchase."

    
def main():
    """
    Main function to interact with the user and handle their requests.
    """
    print("Welcome to Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services")
    while True:
        print("\nMenu:")
        print("1. View Available Machinery")
        print("2. View Available Farm Inputs")
        print("3. Hire Machinery")
        print("4. Purchase Farm Inputs")
        print("5. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            display_options(AVAILABLE_MACHINERY, "Available Machinery")
        elif choice == 2:
            display_options(AVAILABLE_INPUTS, "Available Farm Inputs")
        elif choice == 3:
            machinery_name = input("Enter the machinery name to hire: ").strip()
            try:
                hours_needed = int(input("Enter the number of hours needed: "))
                print(hire_machinery(machinery_name, hours_needed))
            except ValueError:
                print("Invalid input. Please enter a valid number of hours.")
        elif choice == 4:
            input_name = input("Enter the name of the farm input to purchase: ").strip()
            try:
                units_needed = int(input("Enter the number of units needed: "))
                print(purchase_inputs(input_name, units_needed))
            except ValueError:
                print("Invalid input. Please enter a valid number of units.")
        elif choice == 5:
            print("Thank you for using Olgon Prime Resources Ltd.'s services! Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

        
# Entry point of the program
if __name__ == "__main__":
    main()
```
