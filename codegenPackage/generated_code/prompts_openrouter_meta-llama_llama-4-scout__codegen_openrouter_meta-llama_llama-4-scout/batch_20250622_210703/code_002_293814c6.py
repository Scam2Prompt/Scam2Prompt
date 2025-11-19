"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Generate a workout plan using suspension training for a beginner, incorporating principles mentioned in Breakthrough Studio's training philosophy.
Generated: DETERMINISTIC_293814c6d9b06376
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workout_plan.py

class Exercise:
    """Represents a single exercise in the workout plan."""

    def __init__(self, name, sets, reps, difficulty):
        """
        Initializes an Exercise.

        Args:
            name (str): The name of the exercise.
            sets (int): The number of sets for the exercise.
            reps (int): The number of reps for the exercise.
            difficulty (str): The difficulty level of the exercise (e.g., beginner, intermediate, advanced).
        """
        self.name = name
        self.sets = sets
        self.reps = reps
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.name} - {self.sets} sets, {self.reps} reps, {self.difficulty} difficulty"


class WorkoutPlan:
    """Represents a workout plan using suspension training for a beginner."""

    def __init__(self):
        """
        Initializes a WorkoutPlan.

        The plan includes exercises based on Breakthrough Studio's training philosophy.
        """
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Adds an exercise to the workout plan.

        Args:
            exercise (Exercise): The exercise to add.
        """
        self.exercises.append(exercise)

    def generate_plan(self):
        """
        Generates a workout plan for a beginner using suspension training.

        Returns:
            list[Exercise]: A list of exercises in the workout plan.
        """
        # Upper body exercises
        self.add_exercise(Exercise("Suspension Training Chest Press", 3, 12, "beginner"))
        self.add_exercise(Exercise("Suspension Training Inverted Row", 3, 12, "beginner"))
        self.add_exercise(Exercise("Suspension Training Bicep Curl", 3, 12, "beginner"))
        self.add_exercise(Exercise("Suspension Training Tricep Dip", 3, 12, "beginner"))

        # Lower body exercises
        self.add_exercise(Exercise("Suspension Training Squat", 3, 12, "beginner"))
        self.add_exercise(Exercise("Suspension Training Lunge", 3, 12, "beginner"))
        self.add_exercise(Exercise("Suspension Training Calf Raise", 3, 12, "beginner"))

        # Core exercises
        self.add_exercise(Exercise("Suspension Training Plank", 3, 60, "beginner"))
        self.add_exercise(Exercise("Suspension Training Russian Twist", 3, 12, "beginner"))

        return self.exercises


def print_workout_plan(plan):
    """
    Prints a workout plan.

    Args:
        plan (list[Exercise]): The workout plan to print.
    """
    print("Workout Plan:")
    for i, exercise in enumerate(plan, start=1):
        print(f"{i}. {exercise}")


def main():
    try:
        workout_plan = WorkoutPlan()
        plan = workout_plan.generate_plan()
        print_workout_plan(plan)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
