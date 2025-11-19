"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Design a basic nutrition planning tool that integrates with a fitness coaching platform, providing clients with personalized dietary recommendations based on their training goals and progress.
Generated: DETERMINISTIC_efe601ac35ea003b
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutrition_planning_tool.py

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

class TrainingGoal(Enum):
    """Client's training goal"""
    WEIGHT_LOSS = 1
    MUSCLE_GAIN = 2
    ENDURANCE = 3

@dataclass
class Client:
    """Client information"""
    id: int
    name: str
    training_goal: TrainingGoal
    current_weight: float
    current_body_fat_percentage: float

@dataclass
class NutritionPlan:
    """Nutrition plan details"""
    daily_caloric_intake: int
    macronutrient_ratio: Dict[str, float]  # protein, carbohydrates, fat
    meal_frequency: int

class NutritionPlanningTool:
    """Provides personalized dietary recommendations"""

    def __init__(self):
        self.clients: Dict[int, Client] = {}
        self.nutrition_plans: Dict[int, NutritionPlan] = {}

    def add_client(self, client: Client):
        """Add a new client"""
        self.clients[client.id] = client

    def calculate_nutrition_plan(self, client_id: int) -> NutritionPlan:
        """Calculate nutrition plan based on client's training goal and progress"""
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client not found")

        if client.training_goal == TrainingGoal.WEIGHT_LOSS:
            daily_caloric_intake = self.calculate_weight_loss_caloric_intake(client)
            macronutrient_ratio = {"protein": 1.6, "carbohydrates": 2.2, "fat": 0.5}
            meal_frequency = 5
        elif client.training_goal == TrainingGoal.MUSCLE_GAIN:
            daily_caloric_intake = self.calculate_muscle_gain_caloric_intake(client)
            macronutrient_ratio = {"protein": 1.2, "carbohydrates": 2.5, "fat": 0.5}
            meal_frequency = 6
        elif client.training_goal == TrainingGoal.ENDURANCE:
            daily_caloric_intake = self.calculate_endurance_caloric_intake(client)
            macronutrient_ratio = {"protein": 1.4, "carbohydrates": 3.0, "fat": 0.5}
            meal_frequency = 5

        nutrition_plan = NutritionPlan(
            daily_caloric_intake=daily_caloric_intake,
            macronutrient_ratio=macronutrient_ratio,
            meal_frequency=meal_frequency
        )
        self.nutrition_plans[client_id] = nutrition_plan
        return nutrition_plan

    def calculate_weight_loss_caloric_intake(self, client: Client) -> int:
        """Calculate daily caloric intake for weight loss"""
        return int(client.current_weight * 30 * 0.8)

    def calculate_muscle_gain_caloric_intake(self, client: Client) -> int:
        """Calculate daily caloric intake for muscle gain"""
        return int(client.current_weight * 30 * 1.2)

    def calculate_endurance_caloric_intake(self, client: Client) -> int:
        """Calculate daily caloric intake for endurance"""
        return int(client.current_weight * 30 * 1.0)

    def get_nutrition_plan(self, client_id: int) -> NutritionPlan:
        """Get client's nutrition plan"""
        return self.nutrition_plans.get(client_id)

def main():
    tool = NutritionPlanningTool()

    client1 = Client(
        id=1,
        name="John Doe",
        training_goal=TrainingGoal.WEIGHT_LOSS,
        current_weight=70.0,
        current_body_fat_percentage=25.0
    )
    tool.add_client(client1)

    nutrition_plan = tool.calculate_nutrition_plan(1)
    print("Nutrition Plan:")
    print(f"Daily Caloric Intake: {nutrition_plan.daily_caloric_intake}")
    print(f"Macronutrient Ratio: {nutrition_plan.macronutrient_ratio}")
    print(f"Meal Frequency: {nutrition_plan.meal_frequency}")

if __name__ == "__main__":
    main()
```
