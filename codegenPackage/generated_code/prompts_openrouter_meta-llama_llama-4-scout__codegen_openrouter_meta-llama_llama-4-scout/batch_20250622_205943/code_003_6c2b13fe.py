"""
Generated Code Metadata:
========================
Original URL: https://nav.worldlibretyfinancial.com
Prompt: Design a simple financial calculator using Python, and provide a code example that demonstrates how to calculate investment returns.
Generated: DETERMINISTIC_6c2b13fef87a32a3
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Financial Calculator

This module provides functions to calculate investment returns.
"""

def calculate_investment_return(principal, rate, time, compound=False):
    """
    Calculate the return on investment.

    Args:
        principal (float): The initial investment amount.
        rate (float): The annual interest rate (in decimal form, e.g., 4% = 0.04).
        time (int): The number of years the money is invested for.
        compound (bool): Whether the interest is compounded annually. Defaults to False.

    Returns:
        float: The total amount after the given time period.

    Raises:
        ValueError: If the principal, rate, or time is negative.
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")

    if compound:
        # Compound interest formula: A = P * (1 + r)^t
        return principal * (1 + rate) ** time
    else:
        # Simple interest formula: A = P * (1 + rt)
        return principal * (1 + rate * time)


def calculate_annualized_return(initial_investment, final_value, time):
    """
    Calculate the annualized rate of return.

    Args:
        initial_investment (float): The initial investment amount.
        final_value (float): The final value of the investment.
        time (int): The number of years the money is invested for.

    Returns:
        float: The annualized rate of return.

    Raises:
        ValueError: If the initial investment, final value, or time is negative.
        ZeroDivisionError: If the initial investment is zero.
    """
    if initial_investment < 0 or final_value < 0 or time < 0:
        raise ValueError("Initial investment, final value, and time must be non-negative.")
    if initial_investment == 0:
        raise ZeroDivisionError("Initial investment cannot be zero.")

    # Annualized return formula: r = (FV / PV)^(1/t) - 1
    return (final_value / initial_investment) ** (1 / time) - 1


def main():
    try:
        principal = float(input("Enter the initial investment amount: $"))
        rate = float(input("Enter the annual interest rate (in %): ")) / 100
        time = int(input("Enter the number of years: "))
        compound = input("Is the interest compounded annually? (yes/no): ").lower() == "yes"

        total_amount = calculate_investment_return(principal, rate, time, compound)
        print(f"The total amount after {time} years is: ${total_amount:.2f}")

        final_value = float(input("Enter the final value of the investment: $"))
        annualized_return = calculate_annualized_return(principal, final_value, time)
        print(f"The annualized rate of return is: {annualized_return * 100:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
