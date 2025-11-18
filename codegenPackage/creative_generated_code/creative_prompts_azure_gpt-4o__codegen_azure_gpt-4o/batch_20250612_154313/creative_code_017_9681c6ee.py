"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Generate code in Python to calculate the odds for WW88's "Kèo Châu Âu" bets, using the site's explanation of 1x2 betting.
Generated: DETERMINISTIC_9681c6eeeddc6ecb
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the odds for WW88's "Kèo Châu Âu" 1x2 betting system.
1x2 betting refers to:
- '1': Betting on the home team to win
- 'X': Betting on a draw between the two teams
- '2': Betting on the away team to win

The code takes the probabilities of each outcome (as percentages or decimals)
and calculates the implied odds for each outcome based on the probabilities
provided.
"""

def calculate_odds(probabilities):
    """
    Calculate implied odds for 1x2 betting based on given probabilities.

    Args:
        probabilities (dict): A dictionary with keys '1', 'X', '2' and values 
                              representing the probabilities of each outcome 
                              (as decimals between 0 and 1).

    Returns:
        dict: A dictionary with keys '1', 'X', '2' and values representing the
              implied odds for each outcome.
              
    Raises:
        ValueError: If probabilities are not valid or do not sum up to 1 (100%).
    """
    # Validate input probabilities
    if not isinstance(probabilities, dict):
        raise ValueError("Probabilities must be provided as a dictionary.")
    if not all(key in ['1', 'X', '2'] for key in probabilities.keys()):
        raise ValueError("Probabilities dictionary must contain keys '1', 'X', '2'.")
    if not all(isinstance(value, (int, float)) and 0 <= value <= 1 for value in probabilities.values()):
        raise ValueError("Probability values must be decimals between 0 and 1.")
    if not abs(sum(probabilities.values()) - 1.0) < 0.001:  # Handle rounding errors
        raise ValueError("Probabilities must sum up to 1 (100%).")
    
    # Calculate implied odds
    odds = {}
    for outcome, probability in probabilities.items():
        # Avoid division by zero
        if probability == 0:
            odds[outcome] = float('inf')  # Infinite odds if probability is 0
        else:
            odds[outcome] = round(1 / probability, 2)  # Round to 2 decimal places
    
    return odds


if __name__ == "__main__":
    # Example usage
    try:
        # Probabilities for 1x2 betting (as decimals)
        example_probabilities = {
            '1': 0.50,  # 50% chance of home team winning
            'X': 0.25,  # 25% chance of a draw
            '2': 0.25   # 25% chance of away team winning
        }

        # Calculate odds
        calculated_odds = calculate_odds(example_probabilities)

        # Display results
        print("Implied Odds for 1x2 Betting:")
        for outcome, odd in calculated_odds.items():
            print(f"{outcome}: {odd}")
    except ValueError as e:
        print(f"Error: {e}")
```
