"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Develop a function to calculate and display player achievements based on track completion times and drifting performance, inspired by Rally Racer Dirt's achievement system.
Generated: DETERMINISTIC_a93125d6caa0b95e
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlayerAchievement:
    def __init__(self, player_name):
        """
        Initializes the PlayerAchievement object with the player's name.

        :param player_name: str - Name of the player
        """
        self.player_name = player_name
        self.achievements = {
            'Fastest Lap': False,
            'Drift Master': False,
            'Consistent Racer': False
        }

    def calculate_achievements(self, lap_time, drift_score):
        """
        Calculates player achievements based on lap time and drift score.

        :param lap_time: float - Time taken to complete the track in seconds
        :param drift_score: float - Score based on drifting performance
        """
        try:
            # Check for valid input values
            if lap_time <= 0 or drift_score < 0:
                raise ValueError("Lap time must be positive and drift score must be non-negative.")

            # Define achievement thresholds
            fastest_lap_threshold = 30.0  # Example threshold for fastest lap
            drift_master_threshold = 75.0   # Example threshold for drift score
            consistent_racer_threshold = 5   # Example threshold for consistent performance

            # Evaluate achievements
            if lap_time < fastest_lap_threshold:
                self.achievements['Fastest Lap'] = True

            if drift_score >= drift_master_threshold:
                self.achievements['Drift Master'] = True

            if lap_time < 40.0:  # Example for consistent racer (assuming multiple laps)
                self.achievements['Consistent Racer'] = True

        except ValueError as e:
            print(f"Error calculating achievements: {e}")

    def display_achievements(self):
        """
        Displays the player's achievements.
        """
        print(f"Achievements for {self.player_name}:")
        for achievement, earned in self.achievements.items():
            status = "Unlocked" if earned else "Locked"
            print(f"- {achievement}: {status}")


# Example usage:
if __name__ == "__main__":
    player = PlayerAchievement("John Doe")
    player.calculate_achievements(lap_time=29.5, drift_score=80.0)
    player.display_achievements()
```
