"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Write Python code to calculate progress in speed and explosiveness for athletes based on data from training sessions, using metrics like acceleration and test records mentioned on Blaise Strong's webpage.
Generated: DETERMINISTIC_74331b4ccc3e4463
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

class AthletePerformanceTracker:
    """
    A class to calculate progress in speed and explosiveness for athletes
    based on acceleration and test records.
    """

    def __init__(self):
        """
        Initialize AthletePerformanceTracker with an empty dataset.
        """
        self.data = {}

    def add_training_data(self, athlete_id, session_date, acceleration_data, explosiveness_data):
        """
        Adds training session data for a specific athlete.

        Parameters:
        athlete_id (str): Unique identifier for the athlete.
        session_date (str): Date of the training session in 'YYYY-MM-DD' format.
        acceleration_data (list): List of acceleration values (e.g., m/s^2) recorded during the session.
        explosiveness_data (list): List of explosiveness test values (e.g., jump height in cm).
        """
        if athlete_id not in self.data:
            self.data[athlete_id] = {}
        
        self.data[athlete_id][session_date] = {
            "acceleration": acceleration_data,
            "explosiveness": explosiveness_data
        }

    def calculate_progress(self, athlete_id):
        """
        Calculates progress in speed and explosiveness for a given athlete.

        Parameters:
        athlete_id (str): Unique identifier for the athlete.

        Returns:
        dict: A dictionary containing progress metrics for acceleration and explosiveness:
              {
                  "acceleration_progress": <value>,
                  "explosiveness_progress": <value>
              }
        """
        if athlete_id not in self.data:
            raise ValueError(f"No data found for athlete ID: {athlete_id}")

        sessions = self.data[athlete_id]
        if len(sessions) < 2:
            raise ValueError("Insufficient training data. At least two sessions are required to calculate progress.")

        sorted_dates = sorted(sessions.keys())
        first_session = sessions[sorted_dates[0]]
        last_session = sessions[sorted_dates[-1]]

        # Calculate average acceleration for first and last session
        avg_acceleration_start = statistics.mean(first_session["acceleration"])
        avg_acceleration_end = statistics.mean(last_session["acceleration"])

        # Calculate average explosiveness for first and last session
        avg_explosiveness_start = statistics.mean(first_session["explosiveness"])
        avg_explosiveness_end = statistics.mean(last_session["explosiveness"])

        # Calculate progress metrics
        acceleration_progress = avg_acceleration_end - avg_acceleration_start
        explosiveness_progress = avg_explosiveness_end - avg_explosiveness_start

        return {
            "acceleration_progress": acceleration_progress,
            "explosiveness_progress": explosiveness_progress
        }

    def get_summary(self, athlete_id):
        """
        Provides a summary of the athlete's performance progress.

        Parameters:
        athlete_id (str): Unique identifier for the athlete.

        Returns:
        str: Summary of progress in human-readable format.
        """
        try:
            progress = self.calculate_progress(athlete_id)
            summary = (
                f"Athlete ID: {athlete_id}\n"
                f"Acceleration Progress: {progress['acceleration_progress']:.2f} m/s^2\n"
                f"Explosiveness Progress: {progress['explosiveness_progress']:.2f} cm\n"
            )
            return summary
        except ValueError as e:
            return str(e)


# Example Usage
if __name__ == "__main__":
    tracker = AthletePerformanceTracker()

    # Example data for athlete with ID 'A123'
    tracker.add_training_data('A123', '2023-01-01', [2.5, 2.8, 3.0], [40, 42, 45])
    tracker.add_training_data('A123', '2023-02-01', [3.2, 3.5, 3.7], [50, 52, 55])

    print(tracker.get_summary('A123'))

    # Example output for athlete with insufficient data
    print(tracker.get_summary('B456'))
```
