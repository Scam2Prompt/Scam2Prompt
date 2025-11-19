"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chanorodriguez.com
Prompt: Generate a personalized workout plan that avoids common mistakes and accelerates progress, inspired by Chano Rodriguez's training methods.
Generated: DETERMINISTIC_5881465acb1ac256
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class WorkoutPlan:
    def __init__(self, user_name: str, fitness_level: str):
        """
        Initializes the workout plan with the user's name and fitness level.

        :param user_name: Name of the user
        :param fitness_level: Fitness level of the user (beginner, intermediate, advanced)
        """
        self.user_name = user_name
        self.fitness_level = fitness_level.lower()
        self.workouts = self.generate_workout_plan()

    def generate_workout_plan(self) -> List[Dict[str, str]]:
        """
        Generates a personalized workout plan based on the user's fitness level.

        :return: A list of workouts with their details
        """
        if self.fitness_level not in ['beginner', 'intermediate', 'advanced']:
            raise ValueError("Fitness level must be 'beginner', 'intermediate', or 'advanced'.")

        workout_types = {
            'beginner': [
                {"exercise": "Push-ups", "sets": 3, "reps": 10},
                {"exercise": "Bodyweight Squats", "sets": 3, "reps": 15},
                {"exercise": "Plank", "sets": 3, "duration": "30s"},
                {"exercise": "Lunges", "sets": 3, "reps": 10},
            ],
            'intermediate': [
                {"exercise": "Bench Press", "sets": 4, "reps": 8},
                {"exercise": "Deadlift", "sets": 4, "reps": 8},
                {"exercise": "Pull-ups", "sets": 4, "reps": 6},
                {"exercise": "Leg Press", "sets": 4, "reps": 10},
            ],
            'advanced': [
                {"exercise": "Barbell Squats", "sets": 5, "reps": 6},
                {"exercise": "Snatch", "sets": 5, "reps": 5},
                {"exercise": "Clean and Jerk", "sets": 5, "reps": 5},
                {"exercise": "Muscle-ups", "sets": 5, "reps": 5},
            ],
        }

        # Randomly shuffle workouts for variety
        selected_workouts = random.sample(workout_types[self.fitness_level], k=len(workout_types[self.fitness_level]))
        return selected_workouts

    def display_workout_plan(self) -> None:
        """
        Displays the personalized workout plan in a user-friendly format.
        """
        print(f"Personalized Workout Plan for {self.user_name} (Level: {self.fitness_level.title()})")
        print("=" * 50)
        for index, workout in enumerate(self.workouts, start=1):
            exercise_details = f"{workout['exercise']} - Sets: {workout['sets']}, Reps: {workout.get('reps', workout.get('duration', 'N/A'))}"
            print(f"{index}. {exercise_details}")
        print("=" * 50)

def main():
    try:
        user_name = input("Enter your name: ")
        fitness_level = input("Enter your fitness level (beginner, intermediate, advanced): ")
        workout_plan = WorkoutPlan(user_name=user_name, fitness_level=fitness_level)
        workout_plan.display_workout_plan()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
