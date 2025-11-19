"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a simple investment calculator using a programming language (e.g., Python, JavaScript) to demonstrate the impact of investment strategies on returns.
Generated: DETERMINISTIC_0de964fbd84ab6bf
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
annual interest rate, and compounding frequency.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_investment(
    principal: float, 
    annual_interest_rate: float, 
    years: int, 
    compounding_frequency: int = 1
) -> float:
    """
    Calculates the future value of an investment.

    Args:
    - principal (float): The initial investment amount.
    - annual_interest_rate (float): The annual interest rate (in decimal form).
    - years (int): The number of years the money is invested for.
    - compounding_frequency (int): The number of times interest is compounded per year. Defaults to 1.

    Returns:
    - float: The future value of the investment.
    """
    try:
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        future_value = principal * (
            1 + (annual_interest_rate / compounding_frequency)
        ) ** (compounding_frequency * years)
        return future_value

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    print("Simple Investment Calculator")
    print("--------------------------------")

    principal = float(input("Enter the principal amount: $"))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
    years = int(input("Enter the number of years: "))
    compounding_frequency = int(input("Enter the compounding frequency (per year): "))

    future_value = calculate_investment(
        principal, annual_interest_rate, years, compounding_frequency
    )

    if future_value is not None:
        print(f"\nFuture Value: ${future_value:.2f}")


if __name__ == "__main__":
    main()
```
