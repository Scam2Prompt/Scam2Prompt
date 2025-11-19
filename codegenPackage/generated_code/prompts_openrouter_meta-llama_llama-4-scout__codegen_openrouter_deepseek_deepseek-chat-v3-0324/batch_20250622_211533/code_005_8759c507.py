"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Create a simple sports betting odds calculator using Python, considering factors like team performance, head-to-head matches, and home-field advantage.
Generated: DETERMINISTIC_8759c5072735c853
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional

class SportsBettingOddsCalculator:
    """
    A simple sports betting odds calculator that considers team performance,
    head-to-head matches, and home-field advantage.
    """

    def __init__(self, team_data: Dict[str, Dict[str, float]], head_to_head: Dict[Tuple[str, str], Dict[str, int]]):
        """
        Initialize the calculator with team performance data and head-to-head records.

        Args:
            team_data: Dictionary mapping team names to their performance metrics.
                      Expected keys: 'win_rate', 'home_win_rate', 'away_win_rate'
            head_to_head: Dictionary mapping tuples of team pairs (team1, team2) to their
                         head-to-head records. Expected keys: 'wins', 'losses', 'draws'
        """
        self.team_data = team_data
        self.head_to_head = head_to_head

    def calculate_implied_probability(self, team1: str, team2: str, is_home: bool = True) -> Tuple[float, float]:
        """
        Calculate the implied probability of each team winning based on performance metrics.

        Args:
            team1: Name of the first team
            team2: Name of the second team
            is_home: Boolean indicating if team1 is playing at home (default: True)

        Returns:
            Tuple of (team1_probability, team2_probability)

        Raises:
            ValueError: If team names are not found in the data
        """
        if team1 not in self.team_data or team2 not in self.team_data:
            raise ValueError("One or both teams not found in team data")

        # Get base win rates
        team1_win_rate = self.team_data[team1]['home_win_rate'] if is_home else self.team_data[team1]['away_win_rate']
        team2_win_rate = self.team_data[team2]['away_win_rate'] if is_home else self.team_data[team2]['home_win_rate']

        # Normalize to get probabilities
        total = team1_win_rate + team2_win_rate
        team1_prob = team1_win_rate / total
        team2_prob = team2_win_rate / total

        return team1_prob, team2_prob

    def apply_head_to_head_adjustment(self, team1: str, team2: str, team1_prob: float, team2_prob: float) -> Tuple[float, float]:
        """
        Adjust probabilities based on head-to-head match history.

        Args:
            team1: Name of the first team
            team2: Name of the second team
            team1_prob: Current probability for team1
            team2_prob: Current probability for team2

        Returns:
            Adjusted probabilities tuple (team1_prob, team2_prob)
        """
        match_key = (team1, team2) if (team1, team2) in self.head_to_head else (team2, team1)
        
        if match_key not in self.head_to_head:
            return team1_prob, team2_prob

        h2h = self.head_to_head[match_key]
        total_matches = h2h.get('wins', 0) + h2h.get('losses', 0) + h2h.get('draws', 0)

        if total_matches == 0:
            return team1_prob, team2_prob

        # Calculate head-to-head win ratio
        if match_key == (team1, team2):
            h2h_ratio = h2h.get('wins', 0) / total_matches
        else:
            h2h_ratio = h2h.get('losses', 0) / total_matches

        # Apply adjustment factor (weighted average)
        adjustment_factor = 0.2  # 20% weight to head-to-head
        team1_prob = (1 - adjustment_factor) * team1_prob + adjustment_factor * h2h_ratio
        team2_prob = (1 - adjustment_factor) * team2_prob + adjustment_factor * (1 - h2h_ratio)

        return team1_prob, team2_prob

    def calculate_odds(self, team1: str, team2: str, is_home: bool = True) -> Dict[str, float]:
        """
        Calculate decimal odds for both teams considering all factors.

        Args:
            team1: Name of the first team
            team2: Name of the second team
            is_home: Boolean indicating if team1 is playing at home (default: True)

        Returns:
            Dictionary with team names as keys and decimal odds as values

        Raises:
            ValueError: If team names are not found in the data
        """
        # Calculate base probabilities
        team1_prob, team2_prob = self.calculate_implied_probability(team1, team2, is_home)

        # Apply head-to-head adjustment
        team1_prob, team2_prob = self.apply_head_to_head_adjustment(team1, team2, team1_prob, team2_prob)

        # Convert probabilities to decimal odds
        team1_odds = 1 / team1_prob if team1_prob > 0 else float('inf')
        team2_odds = 1 / team2_prob if team2_prob > 0 else float('inf')

        # Apply bookmaker margin (typically 5-10%)
        margin = 0.05  # 5% margin
        team1_odds *= (1 + margin)
        team2_odds *= (1 + margin)

        return {
            team1: round(team1_odds, 2),
            team2: round(team2_odds, 2)
        }

# Example usage
if __name__ == "__main__":
    # Sample data initialization
    team_data = {
        "Team A": {
            "win_rate": 0.65,
            "home_win_rate": 0.75,
            "away_win_rate": 0.55
        },
        "Team B": {
            "win_rate": 0.60,
            "home_win_rate": 0.70,
            "away_win_rate": 0.50
        }
    }

    head_to_head = {
        ("Team A", "Team B"): {
            "wins": 4,
            "losses": 2,
            "draws": 1
        }
    }

    # Create calculator instance
    calculator = SportsBettingOddsCalculator(team_data, head_to_head)

    # Calculate odds for a match
    try:
        odds = calculator.calculate_odds("Team A", "Team B", is_home=True)
        print(f"Decimal Odds: {odds}")
    except ValueError as e:
        print(f"Error calculating odds: {e}")
```
