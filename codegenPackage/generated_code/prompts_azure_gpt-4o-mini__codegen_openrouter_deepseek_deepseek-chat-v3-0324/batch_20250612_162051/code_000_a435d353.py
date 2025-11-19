"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Write a Python script that utilizes the principles of clinical nutrition to create a personalized meal plan for weight loss, considering common lifestyle disorders mentioned on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_a435d3539911dd2d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
import random

class LifestyleDisorder(Enum):
    DIABETES = "Diabetes"
    HYPERTENSION = "Hypertension"
    PCOS = "PCOS"
    THYROID = "Thyroid Disorder"
    NONE = "None"

class MealTime(Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACKS = "Snacks"

class FoodItem:
    def __init__(self, name: str, calories: int, protein: float, carbs: float, fats: float, 
                 suitable_for: List[LifestyleDisorder] = None):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.suitable_for = suitable_for if suitable_for else [LifestyleDisorder.NONE]

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fats": self.fats,
            "suitable_for": [disorder.value for disorder in self.suitable_for]
        }

class MealPlan:
    def __init__(self):
        self.meals = {
            MealTime.BREAKFAST: [],
            MealTime.LUNCH: [],
            MealTime.DINNER: [],
            MealTime.SNACKS: []
        }
    
    def add_meal(self, meal_time: MealTime, food_item: FoodItem):
        self.meals[meal_time].append(food_item)
    
    def get_total_nutrition(self) -> Dict[str, float]:
        total = {
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fats": 0
        }
        for meal_time in self.meals:
            for food in self.meals[meal_time]:
                total["calories"] += food.calories
                total["protein"] += food.protein
                total["carbs"] += food.carbs
                total["fats"] += food.fats
        return total
    
    def to_dict(self) -> Dict:
        return {
            meal_time.value: [food.to_dict() for food in foods]
            for meal_time, foods in self.meals.items()
        }

class NutritionDatabase:
    def __init__(self):
        self.food_items = []
        self._initialize_database()
    
    def _initialize_database(self):
        # Basic food items with nutritional values per 100g
        self.food_items.extend([
            # General foods
            FoodItem("Oatmeal", 68, 2.4, 12, 1.4),
            FoodItem("Whole Wheat Bread", 247, 13, 41, 3.4),
            FoodItem("Brown Rice", 111, 2.6, 23, 0.9),
            FoodItem("Grilled Chicken Breast", 165, 31, 0, 3.6),
            FoodItem("Salmon", 208, 20, 0, 13),
            FoodItem("Broccoli", 34, 2.8, 6.6, 0.4),
            FoodItem("Spinach", 23, 2.9, 3.6, 0.4),
            FoodItem("Almonds", 579, 21, 22, 50),
            FoodItem("Greek Yogurt", 59, 10, 3.6, 0.4),
            FoodItem("Eggs", 143, 13, 0.7, 9.5),
            
            # Diabetes-friendly
            FoodItem("Quinoa", 120, 4.4, 21, 1.9, [LifestyleDisorder.DIABETES]),
            FoodItem("Chia Seeds", 486, 17, 42, 31, [LifestyleDisorder.DIABETES, LifestyleDisorder.PCOS]),
            
            # Hypertension-friendly
            FoodItem("Avocado", 160, 2, 8.5, 15, [LifestyleDisorder.HYPERTENSION]),
            FoodItem("Banana", 89, 1.1, 22.8, 0.3, [LifestyleDisorder.HYPERTENSION]),
            
            # PCOS-friendly
            FoodItem("Flaxseeds", 534, 18, 29, 42, [LifestyleDisorder.PCOS]),
            FoodItem("Walnuts", 654, 15, 14, 65, [LifestyleDisorder.PCOS]),
            
            # Thyroid-friendly
            FoodItem("Brazil Nuts", 659, 14, 12, 67, [LifestyleDisorder.THYROID]),
            FoodItem("Seaweed", 45, 3, 8, 1, [LifestyleDisorder.THYROID])
        ])
    
    def get_food_items(self, disorder: Optional[LifestyleDisorder] = None) -> List[FoodItem]:
        if not disorder or disorder == LifestyleDisorder.NONE:
            return [item for item in self.food_items if LifestyleDisorder.NONE in item.suitable_for]
        return [item for item in self.food_items if disorder in item.suitable_for]

class MealPlanner:
    def __init__(self):
        self.db = NutritionDatabase()
    
    def create_meal_plan(self, target_calories: int, disorder: LifestyleDisorder = LifestyleDisorder.NONE) -> MealPlan:
        """
        Creates a personalized meal plan based on target calories and lifestyle disorder.
        """
        if target_calories < 1200:
            raise ValueError("Target calories should be at least 1200 for healthy weight loss")
        
        plan = MealPlan()
        remaining_calories = target_calories
        
        # Distribute calories across meals (40% breakfast, 30% lunch, 20% dinner, 10% snacks)
        meal_distribution = {
            MealTime.BREAKFAST: 0.4,
            MealTime.LUNCH: 0.3,
            MealTime.DINNER: 0.2,
            MealTime.SNACKS: 0.1
        }
        
        for meal_time, percentage in meal_distribution.items():
            target_meal_calories = int(target_calories * percentage)
            self._add_meal_to_plan(plan, meal_time, target_meal_calories, disorder)
            remaining_calories -= target_meal_calories
        
        return plan
    
    def _add_meal_to_plan(self, plan: MealPlan, meal_time: MealTime, 
                          target_calories: int, disorder: LifestyleDisorder):
        suitable_foods = self.db.get_food_items(disorder)
        selected_foods = []
        remaining_calories = target_calories
        
        # Try to include protein source in each meal
        protein_sources = [f for f in suitable_foods if f.protein > 10]
        if protein_sources:
            protein_item = random.choice(protein_sources)
            selected_foods.append(protein_item)
            remaining_calories -= protein_item.calories
        
        # Fill remaining calories with other foods
        while remaining_calories > 0 and suitable_foods:
            food = random.choice(suitable_foods)
            if food.calories <= remaining_calories:
                selected_foods.append(food)
                remaining_calories -= food.calories
        
        for food in selected_foods:
            plan.add_meal(meal_time, food)

def get_user_input() -> Tuple[int, LifestyleDisorder]:
    print("Welcome to the Personalized Meal Planner for Weight Loss")
    print("Based on principles from Green Apples e-Rx Clinic")
    print("------------------------------------------------------")
    
    while True:
        try:
            calories = int(input("Enter your daily calorie target (minimum 1200): "))
            if calories < 1200:
                print("Calories should be at least 1200 for healthy weight loss")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    
    print("\nSelect any lifestyle disorder you have (enter the number):")
    for i, disorder in enumerate(LifestyleDisorder):
        print(f"{i+1}. {disorder.value}")
    
    while True:
        try:
            choice = int(input("Your choice (1-5): "))
            if 1 <= choice <= len(LifestyleDisorder):
                disorder = list(LifestyleDisorder)[choice-1]
                break
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")
    
    return calories, disorder

def display_meal_plan(plan: MealPlan):
    print("\nYour Personalized Meal Plan:")
    print("----------------------------")
    
    for meal_time, foods in plan.meals.items():
        print(f"\n{meal_time.value}:")
        for food in foods:
            print(f"- {food.name} ({
