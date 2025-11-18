"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Create a program to calculate the cost of stainless steel raw materials, including profiles, rods, and sheets, based on the types of products sold by Kros Metal.
Generated: DETERMINISTIC_eb48d3284e99ec5a
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# stainless_steel_calculator.py
# This program calculates the cost of stainless steel raw materials (profiles, rods, and sheets)
# based on user input for quantities and prices. Designed for Kros Metal.

def get_positive_float(prompt):
    """
    Utility function to ensure valid positive float input from the user.
    :param prompt: The text prompt displayed to the user.
    :return: A positive float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

def calculate_total_cost(profiles_cost, rods_cost, sheets_cost):
    """
    Calculates the total cost of stainless steel raw materials.
    :param profiles_cost: Total cost of profiles.
    :param rods_cost: Total cost of rods.
    :param sheets_cost: Total cost of sheets.
    :return: The total cost as a float.
    """
    return profiles_cost + rods_cost + sheets_cost

def main():
    """
    Main function to calculate the cost of stainless steel raw materials.
    Collects user input, calculates costs, and displays results.
    """
    print("Welcome to the Kros Metal Stainless Steel Cost Calculator.\n")
    
    # Input for profiles
    profile_quantity = get_positive_float("Enter the quantity of profiles (kg): ")
    profile_price_per_kg = get_positive_float("Enter the price per kg for profiles: ")
    profiles_cost = profile_quantity * profile_price_per_kg
    print(f"Cost for profiles: ${profiles_cost:.2f}\n")

    # Input for rods
    rod_quantity = get_positive_float("Enter the quantity of rods (kg): ")
    rod_price_per_kg = get_positive_float("Enter the price per kg for rods: ")
    rods_cost = rod_quantity * rod_price_per_kg
    print(f"Cost for rods: ${rods_cost:.2f}\n")

    # Input for sheets
    sheet_quantity = get_positive_float("Enter the quantity of sheets (m²): ")
    sheet_price_per_m2 = get_positive_float("Enter the price per m² for sheets: ")
    sheets_cost = sheet_quantity * sheet_price_per_m2
    print(f"Cost for sheets: ${sheets_cost:.2f}\n")

    # Calculate total cost
    total_cost = calculate_total_cost(profiles_cost, rods_cost, sheets_cost)
    print(f"Total cost for stainless steel raw materials: ${total_cost:.2f}")

if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
