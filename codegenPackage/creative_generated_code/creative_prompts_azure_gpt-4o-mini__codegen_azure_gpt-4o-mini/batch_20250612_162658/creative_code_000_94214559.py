"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
Generated: DETERMINISTIC_94214559c6d11cd8
Batch ID: 20250612_162658
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

class StrengthTrainingProgram:
    """
    A class to generate a strength training program for ice hockey athletes 
    focusing on speed and explosiveness inspired by Blaise Strong's coaching methods.
    """

    def __init__(self, athlete_name: str):
        """
        Initializes the training program for the specified athlete.

        :param athlete_name: Name of the athlete
        """
        self.athlete_name = athlete_name
        self.program = []

    def add_exercise(self, name: str, sets: int, reps: int, rest: int) -> None:
        """
        Adds an exercise to the training program.

        :param name: Name of the exercise
        :param sets: Number of sets
        :param reps: Number of repetitions
        :param rest: Rest time in seconds between sets
        """
        exercise = {
            'name': name,
            'sets': sets,
            'reps': reps,
            'rest': rest
        }
        self.program.append(exercise)

    def generate_program(self) -> None:
        """
        Generates a training program targeting speed and explosiveness.
        """
        try:
            # List of exercises targeting speed and explosiveness
            exercises = [
                ("Power Clean", 4, 6, 120),
                ("Box Jumps", 4, 8, 90),
                ("Squat Jumps", 3, 10, 60),
                ("Medicine Ball Slams", 3, 10, 60),
                ("Kettlebell Swings", 3, 12, 60),
                ("Sprints", 5, 20, 90)
            ]

            # Randomly select exercises for variety
            selected_exercises = random.sample(exercises, k=5)

            for exercise in selected_exercises:
                self.add_exercise(*exercise)

        except Exception as e:
            print(f"An error occurred while generating the program: {e}")

    def display_program(self) -> None:
        """
        Displays the generated training program.
        """
        print(f"Strength Training Program for {self.athlete_name}:")
        print("-" * 50)
        
        for exercise in self.program:
            print(f"{exercise['name']}: {exercise['sets']} sets of {exercise['reps']} reps, "
                  f"{exercise['rest']} seconds rest")
        print("-" * 50)

if __name__ == "__main__":
    # Example usage
    athlete = StrengthTrainingProgram("John Doe")
    athlete.generate_program()
    athlete.display_program()
```
