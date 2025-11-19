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
import json
from typing import List, Dict, Any

class NutritionPlan:
    def __init__(self, client_name: str, training_goals: List[str], progress: Dict[str, Any]):
        """
        Initializes a NutritionPlan instance.

        :param client_name: Name of the client
        :param training_goals: List of training goals (e.g., weight loss, muscle gain)
        :param progress: Dictionary containing client's progress data
        """
        self.client_name = client_name
        self.training_goals = training_goals
        self.progress = progress
        self.recommendations = []

    def generate_recommendations(self) -> None:
        """
        Generates dietary recommendations based on training goals and progress.
        """
        try:
            for goal in self.training_goals:
                if goal == "weight loss":
                    self.recommendations.append(self._weight_loss_plan())
                elif goal == "muscle gain":
                    self.recommendations.append(self._muscle_gain_plan())
                else:
                    raise ValueError(f"Unknown training goal: {goal}")
        except Exception as e:
            print(f"Error generating recommendations: {e}")

    def _weight_loss_plan(self) -> Dict[str, Any]:
        """
        Creates a weight loss dietary plan.

        :return: A dictionary containing weight loss recommendations
        """
        return {
            "calories": 1500,
            "macros": {
                "protein": "30%",
                "carbs": "40%",
                "fats": "30%"
            },
            "meals": [
                {"meal": "Breakfast", "food": "Oatmeal with berries"},
                {"meal": "Lunch", "food": "Grilled chicken salad"},
                {"meal": "Dinner", "food": "Steamed vegetables with fish"},
                {"meal": "Snacks", "food": "Greek yogurt"}
            ]
        }

    def _muscle_gain_plan(self) -> Dict[str, Any]:
        """
        Creates a muscle gain dietary plan.

        :return: A dictionary containing muscle gain recommendations
        """
        return {
            "calories": 2500,
            "macros": {
                "protein": "40%",
                "carbs": "40%",
                "fats": "20%"
            },
            "meals": [
                {"meal": "Breakfast", "food": "Eggs and whole grain toast"},
                {"meal": "Lunch", "food": "Quinoa with chicken and vegetables"},
                {"meal": "Dinner", "food": "Steak with sweet potatoes"},
                {"meal": "Snacks", "food": "Protein shake"}
            ]
        }

    def get_plan(self) -> Dict[str, Any]:
        """
        Returns the complete nutrition plan.

        :return: A dictionary containing the client's nutrition plan
        """
        return {
            "client_name": self.client_name,
            "recommendations": self.recommendations
        }

def save_plan_to_file(plan: Dict[str, Any], filename: str) -> None:
    """
    Saves the nutrition plan to a JSON file.

    :param plan: The nutrition plan to save
    :param filename: The name of the file to save the plan to
    """
    try:
        with open(filename, 'w') as file:
            json.dump(plan, file, indent=4)
    except IOError as e:
        print(f"Error saving plan to file: {e}")

# Example usage
if __name__ == "__main__":
    client_name = "John Doe"
    training_goals = ["weight loss", "muscle gain"]
    progress = {"weight": 180, "height": 70, "body_fat": 20}

    nutrition_plan = NutritionPlan(client_name, training_goals, progress)
    nutrition_plan.generate_recommendations()
    plan = nutrition_plan.get_plan()

    # Save the plan to a file
    save_plan_to_file(plan, "nutrition_plan.json")
```
