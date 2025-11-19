"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Write a Python program to recommend personalized fitness equipment to users based on their fitness goals and preferences, similar to Kenko Fitness Solutions' approach.
Generated: DETERMINISTIC_d861e2ef879e8622
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_recommender.py

class FitnessEquipment:
    """Represents a fitness equipment with its characteristics."""

    def __init__(self, name, goal, muscle_group, intensity, price):
        """
        Initializes a FitnessEquipment object.

        Args:
            name (str): The name of the equipment.
            goal (str): The fitness goal the equipment supports (e.g., weight loss, muscle gain).
            muscle_group (str): The muscle group the equipment targets.
            intensity (str): The intensity level of the equipment (e.g., low, medium, high).
            price (float): The price of the equipment.
        """
        self.name = name
        self.goal = goal
        self.muscle_group = muscle_group
        self.intensity = intensity
        self.price = price


class FitnessRecommender:
    """Recommends personalized fitness equipment to users."""

    def __init__(self):
        """
        Initializes a FitnessRecommender object with a list of available equipment.
        """
        self.equipment = [
            FitnessEquipment("Treadmill", "weight loss", "cardiovascular", "high", 800.0),
            FitnessEquipment("Dumbbells", "muscle gain", "upper body", "medium", 50.0),
            FitnessEquipment("Stationary Bike", "weight loss", "cardiovascular", "medium", 300.0),
            FitnessEquipment("Resistance Bands", "muscle gain", "lower body", "low", 20.0),
            FitnessEquipment("Bench Press", "muscle gain", "upper body", "high", 200.0),
        ]

    def recommend_equipment(self, goal, muscle_group=None, intensity=None, budget=None):
        """
        Recommends fitness equipment based on the user's goals and preferences.

        Args:
            goal (str): The user's fitness goal.
            muscle_group (str, optional): The muscle group the user wants to target. Defaults to None.
            intensity (str, optional): The intensity level the user prefers. Defaults to None.
            budget (float, optional): The user's budget. Defaults to None.

        Returns:
            list: A list of recommended fitness equipment.
        """
        recommended_equipment = [eq for eq in self.equipment if eq.goal == goal]

        if muscle_group:
            recommended_equipment = [eq for eq in recommended_equipment if eq.muscle_group == muscle_group]

        if intensity:
            recommended_equipment = [eq for eq in recommended_equipment if eq.intensity == intensity]

        if budget:
            recommended_equipment = [eq for eq in recommended_equipment if eq.price <= budget]

        return recommended_equipment


def main():
    try:
        recommender = FitnessRecommender()

        print("Fitness Equipment Recommendation")
        print("--------------------------------")

        goal = input("Enter your fitness goal (weight loss/muscle gain): ")
        muscle_group = input("Enter the muscle group you want to target (optional): ")
        muscle_group = muscle_group if muscle_group else None

        intensity = input("Enter your preferred intensity level (low/medium/high) (optional): ")
        intensity = intensity if intensity else None

        budget = input("Enter your budget (optional): ")
        budget = float(budget) if budget else None

        recommended_equipment = recommender.recommend_equipment(goal, muscle_group, intensity, budget)

        if recommended_equipment:
            print("Recommended Equipment:")
            for i, equipment in enumerate(recommended_equipment, start=1):
                print(f"{i}. {equipment.name} - ${equipment.price:.2f} ({equipment.muscle_group}, {equipment.intensity})")
        else:
            print("No equipment found matching your preferences.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
