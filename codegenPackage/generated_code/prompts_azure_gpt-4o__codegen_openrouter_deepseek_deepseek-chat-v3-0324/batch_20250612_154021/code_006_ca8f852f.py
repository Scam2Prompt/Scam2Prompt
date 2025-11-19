"""
Generated Code Metadata:
========================
Original URL: https://aterdex.com
Prompt: Develop a function to calculate leverage and margin requirements for a trade on Aster DEX's Simple Mode.
Generated: DETERMINISTIC_ca8f852fa4f5bae5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_leverage_and_margin(
    position_size: float,
    leverage: int,
    entry_price: float,
    is_long: bool,
    risk_adjustment_factor: float = 1.0
) -> dict:
    """
    Calculate leverage and margin requirements for a trade on Aster DEX's Simple Mode.
    
    Args:
        position_size: Total value of the position in quote currency
        leverage: Leverage multiplier (e.g., 10 for 10x)
        entry_price: Entry price of the position
        is_long: Boolean indicating if the position is long (True) or short (False)
        risk_adjustment_factor: Factor to adjust margin requirements (default 1.0)
        
    Returns:
        dict: Dictionary containing:
            - initial_margin: Required margin in quote currency
            - maintenance_margin: Maintenance margin in quote currency
            - liquidation_price: Estimated liquidation price
            - position_size: Original position size
            - leverage: Original leverage
            
    Raises:
        ValueError: If any input is invalid
    """
    
    # Input validation
    if position_size <= 0:
        raise ValueError("Position size must be positive")
    if leverage <= 0:
        raise ValueError("Leverage must be positive")
    if entry_price <= 0:
        raise ValueError("Entry price must be positive")
    if risk_adjustment_factor <= 0:
        raise ValueError("Risk adjustment factor must be positive")
    
    try:
        # Calculate initial margin (position_size / leverage)
        initial_margin = position_size / leverage
        
        # Calculate maintenance margin (typically 50% of initial margin)
        maintenance_margin = initial_margin * 0.5 * risk_adjustment_factor
        
        # Calculate liquidation price
        if is_long:
            liquidation_price = entry_price * (1 - (1 / leverage))
        else:
            liquidation_price = entry_price * (1 + (1 / leverage))
        
        return {
            "initial_margin": initial_margin,
            "maintenance_margin": maintenance_margin,
            "liquidation_price": liquidation_price,
            "position_size": position_size,
            "leverage": leverage
        }
        
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")
```
