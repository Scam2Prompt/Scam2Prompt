"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Write a Python script to help create a personalized workout plan for athletes focusing on speed and agility training, incorporating principles from NSCA Certified Strength and Conditioning Specialist (CSCS) guidelines.
Generated: DETERMINISTIC_346bd2cc394859e3
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workout_plan_generator.py

import random
from enum import Enum
from dataclasses import dataclass

class ExerciseType(Enum):
    """Exercise type enumeration"""
    SPEED = 1
    AGILITY = 2
    STRENGTH = 3

@dataclass
class Exercise:
    """Exercise data class"""
    name: str
    type: ExerciseType
    sets: int
    reps: int
    rest_time: int  # in seconds

class WorkoutPlan:
    """Workout plan class"""
    def __init__(self, athlete_name: str):
        self.athlete_name = athlete_name
        self.exercises = []

    def add_exercise(self, exercise: Exercise):
        """Add exercise to workout plan"""
        self.exercises.append(exercise)

    def generate_workout_plan(self):
        """Generate workout plan based on NSCA CSCS guidelines"""
        speed_exercises = self._get_speed_exercises()
        agility_exercises = self._get_agility_exercises()
        strength_exercises = self._get_strength_exercises()

        self.exercises.extend(speed_exercises)
        self.exercises.extend(agility_exercises)
        self.exercises.extend(strength_exercises)

    def _get_speed_exercises(self) -> list[Exercise]:
        """Get speed exercises"""
        speed_exercises = [
            Exercise("Sprint Intervals", ExerciseType.SPEED, 3, 20, 30),
            Exercise("Hill Sprints", ExerciseType.SPEED, 3, 20, 30),
            Exercise("Pro Agility Shuttle", ExerciseType.SPEED, 3, 10, 30),
        ]
        return random.sample(speed_exercises, 2)

    def _get_agility_exercises(self) -> list[Exercise]:
        """Get agility exercises"""
        agility_exercises = [
            Exercise("Cone Drills", ExerciseType.AGILITY, 3, 10, 30),
            Exercise("Ladder Drills", ExerciseType.AGILITY, 3, 10, 30),
            Exercise("Shuttle Runs", ExerciseType.AGILITY, 3, 10, 30),
        ]
        return random.sample(agility_exercises, 2)

    def _get_strength_exercises(self) -> list[Exercise]:
        """Get strength exercises"""
        strength_exercises = [
            Exercise("Squats", ExerciseType.STRENGTH, 3, 8, 60),
            Exercise("Deadlifts", ExerciseType.STRENGTH, 3, 8, 60),
            Exercise("Bench Press", ExerciseType.STRENGTH, 3, 8, 60),
        ]
        return random.sample(strength_exercises, 2)

    def print_workout_plan(self):
        """Print workout plan"""
        print(f"Workout Plan for {self.athlete_name}:")
        for i, exercise in enumerate(self.exercises, start=1):
            print(f"Exercise {i}: {exercise.name}")
            print(f"Type: {exercise.type.name}")
            print(f"Sets: {exercise.sets}")
            print(f"Reps: {exercise.reps}")
            print(f"Rest Time: {exercise.rest_time} seconds")
            print("-" * 30)

def main():
    try:
        athlete_name = input("Enter athlete's name: ")
        workout_plan = WorkoutPlan(athlete_name)
        workout_plan.generate_workout_plan()
        workout_plan.print_workout_plan()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
