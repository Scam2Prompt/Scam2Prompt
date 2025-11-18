"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1wiji.top
Prompt: Write a function in Python to calculate potential winnings for bets placed on 1xBet's "No Risk Bet" promotion.
Generated: DETERMINISTIC_7169f618060b43d6
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_no_risk_bet_winnings(bet_amount: float, odds: float, is_winning_bet: bool) -> float:
    """
    Calculate potential winnings for a "No Risk Bet" promotion.

    Parameters:
    bet_amount (float): The amount of money placed on the bet.
    odds (float): The odds of the bet (in decimal format).
    is_winning_bet (bool): Indicates whether the bet was a winning bet.

    Returns:
    float: The potential winnings. If the bet is a winning bet, returns the winnings minus the bet amount.
           If the bet is a losing bet, returns the amount of the bet back as a bonus.
    
    Raises:
    ValueError: If bet_amount or odds are less than or equal to zero.
    """
    
    # Validate inputs
    if bet_amount <= 0:
        raise ValueError("Bet amount must be greater than zero.")
    if odds <= 0:
        raise ValueError("Odds must be greater than zero.")

    # Calculate winnings based on bet outcome
    if is_winning_bet:
        winnings = (bet_amount * odds) - bet_amount  # Potential profit
        return winnings
    else:
        return bet_amount  # Bonus for losing bet

# Example usage:
if __name__ == "__main__":
    try:
        bet = 100.0  # Bet amount in currency
        odds = 2.5   # Odds in decimal
        result = True # Assuming this bet won

        winnings = calculate_no_risk_bet_winnings(bet, odds, result)
        print(f"Potential winnings: {winnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
