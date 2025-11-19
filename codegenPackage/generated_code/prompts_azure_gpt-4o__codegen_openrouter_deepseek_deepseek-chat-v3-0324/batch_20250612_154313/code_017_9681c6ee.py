"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Generate code in Python to calculate the odds for WW88's "Kèo Châu Âu" bets, using the site's explanation of 1x2 betting.
Generated: DETERMINISTIC_9681c6eeeddc6ecb
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_european_odds(home_win_prob, draw_prob, away_win_prob, margin=0.05):
    """
    Calculate the European odds (1x2 betting) based on probabilities and bookmaker margin.
    
    Args:
        home_win_prob (float): Probability of home team winning (0 < p < 1)
        draw_prob (float): Probability of draw (0 < p < 1)
        away_win_prob (float): Probability of away team winning (0 < p < 1)
        margin (float): Bookmaker's profit margin (default: 0.05 or 5%)
        
    Returns:
        dict: Dictionary containing the calculated odds for 1 (home), X (draw), 2 (away)
        
    Raises:
        ValueError: If probabilities don't sum to 1 or any probability is invalid
    """
    
    # Validate input probabilities
    if not (0 < home_win_prob < 1 and 0 < draw_prob < 1 and 0 < away_win_prob < 1):
        raise ValueError("All probabilities must be between 0 and 1")
    
    total_prob = home_win_prob + draw_prob + away_win_prob
    if not abs(total_prob - 1) < 0.0001:  # Account for floating point precision
        raise ValueError(f"Probabilities must sum to 1 (current sum: {total_prob})")
    
    # Apply bookmaker margin
    margin_factor = 1 + margin
    
    # Calculate fair odds (without margin)
    fair_odds_home = 1 / home_win_prob
    fair_odds_draw = 1 / draw_prob
    fair_odds_away = 1 / away_win_prob
    
    # Apply margin to get actual odds
    odds_home = fair_odds_home / margin_factor
    odds_draw = fair_odds_draw / margin_factor
    odds_away = fair_odds_away / margin_factor
    
    # Round to 2 decimal places for display
    return {
        '1': round(odds_home, 2),
        'X': round(odds_draw, 2),
        '2': round(odds_away, 2)
    }

def implied_probability_from_odds(odds_home, odds_draw, odds_away):
    """
    Calculate implied probabilities from given European odds.
    
    Args:
        odds_home (float): Odds for home win
        odds_draw (float): Odds for draw
        odds_away (float): Odds for away win
        
    Returns:
        dict: Dictionary containing implied probabilities for 1, X, 2
        
    Raises:
        ValueError: If any odds are <= 1
    """
    
    if odds_home <= 1 or odds_draw <= 1 or odds_away <= 1:
        raise ValueError("All odds must be greater than 1")
    
    # Calculate implied probabilities
    implied_home = 1 / odds_home
    implied_draw = 1 / odds_draw
    implied_away = 1 / odds_away
    
    total_implied = implied_home + implied_draw + implied_away
    
    # Normalize to get true probabilities (accounting for bookmaker margin)
    true_home = implied_home / total_implied
    true_draw = implied_draw / total_implied
    true_away = implied_away / total_implied
    
    return {
        '1': round(true_home, 4),
        'X': round(true_draw, 4),
        '2': round(true_away, 4)
    }

def calculate_payout(bet_amount, selected_outcome, odds_home, odds_draw, odds_away):
    """
    Calculate potential payout for a European odds bet.
    
    Args:
        bet_amount (float): Amount wagered
        selected_outcome (str): '1', 'X', or '2'
        odds_home (float): Odds for home win
        odds_draw (float): Odds for draw
        odds_away (float): Odds for away win
        
    Returns:
        float: Potential payout amount
        
    Raises:
        ValueError: For invalid inputs
    """
    
    if bet_amount <= 0:
        raise ValueError("Bet amount must be positive")
    
    if selected_outcome not in ('1', 'X', '2'):
        raise ValueError("Outcome must be '1', 'X', or '2'")
    
    odds_map = {
        '1': odds_home,
        'X': odds_draw,
        '2': odds_away
    }
    
    selected_odds = odds_map[selected_outcome]
    
    if selected_odds <= 1:
        raise ValueError("Odds must be greater than 1")
    
    return round(bet_amount * selected_odds, 2)
```
