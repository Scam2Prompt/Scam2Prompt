"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write Python code to calculate the cost savings from using the XT300D EPS foam densifier, given input parameters like waste hauling cost reduction percentage, foam processing capacity, and operational cost.
Generated: DETERMINISTIC_cef010b646f118c8
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

def calculate_cost_savings(hauling_cost_reduction_percentage, foam_processing_capacity, operational_cost):
    """
    Calculates cost savings from using the XT300D EPS foam densifier.

    Parameters:
        hauling_cost_reduction_percentage (float): Percentage reduction in waste hauling costs (e.g., 20 for 20% reduction).
        foam_processing_capacity (float): Monthly foam processing capacity in tons.
        operational_cost (float): Monthly operational cost in USD.

    Returns:
        float: Monthly cost savings in USD.
    """
    try:
        # Validate the input parameters
        if hauling_cost_reduction_percentage < 0 or hauling_cost_reduction_percentage > 100:
            raise ValueError("Hauling cost reduction percentage must be between 0 and 100.")
        if foam_processing_capacity <= 0:
            raise ValueError("Foam processing capacity must be greater than 0.")
        if operational_cost < 0:
            raise ValueError("Operational cost cannot be negative.")
        
        # Assume hauling cost per ton before using XT300D (example value, can be parameterized)
        hauling_cost_per_ton = 200  # USD per ton

        # Calculate hauling cost savings
        hauling_cost_savings = (hauling_cost_reduction_percentage / 100) * foam_processing_capacity * hauling_cost_per_ton

        # Calculate total savings
        total_savings = hauling_cost_savings - operational_cost

        return total_savings

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        hauling_cost_reduction_percentage = float(input("Enter hauling cost reduction percentage (e.g., 20 for 20%): "))
        foam_processing_capacity = float(input("Enter foam processing capacity in tons per month: "))
        operational_cost = float(input("Enter operational cost in USD per month: "))

        # Calculate cost savings
        cost_savings = calculate_cost_savings(
            hauling_cost_reduction_percentage, foam_processing_capacity, operational_cost
        )

        if cost_savings is not None:
            print(f"Monthly cost savings: ${cost_savings:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
```
