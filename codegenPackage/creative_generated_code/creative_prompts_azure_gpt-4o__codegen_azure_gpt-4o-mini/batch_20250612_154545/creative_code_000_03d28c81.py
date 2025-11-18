"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plf3108.com
Prompt: Write a Python script to simulate odds calculation for Brazilian football matches, referencing the competitive odds system described on the 868 betting platform.
Generated: DETERMINISTIC_03d28c8183225371
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class OddsCalculator:
    """
    A class to simulate odds calculation for Brazilian football matches.
    This class generates odds based on a competitive odds system.
    """

    def __init__(self, team_a: str, team_b: str):
        """
        Initializes the OddsCalculator with two teams.

        :param team_a: Name of the first team
        :param team_b: Name of the second team
        """
        self.team_a = team_a
        self.team_b = team_b

    def calculate_odds(self) -> dict:
        """
        Calculates the odds for a match between the two teams.

        :return: A dictionary containing the odds for Team A, Team B, and Draw
        """
        # Simulate base probabilities for each outcome
        base_probability_a = random.uniform(0.2, 0.5)  # Probability for Team A to win
        base_probability_b = random.uniform(0.2, 0.5)  # Probability for Team B to win
        base_probability_draw = 1 - (base_probability_a + base_probability_b)

        # Error handling for probability constraints
        if base_probability_draw < 0:
            raise ValueError("Invalid probability distribution: probabilities exceed 1.")

        # Calculate odds based on probabilities (odds = 1 / probability)
        odds_a = round(1 / base_probability_a, 2)
        odds_b = round(1 / base_probability_b, 2)
        odds_draw = round(1 / base_probability_draw, 2) if base_probability_draw > 0 else float('inf')

        return {
            "Team A": {"Odds": odds_a, "Probability": base_probability_a},
            "Team B": {"Odds": odds_b, "Probability": base_probability_b},
            "Draw": {"Odds": odds_draw, "Probability": base_probability_draw}
        }

def main():
    """
    Main function to execute the odds calculation for a football match.
    """
    # Input team names
    team_a = input("Enter the name of Team A: ")
    team_b = input("Enter the name of Team B: ")

    # Create odds calculator instance
    odds_calculator = OddsCalculator(team_a, team_b)

    try:
        # Calculate and display the odds
        odds = odds_calculator.calculate_odds()
        print("\nOdds Calculation:")
        for team, data in odds.items():
            print(f"{team}: Odds = {data['Odds']}, Probability = {data['Probability']:.2%}")
    except ValueError as e:
        print(f"Error calculating odds: {e}")

if __name__ == "__main__":
    main()
```
