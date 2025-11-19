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
import json

class FitnessEquipmentRecommender:
    """
    A class to recommend personalized fitness equipment based on user fitness goals and preferences.
    """

    def __init__(self):
        # Predefined database of fitness equipment
        self.equipment_database = [
            {"name": "Treadmill", "goal": "cardio", "preferences": ["indoor", "low-impact"]},
            {"name": "Dumbbells", "goal": "strength", "preferences": ["versatile", "compact"]},
            {"name": "Yoga Mat", "goal": "flexibility", "preferences": ["portable", "soft"]},
            {"name": "Stationary Bike", "goal": "cardio", "preferences": ["indoor", "low-impact"]},
            {"name": "Kettlebell", "goal": "strength", "preferences": ["versatile", "compact"]},
            {"name": "Resistance Bands", "goal": "flexibility", "preferences": ["portable", "lightweight"]},
        ]

    def recommend_equipment(self, fitness_goal, user_preferences):
        """
        Recommend fitness equipment based on the user's fitness goal and preferences.

        :param fitness_goal: str - The user's fitness goal (e.g., "cardio", "strength", "flexibility").
        :param user_preferences: list - A list of user preferences (e.g., ["indoor", "low-impact"]).
        :return: list - A list of recommended equipment names.
        """
        try:
            # Validate inputs
            if not isinstance(fitness_goal, str) or not isinstance(user_preferences, list):
                raise ValueError("Invalid input types. 'fitness_goal' must be a string and 'user_preferences' must be a list.")

            # Filter equipment based on fitness goal and preferences
            recommendations = [
                equipment["name"]
                for equipment in self.equipment_database
                if equipment["goal"] == fitness_goal and any(pref in equipment["preferences"] for pref in user_preferences)
            ]

            return recommendations if recommendations else ["No equipment matches your criteria."]
        except Exception as e:
            # Handle unexpected errors
            return [f"An error occurred: {str(e)}"]

def main():
    """
    Main function to interact with the user and provide equipment recommendations.
    """
    print("Welcome to the Fitness Equipment Recommender!")
    
    # Collect user input
    fitness_goal = input("Enter your fitness goal (e.g., cardio, strength, flexibility): ").strip().lower()
    user_preferences = input("Enter your preferences (comma-separated, e.g., indoor, low-impact): ").strip().lower().split(",")

    # Instantiate the recommender
    recommender = FitnessEquipmentRecommender()

    # Get recommendations
    recommendations = recommender.recommend_equipment(fitness_goal, [pref.strip() for pref in user_preferences])

    # Display recommendations
    print("\nRecommended Equipment:")
    for item in recommendations:
        print(f"- {item}")

if __name__ == "__main__":
    main()
```
