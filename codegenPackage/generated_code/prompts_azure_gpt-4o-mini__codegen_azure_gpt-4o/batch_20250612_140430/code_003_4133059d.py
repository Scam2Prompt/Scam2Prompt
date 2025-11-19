"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Develop a function that calculates potential winnings for a sports bet based on odds and stake, reflecting the betting options available at 868.
Generated: DETERMINISTIC_4133059d8fabec6a
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sports_betting.py

def calculate_potential_winnings(odds: float, stake: float) -> float:
    """
    Calculate potential winnings for a sports bet.

    Args:
        odds (float): The decimal odds for the bet. 
                      Example: 2.5 means you win 2.5 times your stake if successful.
        stake (float): The amount of money wagered on the bet.

    Returns:
        float: The potential winnings, including the original stake.

    Raises:
        ValueError: If odds or stake are invalid (e.g., negative or zero).
    """
    # Validate inputs
    if odds <= 0:
        raise ValueError("Odds must be greater than zero.")
    if stake <= 0:
        raise ValueError("Stake must be greater than zero.")

    # Calculate potential winnings
    potential_winnings = odds * stake

    return potential_winnings


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        odds = 2.5  # Decimal odds
        stake = 100.0  # Stake in currency (e.g., dollars)

        # Calculate and display potential winnings
        winnings = calculate_potential_winnings(odds, stake)
        print(f"Potential winnings: ${winnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
