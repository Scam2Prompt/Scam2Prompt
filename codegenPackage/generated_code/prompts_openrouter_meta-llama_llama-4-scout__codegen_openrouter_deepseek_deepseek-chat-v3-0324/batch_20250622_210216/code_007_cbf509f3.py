"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Write a function in Python to calculate the price increase of Green Bitcoin ($GBTC) tokens during the presale stages, considering the dynamic pricing mechanism.
Generated: DETERMINISTIC_cbf509f3208abfc4
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_gbtc_price_increase(initial_price: float, current_stage: int, total_stages: int, price_increase_per_stage: float) -> float:
    """
    Calculate the current price of Green Bitcoin ($GBTC) tokens based on presale stage.
    
    Args:
        initial_price (float): Initial price of the token at stage 0.
        current_stage (int): Current presale stage (0-indexed).
        total_stages (int): Total number of presale stages.
        price_increase_per_stage (float): Percentage increase per stage (as decimal, e.g., 0.1 for 10%).
        
    Returns:
        float: Current price after stage increases.
        
    Raises:
        ValueError: If any input is invalid (negative values, current_stage exceeds total_stages, etc.)
    """
    # Validate inputs
    if initial_price <= 0:
        raise ValueError("Initial price must be positive")
    if current_stage < 0:
        raise ValueError("Current stage cannot be negative")
    if total_stages <= 0:
        raise ValueError("Total stages must be positive")
    if current_stage >= total_stages:
        raise ValueError("Current stage cannot exceed total stages")
    if price_increase_per_stage < 0:
        raise ValueError("Price increase per stage cannot be negative")
    
    # Calculate price increase
    current_price = initial_price * (1 + price_increase_per_stage) ** current_stage
    return round(current_price, 4)  # Round to 4 decimal places for currency
```
