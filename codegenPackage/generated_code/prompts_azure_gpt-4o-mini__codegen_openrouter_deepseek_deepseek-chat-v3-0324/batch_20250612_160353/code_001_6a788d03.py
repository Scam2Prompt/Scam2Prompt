"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a function to calculate the total bonuses a new player would receive after their first four deposits at Jackpot Cow Casino, including the 100% up to €500 first deposit bonus.
Generated: DETERMINISTIC_6a788d030772134c
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_bonuses(deposits):
    """
    Calculate the total bonuses a new player receives after their first four deposits at Jackpot Cow Casino.
    
    The bonus structure is:
    - 1st deposit: 100% up to €500
    - 2nd deposit: 50% up to €300
    - 3rd deposit: 25% up to €200
    - 4th deposit: 25% up to €200
    
    Args:
        deposits (list): List of 4 deposit amounts in euros
        
    Returns:
        float: Total bonus amount in euros
        
    Raises:
        ValueError: If deposits list doesn't contain exactly 4 values or contains negative numbers
    """
    if len(deposits) != 4:
        raise ValueError("Exactly 4 deposit amounts are required")
    
    if any(deposit < 0 for deposit in deposits):
        raise ValueError("Deposit amounts cannot be negative")
    
    bonus_rules = [
        {"percentage": 1.0, "cap": 500},   # 1st deposit
        {"percentage": 0.5, "cap": 300},   # 2nd deposit
        {"percentage": 0.25, "cap": 200},  # 3rd deposit
        {"percentage": 0.25, "cap": 200}   # 4th deposit
    ]
    
    total_bonus = 0.0
    
    for i in range(4):
        deposit = deposits[i]
        rule = bonus_rules[i]
        bonus = min(deposit * rule["percentage"], rule["cap"])
        total_bonus += bonus
    
    return round(total_bonus, 2)
```
