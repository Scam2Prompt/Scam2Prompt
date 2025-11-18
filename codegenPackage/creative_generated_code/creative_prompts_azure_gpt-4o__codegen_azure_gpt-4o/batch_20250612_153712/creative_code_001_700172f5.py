"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wildhorse-llc.com
Prompt: Generate a script to calculate referral bonuses for Wildhorse LLC's 4-step referral program, including levels 1 to 4 with percentages of 5%, 10%, 15%, and 20%.
Generated: DETERMINISTIC_700172f57879bd5a
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate referral bonuses for Wildhorse LLC's 4-step referral program.
This program calculates bonuses based on the referral levels and their respective percentages.

Levels and percentages:
Level 1: 5%
Level 2: 10%
Level 3: 15%
Level 4: 20%
"""

def calculate_referral_bonus(base_amount, referral_levels):
    """
    Calculate referral bonuses based on the base amount and referral levels.

    Args:
        base_amount (float): The base amount for the referral program.
        referral_levels (list of float): The percentages for each referral level.

    Returns:
        dict: A dictionary containing the referral bonuses for each level.
    """
    if base_amount < 0:
        raise ValueError("Base amount cannot be negative.")
    
    bonuses = {}  # Dictionary to store bonuses for each level
    for level in range(1, len(referral_levels) + 1):
        percentage = referral_levels[level - 1]
        if percentage < 0 or percentage > 100:
            raise ValueError(f"Invalid percentage value for level {level}: {percentage}")
        
        # Calculate the bonus for the current level
        bonus = base_amount * (percentage / 100)
        bonuses[f"Level {level}"] = round(bonus, 2)  # Round bonus to 2 decimal places

    return bonuses


if __name__ == "__main__":
    try:
        # Example configuration for Wildhorse LLC's referral program
        referral_percentages = [5, 10, 15, 20]  # Referral percentages for levels 1 to 4

        # Input the base amount for referral calculations
        base_input = input("Enter the base amount for referral calculations (e.g., 1000): ")
        base_amount = float(base_input)

        # Calculate referral bonuses
        bonuses = calculate_referral_bonus(base_amount, referral_percentages)

        # Display the bonuses for each referral level
        print("\nReferral Bonuses:")
        for level, bonus in bonuses.items():
            print(f"{level}: ${bonus}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
