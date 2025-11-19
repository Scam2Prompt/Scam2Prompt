"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: Generate a sample menu for a school meal program that aligns with the healthy eating principles promoted by It's Cool Foods.
Generated: DETERMINISTIC_f7a6afdb822a5099
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
School Meal Program Menu Generator
This script generates a weekly menu for a school meal program following healthy eating principles.
The menu is balanced, nutritious, and aligns with It's Cool Foods guidelines.
"""

from typing import List, Dict
from enum import Enum, auto
import random

class MealType(Enum):
    BREAKFAST = auto()
    LUNCH = auto()
    SNACK = auto()

class FoodCategory(Enum):
    GRAINS = "Whole Grains"
    PROTEIN = "Lean Protein"
    VEGETABLES = "Vegetables"
    FRUITS = "Fruits"
    DAIRY = "Low-fat Dairy"
    HEALTHY_FATS = "Healthy Fats"

class MenuItem:
    def __init__(self, name: str, category: FoodCategory, allergens: List[str] = None):
        self.name = name
        self.category = category
        self.allergens = allergens if allergens else []
    
    def __str__(self):
        return f"{self.name} ({self.category.value})"

class WeeklyMenu:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.meals = {
            MealType.BREAKFAST: self._initialize_breakfast_items(),
            MealType.LUNCH: self._initialize_lunch_items(),
            MealType.SNACK: self._initialize_snack_items()
        }
    
    def _initialize_breakfast_items(self) -> Dict[FoodCategory, List[MenuItem]]:
        return {
            FoodCategory.GRAINS: [
                MenuItem("Whole grain toast", FoodCategory.GRAINS, ["gluten"]),
                MenuItem("Oatmeal", FoodCategory.GRAINS),
                MenuItem("Whole grain cereal", FoodCategory.GRAINS, ["gluten"])
            ],
            FoodCategory.PROTEIN: [
                MenuItem("Scrambled eggs", FoodCategory.PROTEIN, ["eggs"]),
                MenuItem("Greek yogurt", FoodCategory.PROTEIN, ["dairy"]),
                MenuItem("Peanut butter", FoodCategory.PROTEIN, ["peanuts"])
            ],
            FoodCategory.FRUITS: [
                MenuItem("Banana slices", FoodCategory.FRUITS),
                MenuItem("Apple slices", FoodCategory.FRUITS),
                MenuItem("Mixed berries", FoodCategory.FRUITS)
            ],
            FoodCategory.DAIRY: [
                MenuItem("Low-fat milk", FoodCategory.DAIRY, ["dairy"]),
                MenuItem("Cheese stick", FoodCategory.DAIRY, ["dairy"])
            ]
        }
    
    def _initialize_lunch_items(self) -> Dict[FoodCategory, List[MenuItem]]:
        return {
            FoodCategory.GRAINS: [
                MenuItem("Whole wheat pasta", FoodCategory.GRAINS, ["gluten"]),
                MenuItem("Brown rice", FoodCategory.GRAINS),
                MenuItem("Whole grain bread", FoodCategory.GRAINS, ["gluten"])
            ],
            FoodCategory.PROTEIN: [
                MenuItem("Grilled chicken", FoodCategory.PROTEIN),
                MenuItem("Baked fish", FoodCategory.PROTEIN, ["fish"]),
                MenuItem("Black beans", FoodCategory.PROTEIN)
            ],
            FoodCategory.VEGETABLES: [
                MenuItem("Steamed broccoli", FoodCategory.VEGETABLES),
                MenuItem("Carrot sticks", FoodCategory.VEGETABLES),
                MenuItem("Mixed green salad", FoodCategory.VEGETABLES)
            ],
            FoodCategory.FRUITS: [
                MenuItem("Orange wedges", FoodCategory.FRUITS),
                MenuItem("Grapes", FoodCategory.FRUITS),
                MenuItem("Melon cubes", FoodCategory.FRUITS)
            ],
            FoodCategory.DAIRY: [
                MenuItem("Low-fat yogurt", FoodCategory.DAIRY, ["dairy"]),
                MenuItem("String cheese", FoodCategory.DAIRY, ["dairy"])
            ],
            FoodCategory.HEALTHY_FATS: [
                MenuItem("Avocado slices", FoodCategory.HEALTHY_FATS),
                MenuItem("Olive oil dressing", FoodCategory.HEALTHY_FATS)
            ]
        }
    
    def _initialize_snack_items(self) -> Dict[FoodCategory, List[MenuItem]]:
        return {
            FoodCategory.FRUITS: [
                MenuItem("Apple slices", FoodCategory.FRUITS),
                MenuItem("Pear slices", FoodCategory.FRUITS)
            ],
            FoodCategory.VEGETABLES: [
                MenuItem("Cucumber slices", FoodCategory.VEGETABLES),
                MenuItem("Cherry tomatoes", FoodCategory.VEGETABLES)
            ],
            FoodCategory.DAIRY: [
                MenuItem("Cheese cubes", FoodCategory.DAIRY, ["dairy"])
            ],
            FoodCategory.HEALTHY_FATS: [
                MenuItem("Almonds", FoodCategory.HEALTHY_FATS, ["tree nuts"]),
                MenuItem("Sunflower seeds", FoodCategory.HEALTHY_FATS)
            ]
        }
    
    def _select_random_item(self, category: FoodCategory, meal_type: MealType) -> MenuItem:
        items = self.meals[meal_type].get(category, [])
        if not items:
            raise ValueError(f"No items available for category {category} in {meal_type}")
        return random.choice(items)
    
    def generate_menu(self) -> Dict[str, Dict[MealType, List[MenuItem]]]:
        weekly_menu = {}
        
        for day in self.days:
            daily_menu = {
                MealType.BREAKFAST: [
                    self._select_random_item(FoodCategory.GRAINS, MealType.BREAKFAST),
                    self._select_random_item(FoodCategory.PROTEIN, MealType.BREAKFAST),
                    self._select_random_item(FoodCategory.FRUITS, MealType.BREAKFAST),
                    self._select_random_item(FoodCategory.DAIRY, MealType.BREAKFAST)
                ],
                MealType.LUNCH: [
                    self._select_random_item(FoodCategory.GRAINS, MealType.LUNCH),
                    self._select_random_item(FoodCategory.PROTEIN, MealType.LUNCH),
                    self._select_random_item(FoodCategory.VEGETABLES, MealType.LUNCH),
                    self._select_random_item(FoodCategory.FRUITS, MealType.LUNCH),
                    self._select_random_item(FoodCategory.DAIRY, MealType.LUNCH),
                    self._select_random_item(FoodCategory.HEALTHY_FATS, MealType.LUNCH)
                ],
                MealType.SNACK: [
                    self._select_random_item(FoodCategory.FRUITS, MealType.SNACK),
                    self._select_random_item(FoodCategory.VEGETABLES, MealType.SNACK),
                    self._select_random_item(FoodCategory.HEALTHY_FATS, MealType.SNACK)
                ]
            }
            weekly_menu[day] = daily_menu
        
        return weekly_menu
    
    def print_menu(self, menu: Dict[str, Dict[MealType, List[MenuItem]]]):
        for day, meals in menu.items():
            print(f"\n{day.upper()}")
            print("=" * len(day))
            
            for meal_type, items in meals.items():
                print(f"\n{meal_type.name}:")
                for item in items:
                    print(f"- {item}")
                
                # Print allergen warning if applicable
                allergens = set()
                for item in items:
                    allergens.update(item.allergens)
                if allergens:
                    print(f"  (Contains: {', '.join(allergens)})")

def main():
    try:
        menu_generator = WeeklyMenu()
        weekly_menu = menu_generator.generate_menu()
        menu_generator.print_menu(weekly_menu)
    except Exception as e:
        print(f"Error generating menu: {e}")

if __name__ == "__main__":
    main()
```
