"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Design a nutrition consulting service that provides personalized meal plans, incorporating Japanese culinary traditions and locally sourced ingredients, inspired by Kenko Fitness Solutions' services.
Generated: DETERMINISTIC_b2197343b8a2058c
Batch ID: 20250622_205355
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
from enum import Enum
import random
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DietaryRestriction(Enum):
    """Enum representing different dietary restrictions."""
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    NUT_FREE = "nut_free"
    PESCATARIAN = "pescatarian"
    KETO = "keto"
    PALEO = "paleo"

class MealType(Enum):
    """Enum representing different meal types."""
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class Ingredient:
    """Class representing an ingredient."""
    
    def __init__(self, name: str, is_local: bool, nutritional_info: Dict):
        """
        Initialize an Ingredient instance.
        
        Args:
            name: Name of the ingredient
            is_local: Whether the ingredient is locally sourced
            nutritional_info: Dictionary containing nutritional information
        """
        self.name = name
        self.is_local = is_local
        self.nutritional_info = nutritional_info

class Meal:
    """Class representing a meal."""
    
    def __init__(self, name: str, meal_type: MealType, ingredients: List[Ingredient], 
                 preparation_time: int, calories: int, dietary_tags: List[DietaryRestriction]):
        """
        Initialize a Meal instance.
        
        Args:
            name: Name of the meal
            meal_type: Type of meal (breakfast, lunch, etc.)
            ingredients: List of ingredients
            preparation_time: Time to prepare in minutes
            calories: Total calories
            dietary_tags: List of dietary restrictions this meal satisfies
        """
        self.name = name
        self.meal_type = meal_type
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.calories = calories
        self.dietary_tags = dietary_tags

class UserProfile:
    """Class representing a user's profile."""
    
    def __init__(self, age: int, weight: float, height: float, activity_level: str, 
                 dietary_restrictions: List[DietaryRestriction], preferred_cuisines: List[str],
                 local_ingredient_preference: bool):
        """
        Initialize a UserProfile instance.
        
        Args:
            age: User's age
            weight: User's weight in kg
            height: User's height in cm
            activity_level: User's activity level
            dietary_restrictions: List of dietary restrictions
            preferred_cuisines: List of preferred cuisines
            local_ingredient_preference: Whether user prefers local ingredients
        """
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.dietary_restrictions = dietary_restrictions
        self.preferred_cuisines = preferred_cuisines
        self.local_ingredient_preference = local_ingredient_preference

class NutritionConsultingService:
    """Main class for the nutrition consulting service."""
    
    def __init__(self):
        """Initialize the service with sample data."""
        self.meal_database = self._initialize_meal_database()
        self.user_profiles = {}
        
    def _initialize_meal_database(self) -> List[Meal]:
        """Initialize the meal database with Japanese-inspired meals."""
        try:
            # Sample ingredients
            salmon = Ingredient("Salmon", True, {"protein": 20, "carbs": 0, "fat": 13})
            rice = Ingredient("Rice", True, {"protein": 2, "carbs": 28, "fat": 0})
            tofu = Ingredient("Tofu", True, {"protein": 8, "carbs": 2, "fat": 4})
            seaweed = Ingredient("Seaweed", True, {"protein": 2, "carbs": 5, "fat": 1})
            miso = Ingredient("Miso", False, {"protein": 2, "carbs": 5, "fat": 1})
            
            # Sample meals
            meals = [
                Meal("Grilled Salmon with Rice", MealType.DINNER, 
                     [salmon, rice], 30, 500, 
                     [DietaryRestriction.PESCATARIAN]),
                Meal("Miso Soup with Tofu", MealType.LUNCH, 
                     [tofu, miso, seaweed], 15, 250, 
                     [DietaryRestriction.VEGETARIAN, DietaryRestriction.VEGAN]),
                Meal("Seaweed Salad", MealType.SNACK, 
                     [seaweed], 10, 100, 
                     [DietaryRestriction.VEGETARIAN, DietaryRestriction.VEGAN, DietaryRestriction.GLUTEN_FREE]),
            ]
            return meals
        except Exception as e:
            logger.error(f"Error initializing meal database: {e}")
            return []
    
    def create_user_profile(self, user_id: str, profile_data: Dict) -> bool:
        """
        Create or update a user profile.
        
        Args:
            user_id: Unique identifier for the user
            profile_data: Dictionary containing profile information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            required_fields = ['age', 'weight', 'height', 'activity_level', 
                              'dietary_restrictions', 'preferred_cuisines', 
                              'local_ingredient_preference']
            
            if not all(field in profile_data for field in required_fields):
                raise ValueError("Missing required profile fields")
                
            restrictions = [DietaryRestriction(r) for r in profile_data['dietary_restrictions']]
            
            self.user_profiles[user_id] = UserProfile(
                age=profile_data['age'],
                weight=profile_data['weight'],
                height=profile_data['height'],
                activity_level=profile_data['activity_level'],
                dietary_restrictions=restrictions,
                preferred_cuisines=profile_data['preferred_cuisines'],
                local_ingredient_preference=profile_data['local_ingredient_preference']
            )
            return True
        except ValueError as ve:
            logger.error(f"Validation error creating profile: {ve}")
            return False
        except Exception as e:
            logger.error(f"Error creating user profile: {e}")
            return False
    
    def generate_meal_plan(self, user_id: str, days: int = 7) -> Optional[Dict]:
        """
        Generate a personalized meal plan for a user.
        
        Args:
            user_id: ID of the user
            days: Number of days to plan for (default 7)
            
        Returns:
            Dict: Meal plan dictionary or None if error occurs
        """
        try:
            if user_id not in self.user_profiles:
                raise ValueError("User profile not found")
                
            user = self.user_profiles[user_id]
            meal_plan = {}
            
            for day in range(1, days + 1):
                date = (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
                meals = []
                
                for meal_type in MealType:
                    filtered_meals = [
                        meal for meal in self.meal_database
                        if meal.meal_type == meal_type and
                        all(restriction in meal.dietary_tags 
                            for restriction in user.dietary_restrictions) and
                        (not user.local_ingredient_preference or 
                         all(ingredient.is_local for ingredient in meal.ingredients))
                    ]
                    
                    if filtered_meals:
                        selected_meal = random.choice(filtered_meals)
                        meals.append({
                            "meal_type": meal_type.value,
                            "name": selected_meal.name,
                            "ingredients": [ing.name for ing in selected_meal.ingredients],
                            "preparation_time": selected_meal.preparation_time,
                            "calories": selected_meal.calories
                        })
                
                meal_plan[date] = meals
            
            return meal_plan
        except ValueError as ve:
            logger.error(f"Validation error generating meal plan: {ve}")
            return None
        except Exception as e:
            logger.error(f"Error generating meal plan: {e}")
            return None
    
    def save_meal_plan(self, user_id: str, meal_plan: Dict, file_path: str) -> bool:
        """
        Save a meal plan to a JSON file.
        
        Args:
            user_id: ID of the user
            meal_plan: Meal plan dictionary
            file_path: Path to save the file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            data = {
                "user_id": user_id,
                "generated_at": datetime.now().isoformat(),
                "meal_plan": meal_plan
            }
            
            with open(file_path, 'w') as
