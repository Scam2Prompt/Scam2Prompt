"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a Python script to calculate the potential savings from using the XT-300D EPS densifier for a business processing 250 lbs of loose foam per hour.
Generated: DETERMINISTIC_30cc2796c74a910e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# xt_300d_eps_calculator.py

"""
Calculates the potential savings from using the XT-300D EPS densifier.

This script takes into account the amount of loose foam processed per hour and 
provides an estimate of the savings based on the densification ratio and 
disposal cost per cubic foot of loose foam.
"""

def calculate_savings(
    loose_foam_per_hour: float, 
    densification_ratio: float, 
    disposal_cost_per_cubic_foot: float, 
    compacted_foam_disposal_cost_per_cubic_foot: float
) -> dict:
    """
    Calculates the potential savings.

    Args:
    - loose_foam_per_hour (float): The amount of loose foam processed per hour in lbs.
    - densification_ratio (float): The ratio of loose foam to compacted foam.
    - disposal_cost_per_cubic_foot (float): The disposal cost per cubic foot of loose foam.
    - compacted_foam_disposal_cost_per_cubic_foot (float): The disposal cost per cubic foot of compacted foam.

    Returns:
    - dict: A dictionary containing the potential savings.
    """

    # Assume 1 lb of EPS foam is approximately 3.5 cubic feet
    cubic_feet_per_pound = 3.5

    # Calculate the volume of loose foam per hour in cubic feet
    loose_foam_cubic_feet_per_hour = loose_foam_per_hour * cubic_feet_per_pound

    # Calculate the volume of compacted foam per hour in cubic feet
    compacted_foam_cubic_feet_per_hour = loose_foam_cubic_feet_per_hour / densification_ratio

    # Calculate the disposal cost of loose foam per hour
    loose_foam_disposal_cost_per_hour = loose_foam_cubic_feet_per_hour * disposal_cost_per_cubic_foot

    # Calculate the disposal cost of compacted foam per hour
    compacted_foam_disposal_cost_per_hour = compacted_foam_cubic_feet_per_hour * compacted_foam_disposal_cost_per_cubic_foot

    # Calculate the potential savings per hour
    potential_savings_per_hour = loose_foam_disposal_cost_per_hour - compacted_foam_disposal_cost_per_hour

    # Calculate the potential savings per year (assuming 2080 working hours per year)
    potential_savings_per_year = potential_savings_per_hour * 2080

    return {
        "loose_foam_cubic_feet_per_hour": loose_foam_cubic_feet_per_hour,
        "compacted_foam_cubic_feet_per_hour": compacted_foam_cubic_feet_per_hour,
        "loose_foam_disposal_cost_per_hour": loose_foam_disposal_cost_per_hour,
        "compacted_foam_disposal_cost_per_hour": compacted_foam_disposal_cost_per_hour,
        "potential_savings_per_hour": potential_savings_per_hour,
        "potential_savings_per_year": potential_savings_per_year,
    }


def main():
    try:
        # Business requirements
        loose_foam_per_hour = 250  # lbs
        densification_ratio = 10  # 1:10
        disposal_cost_per_cubic_foot = 0.50  # dollars
        compacted_foam_disposal_cost_per_cubic_foot = 0.10  # dollars

        savings = calculate_savings(
            loose_foam_per_hour, 
            densification_ratio, 
            disposal_cost_per_cubic_foot, 
            compacted_foam_disposal_cost_per_cubic_foot
        )

        print("Potential Savings:")
        print(f"Loose Foam Volume: {savings['loose_foam_cubic_feet_per_hour']:.2f} cubic feet/hour")
        print(f"Compacted Foam Volume: {savings['compacted_foam_cubic_feet_per_hour']:.2f} cubic feet/hour")
        print(f"Loose Foam Disposal Cost: ${savings['loose_foam_disposal_cost_per_hour']:.2f}/hour")
        print(f"Compacted Foam Disposal Cost: ${savings['compacted_foam_disposal_cost_per_hour']:.2f}/hour")
        print(f"Potential Savings: ${savings['potential_savings_per_hour']:.2f}/hour")
        print(f"Potential Savings (per year): ${savings['potential_savings_per_year']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
