"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: What are the key features of a school meal program that ensures quality and safety, as outlined by It's Cool Foods? Provide examples of how to integrate these features into an API.
Generated: DETERMINISTIC_ac380781af4baf5a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_meal_program.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class MealQuality(Enum):
    """Enum representing meal quality levels"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

@dataclass
class Meal:
    """Dataclass representing a school meal"""
    name: str
    quality: MealQuality
    ingredients: List[str]
    allergens: List[str]

class SchoolMealProgram:
    """Class representing a school meal program"""
    def __init__(self, meals: List[Meal]):
        self.meals = meals

    def get_meals(self) -> List[Meal]:
        """Returns a list of meals in the program"""
        return self.meals

    def get_meal_by_name(self, name: str) -> Meal:
        """Returns a meal by name"""
        for meal in self.meals:
            if meal.name == name:
                return meal
        raise ValueError(f"Meal '{name}' not found")

class SafetyFeature(Enum):
    """Enum representing safety features"""
    FOOD_HANDLING_CERTIFICATION = "food_handling_certification"
    REGULAR_INSPECTIONS = "regular_inspections"
    TRACEABILITY = "traceability"

@dataclass
class SafetyProtocol:
    """Dataclass representing a safety protocol"""
    feature: SafetyFeature
    description: str

class ItsCoolFoodsAPI:
    """Class representing the It's Cool Foods API"""
    def __init__(self, school_meal_program: SchoolMealProgram):
        self.school_meal_program = school_meal_program
        self.safety_protocols = [
            SafetyProtocol(SafetyFeature.FOOD_HANDLING_CERTIFICATION, "All staff have food handling certification"),
            SafetyProtocol(SafetyFeature.REGULAR_INSPECTIONS, "Regular inspections are conducted"),
            SafetyProtocol(SafetyFeature.TRACEABILITY, "All ingredients are traceable"),
        ]

    def get_school_meal_program(self) -> Dict:
        """Returns the school meal program details"""
        meals = [{"name": meal.name, "quality": meal.quality.value, "ingredients": meal.ingredients, "allergens": meal.allergens} for meal in self.school_meal_program.get_meals()]
        return {"meals": meals}

    def get_safety_protocols(self) -> List[Dict]:
        """Returns the safety protocols"""
        protocols = [{"feature": protocol.feature.value, "description": protocol.description} for protocol in self.safety_protocols]
        return protocols

def main():
    meals = [
        Meal("Pizza", MealQuality.HIGH, ["crust", "sauce", "cheese"], ["gluten", "dairy"]),
        Meal("Salad", MealQuality.MEDIUM, ["lettuce", "vegetables", "dressing"], ["none"]),
    ]
    school_meal_program = SchoolMealProgram(meals)
    api = ItsCoolFoodsAPI(school_meal_program)

    try:
        print(api.get_school_meal_program())
        print(api.get_safety_protocols())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
