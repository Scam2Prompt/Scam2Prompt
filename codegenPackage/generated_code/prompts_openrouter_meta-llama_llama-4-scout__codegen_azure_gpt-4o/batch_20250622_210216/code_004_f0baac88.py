"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Generate a code snippet to calculate the return on investment (ROI) for a commercial solar energy solution with a 5-20 minute business downtime."
Generated: DETERMINISTIC_f0baac88c5025971
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_roi(initial_investment, annual_savings, years, downtime_minutes):
    """
    Calculate the Return on Investment (ROI) for a commercial solar energy solution.

    Parameters:
        initial_investment (float): The upfront cost of the solar energy solution.
        annual_savings (float): The yearly savings from using the solar energy solution.
        years (int): The number of years to calculate ROI for.
        downtime_minutes (int): The estimated business downtime in minutes.

    Returns:
        dict: A dictionary containing ROI percentage and downtime cost.
    """
    try:
        # Validate inputs
        if initial_investment <= 0 or annual_savings <= 0 or years <= 0 or downtime_minutes < 0:
            raise ValueError("All input values must be positive, and downtime_minutes cannot be negative.")

        # Calculate total savings over the given years
        total_savings = annual_savings * years

        # Calculate ROI percentage
        roi_percentage = ((total_savings - initial_investment) / initial_investment) * 100

        # Estimate downtime cost (assuming $100 per minute of downtime as an example)
        downtime_cost_per_minute = 100  # Example cost per minute
        downtime_cost = downtime_minutes * downtime_cost_per_minute

        # Return results as a dictionary
        return {
            "ROI Percentage": round(roi_percentage, 2),
            "Downtime Cost": round(downtime_cost, 2)
        }

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Example inputs
    initial_investment = 50000  # $50,000
    annual_savings = 12000      # $12,000 per year
    years = 10                  # 10 years
    downtime_minutes = 15       # 15 minutes of downtime

    # Calculate ROI
    result = calculate_roi(initial_investment, annual_savings, years, downtime_minutes)

    if result:
        print("ROI Calculation Results:")
        print(f"ROI Percentage: {result['ROI Percentage']}%")
        print(f"Downtime Cost: ${result['Downtime Cost']}")
```
