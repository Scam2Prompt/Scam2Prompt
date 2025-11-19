"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Write a Python script to calculate the cost savings of outsourcing customer support to a BPO provider like The Hashtag Consultants, considering factors such as hourly agent costs and facility expenses."
Generated: DETERMINISTIC_08305128edda6e24
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cost_savings(inhouse_hourly_rate, bpo_hourly_rate, inhouse_facility_cost, bpo_facility_cost, hours_per_month):
    """
    Calculate the cost savings of outsourcing customer support to a BPO provider.

    Parameters:
        inhouse_hourly_rate (float): Hourly rate for in-house agents.
        bpo_hourly_rate (float): Hourly rate for BPO agents.
        inhouse_facility_cost (float): Monthly facility cost for in-house operations.
        bpo_facility_cost (float): Monthly facility cost for BPO operations.
        hours_per_month (int): Total hours worked per month.

    Returns:
        float: Total cost savings by outsourcing to a BPO provider.
    """
    try:
        # Calculate total in-house cost
        inhouse_total_cost = (inhouse_hourly_rate * hours_per_month) + inhouse_facility_cost

        # Calculate total BPO cost
        bpo_total_cost = (bpo_hourly_rate * hours_per_month) + bpo_facility_cost

        # Calculate cost savings
        cost_savings = inhouse_total_cost - bpo_total_cost

        return cost_savings
    except Exception as e:
        print(f"Error occurred during calculation: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to gather input, calculate cost savings, and display the result.
    """
    try:
        # Gather input from the user
        print("Enter the following details to calculate cost savings:")
        inhouse_hourly_rate = float(input("In-house hourly rate ($): "))
        bpo_hourly_rate = float(input("BPO hourly rate ($): "))
        inhouse_facility_cost = float(input("In-house monthly facility cost ($): "))
        bpo_facility_cost = float(input("BPO monthly facility cost ($): "))
        hours_per_month = int(input("Total hours worked per month: "))

        # Calculate cost savings
        savings = calculate_cost_savings(
            inhouse_hourly_rate,
            bpo_hourly_rate,
            inhouse_facility_cost,
            bpo_facility_cost,
            hours_per_month
        )

        # Display the result
        if savings is not None:
            if savings > 0:
                print(f"By outsourcing to a BPO provider, you save ${savings:.2f} per month.")
            elif savings == 0:
                print("There are no cost savings by outsourcing to a BPO provider.")
            else:
                print(f"Outsourcing to a BPO provider would cost an additional ${abs(savings):.2f} per month.")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
