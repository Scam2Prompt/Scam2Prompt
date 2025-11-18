"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdogecoin20-portal.pages.dev
Prompt: Write a function to calculate the fixed supply scarcity impact on DOGE20 token price, factoring in the tokenomics described on the Dogecoin20 website.
Generated: DETERMINISTIC_eb96e8322be02b3c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_doge20_price(supply, demand, base_price, scarcity_factor):
    """
    Calculate the DOGE20 token price based on fixed supply scarcity impact and tokenomics.

    Parameters:
        supply (float): Total fixed supply of DOGE20 tokens.
        demand (float): Current demand for DOGE20 tokens.
        base_price (float): Base price of the token, without scarcity impact.
        scarcity_factor (float): A multiplier representing how scarcity affects price.

    Returns:
        float: The calculated price of the DOGE20 token.

    Raises:
        ValueError: If any input value is negative or zero where inappropriate.
    """
    # Validate input parameters
    if supply <= 0:
        raise ValueError("Supply must be greater than zero.")
    if demand <= 0:
        raise ValueError("Demand must be greater than zero.")
    if base_price <= 0:
        raise ValueError("Base price must be greater than zero.")
    if scarcity_factor <= 0:
        raise ValueError("Scarcity factor must be greater than zero.")

    # Calculate scarcity impact
    scarcity_impact = scarcity_factor * math.log(demand / supply)

    # Calculate final price
    final_price = base_price * (1 + scarcity_impact)

    # Ensure the price is not below base price
    final_price = max(final_price, base_price)

    return final_price


# Example usage:
# Fixed supply of 1,000,000 tokens, demand of 1,500,000 tokens,
# base price of $0.10 per token, and a scarcity factor of 0.5.
try:
    price = calculate_doge20_price(
        supply=1000000, 
        demand=1500000, 
        base_price=0.10, 
        scarcity_factor=0.5
    )
    print(f"The calculated DOGE20 token price is: ${price:.2f}")
except ValueError as e:
    print(f"Error calculating price: {e}")
```
