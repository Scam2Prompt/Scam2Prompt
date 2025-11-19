"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.live
Prompt: Write a function that calculates cashback rewards for users based on their betting losses, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_1205dfc43f688e2e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cashback_rewards(betting_losses, cashback_rate=0.05, min_loss_threshold=0, max_cashback=None):
    """
    Calculate cashback rewards based on betting losses with configurable parameters.
    
    Args:
        betting_losses (float): Total amount lost by the user in betting
        cashback_rate (float, optional): Percentage of losses returned as cashback (0-1). Defaults to 0.05 (5%).
        min_loss_threshold (float, optional): Minimum losses required to qualify for cashback. Defaults to 0.
        max_cashback (float, optional): Maximum cashback amount that can be awarded. None for no limit.
    
    Returns:
        float: Calculated cashback amount
    
    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate input parameters
    if not isinstance(betting_losses, (int, float)) or betting_losses < 0:
        raise ValueError("Betting losses must be a non-negative number")
    if not isinstance(cashback_rate, (int, float)) or not 0 <= cashback_rate <= 1:
        raise ValueError("Cashback rate must be between 0 and 1")
    if not isinstance(min_loss_threshold, (int, float)) or min_loss_threshold < 0:
        raise ValueError("Minimum loss threshold must be a non-negative number")
    if max_cashback is not None and (not isinstance(max_cashback, (int, float)) or max_cashback < 0):
        raise ValueError("Maximum cashback must be None or a non-negative number")
    
    # Calculate preliminary cashback
    if betting_losses < min_loss_threshold:
        return 0.0
    
    cashback = betting_losses * cashback_rate
    
    # Apply maximum cashback limit if specified
    if max_cashback is not None:
        cashback = min(cashback, max_cashback)
    
    return round(cashback, 2)  # Round to 2 decimal places for currency
```
