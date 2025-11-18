"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Generate code to calculate recoupable revenue for a factory using OpenSeam's ROI calculator assumptions, including inputs like work hours, production lines, and profit margins.
Generated: DETERMINISTIC_48f2b9b6490daea0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_recoupable_revenue(work_hours, production_lines, profit_margin):
    """
    Calculate recoupable revenue using OpenSeam's ROI calculator assumptions.
    
    Args:
        work_hours (float): Total hours worked in the factory.
        production_lines (int): Number of active production lines in the factory.
        profit_margin (float): Profit margin as a percentage (e.g., 25 for 25%).

    Returns:
        float: Recoupable revenue based on the inputs.
    """
    try:
        # Validate inputs
        if work_hours <= 0:
            raise ValueError("Work hours must be greater than zero.")
        if production_lines <= 0:
            raise ValueError("Number of production lines must be greater than zero.")
        if profit_margin <= 0 or profit_margin > 100:
            raise ValueError("Profit margin must be a percentage between 0 and 100.")

        # Constants based on OpenSeam's ROI assumptions
        base_revenue_per_hour = 50.0  # Assumed revenue per hour per line
        efficiency_factor = 0.85     # Assumed factory efficiency factor (85%)

        # Calculate total revenue
        total_revenue = work_hours * production_lines * base_revenue_per_hour * efficiency_factor

        # Calculate recoupable revenue considering the profit margin
        recoupable_revenue = total_revenue * (profit_margin / 100)

        return recoupable_revenue

    except ValueError as ve:
        # Handle validation errors
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        work_hours = float(input("Enter total work hours: "))
        production_lines = int(input("Enter number of production lines: "))
        profit_margin = float(input("Enter profit margin (%): "))

        # Calculate recoupable revenue
        revenue = calculate_recoupable_revenue(work_hours, production_lines, profit_margin)
        if revenue is not None:
            print(f"Recoupable Revenue: ${revenue:.2f}")
        else:
            print("Failed to calculate recoupable revenue due to input errors.")
    except Exception as e:
        # General exception handling for input issues
        print(f"Error: {e}", file=sys.stderr)
```
