"""
Generated Code Metadata:
========================
Original URL: https://xchangelite.com
Prompt: Write a Python function to calculate potential winnings from a no deposit bonus in a casino, similar to the examples provided on Xchange Elite.
Generated: DETERMINISTIC_e5f1982801c2bbf0
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_no_deposit_bonus_winnings(
    bonus_amount: float,
    wagering_requirement: float,
    max_withdrawal: float = None,
    game_contribution: float = 1.0
) -> dict:
    """
    Calculate potential winnings from a no deposit casino bonus.

    Args:
        bonus_amount: The amount of bonus received (e.g., $10)
        wagering_requirement: The multiplier for wagering (e.g., 40x)
        max_withdrawal: Maximum allowed withdrawal from bonus (optional)
        game_contribution: Percentage of bets that count towards wagering (default 1.0)

    Returns:
        dict: {
            'wagering_required': total amount to wager,
            'max_possible_winnings': theoretical maximum winnings,
            'realistic_winnings': estimated winnings considering game contribution,
            'max_withdrawal': capped winnings if max_withdrawal is set
        }

    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if bonus_amount <= 0:
        raise ValueError("Bonus amount must be positive")
    if wagering_requirement <= 0:
        raise ValueError("Wagering requirement must be positive")
    if game_contribution <= 0 or game_contribution > 1:
        raise ValueError("Game contribution must be between 0 and 1")
    if max_withdrawal is not None and max_withdrawal <= 0:
        raise ValueError("Max withdrawal must be positive if specified")

    # Calculate wagering required
    wagering_required = bonus_amount * wagering_requirement

    # Calculate theoretical maximum winnings (assuming 100% RTP)
    max_possible_winnings = bonus_amount

    # Calculate realistic winnings considering game contribution
    realistic_winnings = max_possible_winnings * game_contribution

    # Apply max withdrawal limit if specified
    if max_withdrawal is not None:
        realistic_winnings = min(realistic_winnings, max_withdrawal)
        max_possible_winnings = min(max_possible_winnings, max_withdrawal)

    return {
        'wagering_required': round(wagering_required, 2),
        'max_possible_winnings': round(max_possible_winnings, 2),
        'realistic_winnings': round(realistic_winnings, 2),
        'max_withdrawal': round(max_withdrawal, 2) if max_withdrawal is not None else None
    }
```
