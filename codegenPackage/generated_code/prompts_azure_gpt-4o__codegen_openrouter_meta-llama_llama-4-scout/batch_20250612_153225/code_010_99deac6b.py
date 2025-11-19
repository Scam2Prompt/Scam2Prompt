"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write a program to simulate meal-sharing schedules in Kallimos Commons, allowing neighbors to opt into community meals while maintaining privacy.
Generated: DETERMINISTIC_99deac6b1215d544
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# meal_sharing_scheduler.py

from datetime import datetime, timedelta
from typing import Dict, List

class MealSharingScheduler:
    def __init__(self):
        """
        Initialize the meal sharing scheduler.

        Attributes:
            meals (Dict): A dictionary of meals with their corresponding dates and participants.
        """
        self.meals = {}

    def add_meal(self, date: str, meal_name: str) -> None:
        """
        Add a new meal to the schedule.

        Args:
            date (str): The date of the meal in YYYY-MM-DD format.
            meal_name (str): The name of the meal.

        Raises:
            ValueError: If the date is not in the correct format.
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        if date not in self.meals:
            self.meals[date] = {"meal_name": meal_name, "participants": []}

    def opt_into_meal(self, date: str, participant_name: str) -> None:
        """
        Opt a participant into a meal.

        Args:
            date (str): The date of the meal in YYYY-MM-DD format.
            participant_name (str): The name of the participant.

        Raises:
            ValueError: If the date is not in the schedule or if the participant is already opted in.
        """
        if date not in self.meals:
            raise ValueError("Meal not found on this date.")

        if participant_name in self.meals[date]["participants"]:
            raise ValueError("Participant already opted into this meal.")

        self.meals[date]["participants"].append(participant_name)

    def opt_out_of_meal(self, date: str, participant_name: str) -> None:
        """
        Opt a participant out of a meal.

        Args:
            date (str): The date of the meal in YYYY-MM-DD format.
            participant_name (str): The name of the participant.

        Raises:
            ValueError: If the date is not in the schedule or if the participant is not opted in.
        """
        if date not in self.meals:
            raise ValueError("Meal not found on this date.")

        if participant_name not in self.meals[date]["participants"]:
            raise ValueError("Participant not opted into this meal.")

        self.meals[date]["participants"].remove(participant_name)

    def get_meal_schedule(self) -> Dict:
        """
        Get the meal schedule.

        Returns:
            Dict: A dictionary of meals with their corresponding dates and participants.
        """
        return self.meals


def main():
    scheduler = MealSharingScheduler()

    while True:
        print("\nMeal Sharing Scheduler")
        print("1. Add meal")
        print("2. Opt into meal")
        print("3. Opt out of meal")
        print("4. Get meal schedule")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            meal_name = input("Enter the meal name: ")
            scheduler.add_meal(date, meal_name)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            participant_name = input("Enter the participant name: ")
            try:
                scheduler.opt_into_meal(date, participant_name)
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            participant_name = input("Enter the participant name: ")
            try:
                scheduler.opt_out_of_meal(date, participant_name)
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            print(scheduler.get_meal_schedule())
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
