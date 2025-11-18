"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write a program to calculate estimated costs for studying abroad, including tuition fees, housing, and living expenses, as mentioned in RNW International's scholarship program.
Generated: DETERMINISTIC_c6bf502a66ce9e09
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_study_abroad_costs(tuition_fee, housing_cost, living_expenses, scholarship_amount):
    """
    Calculate the total estimated cost for studying abroad after applying the scholarship.

    Parameters:
    tuition_fee (float): The tuition fee per year.
    housing_cost (float): The housing cost per year.
    living_expenses (float): The living expenses per year.
    scholarship_amount (float): The scholarship amount provided per year.

    Returns:
    float: The total cost after applying the scholarship.
    """
    try:
        # Validate parameters
        if tuition_fee < 0 or housing_cost < 0 or living_expenses < 0 or scholarship_amount < 0:
            raise ValueError("All inputs must be non-negative values.")

        # Calculate total costs
        total_cost = tuition_fee + housing_cost + living_expenses

        # Calculate net cost after applying scholarship
        net_cost = total_cost - scholarship_amount

        # Ensure net cost is not negative
        if net_cost < 0:
            net_cost = 0  # If scholarship exceeds total costs, net cost is zero

        return net_cost
    except TypeError:
        raise TypeError("All inputs must be numeric.")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")


def main():
    """
    Main function to interact with the user and calculate study abroad costs.
    """
    try:
        print("Welcome to the Study Abroad Cost Calculator (RNW International Program)\n")

        # Gather inputs from the user
        tuition_fee = float(input("Enter the annual tuition fee (in USD): "))
        housing_cost = float(input("Enter the annual housing cost (in USD): "))
        living_expenses = float(input("Enter the annual living expenses (in USD): "))
        scholarship_amount = float(input("Enter the annual scholarship amount (in USD): "))

        # Calculate total estimated cost
        total_cost = calculate_study_abroad_costs(
            tuition_fee, housing_cost, living_expenses, scholarship_amount
        )

        # Display result
        print(f"\nEstimated total cost after scholarship: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
