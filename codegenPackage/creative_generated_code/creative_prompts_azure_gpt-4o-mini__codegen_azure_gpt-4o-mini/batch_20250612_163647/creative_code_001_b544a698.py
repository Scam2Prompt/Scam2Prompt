"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Write a Python function to calculate potential gains from a high-risk savings plan with a variable average rate of 24.56% for 2023, based on the offerings from Pipeline Finance Conseil.
Generated: DETERMINISTIC_b544a69838f95e5a
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_gains(principal: float, years: int, annual_rate: float = 24.56) -> float:
    """
    Calculate potential gains from a high-risk savings plan.

    Args:
        principal (float): The initial amount of money invested.
        years (int): The number of years the money is invested for.
        annual_rate (float): The average annual interest rate (default is 24.56%).

    Returns:
        float: The total amount after the specified number of years, including potential gains.

    Raises:
        ValueError: If principal is negative or years is negative.
    """
    
    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if years < 0:
        raise ValueError("Number of years must be non-negative.")
    
    # Convert annual rate from percentage to a decimal
    rate_decimal = annual_rate / 100

    # Calculate the total amount after 'years' using the compound interest formula
    total_amount = principal * (1 + rate_decimal) ** years
    
    return total_amount

# Example usage
if __name__ == "__main__":
    try:
        principal_amount = 1000.0  # Example principal amount
        investment_years = 5        # Example investment duration
        potential_gains = calculate_potential_gains(principal_amount, investment_years)
        print(f"Total amount after {investment_years} years: ${potential_gains:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
