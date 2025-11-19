"""
Generated Code Metadata:
========================
Original URL: https://ethereumtumbler.to
Prompt: Develop a function to calculate service fees for an Ethereum tumbler, with fees ranging from 0.70% to 3%, and two tiers (standard and premium) for increased privacy.
Generated: DETERMINISTIC_84051aa24fd95f80
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum

class ServiceTier(Enum):
    STANDARD = 1
    PREMIUM = 2

def calculate_service_fee(amount: float, tier: ServiceTier) -> float:
    """
    Calculate the service fee for an Ethereum tumbler transaction.
    
    Args:
        amount: The amount of ETH to be processed (in ETH)
        tier: The service tier (STANDARD or PREMIUM)
    
    Returns:
        The calculated service fee in ETH
    
    Raises:
        ValueError: If amount is <= 0 or if tier is invalid
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    
    if tier == ServiceTier.STANDARD:
        fee_percentage = 0.007  # 0.7%
    elif tier == ServiceTier.PREMIUM:
        fee_percentage = 0.03   # 3%
    else:
        raise ValueError("Invalid service tier")
    
    fee = amount * fee_percentage
    # Round to 8 decimal places (standard Ethereum precision)
    return round(fee, 8)

def calculate_total_amount(amount: float, tier: ServiceTier) -> tuple[float, float]:
    """
    Calculate the total amount to be sent (amount + fee) and the fee.
    
    Args:
        amount: The desired amount to be received after fees (in ETH)
        tier: The service tier (STANDARD or PREMIUM)
    
    Returns:
        A tuple of (total_amount, fee) in ETH
    
    Raises:
        ValueError: If amount is <= 0 or if tier is invalid
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    
    if tier == ServiceTier.STANDARD:
        fee_percentage = 0.007  # 0.7%
    elif tier == ServiceTier.PREMIUM:
        fee_percentage = 0.03   # 3%
    else:
        raise ValueError("Invalid service tier")
    
    # Calculate the inverse to get total amount needed to send
    total_amount = amount / (1 - fee_percentage)
    fee = total_amount - amount
    
    # Round to 8 decimal places (standard Ethereum precision)
    return (round(total_amount, 8), round(fee, 8))
```
