"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Develop a basic investment calculator using a programming language like Python that takes into account factors like inflation rate and investment horizon.
Generated: DETERMINISTIC_346a895d99e7d794
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Calculator

Calculates the future value of an investment based on the principal amount,
inflation rate, investment horizon, and expected annual returns.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_investment(
    principal: float, 
    inflation_rate: float, 
    investment_horizon: int, 
    annual_returns: float
) -> float:
    """
    Calculates the future value of an investment.

    Args:
    - principal (float): The initial investment amount.
    - inflation_rate (float): The expected inflation rate (in decimal form, e.g., 2% = 0.02).
    - investment_horizon (int): The number of years the money is invested for.
    - annual_returns (float): The expected annual returns (in decimal form, e.g., 5% = 0.05).

    Returns:
    - float: The future value of the investment.
    """
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if inflation_rate < 0:
        raise ValueError("Inflation rate cannot be negative.")
    if investment_horizon < 0:
        raise ValueError("Investment horizon cannot be negative.")
    if annual_returns < 0:
        raise ValueError("Annual returns cannot be negative.")

    # Calculate the future value using the formula: FV = PV * (1 + r - i)^n
    # Where:
    #   FV = Future Value
    #   PV = Present Value (principal)
    #   r = annual returns
    #   i = inflation rate
    #   n = investment horizon
    future_value = principal * ((1 + annual_returns - inflation_rate) ** investment_horizon)
    return future_value


def main():
    try:
        principal = float(input("Enter the principal amount: $"))
        inflation_rate = float(input("Enter the inflation rate (in %): ")) / 100
        investment_horizon = int(input("Enter the investment horizon (in years): "))
        annual_returns = float(input("Enter the expected annual returns (in %): ")) / 100

        future_value = calculate_investment(principal, inflation_rate, investment_horizon, annual_returns)

        print(f"The future value of the investment is: ${future_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
