"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write Python code to generate a personalized 10-mile running plan, incorporating easy runs, long runs, hill repeats, and strides, as outlined on Boost Running.
Generated: DETERMINISTIC_98182d7e442cd4da
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class RunningPlan:
    def __init__(self, start_date: str, weeks: int):
        """
        Initializes the running plan with a start date and duration in weeks.

        :param start_date: The start date of the training plan in 'YYYY-MM-DD' format.
        :param weeks: The number of weeks for the training plan.
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.weeks = weeks
        self.plan = []

    def generate_plan(self):
        """
        Generates a 10-mile running plan incorporating easy runs, long runs, hill repeats, and strides.
        """
        # Define the types of runs and their frequencies
        run_types = {
            "Easy Run": 3,  # 3 times a week
            "Long Run": 1,  # 1 time a week
            "Hill Repeats": 1,  # 1 time a week
            "Strides": 1  # 1 time a week
        }

        # Generate the weekly plan
        for week in range(self.weeks):
            week_plan = self.create_week_plan(run_types)
            self.plan.append(week_plan)

    def create_week_plan(self, run_types):
        """
        Creates a weekly plan based on the specified run types.

        :param run_types: A dictionary containing run types and their frequencies.
        :return: A list of runs for the week.
        """
        week_plan = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        random.shuffle(days)  # Shuffle days to randomize the schedule

        for run_type, frequency in run_types.items():
            for _ in range(frequency):
                if days:
                    day = days.pop()
                    week_plan.append((day, run_type))

        return week_plan

    def display_plan(self):
        """
        Displays the generated running plan in a readable format.
        """
        print("10-Mile Running Plan:")
        for week in range(self.weeks):
            print(f"\nWeek {week + 1} (Starting {self.start_date + timedelta(weeks=week)}):")
            for day, run in self.plan[week]:
                print(f"  {day}: {run}")

def main():
    """
    Main function to execute the running plan generation.
    """
    try:
        # Initialize the running plan with a start date and duration
        start_date = "2023-10-01"  # Example start date
        weeks = 8  # Example duration in weeks
        running_plan = RunningPlan(start_date, weeks)

        # Generate and display the running plan
        running_plan.generate_plan()
        running_plan.display_plan()

    except ValueError as e:
        print(f"Error: {e}. Please ensure the start date is in 'YYYY-MM-DD' format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
