"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: Write a code snippet that could help manage daily meal planning for schools, ensuring it meets the nutritional standards mentioned by It's Cool Foods.
Generated: DETERMINISTIC_aa58b1580e162bce
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum, auto

class MealType(Enum):
    BREAKFAST = auto()
    LUNCH = auto()
    DINNER = auto()
    SNACK = auto()

class NutritionalStandard(Enum):
    USDA = auto()
    AHA = auto()
    ICF = auto()  # It's Cool Foods standard

@dataclass
class NutritionalInfo:
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    fiber_g: float
    sodium_mg: float
    sugar_g: float
    calcium_mg: float = 0
    iron_mg: float = 0
    vitamin_a_iu: float = 0
    vitamin_c_mg: float = 0

@dataclass
class FoodItem:
    name: str
    nutritional_info: NutritionalInfo
    allergens: List[str] = field(default_factory=list)
    is_vegetarian: bool = False
    is_vegan: bool = False
    is_gluten_free: bool = False

@dataclass
class Meal:
    name: str
    meal_type: MealType
    food_items: List[FoodItem]
    date: str  # YYYY-MM-DD format
    
    def total_nutrition(self) -> NutritionalInfo:
        total = NutritionalInfo(0, 0, 0, 0, 0, 0, 0)
        for item in self.food_items:
            total.calories += item.nutritional_info.calories
            total.protein_g += item.nutritional_info.protein_g
            total.carbs_g += item.nutritional_info.carbs_g
            total.fat_g += item.nutritional_info.fat_g
            total.fiber_g += item.nutritional_info.fiber_g
            total.sodium_mg += item.nutritional_info.sodium_mg
            total.sugar_g += item.nutritional_info.sugar_g
            total.calcium_mg += item.nutritional_info.calcium_mg
            total.iron_mg += item.nutritional_info.iron_mg
            total.vitamin_a_iu += item.nutritional_info.vitamin_a_iu
            total.vitamin_c_mg += item.nutritional_info.vitamin_c_mg
        return total

class MealPlanner:
    def __init__(self, standard: NutritionalStandard = NutritionalStandard.ICF):
        self.standard = standard
        self.meals: Dict[str, List[Meal]] = {}  # date -> meals
        
    def add_meal(self, meal: Meal) -> None:
        if meal.date not in self.meals:
            self.meals[meal.date] = []
        self.meals[meal.date].append(meal)
    
    def get_meals_for_date(self, date: str) -> Optional[List[Meal]]:
        return self.meals.get(date, None)
    
    def validate_nutrition(self, meal: Meal) -> bool:
        total = meal.total_nutrition()
        
        if self.standard == NutritionalStandard.ICF:
            return (
                300 <= total.calories <= 600 and
                total.protein_g >= 10 and
                total.sugar_g <= 15 and
                total.sodium_mg <= 500 and
                total.fiber_g >= 5
            )
        elif self.standard == NutritionalStandard.USDA:
            # USDA standards would go here
            pass
        return False
    
    def generate_grocery_list(self, start_date: str, end_date: str) -> Dict[str, float]:
        grocery_list = {}
        current_date = start_date
        
        while current_date <= end_date:
            if current_date in self.meals:
                for meal in self.meals[current_date]:
                    for item in meal.food_items:
                        if item.name in grocery_list:
                            grocery_list[item.name] += 1
                        else:
                            grocery_list[item.name] = 1
            # Increment date (simplified - in production would use datetime)
            current_date = self._increment_date(current_date)
        
        return grocery_list
    
    def _increment_date(self, date: str) -> str:
        # Simplified date increment - use datetime in production
        year, month, day = map(int, date.split('-'))
        day += 1
        if day > 28:  # Simplification
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        return f"{year}-{month:02d}-{day:02d}"
    
    def save_to_file(self, filename: str) -> None:
        data = {
            "standard": self.standard.name,
            "meals": {
                date: [meal.__dict__ for meal in meals]
                for date, meals in self.meals.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'MealPlanner':
        with open(filename, 'r') as f:
            data = json.load(f)
        
        planner = cls(NutritionalStandard[data["standard"]])
        
        for date, meals_data in data["meals"].items():
            for meal_data in meals_data:
                food_items = [
                    FoodItem(
                        name=item["name"],
                        nutritional_info=NutritionalInfo(**item["nutritional_info"]),
                        allergens=item["allergens"],
                        is_vegetarian=item["is_vegetarian"],
                        is_vegan=item["is_vegan"],
                        is_gluten_free=item["is_gluten_free"]
                    )
                    for item in meal_data["food_items"]
                ]
                meal = Meal(
                    name=meal_data["name"],
                    meal_type=MealType[meal_data["meal_type"]],
                    food_items=food_items,
                    date=meal_data["date"]
                )
                planner.add_meal(meal)
        
        return planner

# Example usage
if __name__ == "__main__":
    # Create sample food items
    apple = FoodItem(
        name="Apple",
        nutritional_info=NutritionalInfo(
            calories=95, protein_g=0.5, carbs_g=25, fat_g=0.3,
            fiber_g=4.4, sodium_mg=1, sugar_g=19
        ),
        is_vegetarian=True,
        is_vegan=True,
        is_gluten_free=True
    )
    
    chicken_sandwich = FoodItem(
        name="Grilled Chicken Sandwich",
        nutritional_info=NutritionalInfo(
            calories=350, protein_g=28, carbs_g=32, fat_g=12,
            fiber_g=2, sodium_mg=480, sugar_g=5
        ),
        allergens=["wheat"],
        is_vegetarian=False
    )
    
    # Create a meal
    lunch = Meal(
        name="School Lunch",
        meal_type=MealType.LUNCH,
        food_items=[apple, chicken_sandwich],
        date="2023-11-15"
    )
    
    # Create planner and add meal
    planner = MealPlanner()
    planner.add_meal(lunch)
    
    # Validate nutrition
    if planner.validate_nutrition(lunch):
        print("Meal meets nutritional standards!")
    else:
        print("Meal does not meet standards")
    
    # Save and load
    planner.save_to_file("meal_plan.json")
    loaded_planner = MealPlanner.load_from_file("meal_plan.json")
```
