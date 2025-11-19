"""
Generated Code Metadata:
========================
Original URL: https://assets-maple.finance
Prompt: Create a function that calculates potential yields for BTC holders using Maple's BTC Yield Product, considering the target APY of 5%.
Generated: DETERMINISTIC_938bd03f8221faf9
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_btc_yield(principal_btc, days_staked, target_apy=5.0):
    """
    Calculate the potential yield for BTC holders using Maple's BTC Yield Product.
    
    Args:
        principal_btc (float): Amount of BTC to stake
        days_staked (int): Number of days the BTC will be staked
        target_apy (float, optional): Target Annual Percentage Yield (default: 5.0)
    
    Returns:
        dict: {
            'principal_btc': principal_btc,
            'days_staked': days_staked,
            'target_apy': target_apy,
            'yield_btc': yield_btc,
            'total_btc': total_btc
        }
    
    Raises:
        ValueError: If principal_btc is negative or days_staked is not positive
    """
    # Input validation
    if principal_btc < 0:
        raise ValueError("Principal BTC amount cannot be negative")
    if days_staked <= 0:
        raise ValueError("Days staked must be a positive number")
    
    # Calculate daily yield rate from APY
    daily_rate = (1 + target_apy / 100) ** (1/365) - 1
    
    # Calculate yield
    yield_btc = principal_btc * ((1 + daily_rate) ** days_staked - 1)
    total_btc = principal_btc + yield_btc
    
    return {
        'principal_btc': principal_btc,
        'days_staked': days_staked,
        'target_apy': target_apy,
        'yield_btc': yield_btc,
        'total_btc': total_btc
    }

# Example usage
if __name__ == "__main__":
    try:
        result = calculate_btc_yield(1.5, 90)
        print(f"Principal BTC: {result['principal_btc']}")
        print(f"Days Staked: {result['days_staked']}")
        print(f"Target APY: {result['target_apy']}%")
        print(f"Yield BTC: {result['yield_btc']:.8f}")
        print(f"Total BTC: {result['total_btc']:.8f}")
    except ValueError as e:
        print(f"Error: {e}")
```
