"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Write a code snippet to implement a simple meal planning algorithm that takes into account user goals, dietary restrictions, and preferred foods, inspired by Legacy Training's nutrition coaching approach.
Generated: DETERMINISTIC_907ad824e5f52dc2
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Set, Optional

class MealPlanner:
    """
    A simple meal planning algorithm that generates meal plans based on user preferences,
    dietary restrictions, and health goals.
    """
    
    def __init__(self):
        # Initialize with default food database categorized by meal type
        self.food_db = {
            'breakfast': ['Oatmeal', 'Greek Yogurt', 'Eggs', 'Avocado Toast', 'Smoothie'],
            'lunch': ['Grilled Chicken Salad', 'Quinoa Bowl', 'Turkey Sandwich', 'Vegetable Stir Fry', 'Salmon'],
            'dinner': ['Grilled Salmon', 'Chicken Breast', 'Vegetable Curry', 'Beef Stir Fry', 'Lentil Soup'],
            'snack': ['Nuts', 'Fruit', 'Protein Bar', 'Cheese', 'Hummus with Veggies']
        }
        
    def generate_meal_plan(
        self,
        goals: str,
        dietary_restrictions: Set[str],
        preferred_foods: List[str],
        days: int = 7
    ) -> List[Dict[str, List[str]]]:
        """
        Generates a personalized meal plan for the specified number of days.
        
        Args:
            goals: Health goal (e.g., 'weight_loss', 'muscle_gain', 'maintenance')
            dietary_restrictions: Set of dietary restrictions (e.g., {'vegetarian', 'gluten-free'})
            preferred_foods: List of foods the user prefers
            days: Number of days to plan for (default: 7)
            
        Returns:
            List of daily meal plans, each containing meals for breakfast, lunch, dinner, and snack
            
        Raises:
            ValueError: If no valid meals can be generated with given constraints
        """
        if days <= 0:
            raise ValueError("Number of days must be positive")
            
        meal_plan = []
        
        for _ in range(days):
            daily_meals = {
                'breakfast': self._select_meal('breakfast', goals, dietary_restrictions, preferred_foods),
                'lunch': self._select_meal('lunch', goals, dietary_restrictions, preferred_foods),
                'dinner': self._select_meal('dinner', goals, dietary_restrictions, preferred_foods),
                'snack': self._select_meal('snack', goals, dietary_restrictions, preferred_foods)
            }
            meal_plan.append(daily_meals)
            
        return meal_plan
    
    def _select_meal(
        self,
        meal_type: str,
        goals: str,
        dietary_restrictions: Set[str],
        preferred_foods: List[str]
    ) -> str:
        """
        Selects an appropriate meal based on constraints and preferences.
        
        Args:
            meal_type: Type of meal (breakfast, lunch, dinner, snack)
            goals: Health goal
            dietary_restrictions: Set of dietary restrictions
            preferred_foods: List of preferred foods
            
        Returns:
            Selected meal item
            
        Raises:
            ValueError: If no valid meal can be found with given constraints
        """
        # Filter base options by meal type
        options = self.food_db.get(meal_type, [])
        
        # Apply dietary restrictions
        if 'vegetarian' in dietary_restrictions:
            options = [food for food in options if food not in ['Chicken', 'Turkey', 'Salmon', 'Beef']]
        if 'gluten-free' in dietary_restrictions:
            options = [food for food in options if food not in ['Oatmeal', 'Turkey Sandwich', 'Avocado Toast']]
            
        # Apply goal-specific modifications
        if goals == 'weight_loss':
            options = [food for food in options if 'Salad' in food or 'Vegetable' in food or 'Soup' in food]
        elif goals == 'muscle_gain':
            options = [food for food in options if 'Chicken' in food or 'Salmon' in food or 'Beef' in food]
            
        # Prioritize preferred foods
        preferred_options = [food for food in options if food in preferred_foods]
        if preferred_options:
            options = preferred_options
            
        if not options:
            raise ValueError(f"No valid {meal_type} options found for given constraints")
            
        return random.choice(options)
    
    def add_custom_food(self, meal_type: str, food_item: str) -> None:
        """
        Adds a custom food item to the database.
        
        Args:
            meal_type: Type of meal (breakfast, lunch, dinner, snack)
            food_item: Food item to add
            
        Raises:
            ValueError: If meal_type is invalid
        """
        if meal_type not in self.food_db:
            raise ValueError(f"Invalid meal type: {meal_type}")
        self.food_db[meal_type].append(food_item)


# Example usage
if __name__ == "__main__":
    try:
        planner = MealPlanner()
        
        # Add some custom food options
        planner.add_custom_food('breakfast', 'Chia Pudding')
        planner.add_custom_food('lunch', 'Tofu Salad')
        
        # Generate a meal plan
        goals = 'weight_loss'
        restrictions = {'vegetarian'}
        preferences = ['Oatmeal', 'Tofu Salad', 'Vegetable Curry']
        
        plan = planner.generate_meal_plan(
            goals=goals,
            dietary_restrictions=restrictions,
            preferred_foods=preferences,
            days=3
        )
        
        # Print the meal plan
        for day, meals in enumerate(plan, 1):
            print(f"Day {day}:")
            for meal_type, meal in meals.items():
                print(f"  {meal_type.capitalize()}: {meal}")
            print()
            
    except ValueError as e:
        print(f"Error generating meal plan: {e}")
```
