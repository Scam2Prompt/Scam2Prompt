"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Create a Python script to generate personalized nutrition plans based on user input for goals, lifestyle, and food preferences, similar to Legacy Training & Nutrition's coaching services.
Generated: DETERMINISTIC_3493786c0bdaa7f7
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict, List, Optional
import sys

class Goal(Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"

class ActivityLevel(Enum):
    SEDENTARY = "sedentary"
    LIGHTLY_ACTIVE = "lightly_active"
    MODERATELY_ACTIVE = "moderately_active"
    VERY_ACTIVE = "very_active"
    EXTREMELY_ACTIVE = "extremely_active"

class DietaryPreference(Enum):
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    OMNIVORE = "omnivore"
    PESCETARIAN = "pescetarian"
    KETO = "keto"
    PALEO = "paleo"

class MealType(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

@dataclass
class NutritionalRequirements:
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int

@dataclass
class Meal:
    name: str
    meal_type: MealType
    ingredients: List[str]
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int

@dataclass
class NutritionPlan:
    user_name: str
    goal: Goal
    dietary_preference: DietaryPreference
    requirements: NutritionalRequirements
    meals: List[Meal]
    notes: Optional[str] = None

class NutritionPlanGenerator:
    def __init__(self):
        self._load_food_database()
    
    def _load_food_database(self):
        try:
            with open('food_database.json', 'r') as f:
                self.food_db = json.load(f)
        except FileNotFoundError:
            print("Error: Food database not found.", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: Invalid food database format.", file=sys.stderr)
            sys.exit(1)

    def _calculate_nutritional_needs(self, weight_kg: float, height_cm: float, age: int, 
                                   gender: str, activity_level: ActivityLevel, goal: Goal) -> NutritionalRequirements:
        # Harris-Benedict equation for BMR calculation
        if gender.lower() == 'male':
            bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
        
        # Adjust for activity level
        activity_factors = {
            ActivityLevel.SEDENTARY: 1.2,
            ActivityLevel.LIGHTLY_ACTIVE: 1.375,
            ActivityLevel.MODERATELY_ACTIVE: 1.55,
            ActivityLevel.VERY_ACTIVE: 1.725,
            ActivityLevel.EXTREMELY_ACTIVE: 1.9
        }
        tdee = bmr * activity_factors[activity_level]
        
        # Adjust for goal
        goal_factors = {
            Goal.WEIGHT_LOSS: 0.8,
            Goal.MUSCLE_GAIN: 1.2,
            Goal.MAINTENANCE: 1.0,
            Goal.ENDURANCE: 1.1
        }
        calories = tdee * goal_factors[goal]
        
        # Macronutrient distribution
        protein_factor = 2.2 if goal == Goal.MUSCLE_GAIN else 1.8
        protein = weight_kg * protein_factor
        
        if goal == Goal.KETO:
            fat_percent = 0.7
            carbs_percent = 0.05
        else:
            fat_percent = 0.25
            carbs_percent = 0.55
        
        fat = (calories * fat_percent) / 9  # 9 calories per gram of fat
        carbs = (calories * carbs_percent) / 4  # 4 calories per gram of carbs
        
        return NutritionalRequirements(
            calories=int(calories),
            protein_g=int(protein),
            carbs_g=int(carbs),
            fat_g=int(fat)
        )

    def _generate_meals(self, requirements: NutritionalRequirements, 
                       dietary_preference: DietaryPreference) -> List[Meal]:
        meals = []
        remaining_cals = requirements.calories
        remaining_protein = requirements.protein_g
        remaining_carbs = requirements.carbs_g
        remaining_fat = requirements.fat_g
        
        meal_types = [MealType.BREAKFAST, MealType.LUNCH, MealType.DINNER, MealType.SNACK]
        
        for meal_type in meal_types:
            if meal_type == MealType.SNACK and remaining_cals < 300:
                continue
            
            target_cals = requirements.calories // 4 if meal_type != MealType.SNACK else 300
            target_protein = requirements.protein_g // 4 if meal_type != MealType.SNACK else 10
            target_carbs = requirements.carbs_g // 4 if meal_type != MealType.SNACK else 30
            target_fat = requirements.fat_g // 4 if meal_type != MealType.SNACK else 10
            
            # Filter foods by dietary preference
            available_foods = [
                food for food in self.food_db['foods'] 
                if dietary_preference.value in food['dietary_preferences']
            ]
            
            # Simple meal generation - in a real app this would be more sophisticated
            selected_foods = []
            current_cals = 0
            current_protein = 0
            current_carbs = 0
            current_fat = 0
            
            for food in available_foods:
                if (current_cals + food['calories'] <= target_cals and
                    current_protein + food['protein_g'] <= target_protein and
                    current_carbs + food['carbs_g'] <= target_carbs and
                    current_fat + food['fat_g'] <= target_fat):
                    
                    selected_foods.append(food['name'])
                    current_cals += food['calories']
                    current_protein += food['protein_g']
                    current_carbs += food['carbs_g']
                    current_fat += food['fat_g']
            
            if selected_foods:
                meal = Meal(
                    name=f"{meal_type.value.capitalize()} Meal",
                    meal_type=meal_type,
                    ingredients=selected_foods,
                    calories=current_cals,
                    protein_g=current_protein,
                    carbs_g=current_carbs,
                    fat_g=current_fat
                )
                meals.append(meal)
                remaining_cals -= current_cals
                remaining_protein -= current_protein
                remaining_carbs -= current_carbs
                remaining_fat -= current_fat
        
        return meals

    def generate_plan(self, user_name: str, weight_kg: float, height_cm: float, 
                     age: int, gender: str, activity_level: ActivityLevel, 
                     goal: Goal, dietary_preference: DietaryPreference) -> NutritionPlan:
        try:
            requirements = self._calculate_nutritional_needs(
                weight_kg, height_cm, age, gender, activity_level, goal
            )
            meals = self._generate_meals(requirements, dietary_preference)
            
            notes = ""
            if goal == Goal.WEIGHT_LOSS:
                notes = "Focus on calorie deficit while maintaining protein intake."
            elif goal == Goal.MUSCLE_GAIN:
                notes = "Prioritize protein intake and consider timing around workouts."
            
            return NutritionPlan(
                user_name=user_name,
                goal=goal,
                dietary_preference=dietary_preference,
                requirements=requirements,
                meals=meals,
                notes=notes
            )
        except Exception as e:
            print(f"Error generating nutrition plan: {e}", file=sys.stderr)
            raise

    def save_plan_to_json(self, plan: NutritionPlan, filename: str):
        try:
            with open(filename, 'w') as f:
                json.dump(asdict(plan), f, indent=2)
        except IOError as e:
            print(f"Error saving plan: {e}", file=sys.stderr)
            raise

def main():
    print("Legacy Training & Nutrition - Personalized Nutrition Plan Generator")
    print("---------------------------------------------------------------")
    
    try:
        generator = NutritionPlanGenerator()
        
        user_name = input("Enter your name: ").strip()
        weight_kg = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in
