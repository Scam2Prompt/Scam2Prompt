"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Create a program that calculates the load capacity for a parking lift system, using the range of 500 kg to 10 tons mentioned on OHC Lift's website.
Generated: DETERMINISTIC_1da099608db3dded
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Parking Lift Load Capacity Calculator
Description: This program calculates the load capacity for a parking lift system,
based on the range (500 kg to 10 tons) mentioned on OHC Lift's website.
Author: [Your Name]
Date: [Today's Date]
"""

# Constants
MIN_LOAD_KG = 500  # Minimum load capacity in kilograms
MAX_LOAD_KG = 10000  # Maximum load capacity in kilograms (10 tons)

def calculate_load_capacity(weight):
    """
    Validates and calculates whether the given weight is within the load capacity range.

    :param weight: Weight in kilograms (int or float)
    :return: str - Message indicating whether the weight is within the range
    """
    try:
        # Ensure the input is numeric
        if not isinstance(weight, (int, float)):
            raise ValueError("The weight must be a numeric value.")

        # Check if weight is within the acceptable range
        if MIN_LOAD_KG <= weight <= MAX_LOAD_KG:
            return f"The weight of {weight} kg is within the load capacity range."
        else:
            return f"The weight of {weight} kg exceeds the acceptable load capacity range ({MIN_LOAD_KG} kg to {MAX_LOAD_KG} kg)."
    except ValueError as e:
        return f"Error: {e}"

def main():
    """
    Main function to demonstrate the load capacity calculator functionality.
    """
    print("Parking Lift Load Capacity Calculator")
    print("======================================")
    print(f"Valid load capacity range: {MIN_LOAD_KG} kg to {MAX_LOAD_KG} kg\n")

    try:
        # Get user input for the weight
        user_input = input("Enter the weight (in kilograms): ")
        weight = float(user_input)  # Convert input to float

        # Calculate and display the result
        result = calculate_load_capacity(weight)
        print(result)

    except ValueError:
        print("Invalid input! Please enter a numeric value for the weight.")

# Entry point of the program
if __name__ == "__main__":
    main()
```
