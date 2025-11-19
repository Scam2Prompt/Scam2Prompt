"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Generate a 16-week training plan for a half marathon, incorporating long runs, interval runs, and strength training as detailed on Boost Running.
Generated: DETERMINISTIC_7e46089b665f8894
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TrainingPlan:
    def __init__(self, start_date, duration_weeks=16):
        """
        Initializes the training plan with a start date and duration.
        
        :param start_date: The start date of the training plan (datetime object).
        :param duration_weeks: The number of weeks for the training plan (default is 16).
        """
        self.start_date = start_date
        self.duration_weeks = duration_weeks
        self.schedule = self.generate_training_schedule()

    def generate_training_schedule(self):
        """
        Generates the training schedule for the half marathon.
        
        :return: A list of training sessions with dates and descriptions.
        """
        training_schedule = []
        for week in range(self.duration_weeks):
            week_start = self.start_date + timedelta(weeks=week)
            training_schedule.append({
                "week": week + 1,
                "sessions": self.create_weekly_sessions(week_start)
            })
        return training_schedule

    def create_weekly_sessions(self, week_start):
        """
        Creates the training sessions for a given week.
        
        :param week_start: The starting date of the week (datetime object).
        :return: A list of training sessions for the week.
        """
        sessions = []
        # Week structure: Long run, Interval run, Strength training, Easy run
        sessions.append({"date": week_start + timedelta(days=6), "type": "Long Run", "distance_miles": 10 + (week // 2)})
        sessions.append({"date": week_start + timedelta(days=3), "type": "Interval Run", "description": "5x800m intervals with rest"})
        sessions.append({"date": week_start + timedelta(days=1), "type": "Strength Training", "description": "Full body strength workout"})
        sessions.append({"date": week_start + timedelta(days=5), "type": "Easy Run", "distance_miles": 3 + (week // 4)})
        return sessions

    def display_schedule(self):
        """
        Displays the training schedule in a readable format.
        """
        for week in self.schedule:
            print(f"Week {week['week']}:")
            for session in week['sessions']:
                date_str = session["date"].strftime("%Y-%m-%d")
                if "distance_miles" in session:
                    print(f"  {date_str}: {session['type']} - {session['distance_miles']} miles")
                else:
                    print(f"  {date_str}: {session['type']} - {session['description']}")
            print('\n')

def main():
    # Define the start date for the training plan
    try:
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        training_plan = TrainingPlan(start_date)
        training_plan.display_schedule()
    except ValueError as e:
        print(f"Error parsing the date: {e}")

if __name__ == "__main__":
    main()
```
