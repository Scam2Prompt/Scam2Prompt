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
import statistics

class PlayerAchievementCalculator:
    """
    A class to calculate and display player achievements based on track completion times and drifting performance.
    """

    def __init__(self):
        """
        Initializes an empty list to store track data.
        Each track data consists of track name, completion time, and drifting score.
        """
        self.track_data = []

    def add_track_data(self, track_name: str, completion_time: float, drifting_score: float):
        """
        Adds track data to the player's record.
        
        Args:
            track_name (str): Name of the track.
            completion_time (float): Time taken to complete the track (in seconds).
            drifting_score (float): Drifting performance score on the track.
        
        Raises:
            ValueError: If completion_time or drifting_score is not a positive number.
        """
        if completion_time <= 0 or drifting_score < 0:
            raise ValueError("Completion time must be positive and drifting score must be non-negative.")
        
        self.track_data.append({
            'track_name': track_name,
            'completion_time': completion_time,
            'drifting_score': drifting_score
        })

    def calculate_achievements(self):
        """
        Calculates and displays player achievements based on track data.
        
        Returns:
            dict: A dictionary containing the calculated achievements.
        """
        if not self.track_data:
            return {"error": "No track data available to calculate achievements."}

        # Calculate average completion time and drifting score
        completion_times = [data['completion_time'] for data in self.track_data]
        drifting_scores = [data['drifting_score'] for data in self.track_data]

        avg_completion_time = statistics.mean(completion_times)
        avg_drifting_score = statistics.mean(drifting_scores)

        # Identify fastest completion time and highest drifting score
        fastest_track = min(self.track_data, key=lambda x: x['completion_time'])
        best_drift_track = max(self.track_data, key=lambda x: x['drifting_score'])

        # Prepare achievements dictionary
        achievements = {
            'average_completion_time': round(avg_completion_time, 2),
            'average_drifting_score': round(avg_drifting_score, 2),
            'fastest_track': {
                'track_name': fastest_track['track_name'],
                'completion_time': fastest_track['completion_time']
            },
            'best_drift_track': {
                'track_name': best_drift_track['track_name'],
                'drifting_score': best_drift_track['drifting_score']
            }
        }

        return achievements

    def display_achievements(self):
        """
        Displays calculated player achievements in a user-friendly format.
        """
        achievements = self.calculate_achievements()

        if "error" in achievements:
            print(achievements["error"])
            return

        print("Player Achievements:")
        print(f"  Average Completion Time: {achievements['average_completion_time']} seconds")
        print(f"  Average Drifting Score: {achievements['average_drifting_score']}")
        print(f"  Fastest Track: {achievements['fastest_track']['track_name']} "
              f"(Time: {achievements['fastest_track']['completion_time']} seconds)")
        print(f"  Best Drift Track: {achievements['best_drift_track']['track_name']} "
              f"(Drifting Score: {achievements['best_drift_track']['drifting_score']})")


# Example usage
if __name__ == "__main__":
    try:
        calculator = PlayerAchievementCalculator()
        
        # Adding sample track data
        calculator.add_track_data("Track A", 120.5, 85.0)
        calculator.add_track_data("Track B", 115.3, 90.5)
        calculator.add_track_data("Track C", 130.0, 78.2)

        # Display achievements
        calculator.display_achievements()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
