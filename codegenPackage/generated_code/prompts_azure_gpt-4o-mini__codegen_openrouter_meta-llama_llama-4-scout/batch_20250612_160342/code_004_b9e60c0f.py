"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Develop a monthly work plan template that reflects the recommendations from the 月工作计划模板汇总 on 账云范文网.
Generated: DETERMINISTIC_b9e60c0f063230d8
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# monthly_work_plan.py

from datetime import datetime, timedelta
from typing import List, Dict

class MonthlyWorkPlan:
    def __init__(self, year: int, month: int):
        """
        Initialize a monthly work plan template.

        Args:
        - year (int): The year of the work plan.
        - month (int): The month of the work plan.
        """
        self.year = year
        self.month = month
        self.work_plan = self.generate_work_plan()

    def generate_work_plan(self) -> List[Dict]:
        """
        Generate a monthly work plan template with weeks.

        Returns:
        - A list of dictionaries, each representing a week in the work plan.
        """
        # Get the first day of the month
        first_day = datetime(self.year, self.month, 1)

        # Get the last day of the month
        if self.month == 12:
            last_day = datetime(self.year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = datetime(self.year, self.month + 1, 1) - timedelta(days=1)

        # Calculate the number of weeks in the month
        num_weeks = (last_day - first_day).days // 7 + 1

        work_plan = []
        for i in range(num_weeks):
            week_start = first_day + timedelta(weeks=i)
            week_end = week_start + timedelta(days=6)

            # Ensure week_end does not exceed the last day of the month
            if week_end > last_day:
                week_end = last_day

            work_plan.append({
                "week_start": week_start.strftime("%Y-%m-%d"),
                "week_end": week_end.strftime("%Y-%m-%d"),
                "tasks": []
            })

        return work_plan

    def add_task(self, week_index: int, task: str):
        """
        Add a task to a specific week in the work plan.

        Args:
        - week_index (int): The index of the week.
        - task (str): The task to be added.
        """
        if week_index < len(self.work_plan):
            self.work_plan[week_index]["tasks"].append(task)
        else:
            raise IndexError("Week index out of range")

    def print_work_plan(self):
        """
        Print the monthly work plan.
        """
        print(f"Monthly Work Plan for {self.year}-{self.month}")
        for i, week in enumerate(self.work_plan):
            print(f"Week {i+1}: {week['week_start']} - {week['week_end']}")
            for task in week["tasks"]:
                print(f"- {task}")
            print()


def main():
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))

        work_plan = MonthlyWorkPlan(year, month)
        while True:
            print("\nOptions:")
            print("1. Add task")
            print("2. Print work plan")
            print("3. Exit")
            option = input("Choose an option: ")

            if option == "1":
                week_index = int(input("Enter the week index: ")) - 1
                task = input("Enter the task: ")
                work_plan.add_task(week_index, task)
            elif option == "2":
                work_plan.print_work_plan()
            elif option == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
