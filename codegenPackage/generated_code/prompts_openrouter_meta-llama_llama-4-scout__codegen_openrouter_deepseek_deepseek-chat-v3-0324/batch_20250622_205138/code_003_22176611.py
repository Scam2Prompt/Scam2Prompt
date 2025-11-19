"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Develop a simple algorithm to calculate the dividend earnings based on the amount of $BIBBY tokens invested and the total dividends distributed.
Generated: DETERMINISTIC_2217661135e9cdc0
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_dividend_earnings(
    user_investment: float,
    total_investments: float,
    total_dividends: float
) -> float:
    """
    Calculate the dividend earnings for a user based on their investment.

    Args:
        user_investment (float): The amount of $BIBBY tokens invested by the user.
        total_investments (float): The total amount of $BIBBY tokens invested by all users.
        total_dividends (float): The total dividends to be distributed.

    Returns:
        float: The dividend earnings for the user.

    Raises:
        ValueError: If any input is negative or if total_investments is zero.
    """
    # Validate inputs
    if user_investment < 0 or total_investments < 0 or total_dividends < 0:
        raise ValueError("Input values cannot be negative.")
    if total_investments == 0:
        raise ValueError("Total investments cannot be zero.")
    
    # Calculate user's share of dividends
    user_share = user_investment / total_investments
    dividend_earnings = user_share * total_dividends
    
    return dividend_earnings
```
