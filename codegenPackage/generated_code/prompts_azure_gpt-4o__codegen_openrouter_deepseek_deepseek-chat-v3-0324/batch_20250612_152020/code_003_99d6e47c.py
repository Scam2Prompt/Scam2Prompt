"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Create a script to analyze dietary preferences and generate meal plans for seniors, aligning with the Balanced Care Method™ principles described on the Home Care Assistance Barrie webpage.
Generated: DETERMINISTIC_99d6e47c748042d6
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional, Tuple

# Constants for dietary preferences and health conditions
DIETARY_PREFERENCES = [
    "vegetarian",
    "vegan",
    "gluten-free",
    "dairy-free",
    "low-sodium",
    "diabetic-friendly",
    "heart-healthy",
    "soft-foods"
]

HEALTH_CONDITIONS = [
    "diabetes",
    "hypertension",
    "heart_disease",
    "osteoporosis",
    "dementia",
    "arthritis"
]

# Nutritional guidelines based on Balanced Care Method™ principles
NUTRITIONAL_GUIDELINES = {
    "general": {
        "calories": (1600, 2200),
        "protein": (50, 70),  # grams
        "carbs": (130, 200),  # grams
        "fats": (44, 78),     # grams
        "fiber": (25, 30)     # grams
    },
    "diabetes": {
        "carbs": (45, 60),    # grams per meal
        "sugar": "<10g"       # per serving
    },
    "hypertension": {
        "sodium": "<1500mg"   # daily
    },
    "heart_disease": {
        "saturated_fat": "<13g",  # daily
        "cholesterol": "<200mg"   # daily
    }
}

# Meal database categorized by type and dietary preferences
MEAL_DATABASE = {
    "breakfast": {
        "general": [
            {"name": "Oatmeal with berries", "nutrition": {"calories": 300, "protein": 8, "carbs": 54, "fats": 5, "fiber": 8}},
            {"name": "Scrambled eggs with whole wheat toast", "nutrition": {"calories": 350, "protein": 18, "carbs": 30, "fats": 18, "fiber": 5}},
            {"name": "Greek yogurt with nuts and honey", "nutrition": {"calories": 280, "protein": 15, "carbs": 30, "fats": 12, "fiber": 3}}
        ],
        "vegetarian": [
            {"name": "Avocado toast", "nutrition": {"calories": 320, "protein": 10, "carbs": 35, "fats": 18, "fiber": 9}},
            {"name": "Vegetable omelette", "nutrition": {"calories": 290, "protein": 16, "carbs": 12, "fats": 20, "fiber": 4}}
        ],
        "diabetic-friendly": [
            {"name": "Chia pudding with almond milk", "nutrition": {"calories": 250, "protein": 8, "carbs": 20, "fats": 15, "fiber": 10}},
            {"name": "Egg white scramble with spinach", "nutrition": {"calories": 180, "protein": 20, "carbs": 8, "fats": 7, "fiber": 4}}
        ]
    },
    "lunch": {
        "general": [
            {"name": "Grilled chicken salad", "nutrition": {"calories": 400, "protein": 35, "carbs": 20, "fats": 22, "fiber": 6}},
            {"name": "Quinoa bowl with vegetables", "nutrition": {"calories": 380, "protein": 14, "carbs": 58, "fats": 12, "fiber": 9}},
            {"name": "Turkey and avocado wrap", "nutrition": {"calories": 420, "protein": 25, "carbs": 45, "fats": 18, "fiber": 7}}
        ],
        "vegetarian": [
            {"name": "Lentil soup with whole grain bread", "nutrition": {"calories": 350, "protein": 18, "carbs": 50, "fats": 8, "fiber": 12}},
            {"name": "Caprese salad", "nutrition": {"calories": 320, "protein": 15, "carbs": 12, "fats": 24, "fiber": 3}}
        ],
        "heart-healthy": [
            {"name": "Baked salmon with steamed vegetables", "nutrition": {"calories": 380, "protein": 30, "carbs": 25, "fats": 20, "fiber": 8}},
            {"name": "Mediterranean chickpea salad", "nutrition": {"calories": 340, "protein": 12, "carbs": 40, "fats": 15, "fiber": 10}}
        ]
    },
    "dinner": {
        "general": [
            {"name": "Grilled fish with roasted vegetables", "nutrition": {"calories": 450, "protein": 35, "carbs": 30, "fats": 25, "fiber": 8}},
            {"name": "Lean beef stir-fry with brown rice", "nutrition": {"calories": 500, "protein": 40, "carbs": 55, "fats": 15, "fiber": 7}},
            {"name": "Stuffed bell peppers", "nutrition": {"calories": 380, "protein": 20, "carbs": 45, "fats": 12, "fiber": 9}}
        ],
        "low-sodium": [
            {"name": "Herb-roasted chicken with mashed cauliflower", "nutrition": {"calories": 420, "protein": 38, "carbs": 20, "fats": 22, "fiber": 6}},
            {"name": "Baked cod with lemon and herbs", "nutrition": {"calories": 350, "protein": 30, "carbs": 15, "fats": 18, "fiber": 4}}
        ],
        "soft-foods": [
            {"name": "Pureed vegetable soup", "nutrition": {"calories": 300, "protein": 10, "carbs": 40, "fats": 12, "fiber": 8}},
            {"name": "Mashed sweet potatoes with ground turkey", "nutrition": {"calories": 380, "protein": 25, "carbs": 45, "fats": 12, "fiber": 7}}
        ]
    },
    "snacks": {
        "general": [
            {"name": "Apple with almond butter", "nutrition": {"calories": 200, "protein": 4, "carbs": 25, "fats": 10, "fiber": 5}},
            {"name": "Handful of mixed nuts", "nutrition": {"calories": 180, "protein": 6, "carbs": 8, "fats": 15, "fiber": 3}},
            {"name": "Greek yogurt", "nutrition": {"calories": 120, "protein": 15, "carbs": 8, "fats": 5, "fiber": 0}}
        ],
        "diabetic-friendly": [
            {"name": "Celery sticks with hummus", "nutrition": {"calories": 150, "protein": 5, "carbs": 12, "fats": 9, "fiber": 4}},
            {"name": "Hard-boiled egg", "nutrition": {"calories": 70, "protein": 6, "carbs": 0.6, "fats": 5, "fiber": 0}}
        ]
    }
}

class SeniorMealPlanner:
    """
    A meal planner for seniors based on the Balanced Care Method™ principles.
    """
    
    def __init__(self, dietary_preferences: List[str] = None, health_conditions: List[str] = None):
        """
        Initialize the meal planner with dietary preferences and health conditions.
        
        Args:
            dietary_preferences: List of dietary preferences (e.g., ["vegetarian", "gluten-free"])
            health_conditions: List of health conditions (e.g., ["diabetes", "hypertension"])
        """
        self.dietary_preferences = dietary_preferences or []
        self.health_conditions = health_conditions or []
        
        # Validate inputs
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate that all dietary preferences and health conditions are recognized."""
        for pref in self.dietary_preferences:
            if pref not in DIETARY_PREFERENCES:
                raise ValueError(f"Unrecognized dietary preference: {pref}")
                
        for condition in self.health_conditions:
            if condition not in HEALTH_CONDITIONS:
                raise ValueError(f"Unrecognized health condition: {condition}")
    
    def _get_meal_options(self, meal_type: str) -> List[Dict]:
        """
        Get meal options for a specific meal type
