"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Write a Python code snippet to implement a simple calorie counter with a daily checkup feature, similar to Neel's food tracking functionality.
Generated: DETERMINISTIC_4c405087cc523aab
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# calorie_counter.py

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


class CalorieCounter:
    """Tracks daily food intake and provides a daily checkup feature."""

    def __init__(self):
        """Initializes a CalorieCounter object."""
        self.food_log = []
        self.daily_calorie_goal = 2000  # Default daily calorie goal

    def add_food(self, food_item):
        """
        Adds a food item to the food log.

        Args:
            food_item (FoodItem): The food item to add.

        Raises:
            TypeError: If food_item is not a FoodItem object.
        """
        if not isinstance(food_item, FoodItem):
            raise TypeError("Invalid food item.")
        self.food_log.append(food_item)

    def remove_food(self, index):
        """
        Removes a food item from the food log by its index.

        Args:
            index (int): The index of the food item to remove.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            del self.food_log[index]
        except IndexError:
            raise IndexError("Invalid index.")

    def calculate_total_calories(self):
        """
        Calculates the total calories consumed.

        Returns:
            int: The total calories consumed.
        """
        return sum(food_item.calories for food_item in self.food_log)

    def daily_checkup(self):
        """
        Performs a daily checkup and provides feedback.

        Returns:
            str: A message indicating whether the daily calorie goal is met.
        """
        total_calories = self.calculate_total_calories()
        if total_calories <= self.daily_calorie_goal:
            return f"Daily calorie goal met! You consumed {total_calories} calories."
        else:
            return f"You exceeded your daily calorie goal. You consumed {total_calories} calories."


def main():
    calorie_counter = CalorieCounter()

    while True:
        print("\n1. Add food item")
        print("2. Remove food item")
        print("3. Daily checkup")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter food item name: ")
            calories = int(input("Enter calorie count: "))
            food_item = FoodItem(name, calories)
            calorie_counter.add_food(food_item)
            print(f"Added {name} with {calories} calories.")
        elif choice == "2":
            if not calorie_counter.food_log:
                print("No food items to remove.")
                continue
            print("Food log:")
            for index, food_item in enumerate(calorie_counter.food_log):
                print(f"{index + 1}. {food_item.name} - {food_item.calories} calories")
            index = int(input("Enter the index of the food item to remove: ")) - 1
            try:
                calorie_counter.remove_food(index)
                print("Food item removed.")
            except IndexError as e:
                print(str(e))
        elif choice == "3":
            print(calorie_counter.daily_checkup())
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
