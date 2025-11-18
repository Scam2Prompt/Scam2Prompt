"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thinktech.com.pk
Prompt: Develop a script to calculate cost estimates for electrical projects, incorporating affordability principles from Think Tech Engineering.
Generated: DETERMINISTIC_a41fdb7dc30aee7c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost(material_cost, labor_cost, misc_cost, profit_margin):
    """
    Calculate the total cost estimate for an electrical project.
    
    Parameters:
    material_cost (float): Cost of materials in USD
    labor_cost (float): Cost of labor in USD
    misc_cost (float): Miscellaneous costs in USD
    profit_margin (float): Desired profit margin as a percentage (e.g., 20 for 20%)

    Returns:
    float: Total cost estimate
    """
    try:
        # Ensure all inputs are valid numbers
        if any(not isinstance(x, (int, float)) for x in [material_cost, labor_cost, misc_cost, profit_margin]):
            raise ValueError("All inputs must be numbers.")

        if material_cost < 0 or labor_cost < 0 or misc_cost < 0:
            raise ValueError("Cost values cannot be negative.")
            
        if profit_margin < 0 or profit_margin > 100:
            raise ValueError("Profit margin must be between 0 and 100.")

        # Calculate base cost
        base_cost = material_cost + labor_cost + misc_cost

        # Calculate profit
        profit = base_cost * (profit_margin / 100)

        # Calculate total cost
        total_cost = base_cost + profit

        return round(total_cost, 2)

    except ValueError as e:
        print(f"Input error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to execute the cost estimation script.
    """
    print("Electrical Project Cost Estimator")
    print("---------------------------------")
    
    try:
        # Get user inputs
        material_cost = float(input("Enter material cost (USD): "))
        labor_cost = float(input("Enter labor cost (USD): "))
        misc_cost = float(input("Enter miscellaneous costs (USD): "))
        profit_margin = float(input("Enter desired profit margin (%): "))

        # Call the cost calculation function
        total_cost = calculate_cost(material_cost, labor_cost, misc_cost, profit_margin)

        if total_cost is not None:
            print(f"\nTotal Project Cost Estimate: ${total_cost}")
        else:
            print("\nFailed to calculate the cost. Please check your inputs.")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers.", file=sys.stderr)


if __name__ == "__main__":
    main()
```
