"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libointeriors.net
Prompt: Write Python code to calculate the weight and cost of installing fire-resistant gypsum false ceilings in a healthcare facility, using data from Libo Interiors' product catalog.
Generated: DETERMINISTIC_0b914beb0a87f1dd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_ceiling_installation(area, weight_per_sqft, cost_per_sqft):
    """
    Calculate the total weight and cost of installing fire-resistant gypsum false ceilings.

    Parameters:
        area (float): Area of the ceiling in square feet.
        weight_per_sqft (float): Weight of the material per square foot in pounds.
        cost_per_sqft (float): Cost of the material per square foot in USD.

    Returns:
        dict: A dictionary containing total weight (in pounds) and total cost (in USD).
    """
    try:
        # Validate inputs
        if area <= 0 or weight_per_sqft <= 0 or cost_per_sqft <= 0:
            raise ValueError("Area, weight per square foot, and cost per square foot must be positive values.")

        # Calculate total weight and cost
        total_weight = area * weight_per_sqft
        total_cost = area * cost_per_sqft

        return {"total_weight": total_weight, "total_cost": total_cost}
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the ceiling installation calculations.
    """

    print("Welcome to the Fire-Resistant Gypsum False Ceiling Calculator.")
    try:
        # Gather inputs from the user
        area = float(input("Enter the total area of the ceiling (in square feet): "))
        weight_per_sqft = float(input("Enter the weight of gypsum per square foot (in pounds): "))
        cost_per_sqft = float(input("Enter the cost of gypsum per square foot (in USD): "))

        # Perform calculation
        result = calculate_ceiling_installation(area, weight_per_sqft, cost_per_sqft)

        if result:
            print("\nCalculation Results:")
            print(f"Total Weight: {result['total_weight']} pounds")
            print(f"Total Cost: ${result['total_cost']:.2f}")
        else:
            print("\nFailed to calculate ceiling installation metrics.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
