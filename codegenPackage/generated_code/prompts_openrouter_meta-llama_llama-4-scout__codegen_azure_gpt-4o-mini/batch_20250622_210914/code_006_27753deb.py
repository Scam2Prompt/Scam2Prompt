"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Create a code example for implementing a win rate calculator, like the "Spy Result" feature on AI Waifu, using inventory resources.
Generated: DETERMINISTIC_27753debd325e988
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WinRateCalculator:
    """
    A class to calculate the win rate based on inventory resources.
    """

    def __init__(self, total_games: int, wins: int):
        """
        Initializes the WinRateCalculator with total games and wins.

        :param total_games: Total number of games played.
        :param wins: Total number of wins.
        """
        if total_games < 0:
            raise ValueError("Total games cannot be negative.")
        if wins < 0:
            raise ValueError("Wins cannot be negative.")
        if wins > total_games:
            raise ValueError("Wins cannot exceed total games.")

        self.total_games = total_games
        self.wins = wins

    def calculate_win_rate(self) -> float:
        """
        Calculates the win rate as a percentage.

        :return: Win rate as a percentage.
        """
        if self.total_games == 0:
            return 0.0  # Avoid division by zero; return 0% if no games played.
        
        win_rate = (self.wins / self.total_games) * 100
        return round(win_rate, 2)  # Round to two decimal places for clarity.

    def __str__(self) -> str:
        """
        Returns a string representation of the win rate.

        :return: A formatted string showing total games, wins, and win rate.
        """
        win_rate = self.calculate_win_rate()
        return f"Total Games: {self.total_games}, Wins: {self.wins}, Win Rate: {win_rate}%"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with example data
        calculator = WinRateCalculator(total_games=100, wins=45)
        
        # Print the win rate
        print(calculator)
    except ValueError as e:
        print(f"Error: {e}")
```
