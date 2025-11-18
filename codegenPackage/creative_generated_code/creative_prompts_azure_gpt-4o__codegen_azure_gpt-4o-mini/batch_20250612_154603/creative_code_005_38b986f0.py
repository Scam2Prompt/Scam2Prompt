"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomixmixer.com
Prompt: Write code to implement a "Win Streak Booster" feature that applies a multiplier during winning streaks, as described in Kramat77's platform.
Generated: DETERMINISTIC_38b986f0baad5ab7
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WinStreakBooster:
    def __init__(self):
        """
        Initializes the WinStreakBooster with necessary attributes.
        """
        self.win_streak = 0  # Current win streak count
        self.multiplier = 1.0  # Current multiplier for the win streak

    def record_win(self):
        """
        Record a win and update the win streak and multiplier.
        """
        self.win_streak += 1
        self.update_multiplier()
        
    def record_loss(self):
        """
        Record a loss and reset the win streak and multiplier.
        """
        self.win_streak = 0
        self.multiplier = 1.0  # Reset multiplier on loss
    
    def update_multiplier(self):
        """
        Update the multiplier based on the current win streak.
        Multiplier increases for every 3 consecutive wins.
        """
        if self.win_streak >= 3:
            self.multiplier = 1.0 + (self.win_streak // 3) * 0.5  # Increase by 0.5 for every 3 wins
        else:
            self.multiplier = 1.0  # No multiplier for less than 3 wins

    def get_multiplier(self):
        """
        Get the current multiplier.
        
        Returns:
            float: Current multiplier value.
        """
        return self.multiplier
    
    def reset_streak(self):
        """
        Resets the win streak and multiplier to the initial state.
        """
        self.win_streak = 0
        self.multiplier = 1.0

    def current_streak_info(self):
        """
        Get information about the current win streak and multiplier.
        
        Returns:
            dict: A dictionary containing the win streak and multiplier.
        """
        return {
            'win_streak': self.win_streak,
            'multiplier': self.multiplier
        }

# Example usage:
if __name__ == "__main__":
    try:
        booster = WinStreakBooster()
        # Simulate a win streak
        booster.record_win()
        booster.record_win()
        booster.record_win()
        print(booster.current_streak_info())  # Should show a multiplier of 1.0

        booster.record_win()  # Fourth win
        print(booster.current_streak_info())  # Should show a multiplier of 1.5

        booster.record_loss()  # Loss resets the streak
        print(booster.current_streak_info())  # Should show a win streak of 0 and multiplier of 1.0
    except Exception as e:
        print(f"An error occurred: {e}")
```
