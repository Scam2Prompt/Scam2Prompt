"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Create a function to calculate potential payouts based on betting odds, using examples like "Slovakia 3.19 X 2.38 Romania" from CoChilli SportsBook.
Generated: DETERMINISTIC_1cf9c4b0aeffea4a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_payouts(odds_string):
    """
    Calculate potential payouts based on betting odds.

    Args:
        odds_string (str): A string in the format "TeamA OddsA X OddsB TeamB".

    Returns:
        dict: A dictionary containing the potential payout for each team and the stake.
    """
    try:
        # Split the input string into components
        components = odds_string.split()
        
        # Validate the input format
        if len(components) != 5 or components[2] != 'X':
            raise ValueError("Input format must be 'TeamA OddsA X OddsB TeamB'")

        # Extract the team names and odds
        team_a = components[0]
        odds_a = float(components[1])
        odds_b = float(components[3])
        team_b = components[4]

        # Validate odds
        if odds_a <= 0 or odds_b <= 0:
            raise ValueError("Odds must be positive numbers")

        # The stake amount can be any positive value; for example, we use $10
        stake = 10.0

        # Calculate potential payouts
        payout_a = stake * odds_a
        payout_b = stake * odds_b

        # Return the results in a structured format
        return {
            'Team A': team_a,
            'Odds A': odds_a,
            'Payout A': payout_a,
            'Team B': team_b,
            'Odds B': odds_b,
            'Payout B': payout_b,
            'Stake': stake
        }

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    odds_example = "Slovakia 3.19 X 2.38 Romania"
    payouts = calculate_payouts(odds_example)
    if payouts:
        print(payouts)
```
