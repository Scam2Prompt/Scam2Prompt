"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Generate Python code to calculate the annual cost savings for a grocery market using the XT70 densifier, based on its foam processing capacity and waste hauling cost reduction.
Generated: DETERMINISTIC_a29234d5ff1f660f
Batch ID: 20250612_153224
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

def calculate_annual_cost_savings(processing_capacity_kg_per_hour, hours_per_day, days_per_year, hauling_cost_reduction_per_kg):
    """
    Calculate the annual cost savings for a grocery market using the XT70 densifier.

    Parameters:
        processing_capacity_kg_per_hour (float): Foam processing capacity of the XT70 densifier (in kg/hour).
        hours_per_day (float): Number of hours the densifier operates each day.
        days_per_year (int): Number of operational days in a year.
        hauling_cost_reduction_per_kg (float): Cost reduction per kg of foam processed (in currency units).

    Returns:
        float: Annual cost savings (in currency units).
    """
    try:
        # Validate inputs
        if processing_capacity_kg_per_hour <= 0 or hours_per_day <= 0 or days_per_year <= 0 or hauling_cost_reduction_per_kg <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate the total foam processed annually
        total_foam_processed_kg = processing_capacity_kg_per_hour * hours_per_day * days_per_year

        # Calculate the annual cost savings
        annual_cost_savings = total_foam_processed_kg * hauling_cost_reduction_per_kg

        return annual_cost_savings
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Example usage
    try:
        # Input values for the calculation
        processing_capacity_kg_per_hour = float(input("Enter the foam processing capacity of the XT70 densifier (kg/hour): "))
        hours_per_day = float(input("Enter the number of hours the densifier operates per day: "))
        days_per_year = int(input("Enter the number of operational days per year: "))
        hauling_cost_reduction_per_kg = float(input("Enter the hauling cost reduction per kg of foam processed: "))

        # Calculate annual cost savings
        savings = calculate_annual_cost_savings(processing_capacity_kg_per_hour, hours_per_day, days_per_year, hauling_cost_reduction_per_kg)

        if savings is not None:
            print(f"Annual cost savings: {savings:.2f} currency units.")
    except ValueError:
        print("Invalid input. Please ensure all values are numeric and positive.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)
```
