"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Generate a Python function that calculates potential earnings from investments using Klar's investment account, considering an annual return of up to 11.5%.
Generated: DETERMINISTIC_bb493cb8fad9d245
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_investment_earnings(principal: float, years: int, annual_return: float = 0.115) -> float:
    """
    Calculate the potential earnings from an investment over a number of years.

    Parameters:
    principal (float): The initial amount of money invested.
    years (int): The number of years the money is invested for.
    annual_return (float): The expected annual return rate (default is 11.5%).

    Returns:
    float: The total amount accumulated after the investment period.
    
    Raises:
    ValueError: If principal or years are negative or if annual_return is not between 0 and 1.
    """
    
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if years < 0:
        raise ValueError("Investment duration must be non-negative.")
    if not (0 <= annual_return <= 1):
        raise ValueError("Annual return must be between 0 and 1.")

    # Calculate the total amount using compound interest formula
    total_amount = principal * (1 + annual_return) ** years
    
    return total_amount


# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.0  # Example principal amount
        investment_duration = 10       # Example years to invest
        earnings = calculate_investment_earnings(initial_investment, investment_duration)
        print(f"Total amount after {investment_duration} years: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
