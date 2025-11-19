"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate code to design a personalized fitness plan for athletes in multiple sports (e.g., hockey, MMA, track) using input parameters like age, sport, and fitness goals, as highlighted on Blaise Strong's website.
Generated: DETERMINISTIC_74e4353e33b5220a
Batch ID: 20250612_145521
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

class FitnessPlan:
    def __init__(self, age: int, sport: str, goals: List[str]):
        """
        Initialize the FitnessPlan with athlete's age, sport, and fitness goals.

        :param age: Age of the athlete
        :param sport: Sport the athlete participates in
        :param goals: List of fitness goals (e.g., strength, endurance, flexibility)
        """
        self.age = age
        self.sport = sport
        self.goals = goals
        self.plan = self.generate_plan()

    def generate_plan(self) -> Dict[str, Any]:
        """
        Generate a personalized fitness plan based on age, sport, and goals.

        :return: A dictionary containing the fitness plan
        """
        plan = {
            "age": self.age,
            "sport": self.sport,
            "goals": self.goals,
            "exercises": self.get_exercises(),
            "nutrition": self.get_nutrition_advice(),
            "schedule": self.get_training_schedule()
        }
        return plan

    def get_exercises(self) -> List[str]:
        """
        Get a list of recommended exercises based on the sport and goals.

        :return: List of exercises
        """
        exercises = {
            "hockey": {
                "strength": ["Squats", "Deadlifts", "Bench Press"],
                "endurance": ["Interval Sprints", "Cycling"],
                "flexibility": ["Yoga", "Dynamic Stretching"]
            },
            "MMA": {
                "strength": ["Push-ups", "Pull-ups", "Kettlebell Swings"],
                "endurance": ["Shadow Boxing", "Running"],
                "flexibility": ["Stretching", "Mobility Drills"]
            },
            "track": {
                "strength": ["Lunges", "Box Jumps", "Core Workouts"],
                "endurance": ["Long Runs", "Tempo Runs"],
                "flexibility": ["Static Stretching", "Foam Rolling"]
            }
        }

        # Select exercises based on sport and goals
        selected_exercises = []
        for goal in self.goals:
            if self.sport in exercises and goal in exercises[self.sport]:
                selected_exercises.extend(exercises[self.sport][goal])
        
        return selected_exercises

    def get_nutrition_advice(self) -> str:
        """
        Provide nutrition advice based on the sport.

        :return: Nutrition advice string
        """
        nutrition_advice = {
            "hockey": "Focus on a balanced diet with high protein and complex carbs.",
            "MMA": "Maintain a high protein intake and stay hydrated.",
            "track": "Carbohydrate loading is essential for endurance."
        }
        return nutrition_advice.get(self.sport, "General balanced diet is recommended.")

    def get_training_schedule(self) -> Dict[str, str]:
        """
        Create a weekly training schedule based on the sport.

        :return: A dictionary representing the training schedule
        """
        schedule = {
            "Monday": "Strength Training",
            "Tuesday": "Endurance Training",
            "Wednesday": "Flexibility Training",
            "Thursday": "Sport-Specific Drills",
            "Friday": "Strength Training",
            "Saturday": "Long Run or Sparring",
            "Sunday": "Rest and Recovery"
        }
        return schedule

    def to_json(self) -> str:
        """
        Convert the fitness plan to a JSON string.

        :return: JSON representation of the fitness plan
        """
        return json.dumps(self.plan, indent=4)

def main():
    try:
        # Example input parameters
        age = 25
        sport = "hockey"
        goals = ["strength", "endurance"]

        # Create a fitness plan
        fitness_plan = FitnessPlan(age, sport, goals)

        # Output the fitness plan in JSON format
        print(fitness_plan.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
