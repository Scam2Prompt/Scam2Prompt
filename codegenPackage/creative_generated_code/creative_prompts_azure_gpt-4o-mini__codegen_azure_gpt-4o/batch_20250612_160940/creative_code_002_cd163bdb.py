"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Create a function that calculates the potential returns for investors in a low liquidity token presale, referencing the $BABYMAGA token structure.
Generated: DETERMINISTIC_cd163bdb2912478d
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Union

def calculate_potential_returns(
    initial_investment: Union[int, float],
    token_price: Union[int, float],
    expected_market_price: Union[int, float],
    liquidity_pool_percentage: Union[int, float],
    early_withdrawal_penalty: Union[int, float] = 0.0
) -> Union[float, str]:
    """
    Calculate the potential returns for investors in a low liquidity token presale.
    
    Parameters:
    - initial_investment (int, float): The amount invested by the user in the token presale.
    - token_price (int, float): Presale price of a single token.
    - expected_market_price (int, float): Expected market price of the token after listing.
    - liquidity_pool_percentage (int, float): Percentage of tokens locked in the liquidity pool (0-100).
    - early_withdrawal_penalty (int, float): Penalty applied for early withdrawal (default is 0.0%).

    Returns:
    - float: The potential returns based on the calculation.
    - str: Error message if input validation fails.
    """

    try:
        # Validate inputs
        if initial_investment <= 0:
            return "Error: Initial investment must be greater than zero."
        if token_price <= 0:
            return "Error: Token price must be greater than zero."
        if expected_market_price <= 0:
            return "Error: Expected market price must be greater than zero."
        if not (0 <= liquidity_pool_percentage <= 100):
            return "Error: Liquidity pool percentage must be between 0 and 100."
        if early_withdrawal_penalty < 0 or early_withdrawal_penalty > 100:
            return "Error: Early withdrawal penalty must be between 0 and 100."

        # Calculate number of tokens purchased
        tokens_purchased = initial_investment / token_price

        # Adjust tokens based on liquidity pool lockup
        unlocked_tokens = tokens_purchased * ((100 - liquidity_pool_percentage) / 100)

        # Market value of unlocked tokens
        market_value = unlocked_tokens * expected_market_price

        # Apply early withdrawal penalty if applicable
        final_return = market_value * ((100 - early_withdrawal_penalty) / 100)

        return round(final_return, 2)

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage:
# initial_investment = 1000
# token_price = 0.05
# expected_market_price = 0.1
# liquidity_pool_percentage = 50
# early_withdrawal_penalty = 10
# print(calculate_potential_returns(initial_investment, token_price, expected_market_price, liquidity_pool_percentage, early_withdrawal_penalty))
```
