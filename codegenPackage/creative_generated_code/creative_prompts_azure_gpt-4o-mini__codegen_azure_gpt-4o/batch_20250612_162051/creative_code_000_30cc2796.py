"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a Python script to calculate the potential savings from using the XT-300D EPS densifier for a business processing 250 lbs of loose foam per hour.
Generated: DETERMINISTIC_30cc2796c74a910e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_savings(processing_rate_lbs_per_hour, hours_per_day, days_per_week, tipping_fee_per_ton, disposal_cost_per_pound, foam_reduction_rate=90):
    """
    Calculate potential savings from using the XT-300D EPS densifier.

    Parameters:
        processing_rate_lbs_per_hour (float): Amount of loose foam processed per hour (lbs).
        hours_per_day (int): Operating hours per day.
        days_per_week (int): Operating days per week.
        tipping_fee_per_ton (float): Tipping fee for foam disposal ($ per ton).
        disposal_cost_per_pound (float): Cost of disposing loose foam without densifier ($ per pound).
        foam_reduction_rate (float): Percentage reduction in foam volume by the densifier (default: 90%).

    Returns:
        float: Estimated weekly savings in USD.
    """
    try:
        # Constants
        LBS_PER_TON = 2000  # Pounds in a ton

        # Calculate total foam processed per week (lbs)
        weekly_processed_foam_lbs = processing_rate_lbs_per_hour * hours_per_day * days_per_week

        # Calculate disposal cost without the densifier
        weekly_disposal_cost_without_densifier = weekly_processed_foam_lbs * disposal_cost_per_pound

        # Calculate the reduced foam weight after using the densifier
        reduced_foam_weight_lbs = weekly_processed_foam_lbs * (1 - foam_reduction_rate / 100)

        # Calculate disposal cost with the densifier
        tipping_fee_per_lb = tipping_fee_per_ton / LBS_PER_TON
        weekly_disposal_cost_with_densifier = reduced_foam_weight_lbs * tipping_fee_per_lb

        # Calculate potential savings
        potential_savings = weekly_disposal_cost_without_densifier - weekly_disposal_cost_with_densifier

        return potential_savings

    except Exception as e:
        # Log the error and exit gracefully
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Parameters (example values)
    PROCESSING_RATE_LBS_PER_HOUR = 250  # Foam processing rate per hour (lbs)
    HOURS_PER_DAY = 8                   # Operating hours per day
    DAYS_PER_WEEK = 5                   # Operating days per week
    TIPPING_FEE_PER_TON = 50.0          # Tipping fee ($ per ton)
    DISPOSAL_COST_PER_POUND = 0.25      # Loose foam disposal cost ($ per pound)

    # Calculate potential savings
    savings = calculate_potential_savings(
        processing_rate_lbs_per_hour=PROCESSING_RATE_LBS_PER_HOUR,
        hours_per_day=HOURS_PER_DAY,
        days_per_week=DAYS_PER_WEEK,
        tipping_fee_per_ton=TIPPING_FEE_PER_TON,
        disposal_cost_per_pound=DISPOSAL_COST_PER_POUND
    )

    # Display the result to the user
    if savings is not None:
        print(f"Estimated weekly savings from using the XT-300D EPS densifier: ${savings:,.2f}")
    else:
        print("An error occurred while calculating potential savings. Please check your inputs.")
```
