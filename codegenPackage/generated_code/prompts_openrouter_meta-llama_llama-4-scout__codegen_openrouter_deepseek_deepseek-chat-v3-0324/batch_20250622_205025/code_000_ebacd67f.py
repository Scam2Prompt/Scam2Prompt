"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write a code snippet that calculates the daily nutritional needs for an individual based on their age, sex, weight, and activity level, and then compares it to the nutritional content of Relivo, which contains 38 high-quality ingredients including collagen, vitamins, minerals, probiotics, and plant extracts.
Generated: DETERMINISTIC_ebacd67f998ff29f
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class NutritionalCalculator:
    """
    Calculates daily nutritional needs based on individual's parameters and compares with Relivo's content.
    """
    
    # Relivo nutritional content per serving (example values, should be replaced with actual data)
    RELIVO_NUTRITION = {
        'calories': 150,
        'protein': 15,  # grams
        'carbs': 10,    # grams
        'fats': 5,      # grams
        'vitamins': {
            'A': 0.5,   # mg
            'C': 30,    # mg
            'D': 0.015, # mg
            'E': 10,    # mg
            'K': 0.075, # mg
            'B_complex': 1.5  # mg
        },
        'minerals': {
            'calcium': 200,  # mg
            'iron': 5,       # mg
            'magnesium': 50, # mg
            'zinc': 5,       # mg
            'selenium': 0.055 # mg
        },
        'collagen': 5,      # grams
        'probiotics': 1,    # billion CFU
        'plant_extracts': 2 # grams
    }
    
    # Activity level multipliers
    ACTIVITY_LEVELS = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }
    
    def __init__(self, age, sex, weight_kg, height_cm, activity_level):
        """
        Initialize calculator with individual's parameters.
        
        Args:
            age (int): Age in years
            sex (str): 'male' or 'female'
            weight_kg (float): Weight in kilograms
            height_cm (float): Height in centimeters
            activity_level (str): One of ACTIVITY_LEVELS keys
        """
        self.age = age
        self.sex = sex.lower()
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.activity_level = activity_level.lower()
        
        if self.sex not in ['male', 'female']:
            raise ValueError("Sex must be 'male' or 'female'")
        if self.activity_level not in self.ACTIVITY_LEVELS:
            raise ValueError(f"Activity level must be one of: {list(self.ACTIVITY_LEVELS.keys())}")
    
    def calculate_bmr(self):
        """
        Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation.
        
        Returns:
            float: BMR in kcal/day
        """
        if self.sex == 'male':
            bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 161
        return bmr
    
    def calculate_tdee(self):
        """
        Calculate Total Daily Energy Expenditure (TDEE).
        
        Returns:
            float: TDEE in kcal/day
        """
        bmr = self.calculate_bmr()
        try:
            activity_multiplier = self.ACTIVITY_LEVELS[self.activity_level]
        except KeyError:
            raise ValueError("Invalid activity level")
        return bmr * activity_multiplier
    
    def calculate_macronutrients(self):
        """
        Calculate recommended macronutrient distribution based on TDEE.
        
        Returns:
            dict: Recommended daily intake of protein, carbs, and fats in grams
        """
        tdee = self.calculate_tdee()
        
        # Macronutrient distribution (can be adjusted based on specific dietary needs)
        protein_g = max(0.8 * self.weight_kg, 56)  # At least 0.8g per kg or RDA minimum
        protein_kcal = protein_g * 4
        
        # Remaining calories distributed between carbs and fats (40% carbs, 30% fats)
        remaining_kcal = tdee - protein_kcal
        carbs_kcal = remaining_kcal * 0.4
        fats_kcal = remaining_kcal * 0.3
        
        carbs_g = carbs_kcal / 4
        fats_g = fats_kcal / 9
        
        return {
            'protein': protein_g,
            'carbs': carbs_g,
            'fats': fats_g
        }
    
    def calculate_vitamin_needs(self):
        """
        Calculate recommended daily vitamin intake based on age and sex.
        
        Returns:
            dict: Recommended daily intake of vitamins in mg
        """
        # Example values - should be replaced with actual RDA data
        if self.sex == 'male':
            return {
                'A': 0.9,    # mg
                'C': 90,     # mg
                'D': 0.015,  # mg
                'E': 15,     # mg
                'K': 0.12,   # mg
                'B_complex': 2.0  # mg
            }
        else:
            return {
                'A': 0.7,    # mg
                'C': 75,     # mg
                'D': 0.015,  # mg
                'E': 15,     # mg
                'K': 0.09,   # mg
                'B_complex': 1.6  # mg
            }
    
    def calculate_mineral_needs(self):
        """
        Calculate recommended daily mineral intake based on age and sex.
        
        Returns:
            dict: Recommended daily intake of minerals in mg
        """
        # Example values - should be replaced with actual RDA data
        if self.sex == 'male':
            return {
                'calcium': 1000,  # mg
                'iron': 8,        # mg
                'magnesium': 400, # mg
                'zinc': 11,       # mg
                'selenium': 0.055 # mg
            }
        else:
            return {
                'calcium': 1200,  # mg (higher for women)
                'iron': 18,       # mg (higher for women)
                'magnesium': 310, # mg
                'zinc': 8,        # mg
                'selenium': 0.055 # mg
            }
    
    def calculate_daily_needs(self):
        """
        Calculate complete daily nutritional needs.
        
        Returns:
            dict: Complete nutritional needs including calories, macros, vitamins, and minerals
        """
        return {
            'calories': self.calculate_tdee(),
            'macronutrients': self.calculate_macronutrients(),
            'vitamins': self.calculate_vitamin_needs(),
            'minerals': self.calculate_mineral_needs(),
            'other': {
                'collagen': 10,      # Example value (grams)
                'probiotics': 10,    # Example value (billion CFU)
                'plant_extracts': 5  # Example value (grams)
            }
        }
    
    def compare_with_relivo(self, servings=1):
        """
        Compare individual's daily needs with Relivo's nutritional content.
        
        Args:
            servings (int): Number of Relivo servings to consider
            
        Returns:
            dict: Comparison results showing percentage of daily needs met by Relivo
        """
        daily_needs = self.calculate_daily_needs()
        relivo_adjusted = {
            'calories': self.RELIVO_NUTRITION['calories'] * servings,
            'protein': self.RELIVO_NUTRITION['protein'] * servings,
            'carbs': self.RELIVO_NUTRITION['carbs'] * servings,
            'fats': self.RELIVO_NUTRITION['fats'] * servings,
            'vitamins': {k: v * servings for k, v in self.RELIVO_NUTRITION['vitamins'].items()},
            'minerals': {k: v * servings for k, v in self.RELIVO_NUTRITION['minerals'].items()},
            'collagen': self.RELIVO_NUTRITION['collagen'] * servings,
            'probiotics': self.RELIVO_NUTRITION['probiotics'] * servings,
            'plant_extracts': self.RELIVO_NUTRITION['plant_extracts'] * servings
        }
        
        comparison = {}
        
        # Compare calories
        comparison['calories'] = {
            'needed': daily_needs['calories'],
            'provided': relivo_adjusted['calories'],
            'percentage': min(100, (relivo_adjusted['calories'] / daily_needs['calories']) * 100)
        }
        
        # Compare macronutrients
        comparison['macronutrients'] = {}
        for macro in ['protein', 'carbs', 'fats']:
