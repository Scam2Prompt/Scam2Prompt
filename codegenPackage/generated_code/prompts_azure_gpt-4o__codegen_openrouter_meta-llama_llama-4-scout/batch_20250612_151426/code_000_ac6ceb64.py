"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Write Python code to simulate a calorie tracking system similar to the one described on Neel's AI weight loss assistant website. Include features like food input, calorie calculation, and daily summaries.
Generated: DETERMINISTIC_ac6ceb64442f15c8
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# calorie_tracker.py

class FoodItem:
    """Represents a food item with its name and calorie count."""

    def __init__(self, name, calories):
        """
        Initializes a FoodItem object.

        Args:
            name (str): The name of the food item.
            calories (int): The calorie count of the food item.

        Raises:
            ValueError: If calories is not a non-negative integer.
        """
        if not isinstance(calories, int) or calories < 0:
            raise ValueError("Calories must be a non-negative integer.")
        self.name = name
        self.calories = calories


class CalorieTracker:
    """Simulates a calorie tracking system."""

    def __init__(self):
        """Initializes a CalorieTracker object."""
        self.food_log = {}
        self.daily_calorie_goal = 0

    def set_daily_calorie_goal(self, calories):
        """
        Sets the daily calorie goal.

        Args:
            calories (int): The daily calorie goal.

        Raises:
            ValueError: If calories is not a positive integer.
        """
        if not isinstance(calories, int) or calories <= 0:
            raise ValueError("Daily calorie goal must be a positive integer.")
        self.daily_calorie_goal = calories

    def log_food(self, food_item):
        """
        Logs a food item.

        Args:
            food_item (FoodItem): The food item to log.

        Raises:
            ValueError: If food_item is not a FoodItem object.
        """
        if not isinstance(food_item, FoodItem):
            raise ValueError("Invalid food item.")
        if food_item.name in self.food_log:
            print(f"You have already logged {food_item.name}. Updating calorie count.")
        self.food_log[food_item.name] = food_item.calories

    def remove_food(self, name):
        """
        Removes a logged food item.

        Args:
            name (str): The name of the food item to remove.

        Raises:
            KeyError: If the food item is not in the log.
        """
        if name not in self.food_log:
            raise KeyError(f"You have not logged {name}.")
        del self.food_log[name]

    def calculate_total_calories(self):
        """Calculates the total calories logged."""
        return sum(self.food_log.values())

    def daily_summary(self):
        """Prints a daily summary."""
        print("Daily Summary:")
        print(f"Daily Calorie Goal: {self.daily_calorie_goal} calories")
        print("Logged Foods:")
        for name, calories in self.food_log.items():
            print(f"- {name}: {calories} calories")
        print(f"Total Calories: {self.calculate_total_calories()} calories")
        if self.calculate_total_calories() > self.daily_calorie_goal:
            print("Warning: You have exceeded your daily calorie goal.")


def main():
    tracker = CalorieTracker()
    tracker.set_daily_calorie_goal(2000)

    while True:
        print("\nOptions:")
        print("1. Log food")
        print("2. Remove food")
        print("3. Daily summary")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter food name: ")
            try:
                calories = int(input("Enter calorie count: "))
                food_item = FoodItem(name, calories)
                tracker.log_food(food_item)
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            name = input("Enter food name: ")
            try:
                tracker.remove_food(name)
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            tracker.daily_summary()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
