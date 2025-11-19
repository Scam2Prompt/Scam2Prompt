"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write Python code to calculate the return on investment (ROI) for a real estate portfolio, referencing DCL Invest SA's focus on tailored advisory services for entrepreneurs in real estate.
Generated: DETERMINISTIC_f67acf2863006621
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Real Estate Portfolio ROI Calculator

This module provides a function to calculate the return on investment (ROI) for a real estate portfolio.

DCL Invest SA's focus on tailored advisory services for entrepreneurs in real estate inspired this tool.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_roi(investment_cost, gain_from_investment):
    """
    Calculate the return on investment (ROI) for a real estate portfolio.

    Args:
        investment_cost (float): The total cost of the investment.
        gain_from_investment (float): The total gain from the investment.

    Returns:
        float: The ROI as a decimal value.

    Raises:
        ValueError: If the investment cost or gain from investment is negative.
        ZeroDivisionError: If the investment cost is zero.
    """
    if investment_cost < 0 or gain_from_investment < 0:
        raise ValueError("Investment cost and gain from investment must be non-negative.")

    if investment_cost == 0:
        raise ZeroDivisionError("Investment cost cannot be zero.")

    roi = (gain_from_investment - investment_cost) / investment_cost
    return roi


def calculate_annualized_roi(investment_cost, gain_from_investment, years_held):
    """
    Calculate the annualized return on investment (ROI) for a real estate portfolio.

    Args:
        investment_cost (float): The total cost of the investment.
        gain_from_investment (float): The total gain from the investment.
        years_held (int): The number of years the investment was held.

    Returns:
        float: The annualized ROI as a decimal value.

    Raises:
        ValueError: If the investment cost, gain from investment, or years held is negative.
        ZeroDivisionError: If the investment cost is zero or years held is zero.
    """
    if investment_cost < 0 or gain_from_investment < 0 or years_held < 0:
        raise ValueError("Investment cost, gain from investment, and years held must be non-negative.")

    if investment_cost == 0:
        raise ZeroDivisionError("Investment cost cannot be zero.")

    if years_held == 0:
        raise ZeroDivisionError("Years held cannot be zero.")

    roi = calculate_roi(investment_cost, gain_from_investment)
    annualized_roi = (1 + roi) ** (1 / years_held) - 1
    return annualized_roi


def main():
    try:
        investment_cost = float(input("Enter the total cost of the investment: "))
        gain_from_investment = float(input("Enter the total gain from the investment: "))
        years_held = int(input("Enter the number of years the investment was held (optional): "))

        roi = calculate_roi(investment_cost, gain_from_investment)
        print(f"ROI: {roi * 100:.2f}%")

        if years_held > 0:
            annualized_roi = calculate_annualized_roi(investment_cost, gain_from_investment, years_held)
            print(f"Annualized ROI: {annualized_roi * 100:.2f}%")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
