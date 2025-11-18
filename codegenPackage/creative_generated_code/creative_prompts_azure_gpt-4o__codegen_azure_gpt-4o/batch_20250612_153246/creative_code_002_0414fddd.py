"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Generate a script to estimate the cost of implementing StoTherm EIFS systems in a construction project, incorporating material and labor costs as described on the Engenharia WPJ website.
Generated: DETERMINISTIC_0414fdddf29b2faa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost(material_cost_per_sqm, labor_cost_per_sqm, area_sqm):
    """
    Calculate the total cost of StoTherm EIFS system implementation.

    Args:
        material_cost_per_sqm (float): Cost of materials per square meter.
        labor_cost_per_sqm (float): Cost of labor per square meter.
        area_sqm (float): Total area in square meters to be covered.

    Returns:
        float: Total cost for the project.
    """
    try:
        # Ensure inputs are valid numbers
        if material_cost_per_sqm < 0 or labor_cost_per_sqm < 0 or area_sqm <= 0:
            raise ValueError("Costs and area must be positive numbers.")
        
        # Calculate total cost
        total_material_cost = material_cost_per_sqm * area_sqm
        total_labor_cost = labor_cost_per_sqm * area_sqm
        total_cost = total_material_cost + total_labor_cost

        return total_cost
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to interact with the user and estimate StoTherm EIFS costs.
    """
    try:
        print("StoTherm EIFS Cost Estimation")
        
        # Get user input
        material_cost_per_sqm = float(input("Enter material cost per square meter: "))
        labor_cost_per_sqm = float(input("Enter labor cost per square meter: "))
        area_sqm = float(input("Enter total area in square meters to be covered: "))

        # Calculate cost using the function
        total_cost = calculate_cost(material_cost_per_sqm, labor_cost_per_sqm, area_sqm)

        if total_cost is not None:
            print(f"\nEstimated total cost for the project: ${total_cost:.2f}")
        else:
            print("\nCould not calculate the total cost due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the StoTherm EIFS Cost Estimation tool.")

if __name__ == "__main__":
    # Ensure compatibility with different Python environments
    try:
        main()
    except Exception as e:
        print(f"Critical error in execution: {e}")
        sys.exit(1)
```
