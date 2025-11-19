"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Develop a simple calculator to determine the cost of pigments and additives required for a specific project."
Generated: DETERMINISTIC_d270cf93df6a4cc0
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def get_float_input(prompt):
    """
    Safely get a float input from the user.
    Args:
        prompt (str): The input prompt for the user.
    Returns:
        float: The validated float input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive number.")

def calculate_cost(pigment_cost_per_unit, pigment_units, additive_cost_per_unit, additive_units):
    """
    Calculate the total cost of pigments and additives.
    Args:
        pigment_cost_per_unit (float): Cost per unit of pigment.
        pigment_units (float): Number of pigment units required.
        additive_cost_per_unit (float): Cost per unit of additive.
        additive_units (float): Number of additive units required.
    Returns:
        float: Total cost of pigments and additives.
    """
    try:
        pigment_cost = pigment_cost_per_unit * pigment_units
        additive_cost = additive_cost_per_unit * additive_units
        total_cost = pigment_cost + additive_cost
        return total_cost
    except Exception as e:
        print(f"Error calculating cost: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the calculator.
    """
    print("Welcome to the Pigment and Additive Cost Calculator!")
    
    # Get user inputs
    pigment_cost_per_unit = get_float_input("Enter the cost per unit of pigment: ")
    pigment_units = get_float_input("Enter the number of pigment units required: ")
    additive_cost_per_unit = get_float_input("Enter the cost per unit of additive: ")
    additive_units = get_float_input("Enter the number of additive units required: ")
    
    # Calculate total cost
    total_cost = calculate_cost(pigment_cost_per_unit, pigment_units, additive_cost_per_unit, additive_units)
    
    # Display the result
    print(f"\nThe total cost of pigments and additives for the project is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
