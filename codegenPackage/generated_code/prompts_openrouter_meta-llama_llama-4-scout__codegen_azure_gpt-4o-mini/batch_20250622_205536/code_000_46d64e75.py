"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a 16-week half marathon training plan that includes long runs, interval runs, tempo runs, and recovery runs, and provide guidance on building endurance and speed.
Generated: DETERMINISTIC_46d64e75a2d9139d
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class HalfMarathonTrainingPlan:
    def __init__(self, start_date):
        """
        Initializes the training plan with a start date.
        
        :param start_date: The date to start the training plan (YYYY-MM-DD format).
        """
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.plan = self.generate_training_plan()

    def generate_training_plan(self):
        """
        Generates a 16-week training plan for a half marathon.
        
        :return: A list of training days with their respective workouts.
        """
        training_plan = []
        for week in range(1, 17):
            training_plan.append(self.create_week_plan(week))
        return training_plan

    def create_week_plan(self, week):
        """
        Creates a weekly training plan based on the week number.
        
        :param week: The week number in the training plan (1-16).
        :return: A dictionary representing the week's training schedule.
        """
        week_plan = {
            'Week': week,
            'Monday': self.recovery_run(3),
            'Tuesday': self.interval_run(5),
            'Wednesday': self.rest_day(),
            'Thursday': self.tempo_run(4 + week // 2),
            'Friday': self.rest_day(),
            'Saturday': self.long_run(8 + week),
            'Sunday': self.recovery_run(3)
        }
        return week_plan

    def recovery_run(self, distance):
        """
        Returns a recovery run workout.
        
        :param distance: Distance in miles for the recovery run.
        :return: A string describing the recovery run.
        """
        return f"Recovery Run: {distance} miles at an easy pace."

    def interval_run(self, distance):
        """
        Returns an interval run workout.
        
        :param distance: Total distance in miles for the interval run.
        :return: A string describing the interval run.
        """
        return f"Interval Run: {distance} miles with intervals (e.g., 4x800m at 5K pace)."

    def tempo_run(self, distance):
        """
        Returns a tempo run workout.
        
        :param distance: Distance in miles for the tempo run.
        :return: A string describing the tempo run.
        """
        return f"Tempo Run: {distance} miles at a comfortably hard pace."

    def long_run(self, distance):
        """
        Returns a long run workout.
        
        :param distance: Distance in miles for the long run.
        :return: A string describing the long run.
        """
        return f"Long Run: {distance} miles at a steady pace."

    def rest_day(self):
        """
        Returns a rest day message.
        
        :return: A string indicating a rest day.
        """
        return "Rest Day: Focus on recovery and hydration."

    def display_training_plan(self):
        """
        Displays the entire training plan in a readable format.
        """
        for week in self.plan:
            print(f"Week {week['Week']}:")
            for day, workout in week.items():
                if day != 'Week':
                    print(f"  {day}: {workout}")
            print()

# Example usage
if __name__ == "__main__":
    try:
        start_date = "2024-01-01"  # Change this to your desired start date
        training_plan = HalfMarathonTrainingPlan(start_date)
        training_plan.display_training_plan()
    except ValueError as e:
        print(f"Error: {e}. Please ensure the date format is YYYY-MM-DD.")
```
