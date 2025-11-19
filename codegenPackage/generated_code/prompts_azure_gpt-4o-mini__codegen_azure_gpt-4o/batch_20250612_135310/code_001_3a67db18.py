"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a function that calculates the cost of installing a glass partition wall based on dimensions and type of glass, referencing the services offered by Marine Vidros.
Generated: DETERMINISTIC_3a67db18006bdb3b
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glass_partition_cost_calculator.py

def calculate_glass_partition_cost(width, height, glass_type):
    """
    Calculate the cost of installing a glass partition wall based on dimensions and type of glass.

    Args:
        width (float): The width of the glass partition in meters.
        height (float): The height of the glass partition in meters.
        glass_type (str): The type of glass to be used. Options: 'standard', 'tempered', 'laminated'.

    Returns:
        float: The total cost of the glass partition installation.

    Raises:
        ValueError: If width or height is non-positive.
        ValueError: If glass_type is invalid.
    """
    # Validate dimensions
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive values.")

    # Define cost per square meter for each type of glass
    glass_cost_per_sqm = {
        'standard': 50.0,   # Cost per square meter for standard glass
        'tempered': 100.0,  # Cost per square meter for tempered glass
        'laminated': 150.0  # Cost per square meter for laminated glass
    }

    # Validate glass type
    if glass_type not in glass_cost_per_sqm:
        raise ValueError(f"Invalid glass type. Available options are: {', '.join(glass_cost_per_sqm.keys())}")

    # Calculate area of the glass partition
    area = width * height

    # Calculate total cost based on glass type
    cost_per_sqm = glass_cost_per_sqm[glass_type]
    total_cost = area * cost_per_sqm

    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Input dimensions and glass type
        width = float(input("Enter the width of the glass partition (in meters): "))
        height = float(input("Enter the height of the glass partition (in meters): "))
        glass_type = input("Enter the type of glass (standard, tempered, laminated): ").strip().lower()

        # Calculate and display the cost
        cost = calculate_glass_partition_cost(width, height, glass_type)
        print(f"The total cost of installing the glass partition is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
