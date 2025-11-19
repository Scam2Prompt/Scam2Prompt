"""
Generated Code Metadata:
========================
Original URL: https://immediatecore.co
Prompt: "Create a code snippet to calculate compound interest, a concept taught on Immediate Core, using a programming language of choice."
Generated: DETERMINISTIC_30b15ea490de99c2
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_compound_interest(
    principal: float,
    rate: float,
    time: float,
    compounding_frequency: int = 1
) -> float:
    """
    Calculate compound interest based on the given parameters.

    Args:
        principal: Initial amount of money (float).
        rate: Annual interest rate in decimal (e.g., 0.05 for 5%) (float).
        time: Time the money is invested for, in years (float).
        compounding_frequency: Number of times interest is compounded per year (int). Default is 1.

    Returns:
        float: The total amount after compound interest.

    Raises:
        ValueError: If any of the parameters are non-positive.
    """
    if principal <= 0 or rate <= 0 or time <= 0 or compounding_frequency <= 0:
        raise ValueError("All parameters must be positive.")

    amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)
    return round(amount, 2)  # Round to 2 decimal places for currency


# Example usage
if __name__ == "__main__":
    try:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
        t = float(input("Enter the time in years: "))
        n = int(input("Enter the compounding frequency per year (default 1): ") or 1)

        result = calculate_compound_interest(p, r, t, n)
        print(f"The total amount after compound interest is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
