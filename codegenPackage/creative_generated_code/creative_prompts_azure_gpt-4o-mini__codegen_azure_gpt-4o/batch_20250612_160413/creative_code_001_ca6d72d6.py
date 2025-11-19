"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stablegrowthassets.com
Prompt: Write a code snippet that calculates potential ROI for different investment plans, such as the Starter Plan and the Platinum Plan, as described on Stable Growth Assets.
Generated: DETERMINISTIC_ca6d72d68d4db536
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to calculate potential ROI for different investment plans.
This script takes inputs for the initial investment, annual return rates, and
investment duration to calculate the total ROI for plans like Starter and Platinum.
"""

# Import necessary modules
import sys

def calculate_roi(initial_investment, annual_rate, years):
    """
    Calculate the Return on Investment (ROI) based on the given parameters.

    Parameters:
        initial_investment (float): The starting amount of the investment.
        annual_rate (float): The annual rate of return as a percentage.
        years (int): The investment duration in years.

    Returns:
        float: The total ROI after the investment period.
    """
    try:
        # Ensure inputs are valid
        if initial_investment < 0 or annual_rate < 0 or years < 0:
            raise ValueError("Investment, rate, and duration must be non-negative.")
        
        # Formula for compound interest: A = P * (1 + r)^t
        total_amount = initial_investment * (1 + annual_rate / 100) ** years
        
        # ROI is the total amount minus the initial investment
        roi = total_amount - initial_investment
        return round(roi, 2)
    except Exception as e:
        print(f"Error calculating ROI: {e}", file=sys.stderr)
        return None

def main():
    """
    Main execution function to calculate ROI for different investment plans.
    """
    print("### Investment ROI Calculator ###")

    # Define investment plans
    plans = {
        "Starter Plan": {"initial_investment": 5000, "annual_rate": 5, "years": 10},
        "Platinum Plan": {"initial_investment": 20000, "annual_rate": 8, "years": 15},
    }

    # Calculate and display ROI for each plan
    for plan_name, details in plans.items():
        try:
            print(f"\nCalculating ROI for {plan_name}...")
            roi = calculate_roi(
                initial_investment=details["initial_investment"],
                annual_rate=details["annual_rate"],
                years=details["years"]
            )
            if roi is not None:
                print(f"Plan: {plan_name}")
                print(f"Initial Investment: ${details['initial_investment']}")
                print(f"Annual Rate: {details['annual_rate']}%")
                print(f"Duration: {details['years']} years")
                print(f"Potential ROI: ${roi}")
        except Exception as e:
            print(f"Failed to process {plan_name}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
