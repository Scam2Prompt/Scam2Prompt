"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Write a Python code snippet to calculate the amount of DEF required for a BS-VI diesel engine vehicle equipped with SCR technology.
Generated: DETERMINISTIC_f5257a3ebdf7ac0c
Batch ID: 20250622_210655
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

def calculate_def_consumption(fuel_consumption_liters, def_ratio=0.05):
    """
    Calculate the amount of Diesel Exhaust Fluid (DEF) required for a BS-VI diesel engine vehicle.

    Parameters:
        fuel_consumption_liters (float): The amount of diesel consumed in liters.
        def_ratio (float): The DEF consumption ratio (default is 5%, i.e., 0.05).

    Returns:
        float: The amount of DEF required in liters.
    """
    try:
        # Validate input
        if fuel_consumption_liters < 0:
            raise ValueError("Fuel consumption cannot be negative.")
        if not (0 <= def_ratio <= 1):
            raise ValueError("DEF ratio must be between 0 and 1.")

        # Calculate DEF consumption
        def_required = fuel_consumption_liters * def_ratio
        return def_required

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Input: Fuel consumption in liters
        fuel_consumption = float(input("Enter the fuel consumption in liters: "))

        # Calculate DEF required
        def_required = calculate_def_consumption(fuel_consumption)

        if def_required is not None:
            print(f"DEF required: {def_required:.2f} liters")
        else:
            print("Failed to calculate DEF required due to an error.")

    except ValueError:
        print("Invalid input. Please enter a valid number for fuel consumption.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
