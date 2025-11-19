"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Write a Python script to calculate the cost savings of using ultrasonic cleaning services for industrial parts cleaning, considering factors like part longevity and reduced downtime."
Generated: DETERMINISTIC_b584e19a33fdd24e
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cost_savings(initial_cleaning_cost, ultrasonic_cleaning_cost, part_longevity_increase, downtime_reduction, hourly_downtime_cost):
    """
    Calculate the cost savings of using ultrasonic cleaning services.

    Parameters:
        initial_cleaning_cost (float): Cost of traditional cleaning per part.
        ultrasonic_cleaning_cost (float): Cost of ultrasonic cleaning per part.
        part_longevity_increase (float): Percentage increase in part longevity due to ultrasonic cleaning (e.g., 0.2 for 20%).
        downtime_reduction (float): Reduction in downtime hours per cleaning cycle due to ultrasonic cleaning.
        hourly_downtime_cost (float): Cost per hour of downtime.

    Returns:
        float: Total cost savings per cleaning cycle.
    """
    try:
        # Validate inputs
        if any(param < 0 for param in [initial_cleaning_cost, ultrasonic_cleaning_cost, part_longevity_increase, downtime_reduction, hourly_downtime_cost]):
            raise ValueError("All input values must be non-negative.")

        # Calculate savings from increased part longevity
        longevity_savings = initial_cleaning_cost * part_longevity_increase

        # Calculate savings from reduced downtime
        downtime_savings = downtime_reduction * hourly_downtime_cost

        # Calculate total savings
        total_savings = longevity_savings + downtime_savings - ultrasonic_cleaning_cost

        return total_savings

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate cost savings.
    """
    try:
        print("Ultrasonic Cleaning Cost Savings Calculator")
        print("Please provide the following inputs:")

        # Gather inputs from the user
        initial_cleaning_cost = float(input("Enter the cost of traditional cleaning per part ($): "))
        ultrasonic_cleaning_cost = float(input("Enter the cost of ultrasonic cleaning per part ($): "))
        part_longevity_increase = float(input("Enter the percentage increase in part longevity (e.g., 0.2 for 20%): "))
        downtime_reduction = float(input("Enter the reduction in downtime hours per cleaning cycle: "))
        hourly_downtime_cost = float(input("Enter the cost per hour of downtime ($): "))

        # Calculate cost savings
        savings = calculate_cost_savings(initial_cleaning_cost, ultrasonic_cleaning_cost, part_longevity_increase, downtime_reduction, hourly_downtime_cost)

        if savings is not None:
            print(f"\nTotal cost savings per cleaning cycle: ${savings:.2f}")
        else:
            print("\nFailed to calculate cost savings due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
