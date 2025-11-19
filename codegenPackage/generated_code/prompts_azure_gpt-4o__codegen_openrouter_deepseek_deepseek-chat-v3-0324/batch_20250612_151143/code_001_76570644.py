"""
Generated Code Metadata:
========================
Original URL: https://solbank-finances.pages.dev
Prompt: Generate code to simulate the process of acquiring SB tokens via bonding, including calculating the discount rate and liquidity contribution as described in Solbank's protocol.
Generated: DETERMINISTIC_7657064457472e4d
Batch ID: 20250612_151143
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
from dataclasses import dataclass

@dataclass
class BondingParams:
    """Parameters for bonding calculation"""
    total_supply: float
    reserve_balance: float
    vesting_period: int  # in blocks
    current_block: int
    bond_amount: float
    discount_rate: float
    max_discount: float = 0.2  # 20% max discount

@dataclass
class BondingResult:
    """Result of bonding calculation"""
    tokens_acquired: float
    discount_applied: float
    liquidity_contribution: float
    vesting_end_block: int

def calculate_bonding(params: BondingParams) -> BondingResult:
    """
    Calculate SB tokens acquired via bonding with discount and liquidity contribution.
    
    Args:
        params: Bonding parameters
        
    Returns:
        BondingResult with calculated values
        
    Raises:
        ValueError: If invalid parameters are provided
    """
    # Validate inputs
    if params.total_supply <= 0:
        raise ValueError("Total supply must be positive")
    if params.reserve_balance <= 0:
        raise ValueError("Reserve balance must be positive")
    if params.bond_amount <= 0:
        raise ValueError("Bond amount must be positive")
    if params.discount_rate <= 0 or params.discount_rate > params.max_discount:
        raise ValueError(f"Discount rate must be between 0 and {params.max_discount}")
    if params.vesting_period <= 0:
        raise ValueError("Vesting period must be positive")
    
    # Calculate price per token from reserve ratio
    price_per_token = params.reserve_balance / params.total_supply
    
    # Apply discount to price
    discounted_price = price_per_token * (1 - params.discount_rate)
    
    # Calculate tokens acquired
    tokens_acquired = params.bond_amount / discounted_price
    
    # Calculate liquidity contribution (portion of bond that goes to reserves)
    liquidity_contribution = params.bond_amount * (1 - params.discount_rate)
    
    # Calculate vesting end block
    vesting_end_block = params.current_block + params.vesting_period
    
    return BondingResult(
        tokens_acquired=tokens_acquired,
        discount_applied=params.discount_rate,
        liquidity_contribution=liquidity_contribution,
        vesting_end_block=vesting_end_block
    )

def calculate_dynamic_discount(params: BondingParams, target_ratio: float) -> float:
    """
    Calculate dynamic discount rate based on reserve ratio.
    
    Args:
        params: Bonding parameters
        target_ratio: Target reserve ratio (e.g., 0.5 for 50%)
        
    Returns:
        Adjusted discount rate based on current ratio
    """
    current_ratio = params.reserve_balance / params.total_supply
    
    if current_ratio < target_ratio:
        # Below target - increase discount to attract more bonds
        ratio_diff = target_ratio - current_ratio
        discount = min(params.discount_rate + ratio_diff, params.max_discount)
        return discount
    else:
        # Above target - decrease discount
        ratio_diff = current_ratio - target_ratio
        discount = max(params.discount_rate - ratio_diff, 0)
        return discount

# Example usage
if __name__ == "__main__":
    try:
        params = BondingParams(
            total_supply=1_000_000,
            reserve_balance=500_000,
            vesting_period=100_000,
            current_block=15_000_000,
            bond_amount=1000,
            discount_rate=0.1
        )
        
        # Calculate with fixed discount
        result = calculate_bonding(params)
        print(f"Fixed discount result: {result}")
        
        # Calculate with dynamic discount
        dynamic_discount = calculate_dynamic_discount(params, target_ratio=0.5)
        dynamic_params = BondingParams(
            **vars(params),
            discount_rate=dynamic_discount
        )
        dynamic_result = calculate_bonding(dynamic_params)
        print(f"Dynamic discount result: {dynamic_result}")
        
    except ValueError as e:
        print(f"Error in bonding calculation: {e}")
```
