"""
Generated Code Metadata:
========================
Original URL: https://cybro-en.pages.dev
Prompt: Generate code to calculate the yield from CYBRO's liquidity pools, factoring in the APY for stablecoins (5%) and the CYBRO token bonuses.
Generated: DETERMINISTIC_8146f72292b10018
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Union

def calculate_yield(
    principal: float,
    stablecoin_apy: float = 0.05,
    cybro_bonus: float = 0.0,
    days: int = 365
) -> Dict[str, Union[float, str]]:
    """
    Calculate the yield from CYBRO's liquidity pools, factoring in stablecoin APY and CYBRO token bonuses.
    
    Args:
        principal: Initial investment amount
        stablecoin_apy: Annual Percentage Yield for stablecoins (default 5%)
        cybro_bonus: Additional bonus from CYBRO tokens (as decimal, e.g., 0.1 for 10%)
        days: Investment period in days (default 365)
        
    Returns:
        Dictionary containing:
        - 'stablecoin_yield': Yield from stablecoins
        - 'bonus_yield': Yield from CYBRO bonus
        - 'total_yield': Combined yield
        - 'total_amount': Principal + total yield
        - 'roi': Return on investment percentage
    """
    try:
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if days <= 0:
            raise ValueError("Investment period must be positive")
        if stablecoin_apy < 0 or cybro_bonus < 0:
            raise ValueError("APY and bonus values cannot be negative")
            
        # Calculate daily rate
        daily_rate = (1 + stablecoin_apy) ** (1/365) - 1
        
        # Calculate stablecoin yield
        stablecoin_yield = principal * ((1 + daily_rate) ** days - 1)
        
        # Calculate bonus yield
        bonus_yield = stablecoin_yield * cybro_bonus
        
        # Calculate totals
        total_yield = stablecoin_yield + bonus_yield
        total_amount = principal + total_yield
        roi = (total_yield / principal) * 100
        
        return {
            'stablecoin_yield': round(stablecoin_yield, 2),
            'bonus_yield': round(bonus_yield, 2),
            'total_yield': round(total_yield, 2),
            'total_amount': round(total_amount, 2),
            'roi': round(roi, 2)
        }
        
    except ValueError as ve:
        return {'error': str(ve)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    result = calculate_yield(
        principal=10000,
        stablecoin_apy=0.05,
        cybro_bonus=0.1,
        days=365
    )
    print(result)
```
