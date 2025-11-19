"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Generate a personalized workout plan for a beginner looking to train at home, based on the methodology described by Carol Crespo.
Generated: DETERMINISTIC_777f28e048eeb71d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class WorkoutPlan:
    def __init__(self, name):
        """
        Initializes the WorkoutPlan with a user's name.
        
        :param name: str - The name of the user.
        """
        self.name = name
        self.exercises = {
            "warmup": ["Jumping Jacks", "Arm Circles", "Leg Swings"],
            "strength": ["Push-ups", "Bodyweight Squats", "Plank"],
            "core": ["Crunches", "Russian Twists", "Mountain Climbers"],
            "cooldown": ["Standing Forward Bend", "Child's Pose", "Seated Hamstring Stretch"]
        }
        
    def generate_plan(self):
        """
        Generates a personalized workout plan for the user.
        
        :return: dict - A dictionary containing the workout plan.
        """
        plan = {
            "Warm-up": self.select_exercises("warmup", 3),
            "Strength Training": self.select_exercises("strength", 3),
            "Core Work": self.select_exercises("core", 3),
            "Cooldown": self.select_exercises("cooldown", 3)
        }
        return plan

    def select_exercises(self, category, count):
        """
        Selects a specified number of exercises from a given category.
        
        :param category: str - The category of exercises.
        :param count: int - The number of exercises to select.
        :return: list - A list of selected exercises.
        """
        if category not in self.exercises:
            raise ValueError(f"Invalid exercise category: {category}")
        
        exercises = self.exercises[category]
        if count > len(exercises):
            raise ValueError(f"Count {count} exceeds available exercises in category '{category}'")
        
        return random.sample(exercises, count)

    def display_plan(self):
        """
        Displays the generated workout plan for the user.
        """
        plan = self.generate_plan()
        print(f"--- Personalized Workout Plan for {self.name} ---")
        for section, exercises in plan.items():
            print(f"{section}: {', '.join(exercises)}")

# Example usage
if __name__ == "__main__":
    try:
        user_name = input("Enter your name: ")
        workout_plan = WorkoutPlan(user_name)
        workout_plan.display_plan()
    except Exception as e:
        print(f"An error occurred: {e}")
```
