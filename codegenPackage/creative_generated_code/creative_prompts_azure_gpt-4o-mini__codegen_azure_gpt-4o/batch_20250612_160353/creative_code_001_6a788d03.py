"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a function to calculate the total bonuses a new player would receive after their first four deposits at Jackpot Cow Casino, including the 100% up to €500 first deposit bonus.
Generated: DETERMINISTIC_6a788d030772134c
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_bonus(deposits):
    """
    Calculate the total bonuses for a new player after their first four deposits
    at Jackpot Cow Casino.

    Args:
        deposits (list): A list of up to four deposit amounts (in euros).

    Returns:
        float: The total bonus amount (in euros).
    
    Raises:
        ValueError: If deposits are empty or contain invalid data.
    """
    # Validate input
    if not deposits or not isinstance(deposits, list):
        raise ValueError("Deposits must be a non-empty list.")
    if len(deposits) > 4:
        raise ValueError("Only the first four deposits are eligible for bonuses.")
    if any(not isinstance(deposit, (int, float)) or deposit <= 0 for deposit in deposits):
        raise ValueError("All deposit amounts must be positive numbers.")

    total_bonus = 0.0

    # Bonus rules (assuming all are based on percentage matches capped at a maximum)
    bonus_rules = [
        {"match_percent": 100, "max_bonus": 500},  # First deposit: 100% up to €500
        {"match_percent": 50, "max_bonus": 300},   # Second deposit: 50% up to €300
        {"match_percent": 25, "max_bonus": 200},   # Third deposit: 25% up to €200
        {"match_percent": 10, "max_bonus": 100},   # Fourth deposit: 10% up to €100
    ]

    # Iterate over deposits and calculate bonuses
    for i, deposit in enumerate(deposits):
        if i >= len(bonus_rules):  # No more bonus rules for additional deposits
            break

        match_percent = bonus_rules[i]["match_percent"]
        max_bonus = bonus_rules[i]["max_bonus"]

        # Calculate the bonus for this deposit
        bonus = min((deposit * match_percent / 100), max_bonus)
        total_bonus += bonus

    return total_bonus


# Example usage
try:
    player_deposits = [600, 500, 300, 100]  # Deposits in euros
    total = calculate_total_bonus(player_deposits)
    print(f"Total Bonuses: €{total:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
