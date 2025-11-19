"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: Generate a sample menu for a school meal program that aligns with the healthy eating principles promoted by It's Cool Foods.
Generated: DETERMINISTIC_f7a6afdb822a5099
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Meal:
    """Represents a meal item in the school meal program."""
    
    def __init__(self, name: str, category: str, calories: int, is_healthy: bool):
        """
        Initialize a Meal instance.

        Args:
            name (str): Name of the meal item.
            category (str): Category of the meal (e.g., "Main", "Side", "Dessert").
            calories (int): Caloric content of the meal item.
            is_healthy (bool): Indicator of whether the meal is considered healthy.
        """
        self.name = name
        self.category = category
        self.calories = calories
        self.is_healthy = is_healthy

    def to_dict(self) -> Dict:
        """Convert the Meal instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "calories": self.calories,
            "is_healthy": self.is_healthy
        }

class Menu:
    """Represents a menu for a school meal program."""
    
    def __init__(self, week_days: List[str]):
        """
        Initialize a Menu instance.

        Args:
            week_days (List[str]): List of days in the week for which the menu is planned.
        """
        self.week_days = week_days
        self.meals: Dict[str, List[Meal]] = {day: [] for day in week_days}

    def add_meal(self, day: str, meal: Meal):
        """
        Add a meal item to the specified day in the menu.

        Args:
            day (str): The day of the week to which the meal will be added.
            meal (Meal): The meal item to add to the menu.

        Raises:
            ValueError: If the day is invalid or does not exist in the menu.
        """
        if day not in self.week_days:
            raise ValueError(f"Invalid day: {day}. Please choose from {self.week_days}.")
        
        self.meals[day].append(meal)

    def generate_menu_json(self) -> str:
        """Generate the menu in JSON format."""
        return json.dumps({day: [meal.to_dict() for meal in meals] for day, meals in self.meals.items()}, indent=4)

# Sample implementation
if __name__ == "__main__":
    # Define a sample menu for a school week
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    school_menu = Menu(week_days)

    # Sample meals
    meals = [
        Meal("Grilled Chicken Salad", "Main", 300, True),
        Meal("Vegetable Stir Fry", "Main", 250, True),
        Meal("Fruit Cup", "Dessert", 100, True),
        Meal("Whole Grain Sandwich", "Main", 400, True),
        Meal("Baked Sweet Potatoes", "Side", 150, True),
        Meal("Low Fat Yogurt", "Dessert", 120, True),
        Meal("Pasta Primavera", "Main", 350, True),
        Meal("Carrot Sticks", "Side", 50, True),
        Meal("Brown Rice", "Side", 215, True),
        Meal("Apple Slices", "Dessert", 80, True)
    ]

    # Assign meals to the menu
    try:
        for day in week_days:
            for meal in meals:
                school_menu.add_meal(day, meal)
        
        # Output the menu in JSON format
        print(school_menu.generate_menu_json())
    
    except ValueError as e:
        print(f"Error: {e}")
```
