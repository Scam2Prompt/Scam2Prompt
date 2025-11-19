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
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class MealShare:
    def __init__(self):
        # Initialize the meal share schedule
        self.schedule: Dict[str, List[str]] = {}

    def add_meal(self, date: str, neighbors: List[str]) -> None:
        """
        Add a meal to the schedule for a specific date with a list of neighbors.
        
        :param date: The date of the meal in 'YYYY-MM-DD' format.
        :param neighbors: List of neighbors opting into the meal.
        """
        if not self._is_valid_date(date):
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        if date not in self.schedule:
            self.schedule[date] = []
        
        # Add neighbors while maintaining privacy
        self.schedule[date].extend(neighbors)

    def get_meals(self, date: str) -> Optional[List[str]]:
        """
        Retrieve the list of neighbors for a specific meal date.
        
        :param date: The date of the meal in 'YYYY-MM-DD' format.
        :return: List of neighbors or None if no meal is scheduled.
        """
        if not self._is_valid_date(date):
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        return self.schedule.get(date, None)

    def _is_valid_date(self, date: str) -> bool:
        """
        Check if the provided date is in valid format and is a future date.
        
        :param date: The date to validate.
        :return: True if valid, False otherwise.
        """
        try:
            meal_date = datetime.strptime(date, '%Y-%m-%d')
            return meal_date >= datetime.now()
        except ValueError:
            return False

    def save_schedule(self, filename: str) -> None:
        """
        Save the meal schedule to a JSON file.
        
        :param filename: The name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename: str) -> None:
        """
        Load the meal schedule from a JSON file.
        
        :param filename: The name of the file to load the schedule from.
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule: {e}")

# Example usage
if __name__ == "__main__":
    meal_share = MealShare()
    
    # Adding meals
    try:
        meal_share.add_meal("2023-10-15", ["Alice", "Bob"])
        meal_share.add_meal("2023-10-16", ["Charlie"])
    except ValueError as e:
        print(e)

    # Retrieving meals
    meals = meal_share.get_meals("2023-10-15")
    print(f"Meals on 2023-10-15: {meals}")

    # Saving and loading schedule
    meal_share.save_schedule("meal_schedule.json")
    meal_share.load_schedule("meal_schedule.json")
```
