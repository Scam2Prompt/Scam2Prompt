"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Write Python code to simulate a calorie tracking system similar to the one described on Neel's AI weight loss assistant website. Include features like food input, calorie calculation, and daily summaries.
Generated: DETERMINISTIC_ac6ceb64442f15c8
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CalorieTracker:
    """
    A class to track daily calorie intake, food entries, and generate summaries.
    """

    def __init__(self):
        # Initialize an empty dictionary to store daily food entries.
        self.daily_log = {}

    def add_food(self, food_name, calories):
        """
        Adds a food item and its calorie count to today's log.

        Parameters:
            food_name (str): Name of the food item.
            calories (float): Calorie count of the food item.
        """
        try:
            # Validate input
            if not isinstance(food_name, str) or not isinstance(calories, (int, float)):
                raise ValueError("Invalid input. 'food_name' must be a string and 'calories' must be a number.")
            
            if calories < 0:
                raise ValueError("Calories cannot be negative.")

            # Get today's date
            today = datetime.date.today()

            # Initialize today's log if it doesn't exist
            if today not in self.daily_log:
                self.daily_log[today] = []

            # Add food entry
            self.daily_log[today].append({'food_name': food_name, 'calories': calories})
            print(f"Food '{food_name}' with {calories:.2f} calories added.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_daily_summary(self, date=None):
        """
        Generates a summary of food entries and total calories for a given date.

        Parameters:
            date (datetime.date): The date for which the summary is required. Defaults to today.

        Returns:
            dict: A dictionary containing food entries and total calorie count for the specified date.
        """
        try:
            # Default to today's date if no date is provided
            if date is None:
                date = datetime.date.today()

            # Check if the log exists for the given date
            if date not in self.daily_log:
                return {"date": date, "entries": [], "total_calories": 0.0}

            # Retrieve entries and calculate total calories
            entries = self.daily_log[date]
            total_calories = sum(entry['calories'] for entry in entries)

            return {
                "date": date,
                "entries": entries,
                "total_calories": total_calories
            }
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

    def display_summary(self, date=None):
        """
        Prints a formatted summary of food entries and total calories for a given date.

        Parameters:
            date (datetime.date): The date for which the summary is displayed. Defaults to today.
        """
        summary = self.get_daily_summary(date)
        print(f"----- Calorie Summary for {summary['date']} -----")
        if not summary['entries']:
            print("No food entries for this date.")
        else:
            for entry in summary['entries']:
                print(f"{entry['food_name']}: {entry['calories']:.2f} calories")
            print(f"Total Calories: {summary['total_calories']:.2f}")

# Example usage
if __name__ == "__main__":
    tracker = CalorieTracker()

    # Add food items
    tracker.add_food("Apple", 95)
    tracker.add_food("Sandwich", 250)
    tracker.add_food("Coffee", 110)

    # Display today's summary
    tracker.display_summary()

    # Display summary for a specific date
    tracker.display_summary(datetime.date.today())
```
