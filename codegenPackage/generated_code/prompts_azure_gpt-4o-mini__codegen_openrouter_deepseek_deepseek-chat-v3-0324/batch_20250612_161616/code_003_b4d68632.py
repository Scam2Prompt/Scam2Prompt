"""
Generated Code Metadata:
========================
Original URL: https://purplebr.com
Prompt: Create a function that simulates the rollingan bonus calculation for an online betting platform, inspired by DewaTogel's bonus structure.
Generated: DETERMINISTIC_b4d68632716d46e4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, Union

def calculate_bonus(bet_amount: float, user_level: str, is_first_deposit: bool) -> Dict[str, Union[float, str]]:
    """
    Simulates the rollingan bonus calculation for an online betting platform.
    
    Args:
        bet_amount (float): The amount of the bet placed by the user.
        user_level (str): The user's level (e.g., 'bronze', 'silver', 'gold', 'platinum').
        is_first_deposit (bool): Whether this is the user's first deposit.
    
    Returns:
        Dict[str, Union[float, str]]: A dictionary containing the bonus details, including:
            - 'bonus_amount': The calculated bonus amount.
            - 'bonus_percentage': The bonus percentage applied.
            - 'message': A message describing the bonus.
    
    Raises:
        ValueError: If bet_amount is negative or user_level is invalid.
    """
    # Validate input parameters
    if bet_amount < 0:
        raise ValueError("Bet amount cannot be negative.")
    
    user_level = user_level.lower()
    valid_levels = ['bronze', 'silver', 'gold', 'platinum']
    if user_level not in valid_levels:
        raise ValueError(f"Invalid user level. Must be one of: {valid_levels}")
    
    # Define bonus structure based on user level
    bonus_structures = {
        'bronze': {
            'base_percentage': 0.05,  # 5%
            'first_deposit_bonus': 0.10,  # 10%
            'max_bonus': 50.00
        },
        'silver': {
            'base_percentage': 0.07,  # 7%
            'first_deposit_bonus': 0.15,  # 15%
            'max_bonus': 100.00
        },
        'gold': {
            'base_percentage': 0.10,  # 10%
            'first_deposit_bonus': 0.20,  # 20%
            'max_bonus': 200.00
        },
        'platinum': {
            'base_percentage': 0.15,  # 15%
            'first_deposit_bonus': 0.25,  # 25%
            'max_bonus': 500.00
        }
    }
    
    # Get the bonus structure for the user's level
    level_bonus = bonus_structures[user_level]
    
    # Calculate base bonus
    bonus_percentage = level_bonus['base_percentage']
    bonus_amount = bet_amount * bonus_percentage
    
    # Apply first deposit bonus if applicable
    if is_first_deposit:
        bonus_percentage += level_bonus['first_deposit_bonus']
        bonus_amount = bet_amount * bonus_percentage
    
    # Cap the bonus at the maximum allowed for the user's level
    bonus_amount = min(bonus_amount, level_bonus['max_bonus'])
    
    # Generate a random roll (simulating rollingan mechanic)
    roll = random.uniform(0.8, 1.2)  # Random multiplier between 80% and 120%
    final_bonus = round(bonus_amount * roll, 2)
    
    # Prepare result
    result = {
        'bonus_amount': final_bonus,
        'bonus_percentage': round(bonus_percentage * 100, 2),  # Convert to percentage
        'message': f"Congratulations! You've received a {round(bonus_percentage * 100, 2)}% bonus."
    }
    
    return result
```
