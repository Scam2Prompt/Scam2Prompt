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
def calculate_potential_earnings(principal: float, years: int, annual_return_rate: float = 0.115) -> float:
    """
    Calculate potential earnings from investments in Klar's investment account.
    
    Args:
        principal (float): The initial amount of money invested.
        years (int): The number of years the investment will grow.
        annual_return_rate (float): The annual return rate (default is 11.5% or 0.115).
        
    Returns:
        float: The total value of the investment after the specified number of years.
    
    Raises:
        ValueError: If the principal is negative or if years are not positive.
    """
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if years <= 0:
        raise ValueError("Years must be a positive integer.")
    if not (0 <= annual_return_rate <= 1):
        raise ValueError("Annual return rate must be between 0 and 1.")
    
    # Calculate future value using compound interest formula
    # Formula: FV = P * (1 + r)^t
    future_value = principal * (1 + annual_return_rate) ** years
    
    return future_value


# Example Usage (Uncomment to test the function):
# principal_amount = 10000  # Initial investment of $10,000
# investment_years = 5      # Investment duration: 5 years
# earnings = calculate_potential_earnings(principal_amount, investment_years)
# print(f"Potential earnings after {investment_years} years: ${earnings:.2f}")
```
