"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Recommend a 1-month marathon training plan with a structured schedule, gradual mileage increases, and rest days, and provide guidance on balancing training and recovery.
Generated: DETERMINISTIC_3e70d7f120fb1df3
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class MarathonTrainingPlan:
    def __init__(self, start_date, goal_date):
        """
        Initialize a marathon training plan.

        Args:
            start_date (str): The start date of the training plan in YYYY-MM-DD format.
            goal_date (str): The goal date of the marathon in YYYY-MM-DD format.

        Raises:
            ValueError: If the start date or goal date is not in the correct format.
        """
        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.goal_date = datetime.strptime(goal_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        if self.start_date >= self.goal_date:
            raise ValueError("Start date must be before goal date.")

    def generate_training_plan(self):
        """
        Generate a 1-month marathon training plan.

        Returns:
            list: A list of dictionaries representing the daily training plan.
        """
        training_plan = []
        current_date = self.start_date
        weekly_mileage = 10
        max_weekly_mileage = 20

        while current_date < self.goal_date:
            day_plan = {
                "date": current_date.strftime("%Y-%m-%d"),
                "activity": "",
                "mileage": 0,
                "rest": False
            }

            if current_date.weekday() in [0, 2, 4]:
                # Easy run
                day_plan["activity"] = "Easy Run"
                day_plan["mileage"] = weekly_mileage // 3
            elif current_date.weekday() == 1:
                # Interval training
                day_plan["activity"] = "Interval Training"
                day_plan["mileage"] = weekly_mileage // 2
            elif current_date.weekday() == 3:
                # Long run
                day_plan["activity"] = "Long Run"
                day_plan["mileage"] = weekly_mileage
            elif current_date.weekday() == 5:
                # Rest day
                day_plan["rest"] = True
                day_plan["activity"] = "Rest"
            elif current_date.weekday() == 6:
                # Cross-training
                day_plan["activity"] = "Cross-Training"
                day_plan["mileage"] = 0

            training_plan.append(day_plan)

            # Gradually increase weekly mileage
            if weekly_mileage < max_weekly_mileage:
                weekly_mileage += 2

            current_date += timedelta(days=1)

        return training_plan


def print_training_plan(training_plan):
    """
    Print the daily training plan.

    Args:
        training_plan (list): A list of dictionaries representing the daily training plan.
    """
    for day_plan in training_plan:
        if day_plan["rest"]:
            print(f"{day_plan['date']}: Rest")
        else:
            print(f"{day_plan['date']}: {day_plan['activity']} - {day_plan['mileage']} miles")


def main():
    try:
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        goal_date = input("Enter the goal date (YYYY-MM-DD): ")

        training_plan = MarathonTrainingPlan(start_date, goal_date)
        daily_plan = training_plan.generate_training_plan()

        print_training_plan(daily_plan)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
