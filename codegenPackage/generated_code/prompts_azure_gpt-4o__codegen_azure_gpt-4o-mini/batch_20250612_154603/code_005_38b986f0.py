"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Write code to implement a "Win Streak Booster" feature that applies a multiplier during winning streaks, as described in Kramat77's platform.
Generated: DETERMINISTIC_38b986f0baad5ab7
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WinStreakBooster:
    """
    A class to manage win streaks and apply multipliers based on the length of the streak.
    """

    def __init__(self):
        """
        Initializes the WinStreakBooster with default values.
        """
        self.current_streak = 0  # Current win streak count
        self.multiplier = 1.0     # Current multiplier for the streak

    def reset_streak(self):
        """
        Resets the current win streak and multiplier.
        """
        self.current_streak = 0
        self.multiplier = 1.0

    def update_streak(self, won: bool):
        """
        Updates the win streak based on the outcome of a game.

        Args:
            won (bool): True if the game was won, False otherwise.
        """
        if won:
            self.current_streak += 1
            self.multiplier = self.calculate_multiplier(self.current_streak)
        else:
            self.reset_streak()

    def calculate_multiplier(self, streak: int) -> float:
        """
        Calculates the multiplier based on the current win streak.

        Args:
            streak (int): The current win streak count.

        Returns:
            float: The calculated multiplier.
        """
        if streak < 1:
            return 1.0
        elif streak <= 3:
            return 1.0 + (0.1 * streak)  # 10% increase per win for the first 3 wins
        elif streak <= 5:
            return 1.3 + (0.05 * (streak - 3))  # 30% for 3 wins, 5% for each additional win
        else:
            return 1.5  # Cap the multiplier at 1.5 after 5 wins

    def get_current_streak(self) -> int:
        """
        Returns the current win streak count.

        Returns:
            int: The current win streak count.
        """
        return self.current_streak

    def get_multiplier(self) -> float:
        """
        Returns the current multiplier based on the win streak.

        Returns:
            float: The current multiplier.
        """
        return self.multiplier


# Example usage
if __name__ == "__main__":
    booster = WinStreakBooster()

    # Simulate a series of game outcomes
    outcomes = [True, True, True, False, True, True, True, True, True]  # True = win, False = loss

    for outcome in outcomes:
        booster.update_streak(outcome)
        print(f"Current Streak: {booster.get_current_streak()}, Multiplier: {booster.get_multiplier():.2f}")
```
