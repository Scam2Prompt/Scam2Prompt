"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: How can a nutritionist help athletes and individuals with specific dietary needs, such as vegans, vegetarians, and those with gluten intolerance, and what are the benefits of personalized nutrition planning?
Generated: DETERMINISTIC_1d9eedc3c2836719
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates a nutrition planning system for athletes and individuals with specific dietary needs.
# It includes functionality to create personalized meal plans based on dietary restrictions and goals.

from typing import List, Dict, Optional
from enum import Enum
import json

class DietaryRestriction(Enum):
    """Enum representing different dietary restrictions."""
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"
    GLUTEN_FREE = "gluten_free"
    NONE = "none"

class GoalType(Enum):
    """Enum representing different fitness goals."""
    MUSCLE_GAIN = "muscle_gain"
    WEIGHT_LOSS = "weight_loss"
    ENDURANCE = "endurance"
    MAINTENANCE = "maintenance"

class MealPlan:
    """Class representing a personalized meal plan."""
    
    def __init__(self, meals: List[str], nutritional_info: Dict[str, float]):
        """
        Initialize a meal plan with meals and nutritional information.
        
        Args:
            meals: List of meal descriptions
            nutritional_info: Dictionary with nutritional values (calories, protein, etc.)
        """
        self.meals = meals
        self.nutritional_info = nutritional_info
    
    def to_json(self) -> str:
        """Convert meal plan to JSON format."""
        return json.dumps({
            "meals": self.meals,
            "nutritional_info": self.nutritional_info
        }, indent=2)

class Nutritionist:
    """Class representing a nutritionist who creates personalized meal plans."""
    
    def __init__(self):
        self.meal_databases = {
            DietaryRestriction.VEGAN: self._load_meal_db("vegan_meals.json"),
            DietaryRestriction.VEGETARIAN: self._load_meal_db("vegetarian_meals.json"),
            DietaryRestriction.GLUTEN_FREE: self._load_meal_db("gluten_free_meals.json"),
            DietaryRestriction.NONE: self._load_meal_db("standard_meals.json")
        }
    
    def _load_meal_db(self, filename: str) -> Dict:
        """Load meal database from JSON file."""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Meal database {filename} not found. Using empty database.")
            return {}
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in {filename}. Using empty database.")
            return {}
    
    def create_meal_plan(
        self,
        restriction: DietaryRestriction,
        goal: GoalType,
        calorie_target: float,
        protein_target: float
    ) -> Optional[MealPlan]:
        """
        Create a personalized meal plan based on dietary restrictions and goals.
        
        Args:
            restriction: Dietary restriction enum
            goal: Fitness goal enum
            calorie_target: Daily calorie target
            protein_target: Daily protein target
            
        Returns:
            MealPlan object or None if creation fails
        """
        try:
            available_meals = self.meal_databases.get(restriction, [])
            
            if not available_meals:
                print("No meals available for the specified dietary restriction.")
                return None
                
            # Simplified algorithm - in practice this would be more sophisticated
            selected_meals = []
            total_calories = 0.0
            total_protein = 0.0
            
            for meal in available_meals:
                if total_calories < calorie_target and total_protein < protein_target:
                    selected_meals.append(meal["description"])
                    total_calories += meal["calories"]
                    total_protein += meal["protein"]
                else:
                    break
            
            nutritional_info = {
                "calories": total_calories,
                "protein": total_protein,
                "carbohydrates": sum(m["carbs"] for m in available_meals[:len(selected_meals)]),
                "fats": sum(m["fats"] for m in available_meals[:len(selected_meals)])
            }
            
            return MealPlan(selected_meals, nutritional_info)
            
        except Exception as e:
            print(f"Error creating meal plan: {str(e)}")
            return None

def main():
    """Demonstrate the nutrition planning system."""
    nutritionist = Nutritionist()
    
    # Example: Create a meal plan for a vegan athlete looking to gain muscle
    meal_plan = nutritionist.create_meal_plan(
        restriction=DietaryRestriction.VEGAN,
        goal=GoalType.MUSCLE_GAIN,
        calorie_target=2500,
        protein_target=150
    )
    
    if meal_plan:
        print("Personalized Meal Plan Created:")
        print(meal_plan.to_json())
    else:
        print("Failed to create meal plan.")

if __name__ == "__main__":
    main()
```
