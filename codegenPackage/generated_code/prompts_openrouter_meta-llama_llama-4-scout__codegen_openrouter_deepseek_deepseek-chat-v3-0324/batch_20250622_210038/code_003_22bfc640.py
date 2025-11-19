"""
Generated Code Metadata:
========================
Original URL: https://synthr-mvp.pages.dev
Prompt: Design a function to perform a swap on the SYNTHR platform, taking into account the user's collateral balance and C-ratio.
Generated: DETERMINISTIC_22bfc6407b86c8fb
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple, Optional

class SynthSwapError(Exception):
    """Base exception for SYNTHR swap operations."""
    pass

class InsufficientCollateralError(SynthSwapError):
    """Raised when user's collateral is insufficient for the swap."""
    pass

class InvalidCRatioError(SynthSwapError):
    """Raised when collateral ratio is below the minimum threshold."""
    pass

def calculate_c_ratio(collateral_amount: float, synth_amount: float) -> float:
    """
    Calculate the collateral ratio (C-ratio).
    
    Args:
        collateral_amount: Amount of collateral in USD
        synth_amount: Amount of synths in USD
    
    Returns:
        Collateral ratio (collateral/synth)
    """
    if synth_amount == 0:
        return float('inf')
    return collateral_amount / synth_amount

def validate_swap_parameters(
    collateral_balance: float,
    current_synth_balance: float,
    swap_amount: float,
    min_c_ratio: float
) -> Tuple[bool, Optional[str]]:
    """
    Validate swap parameters before execution.
    
    Args:
        collateral_balance: User's current collateral balance in USD
        current_synth_balance: User's current synth balance in USD
        swap_amount: Amount of synths to swap in USD
        min_c_ratio: Minimum allowed collateral ratio
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if swap_amount <= 0:
        return False, "Swap amount must be positive"
    
    if collateral_balance <= 0:
        return False, "Collateral balance must be positive"
    
    new_synth_balance = current_synth_balance - swap_amount
    if new_synth_balance < 0:
        return False, "Insufficient synth balance"
    
    current_c_ratio = calculate_c_ratio(collateral_balance, new_synth_balance)
    if current_c_ratio < min_c_ratio:
        return False, f"C-ratio {current_c_ratio} below minimum {min_c_ratio}"
    
    return True, None

def perform_synth_swap(
    collateral_balance: float,
    current_synth_balance: float,
    swap_amount: float,
    min_c_ratio: float,
    transaction_fee: float = 0.003
) -> Tuple[float, float]:
    """
    Perform a SYNTHR swap operation with collateral and C-ratio checks.
    
    Args:
        collateral_balance: User's current collateral balance in USD
        current_synth_balance: User's current synth balance in USD
        swap_amount: Amount of synths to swap in USD
        min_c_ratio: Minimum allowed collateral ratio
        transaction_fee: Percentage fee for the swap (default: 0.3%)
    
    Returns:
        Tuple of (new_collateral_balance, new_synth_balance)
    
    Raises:
        InsufficientCollateralError: If collateral is insufficient
        InvalidCRatioError: If resulting C-ratio would be invalid
    """
    # Validate parameters
    is_valid, error_msg = validate_swap_parameters(
        collateral_balance,
        current_synth_balance,
        swap_amount,
        min_c_ratio
    )
    if not is_valid:
        if "C-ratio" in error_msg:
            raise InvalidCRatioError(error_msg)
        raise InsufficientCollateralError(error_msg)
    
    # Calculate fee and net swap amount
    fee_amount = swap_amount * transaction_fee
    net_swap_amount = swap_amount - fee_amount
    
    # Update balances
    new_collateral = collateral_balance + net_swap_amount
    new_synth_balance = current_synth_balance - swap_amount
    
    # Final validation (should never fail if previous checks passed)
    final_c_ratio = calculate_c_ratio(new_collateral, new_synth_balance)
    if final_c_ratio < min_c_ratio:
        raise InvalidCRatioError(
            f"Final C-ratio {final_c_ratio} below minimum {min_c_ratio}"
        )
    
    return new_collateral, new_synth_balance
```
