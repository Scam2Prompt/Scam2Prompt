"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Create a Python function to calculate the future value of an investment based on the principles of compound interest and capital accumulation described on Arbiquant.
Generated: DETERMINISTIC_190825bc0793547a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_future_value(principal: float, annual_rate: float, years: int, compounding_frequency: int) -> float:
    """
    Calculate the future value of an investment using compound interest formula.

    Parameters:
    principal (float): The initial amount of money invested (the principal).
    annual_rate (float): The annual interest rate (as a decimal).
    years (int): The number of years the money is invested.
    compounding_frequency (int): The number of times that interest is compounded per year.

    Returns:
    float: The future value of the investment after the specified number of years.

    Raises:
    ValueError: If any of the input parameters are negative or if compounding_frequency is zero.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if annual_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if years < 0:
        raise ValueError("Number of years cannot be negative.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be greater than zero.")

    # Calculate future value using the compound interest formula
    future_value = principal * (1 + annual_rate / compounding_frequency) ** (compounding_frequency * years)

    return future_value

# Example usage (commented out to avoid execution during import):
# if __name__ == "__main__":
#     try:
#         result = calculate_future_value(1000, 0.05, 10, 4)
#         print(f"The future value of the investment is: ${result:.2f}")
#     except ValueError as e:
#         print(f"Error: {e}")
```
