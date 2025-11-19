"""
Generated Code Metadata:
========================
Original URL: https://maxonex.com
Prompt: "Design a function to calculate potential earnings on Maxonex for betting on political events, considering the 4.05% APY on cash and positions."
Generated: DETERMINISTIC_7f53227bf996ecfd
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_earnings(
    initial_investment: float,
    bet_amount: float,
    bet_odds: float,
    event_probability: float,
    duration_days: int,
    cash_apy: float = 0.0405
) -> dict:
    """
    Calculate potential earnings from political event betting on Maxonex considering cash APY.
    
    Args:
        initial_investment: Initial amount of money invested (USD)
        bet_amount: Amount to bet on the political event (USD)
        bet_odds: Odds for the bet (e.g., 2.0 for even odds)
        event_probability: Probability of the event occurring (0 to 1)
        duration_days: Duration of the investment in days
        cash_apy: Annual Percentage Yield for cash (default 4.05%)
    
    Returns:
        Dictionary containing:
        - cash_earnings: Earnings from cash APY
        - potential_bet_earnings: Potential earnings from successful bet
        - expected_value: Expected value considering probability
        - total_earnings: Sum of cash and bet earnings
        - total_expected_value: Expected value considering both cash and bet
    """
    
    # Validate inputs
    if not all(isinstance(x, (int, float)) for x in [initial_investment, bet_amount, bet_odds, event_probability, duration_days]):
        raise ValueError("All numeric inputs must be numbers")
    if bet_amount > initial_investment:
        raise ValueError("Bet amount cannot exceed initial investment")
    if not 0 <= event_probability <= 1:
        raise ValueError("Event probability must be between 0 and 1")
    if duration_days <= 0:
        raise ValueError("Duration must be positive")
    if bet_odds <= 1:
        raise ValueError("Bet odds must be greater than 1")
    
    # Calculate cash earnings from APY
    daily_rate = cash_apy / 365
    cash_earnings = initial_investment * (1 + daily_rate) ** duration_days - initial_investment
    
    # Calculate potential bet earnings
    potential_bet_earnings = bet_amount * (bet_odds - 1)
    
    # Calculate expected values
    expected_value = potential_bet_earnings * event_probability - bet_amount * (1 - event_probability)
    total_earnings = cash_earnings + potential_bet_earnings
    total_expected_value = cash_earnings + expected_value
    
    return {
        "cash_earnings": round(cash_earnings, 2),
        "potential_bet_earnings": round(potential_bet_earnings, 2),
        "expected_value": round(expected_value, 2),
        "total_earnings": round(total_earnings, 2),
        "total_expected_value": round(total_expected_value, 2)
    }
```
