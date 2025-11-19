"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Develop a 100-mile running training plan with a gradual mileage increase, peak weeks reaching 70-100 miles, and a sample weekly schedule, and provide advice on building endurance and mental tenacity.
Generated: DETERMINISTIC_30fa839a6c1b8660
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class RunningTrainingPlan:
    def __init__(self, goal_mileage, weeks):
        """
        Initialize a running training plan.

        Args:
            goal_mileage (int): The peak mileage goal.
            weeks (int): The number of weeks for the training plan.
        """
        self.goal_mileage = goal_mileage
        self.weeks = weeks
        self.plan = []

    def generate_plan(self):
        """
        Generate a gradual mileage increase plan.

        The plan starts with 30 miles in week 1 and increases by 10% each week.
        """
        current_mileage = 30
        for week in range(1, self.weeks + 1):
            # Calculate mileage increase
            increase = int(current_mileage * 0.1)
            if week > 8:
                # Peak weeks: 70-100 miles
                current_mileage = self.goal_mileage
            else:
                current_mileage += increase

            # Create a sample weekly schedule
            schedule = self.create_weekly_schedule(current_mileage)
            self.plan.append({
                'week': week,
                'mileage': current_mileage,
                'schedule': schedule
            })

    def create_weekly_schedule(self, mileage):
        """
        Create a sample weekly schedule.

        The schedule consists of 1-2 rest days, 1-2 shorter runs, and 1 longer run.

        Args:
            mileage (int): The weekly mileage.

        Returns:
            list: A list of daily runs.
        """
        schedule = []
        rest_days = 1
        shorter_runs = 2
        longer_run = 1

        # Calculate daily run distances
        daily_mileage = mileage // (rest_days + shorter_runs + longer_run)
        remaining_mileage = mileage % (rest_days + shorter_runs + longer_run)

        # Add rest days
        for _ in range(rest_days):
            schedule.append({'day': 'Rest', 'mileage': 0})

        # Add shorter runs
        for _ in range(shorter_runs):
            schedule.append({'day': 'Short Run', 'mileage': daily_mileage})

        # Add longer run
        schedule.append({'day': 'Long Run', 'mileage': daily_mileage + remaining_mileage})

        return schedule

    def print_plan(self):
        """
        Print the training plan.
        """
        for week in self.plan:
            print(f"Week {week['week']}: {week['mileage']} miles")
            for day in week['schedule']:
                print(f"  {day['day']}: {day['mileage']} miles")
            print()

def main():
    try:
        # Create a 100-mile running training plan with 16 weeks
        plan = RunningTrainingPlan(100, 16)
        plan.generate_plan()
        plan.print_plan()

        # Advice on building endurance and mental tenacity
        print("Advice on Building Endurance and Mental Tenacity:")
        print("* Gradually increase your mileage to allow your body to adapt.")
        print("* Incorporate strength training to improve overall running efficiency.")
        print("* Practice mental techniques such as visualization, positive self-talk, and breathing exercises.")
        print("* Get enough rest and recovery time to avoid injury and burnout.")
        print("* Join a running community or find a running buddy for motivation and support.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
