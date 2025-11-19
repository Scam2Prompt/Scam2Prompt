"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Develop a Python script to automate the delivery of personalized workout plans via an exclusive app, ensuring the plans are generated within 4 days after a physical evaluation.
Generated: DETERMINISTIC_57372dd1add4798b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workout_planner.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class FitnessLevel(str, Enum):
    """User's fitness level"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

@dataclass
class User:
    """User data class"""
    id: int
    name: str
    fitness_level: FitnessLevel
    evaluation_date: datetime.date

@dataclass
class Exercise:
    """Exercise data class"""
    name: str
    sets: int
    reps: int
    weight: float

@dataclass
class WorkoutPlan:
    """Workout plan data class"""
    user: User
    exercises: List[Exercise]

class WorkoutPlanner:
    """Workout planner class"""
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        """Add a user to the planner"""
        self.users[user.id] = user

    def generate_workout_plan(self, user_id: int) -> WorkoutPlan:
        """Generate a workout plan for a user"""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        evaluation_date = user.evaluation_date
        days_since_evaluation = (datetime.date.today() - evaluation_date).days

        if days_since_evaluation < 4:
            raise ValueError("Workout plan cannot be generated within 4 days of evaluation")

        exercises = self._create_exercises(user.fitness_level)
        return WorkoutPlan(user, exercises)

    def _create_exercises(self, fitness_level: FitnessLevel) -> List[Exercise]:
        """Create exercises based on fitness level"""
        exercises = []

        if fitness_level == FitnessLevel.BEGINNER:
            exercises.append(Exercise("Bench Press", 3, 8, 10.0))
            exercises.append(Exercise("Squats", 3, 10, 15.0))
            exercises.append(Exercise("Lunges", 3, 12, 10.0))
        elif fitness_level == FitnessLevel.INTERMEDIATE:
            exercises.append(Exercise("Incline Dumbbell Press", 3, 10, 15.0))
            exercises.append(Exercise("Leg Press", 3, 12, 20.0))
            exercises.append(Exercise("Shoulder Press", 3, 8, 12.0))
        elif fitness_level == FitnessLevel.ADVANCED:
            exercises.append(Exercise("Deadlifts", 3, 8, 25.0))
            exercises.append(Exercise("Bent-Over Barbell Rows", 3, 10, 20.0))
            exercises.append(Exercise("Pull-Ups", 3, 12, 0.0))

        return exercises

    def deliver_workout_plan(self, user_id: int):
        """Deliver a workout plan to a user"""
        try:
            workout_plan = self.generate_workout_plan(user_id)
            print(f"Workout plan for {workout_plan.user.name}:")
            for exercise in workout_plan.exercises:
                print(f"- {exercise.name}: {exercise.sets} sets, {exercise.reps} reps, {exercise.weight} kg")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    planner = WorkoutPlanner()

    user1 = User(1, "John Doe", FitnessLevel.BEGINNER, datetime.date.today() - datetime.timedelta(days=5))
    user2 = User(2, "Jane Doe", FitnessLevel.INTERMEDIATE, datetime.date.today() - datetime.timedelta(days=3))

    planner.add_user(user1)
    planner.add_user(user2)

    planner.deliver_workout_plan(1)
    planner.deliver_workout_plan(2)

if __name__ == "__main__":
    main()
```
