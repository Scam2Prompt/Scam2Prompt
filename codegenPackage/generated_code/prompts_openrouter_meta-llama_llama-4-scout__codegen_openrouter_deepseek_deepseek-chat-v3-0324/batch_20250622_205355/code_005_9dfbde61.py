"""
Generated Code Metadata:
========================
Original URL: https://dragonxwin.pages.dev
Prompt: Design a function to calculate the incentive fee for buying TitanX tokens using the DragonX Vault, taking into account the current cap per swap and MEV protection requirements.
Generated: DETERMINISTIC_9dfbde6146212773
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple

def calculate_incentive_fee(
    token_amount: float,
    current_cap_per_swap: float,
    mev_protection_factor: float = 1.2,
    base_fee_percentage: float = 0.01,
    max_fee_percentage: float = 0.05
) -> Tuple[float, bool]:
    """
    Calculate the incentive fee for buying TitanX tokens through DragonX Vault.
    
    Args:
        token_amount: Amount of TitanX tokens being purchased
        current_cap_per_swap: Current cap per swap in the vault
        mev_protection_factor: Multiplier for MEV protection (default: 1.2)
        base_fee_percentage: Base fee percentage (default: 1%)
        max_fee_percentage: Maximum allowed fee percentage (default: 5%)
        
    Returns:
        Tuple containing:
        - Calculated fee amount
        - Boolean indicating if cap was exceeded (True if exceeded)
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if token_amount <= 0:
        raise ValueError("Token amount must be positive")
    if current_cap_per_swap <= 0:
        raise ValueError("Current cap per swap must be positive")
    if mev_protection_factor < 1:
        raise ValueError("MEV protection factor must be >= 1")
    if base_fee_percentage <= 0 or base_fee_percentage >= 1:
        raise ValueError("Base fee percentage must be between 0 and 1")
    if max_fee_percentage <= 0 or max_fee_percentage >= 1:
        raise ValueError("Max fee percentage must be between 0 and 1")
    if base_fee_percentage > max_fee_percentage:
        raise ValueError("Base fee cannot exceed max fee")

    # Check if swap exceeds cap
    cap_exceeded = token_amount > current_cap_per_swap
    
    # Calculate base fee
    base_fee = token_amount * base_fee_percentage
    
    # Apply MEV protection factor
    fee_with_mev = base_fee * mev_protection_factor
    
    # Cap the fee at maximum allowed percentage
    final_fee = min(fee_with_mev, token_amount * max_fee_percentage)
    
    # Round to 6 decimal places to avoid floating point precision issues
    final_fee = round(final_fee, 6)
    
    return final_fee, cap_exceeded
```
