"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Provide a Python script to calculate the cost of stainless steel coils based on their weight and the competitive pricing model described on Hilde Inox for "Paslanmaz Şerit / Rulo."
Generated: DETERMINISTIC_5191e74d77eb9608
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Calculate the Cost of Stainless Steel Coils Based on Weight and Pricing Model.

This script implements a competitive pricing model for stainless steel coils inspired by Hilde Inox's 
pricing calculations for "Paslanmaz Şerit / Rulo". The user can input weight and unit price to calculate 
the total cost.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

def calculate_stainless_steel_cost(weight_kg, price_per_kg):
    """
    Calculate the cost of stainless steel coils based on weight and unit price.
    
    Args:
        weight_kg (float): Weight of the stainless steel coil in kilograms (kg).
        price_per_kg (float): Price per kilogram in the competitive pricing model.
    
    Returns:
        float: Total cost of the stainless steel coil.
    
    Raises:
        ValueError: If weight or price is negative or non-numeric.
    """
    try:
        # Validate input
        if weight_kg <= 0 or price_per_kg <= 0:
            raise ValueError("Weight and price per kilogram must be positive values.")
        # Calculate total cost
        total_cost = weight_kg * price_per_kg
        return total_cost
    except TypeError as te:
        raise ValueError("Invalid input types. Please provide numeric values.") from te


def main():
    """
    Main function to execute the stainless steel coil cost calculation.
    
    Prompts the user for weight and pricing input, calculates the cost, and displays the result.
    """
    print("Stainless Steel Coil Cost Calculator")
    print("-----------------------------------")
    
    try:
        # Get user input
        weight_kg = float(input("Enter the weight of the stainless steel coil (kg): "))
        price_per_kg = float(input("Enter the price per kilogram (in your currency): "))
        
        # Calculate the cost
        total_cost = calculate_stainless_steel_cost(weight_kg, price_per_kg)
        
        # Display the result
        print(f"The total cost of the stainless steel coil is: {total_cost:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
