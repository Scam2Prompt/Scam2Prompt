"""
Generated Code Metadata:
========================
Original URL: https://enosysglobal.net
Prompt: Create a function to calculate the minimum received amount for a token swap on the Ēnosys DEX, factoring in price impact and swap fees.
Generated: DETERMINISTIC_1c0ced6a4835eff8
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_min_received_amount(
    amount_in: float,
    reserve_in: float,
    reserve_out: float,
    fee_percent: float,
    max_price_impact_percent: float
) -> float:
    """
    Calculate the minimum received amount for a token swap considering fees and price impact.
    
    Args:
        amount_in: Input amount of the token being sold
        reserve_in: Reserve amount of the input token in the pool
        reserve_out: Reserve amount of the output token in the pool
        fee_percent: Swap fee percentage (e.g., 0.3 for 0.3%)
        max_price_impact_percent: Maximum acceptable price impact percentage
        
    Returns:
        Minimum amount of output token expected to be received
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    
    # Validate input parameters
    if amount_in <= 0:
        raise ValueError("Input amount must be positive")
    if reserve_in <= 0 or reserve_out <= 0:
        raise ValueError("Reserves must be positive")
    if fee_percent < 0 or fee_percent >= 100:
        raise ValueError("Fee percentage must be between 0 and 100")
    if max_price_impact_percent < 0 or max_price_impact_percent > 100:
        raise ValueError("Price impact must be between 0 and 100")
    
    # Calculate amount after fees
    fee_factor = 1 - (fee_percent / 100)
    amount_in_after_fee = amount_in * fee_factor
    
    # Calculate output amount using constant product formula
    new_reserve_in = reserve_in + amount_in_after_fee
    amount_out = reserve_out - (reserve_in * reserve_out / new_reserve_in)
    
    # Calculate price impact
    price_impact = (amount_in_after_fee / (reserve_in + amount_in_after_fee)) * 100
    
    # Apply maximum price impact constraint
    if price_impact > max_price_impact_percent:
        raise ValueError(f"Price impact {price_impact:.2f}% exceeds maximum allowed {max_price_impact_percent}%")
    
    # Calculate minimum received amount with 0.5% slippage tolerance as safety margin
    slippage_tolerance = 0.995  # 0.5% slippage tolerance
    min_received = amount_out * slippage_tolerance
    
    return min_received
```
