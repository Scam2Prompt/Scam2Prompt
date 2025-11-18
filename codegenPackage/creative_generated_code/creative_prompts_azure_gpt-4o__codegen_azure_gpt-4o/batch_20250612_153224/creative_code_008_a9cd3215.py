"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Write a script to calculate the cost of timber products based on dimensions and species, referencing the categories of softwood, hardwood, and sawn timber from Askar Trading International.
Generated: DETERMINISTIC_a9cd3215e972cd59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# timber_cost_calculator.py
"""
A script to calculate the cost of timber products based on dimensions, species, and category.
Categories: Softwood, Hardwood, and Sawn Timber.
Source: Askar Trading International.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

# Timber pricing per cubic meter (USD)
PRICING = {
    "softwood": 250,  # Price per cubic meter for softwood
    "hardwood": 400,  # Price per cubic meter for hardwood
    "sawn_timber": 350  # Price per cubic meter for sawn timber
}

def validate_input(value, name):
    """
    Validates user input to ensure it is a positive number.
    """
    try:
        value = float(value)
        if value <= 0:
            raise ValueError(f"{name} must be a positive number.")
        return value
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def calculate_volume(length, width, height):
    """
    Calculates the volume of timber given dimensions in meters.
    """
    return length * width * height

def calculate_cost(volume, category):
    """
    Calculates the cost of timber based on volume and category.
    """
    if category not in PRICING:
        raise ValueError(f"Invalid category '{category}'. Valid categories are: {', '.join(PRICING.keys())}.")
    return volume * PRICING[category]

def main():
    """
    Main function to prompt user input and calculate timber cost.
    """
    print("Welcome to the Timber Cost Calculator!")
    print("Categories: softwood, hardwood, sawn_timber")

    # Get user inputs
    length = input("Enter timber length (meters): ")
    width = input("Enter timber width (meters): ")
    height = input("Enter timber height (meters): ")
    category = input("Enter timber category (softwood/hardwood/sawn_timber): ").strip().lower()

    # Validate inputs
    length = validate_input(length, "Length")
    width = validate_input(width, "Width")
    height = validate_input(height, "Height")

    # Calculate volume
    volume = calculate_volume(length, width, height)

    try:
        # Calculate cost
        cost = calculate_cost(volume, category)
        print(f"\nThe cost of the timber product is: ${cost:.2f} USD")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
