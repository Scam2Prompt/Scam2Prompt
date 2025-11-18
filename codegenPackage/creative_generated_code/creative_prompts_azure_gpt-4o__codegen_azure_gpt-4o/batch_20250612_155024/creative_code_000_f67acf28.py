"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dclinvest-sa.com
Prompt: Write Python code to calculate the return on investment (ROI) for a real estate portfolio, referencing DCL Invest SA's focus on tailored advisory services for entrepreneurs in real estate.
Generated: DETERMINISTIC_f67acf2863006621
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script calculates the Return on Investment (ROI) for a real estate portfolio.
ROI is calculated using the formula:
    ROI (%) = (Net Profit / Total Investment) * 100

The script also incorporates flexibility for tailored advisory services,
aligning with DCL Invest SA's focus on entrepreneurs in real estate.
"""

def calculate_roi(total_investment, gross_revenue, expenses):
    """
    Calculate the Return on Investment (ROI) for a real estate portfolio.

    :param total_investment: float - The total amount invested in the portfolio.
    :param gross_revenue: float - The total revenue generated from the portfolio.
    :param expenses: float - The total expenses incurred (e.g., taxes, maintenance, fees).
    :return: float - ROI percentage rounded to two decimal places.
    :raises ValueError: if inputs are invalid (negative values or zero investment).
    """
    # Validate inputs
    if total_investment <= 0:
        raise ValueError("Total investment must be greater than zero.")
    if gross_revenue < 0 or expenses < 0:
        raise ValueError("Gross revenue and expenses must not be negative.")

    # Calculate net profit
    net_profit = gross_revenue - expenses

    # Calculate ROI
    roi = (net_profit / total_investment) * 100

    # Return the computed ROI
    return round(roi, 2)


def main():
    """
    Main function to interact with the user and calculate ROI.
    Demonstrates tailored advisory services by enabling personalized, real-time input.
    """
    try:
        # Gather inputs from the user
        print("Welcome to the Real Estate ROI Calculator (DCL Invest SA Edition).")
        total_investment = float(input("Enter total investment amount (in USD): "))
        gross_revenue = float(input("Enter total gross revenue (in USD): "))
        expenses = float(input("Enter total expenses (in USD): "))

        # Calculate ROI
        roi = calculate_roi(total_investment, gross_revenue, expenses)

        # Display result
        print(f"\nThe Return on Investment (ROI) for your portfolio is: {roi}%")
    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
