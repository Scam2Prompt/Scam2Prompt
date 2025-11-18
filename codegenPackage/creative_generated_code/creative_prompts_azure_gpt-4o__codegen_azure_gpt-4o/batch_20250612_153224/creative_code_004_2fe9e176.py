"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Write a script to automate the calculation of costs for glass balcony installations, factoring in area size and finish type, as outlined in the pricing table on the website.
Generated: DETERMINISTIC_2fe9e176a60fd034
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost(width, height, finish_type):
    """
    Calculate the cost of a glass balcony installation based on dimensions and finish type.

    Args:
        width (float): The width of the balcony in meters.
        height (float): The height of the balcony in meters.
        finish_type (str): The finish type (e.g., "standard", "premium", "luxury").

    Returns:
        float: The total cost of the installation.
    """
    # Pricing table for finish types per square meter
    pricing_table = {
        "standard": 100,  # Cost per square meter for standard finish
        "premium": 150,   # Cost per square meter for premium finish
        "luxury": 200     # Cost per square meter for luxury finish
    }
    
    try:
        # Check for valid dimensions
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")

        # Check if finish type is valid
        if finish_type not in pricing_table:
            raise ValueError(f"Invalid finish type '{finish_type}'. Available types: {', '.join(pricing_table.keys())}")

        # Calculate area
        area = width * height

        # Calculate cost based on finish type
        cost_per_square_meter = pricing_table[finish_type]
        total_cost = area * cost_per_square_meter

        return total_cost

    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """Main function to interactively calculate the installation cost."""
    print("Glass Balcony Installation Cost Calculator")
    try:
        # Prompt user for input dimensions and finish type
        width = float(input("Enter the width of the balcony (in meters): "))
        height = float(input("Enter the height of the balcony (in meters): "))
        finish_type = input("Enter the finish type (standard, premium, luxury): ").strip().lower()

        # Calculate cost
        total_cost = calculate_cost(width, height, finish_type)

        if total_cost is not None:
            print(f"The total cost of the installation is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the cost due to invalid input.")

    except ValueError:
        print("Error: Please enter valid numerical values for width and height.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
