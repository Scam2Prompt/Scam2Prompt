"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange-ethena.pages.dev
Prompt: Generate a function that calculates the APY for staking on Ethena, given the current APY of 24.04%.
Generated: DETERMINISTIC_606c74b118ec7aa0
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(principal: float, apy: float, years: int) -> float:
    """
    Calculate the future value of an investment based on the Annual Percentage Yield (APY).

    Args:
        principal (float): The initial amount of money invested (the principal).
        apy (float): The annual percentage yield as a decimal (e.g., 24.04% as 0.2404).
        years (int): The number of years the money is invested or staked.

    Returns:
        float: The future value of the investment after the specified number of years.

    Raises:
        ValueError: If principal is negative, apy is outside the range [0, 1], or years is negative.
    """
    
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if not (0 <= apy <= 1):
        raise ValueError("APY must be a decimal between 0 and 1.")
    if years < 0:
        raise ValueError("Number of years must be non-negative.")

    # Calculate future value using compound interest formula
    future_value = principal * (1 + apy) ** years
    return future_value

# Example usage
if __name__ == "__main__":
    try:
        principal_amount = 1000.0  # Example principal amount
        annual_percentage_yield = 0.2404  # 24.04%
        investment_duration_years = 5  # Example duration

        future_value = calculate_apy(principal_amount, annual_percentage_yield, investment_duration_years)
        print(f"Future value after {investment_duration_years} years: ${future_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
