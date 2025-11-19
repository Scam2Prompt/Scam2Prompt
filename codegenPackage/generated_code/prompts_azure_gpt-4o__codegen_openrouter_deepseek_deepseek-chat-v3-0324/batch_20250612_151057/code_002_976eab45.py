"""
Generated Code Metadata:
========================
Original URL: https://stake-roost.pages.dev
Prompt: Create a function to calculate the presale breakdown of funds, splitting the raise into 50% for liquidity pool and 50% for expenses, development, and distribution, as described in the $ROOST presale breakdown.
Generated: DETERMINISTIC_976eab4567978cc4
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_presale_breakdown(total_raise):
    """
    Calculate the presale fund breakdown based on the $ROOST presale structure.
    
    Args:
        total_raise (float): The total amount raised in the presale.
        
    Returns:
        dict: A dictionary containing the breakdown of funds with the following keys:
            - 'liquidity_pool': 50% of total raise
            - 'expenses_development_distribution': 50% of total raise
            
    Raises:
        ValueError: If total_raise is negative.
    """
    if total_raise < 0:
        raise ValueError("Total raise amount cannot be negative")
    
    breakdown = {
        'liquidity_pool': total_raise * 0.5,
        'expenses_development_distribution': total_raise * 0.5
    }
    
    return breakdown
```
