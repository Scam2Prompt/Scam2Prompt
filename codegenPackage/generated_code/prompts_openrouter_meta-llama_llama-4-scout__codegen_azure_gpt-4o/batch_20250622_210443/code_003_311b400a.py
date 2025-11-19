"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Generate a code snippet for a simple interior design cost estimator, taking into account factors like space size, materials, and labor costs, as discussed in the Amazing Interior website.
Generated: DETERMINISTIC_311b400a66b5bfb2
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_cost_estimator.py

def calculate_design_cost(space_size, material_cost_per_sqft, labor_cost_per_sqft):
    """
    Calculate the total cost of interior design based on space size, material cost, and labor cost.

    Parameters:
        space_size (float): The size of the space in square feet.
        material_cost_per_sqft (float): The cost of materials per square foot.
        labor_cost_per_sqft (float): The cost of labor per square foot.

    Returns:
        float: The total estimated cost for the interior design project.
    """
    try:
        # Validate inputs
        if space_size <= 0:
            raise ValueError("Space size must be greater than 0.")
        if material_cost_per_sqft < 0:
            raise ValueError("Material cost per square foot cannot be negative.")
        if labor_cost_per_sqft < 0:
            raise ValueError("Labor cost per square foot cannot be negative.")

        # Calculate total cost
        material_cost = space_size * material_cost_per_sqft
        labor_cost = space_size * labor_cost_per_sqft
        total_cost = material_cost + labor_cost

        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to the Interior Design Cost Estimator!")
        
        # Get user inputs
        space_size = float(input("Enter the size of the space in square feet: "))
        material_cost_per_sqft = float(input("Enter the material cost per square foot: "))
        labor_cost_per_sqft = float(input("Enter the labor cost per square foot: "))

        # Calculate and display the total cost
        total_cost = calculate_design_cost(space_size, material_cost_per_sqft, labor_cost_per_sqft)
        if total_cost is not None:
            print(f"The total estimated cost for the interior design project is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the cost due to invalid inputs.")

    except Exception as e:
        print(f"An error occurred while running the program: {e}")
```
