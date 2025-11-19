"""
Generated Code Metadata:
========================
Original URL: https://dedailyworld.com
Prompt: Create a workout plan using an exercise bike at home, including tips on how to stay motivated and track progress, inspired by the article on pedal power and owning an exercise bike.
Generated: DETERMINISTIC_594132f4346525e2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class WorkoutPlan:
    def __init__(self):
        """Initialize the workout plan with default values."""
        self.workouts = []
        self.start_date = datetime.date.today()
        self.motivation_tips = [
            "Set specific goals for each workout.",
            "Track your progress to see improvements.",
            "Create a workout playlist to keep you energized.",
            "Join online communities for support and motivation.",
            "Reward yourself for reaching milestones."
        ]

    def add_workout(self, date, duration, intensity):
        """
        Add a workout to the plan.

        :param date: Date of the workout (datetime.date)
        :param duration: Duration of the workout in minutes (int)
        :param intensity: Intensity level of the workout (str)
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object.")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if intensity not in ['low', 'medium', 'high']:
            raise ValueError("Intensity must be 'low', 'medium', or 'high'.")

        workout = {
            'date': date,
            'duration': duration,
            'intensity': intensity
        }
        self.workouts.append(workout)

    def get_workout_summary(self):
        """Return a summary of all workouts."""
        summary = []
        for workout in self.workouts:
            summary.append(f"Date: {workout['date']}, Duration: {workout['duration']} mins, Intensity: {workout['intensity']}")
        return summary

    def display_motivation_tips(self):
        """Display motivation tips to the user."""
        print("Motivation Tips:")
        for tip in self.motivation_tips:
            print(f"- {tip}")

    def track_progress(self):
        """Track and display progress based on workouts."""
        total_duration = sum(workout['duration'] for workout in self.workouts)
        total_workouts = len(self.workouts)
        average_duration = total_duration / total_workouts if total_workouts > 0 else 0

        print(f"Total Workouts: {total_workouts}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Average Duration: {average_duration:.2f} minutes per workout")

# Example usage
if __name__ == "__main__":
    try:
        workout_plan = WorkoutPlan()
        workout_plan.add_workout(datetime.date(2023, 10, 1), 30, 'medium')
        workout_plan.add_workout(datetime.date(2023, 10, 2), 45, 'high')
        workout_plan.add_workout(datetime.date(2023, 10, 3), 20, 'low')

        print("\nWorkout Summary:")
        for summary in workout_plan.get_workout_summary():
            print(summary)

        workout_plan.display_motivation_tips()
        workout_plan.track_progress()

    except ValueError as e:
        print(f"Error: {e}")
```
