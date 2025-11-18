"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Write Python code to generate a personalized 10-mile running plan, incorporating easy runs, long runs, hill repeats, and strides, as outlined on Boost Running.
Generated: DETERMINISTIC_98182d7e442cd4da
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import timedelta, datetime

class RunningPlan:
    def __init__(self, start_date: str, duration_weeks: int):
        """
        Initializes the RunningPlan with a start date and duration in weeks.
        
        :param start_date: The date when the training plan starts (format: 'YYYY-MM-DD').
        :param duration_weeks: The number of weeks the training plan will run.
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.duration_weeks = duration_weeks
        self.plan = self.generate_plan()

    def generate_plan(self):
        """
        Generates a personalized running plan for 10 miles.
        
        :return: A dictionary containing the training schedule.
        """
        plan = {}
        easy_run_days = [2, 4, 6]  # Tuesday, Thursday, Saturday
        long_run_day = 7  # Sunday
        hill_repeat_days = [1]  # Monday
        stride_days = [5]  # Friday
        
        for week in range(self.duration_weeks):
            week_start = self.start_date + timedelta(weeks=week)
            plan[week_start.strftime('%Y-%m-%d')] = self.create_week_schedule(week_start, easy_run_days, long_run_day, hill_repeat_days, stride_days)
        
        return plan

    def create_week_schedule(self, week_start: datetime, easy_run_days, long_run_day, hill_repeat_days, stride_days):
        """
        Creates a schedule for a week, assigning running workouts to each day.
        
        :param week_start: The start date of the week.
        :param easy_run_days: Days assigned for easy runs.
        :param long_run_day: Day assigned for the long run.
        :param hill_repeat_days: Days assigned for hill repeats.
        :param stride_days: Days assigned for strides.
        :return: A dictionary containing the day's workout.
        """
        week_schedule = {}
        
        for day in range(7):
            current_date = week_start + timedelta(days=day)
            if day in easy_run_days:
                week_schedule[current_date.strftime('%A')] = self.easy_run()
            elif day in hill_repeat_days:
                week_schedule[current_date.strftime('%A')] = self.hill_repeats()
            elif day == long_run_day:
                week_schedule[current_date.strftime('%A')] = self.long_run()
            elif day in stride_days:
                week_schedule[current_date.strftime('%A')] = self.strides()
            else:
                week_schedule[current_date.strftime('%A')] = "Rest Day"

        return week_schedule

    def easy_run(self) -> str:
        """
        Returns an easy run workout description.
        
        :return: A string representing the easy run.
        """
        distance = random.choice([3, 4, 5])  # Easy runs can be 3, 4, or 5 miles
        return f"Easy run: {distance} miles at a comfortable pace."

    def long_run(self) -> str:
        """
        Returns a long run workout description.
        
        :return: A string representing the long run.
        """
        distance = 8  # Long run for the plan
        return f"Long run: {distance} miles at an easy pace."

    def hill_repeats(self) -> str:
        """
        Returns a hill repeats workout description.
        
        :return: A string representing the hill repeats.
        """
        repeats = random.randint(4, 8)  # Randomly choose number of repeats
        return f"Hill repeats: {repeats} repeats on a hill with recovery jog back."

    def strides(self) -> str:
        """
        Returns a strides workout description.
        
        :return: A string representing the strides.
        """
        strides_count = random.randint(4, 6)  # Randomly choose number of strides
        return f"Strides: {strides_count} 20-second strides with full recovery."

    def display_plan(self):
        """
        Displays the full running plan.
        """
        for date, workouts in self.plan.items():
            print(f"{date}:")
            for day, workout in workouts.items():
                print(f"  {day}: {workout}")

if __name__ == '__main__':
    # Example usage
    try:
        start_date = '2023-10-01'  # User-defined start date
        duration_weeks = 10  # User-defined duration in weeks
        running_plan = RunningPlan(start_date, duration_weeks)
        running_plan.display_plan()
    except ValueError as e:
        print(f"Error: {e}. Please ensure the start date is in 'YYYY-MM-DD' format.")
```
