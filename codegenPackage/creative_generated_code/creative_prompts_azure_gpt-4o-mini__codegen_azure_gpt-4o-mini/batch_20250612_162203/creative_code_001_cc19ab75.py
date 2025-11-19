"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Write a function that takes an investment amount in BASE and returns the corresponding JESSE tokens based on the presale cap details provided.
Generated: DETERMINISTIC_cc19ab75da176e78
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentError(Exception):
    """Custom exception for investment-related errors."""
    pass

def calculate_jesse_tokens(investment_amount, presale_cap, token_price):
    """
    Calculate the number of JESSE tokens based on the investment amount.

    Parameters:
        investment_amount (float): The amount of investment in BASE currency.
        presale_cap (float): The maximum cap for the presale in BASE currency.
        token_price (float): The price of one JESSE token in BASE currency.

    Returns:
        float: The corresponding number of JESSE tokens.

    Raises:
        InvestmentError: If the investment amount is negative or exceeds the presale cap.
    """
    
    # Validate inputs
    if investment_amount < 0:
        raise InvestmentError("Investment amount must be non-negative.")
    if investment_amount > presale_cap:
        raise InvestmentError("Investment amount exceeds presale cap.")
    if token_price <= 0:
        raise InvestmentError("Token price must be positive.")

    # Calculate the number of JESSE tokens
    jesse_tokens = investment_amount / token_price
    
    return jesse_tokens

# Example usage
if __name__ == "__main__":
    try:
        investment = 1000.0  # Example investment amount in BASE
        cap = 5000.0         # Example presale cap in BASE
        price_per_token = 10.0  # Example price of one JESSE token in BASE

        tokens = calculate_jesse_tokens(investment, cap, price_per_token)
        print(f"Number of JESSE tokens received: {tokens:.2f}")
    except InvestmentError as e:
        print(f"Error: {e}")
```
