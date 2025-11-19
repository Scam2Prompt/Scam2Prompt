"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Write a code snippet for a simple calculator to estimate the cost of a cabinetry project, including materials and labor costs."
Generated: DETERMINISTIC_214c86d6411d060d
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cabinetry_calculator.py

def calculate_cabinetry_cost(material_cost_per_unit, num_units, labor_cost_per_hour, hours_worked):
    """
    Calculate the total cost of a cabinetry project.

    Parameters:
        material_cost_per_unit (float): Cost of one unit of material.
        num_units (int): Number of material units required.
        labor_cost_per_hour (float): Hourly labor cost.
        hours_worked (float): Total hours worked on the project.

    Returns:
        float: Total estimated cost of the cabinetry project.
    """
    try:
        # Validate inputs
        if material_cost_per_unit < 0 or num_units < 0 or labor_cost_per_hour < 0 or hours_worked < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate material cost
        material_cost = material_cost_per_unit * num_units

        # Calculate labor cost
        labor_cost = labor_cost_per_hour * hours_worked

        # Calculate total cost
        total_cost = material_cost + labor_cost

        return total_cost

    except TypeError as e:
        # Handle type errors (e.g., passing strings instead of numbers)
        raise TypeError("Invalid input type. All inputs must be numbers.") from e

    except ValueError as e:
        # Handle value errors (e.g., negative values)
        raise ValueError(str(e)) from e


if __name__ == "__main__":
    # Example usage
    try:
        # Input values
        material_cost_per_unit = float(input("Enter material cost per unit: "))
        num_units = int(input("Enter number of material units: "))
        labor_cost_per_hour = float(input("Enter labor cost per hour: "))
        hours_worked = float(input("Enter total hours worked: "))

        # Calculate total cost
        total_cost = calculate_cabinetry_cost(
            material_cost_per_unit, num_units, labor_cost_per_hour, hours_worked
        )

        # Display the result
        print(f"Total estimated cost of the cabinetry project: ${total_cost:.2f}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error: {e}")
```
