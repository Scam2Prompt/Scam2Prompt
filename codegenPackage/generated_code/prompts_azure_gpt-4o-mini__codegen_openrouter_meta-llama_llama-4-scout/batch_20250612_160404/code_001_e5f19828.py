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
def calculate_potential_winnings(bonus_amount: float, wagering_requirement: int, 
                                  bet_type: str, bet_amount: float, 
                                  odds: float) -> dict:
    """
    Calculate potential winnings from a no deposit bonus in a casino.

    Args:
    - bonus_amount (float): The amount of the no deposit bonus.
    - wagering_requirement (int): The wagering requirement for the bonus.
    - bet_type (str): The type of bet (e.g., 'even money', 'odds against').
    - bet_amount (float): The amount of the bet.
    - odds (float): The decimal odds of the bet.

    Returns:
    - dict: A dictionary containing the potential winnings and the remaining wagering requirement.

    Raises:
    - ValueError: If the bet type is not supported or if the bet amount or odds are invalid.
    """

    # Check if the bet type is supported
    supported_bet_types = ['even money', 'odds against']
    if bet_type not in supported_bet_types:
        raise ValueError(f"Unsupported bet type. Supported types: {supported_bet_types}")

    # Check if the bet amount and odds are valid
    if bet_amount <= 0:
        raise ValueError("Bet amount must be greater than zero.")
    if odds <= 1.0:
        raise ValueError("Odds must be greater than 1.0.")

    # Calculate the potential winnings
    if bet_type == 'even money':
        potential_winnings = bet_amount * odds
    elif bet_type == 'odds against':
        potential_winnings = (bet_amount * odds) - bet_amount

    # Calculate the remaining wagering requirement
    total_wagered = bet_amount
    remaining_wagering_requirement = max(0, wagering_requirement - total_wagered)

    # Check if the wagering requirement is met
    if remaining_wagering_requirement == 0:
        potential_winnings += bonus_amount

    return {
        'potential_winnings': potential_winnings,
        'remaining_wagering_requirement': remaining_wagering_requirement
    }


def main():
    try:
        bonus_amount = 10.0
        wagering_requirement = 30
        bet_type = 'even money'
        bet_amount = 5.0
        odds = 2.0

        result = calculate_potential_winnings(bonus_amount, wagering_requirement, 
                                              bet_type, bet_amount, odds)
        print(f"Potential Winnings: {result['potential_winnings']}")
        print(f"Remaining Wagering Requirement: {result['remaining_wagering_requirement']}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
