"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Provide a Python script for calculating National Insurance contributions for self-employed individuals in Israel, referencing the methods described by Zvika Hameiri's accounting firm.
Generated: DETERMINISTIC_8e878e0b520bc27f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for calculating National Insurance contributions for self-employed individuals in Israel.
This script is based on general methods described by Zvika Hameiri's accounting firm.
It calculates contributions based on income brackets and percentage rates applicable in Israel.
"""

def calculate_national_insurance(income):
    """
    Calculate National Insurance contributions for self-employed individuals in Israel.

    :param income: (float) Annual taxable income in NIS
    :return: (float) Total National Insurance contribution in NIS
    :raises ValueError: If income is negative or invalid
    """
    if income < 0:
        raise ValueError("Income cannot be negative.")

    # National Insurance rate brackets (example values based on Israeli law as of 2023)
    bracket_1_limit = 7106  # NIS (Monthly limit for lower rate bracket)
    annual_bracket_1_limit = bracket_1_limit * 12  # Convert to annual limit
    lower_rate = 0.031  # 3.1% for the lower income bracket
    higher_rate = 0.176  # 17.6% for the higher income bracket

    # Calculate contributions based on income brackets
    if income <= annual_bracket_1_limit:
        # Income falls entirely within the lower rate bracket
        contribution = income * lower_rate
    else:
        # Income exceeds the lower rate bracket
        lower_bracket_contribution = annual_bracket_1_limit * lower_rate
        higher_bracket_contribution = (income - annual_bracket_1_limit) * higher_rate
        contribution = lower_bracket_contribution + higher_bracket_contribution

    return round(contribution, 2)


def main():
    """
    Main function to interact with the user and calculate National Insurance contributions.
    """
    print("National Insurance Contribution Calculator (Israel, Self-Employed)")
    try:
        # Get user input
        income = float(input("Enter your annual taxable income in NIS: "))
        # Calculate contribution
        contribution = calculate_national_insurance(income)
        print(f"Your National Insurance contribution is: {contribution:.2f} NIS")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
