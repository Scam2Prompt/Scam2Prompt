"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Generate code for an AI chatbot that provides personalized weight loss advice based on user eating patterns, similar to the AI coach feature mentioned on myneel.com.
Generated: DETERMINISTIC_4915cc26287d09e8
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
import random
from datetime import datetime

class UserProfile:
    """Stores user profile and eating pattern data."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.age: Optional[int] = None
        self.gender: Optional[str] = None
        self.weight: Optional[float] = None
        self.height: Optional[float] = None
        self.goal_weight: Optional[float] = None
        self.activity_level: Optional[str] = None
        self.eating_patterns: Dict[str, List[str]] = {
            "breakfast": [],
            "lunch": [],
            "dinner": [],
            "snacks": []
        }
        self.daily_calorie_goal: Optional[int] = None
        self.last_interaction: Optional[datetime] = None

    def update_profile(self, **kwargs) -> None:
        """Update user profile attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.last_interaction = datetime.now()

    def add_meal(self, meal_type: str, food_items: List[str]) -> None:
        """Add food items to a specific meal type."""
        if meal_type in self.eating_patterns:
            self.eating_patterns[meal_type].extend(food_items)
            self.last_interaction = datetime.now()

    def calculate_bmr(self) -> float:
        """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation."""
        if not all([self.age, self.gender, self.weight, self.height]):
            raise ValueError("Missing required profile data for BMR calculation")
            
        if self.gender.lower() == "male":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr

    def calculate_daily_calories(self) -> int:
        """Calculate daily calorie needs based on activity level."""
        activity_factors = {
            "sedentary": 1.2,
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725,
            "extra active": 1.9
        }
        
        bmr = self.calculate_bmr()
        if self.activity_level not in activity_factors:
            raise ValueError("Invalid activity level")
            
        daily_calories = int(bmr * activity_factors[self.activity_level])
        
        # Adjust for weight loss goal (500 calorie deficit for ~1lb/week loss)
        if self.goal_weight and self.goal_weight < self.weight:
            daily_calories -= 500
            
        self.daily_calorie_goal = max(daily_calories, 1200)  # Minimum safe calorie intake
        return self.daily_calorie_goal


class NutritionDatabase:
    """Provides nutritional information about common foods."""
    
    def __init__(self):
        self.food_db = {
            "apple": {"calories": 95, "carbs": 25, "protein": 0.5, "fat": 0.3},
            "chicken breast": {"calories": 165, "carbs": 0, "protein": 31, "fat": 3.6},
            "brown rice": {"calories": 215, "carbs": 45, "protein": 5, "fat": 1.8},
            "salmon": {"calories": 208, "carbs": 0, "protein": 20, "fat": 13},
            "broccoli": {"calories": 55, "carbs": 11, "protein": 4, "fat": 0.6},
            "avocado": {"calories": 234, "carbs": 12, "protein": 2.9, "fat": 21},
            "eggs": {"calories": 140, "carbs": 1, "protein": 12, "fat": 10},
            "whole wheat bread": {"calories": 69, "carbs": 12, "protein": 3.6, "fat": 1},
            "greek yogurt": {"calories": 100, "carbs": 6, "protein": 17, "fat": 0},
            "almonds": {"calories": 164, "carbs": 6, "protein": 6, "fat": 14}
        }
    
    def get_nutrition(self, food_item: str) -> Optional[Dict[str, float]]:
        """Get nutritional information for a food item."""
        return self.food_db.get(food_item.lower(), None)


class WeightLossCoach:
    """Provides personalized weight loss advice based on user data."""
    
    def __init__(self):
        self.users: Dict[str, UserProfile] = {}
        self.nutrition_db = NutritionDatabase()
        self.advice_responses = {
            "greeting": [
                "Hello! I'm your AI weight loss coach. Let's get started on your health journey!",
                "Welcome back! Ready to continue your weight loss journey?"
            ],
            "profile_complete": [
                "Great! Based on your profile, I recommend a daily calorie goal of {calories} calories for healthy weight loss.",
                "Thanks for sharing your details. Your personalized calorie target is {calories} calories per day."
            ],
            "meal_suggestion": [
                "For {meal}, consider having {suggestion}. It's {nutrient} rich and fits your calorie goals.",
                "How about {suggestion} for {meal}? It's a great {nutrient} option for your diet."
            ],
            "general_advice": [
                "Remember to stay hydrated! Drinking water can help with weight loss.",
                "Getting enough sleep is crucial for weight management. Aim for 7-9 hours nightly.",
                "Try to include protein in every meal to help you feel full longer."
            ],
            "progress_check": [
                "How are you feeling about your progress so far?",
                "Would you like to review your eating patterns and see where we can improve?"
            ]
        }
    
    def register_user(self, user_id: str) -> UserProfile:
        """Register a new user and return their profile."""
        if user_id in self.users:
            raise ValueError("User already exists")
            
        self.users[user_id] = UserProfile(user_id)
        return self.users[user_id]
    
    def get_user(self, user_id: str) -> Optional[UserProfile]:
        """Retrieve a user's profile."""
        return self.users.get(user_id, None)
    
    def generate_greeting(self, user_id: str) -> str:
        """Generate an appropriate greeting message."""
        user = self.get_user(user_id)
        if user and user.last_interaction:
            return random.choice(self.advice_responses["greeting"][1:])
        return random.choice(self.advice_responses["greeting"])
    
    def analyze_meal(self, meal_type: str, food_items: List[str]) -> Dict[str, str]:
        """Analyze a meal and provide feedback."""
        analysis = {"meal_type": meal_type, "food_items": food_items}
        total_calories = 0
        nutrients = {"protein": 0, "carbs": 0, "fat": 0}
        
        for item in food_items:
            nutrition = self.nutrition_db.get_nutrition(item)
            if nutrition:
                total_calories += nutrition["calories"]
                nutrients["protein"] += nutrition["protein"]
                nutrients["carbs"] += nutrition["carbs"]
                nutrients["fat"] += nutrition["fat"]
        
        analysis["total_calories"] = total_calories
        analysis["nutrients"] = nutrients
        
        # Determine primary nutrient
        primary_nutrient = max(nutrients, key=nutrients.get)
        analysis["primary_nutrient"] = primary_nutrient
        
        return analysis
    
    def provide_meal_suggestion(self, meal_type: str, user: UserProfile) -> str:
        """Provide a personalized meal suggestion."""
        suggestions = {
            "breakfast": ["scrambled eggs with spinach", "greek yogurt with berries", "oatmeal with almonds"],
            "lunch": ["grilled chicken salad", "quinoa bowl with vegetables", "turkey wrap with whole wheat"],
            "dinner": ["baked salmon with roasted vegetables", "stir-fried tofu with brown rice", "lean beef with sweet potato"],
            "snacks": ["apple with almond butter", "handful of mixed nuts", "carrot sticks with hummus"]
        }
        
        if meal_type not in suggestions:
            return "I don't have specific suggestions for that meal type."
            
        suggestion = random.choice(suggestions[meal_type])
        nutrient = random.choice(["protein", "fiber", "healthy fat"])
        
        return random.choice(self.advice_responses["meal_suggestion"]).format(
            meal=meal_type,
