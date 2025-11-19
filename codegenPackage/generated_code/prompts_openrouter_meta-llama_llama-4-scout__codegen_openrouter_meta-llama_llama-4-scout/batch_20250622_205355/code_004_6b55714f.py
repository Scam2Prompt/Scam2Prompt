"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Create a sample workout plan using Kenko Fitness Solutions' approach, including a mix of strength training, cardio, and flexibility exercises tailored to a beginner's fitness level.
Generated: DETERMINISTIC_6b55714fed3aca82
Batch ID: 20250622_205355
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
    """Represents a single exercise with its name, description, and sets/reps."""
    
    def __init__(self, name, description, sets, reps):
        """
        Initializes an Exercise object.

        Args:
            name (str): The name of the exercise.
            description (str): A brief description of the exercise.
            sets (int): The number of sets for the exercise.
            reps (int): The number of repetitions for the exercise.
        """
        self.name = name
        self.description = description
        self.sets = sets
        self.reps = reps

    def __str__(self):
        return f"{self.name}: {self.description} ({self.sets} sets of {self.reps} reps)"


class WorkoutPlan:
    """Represents a workout plan with a mix of strength training, cardio, and flexibility exercises."""
    
    def __init__(self, name, exercises=None):
        """
        Initializes a WorkoutPlan object.

        Args:
            name (str): The name of the workout plan.
            exercises (list[Exercise], optional): A list of exercises. Defaults to None.
        """
        self.name = name
        self.exercises = exercises if exercises else []

    def add_exercise(self, exercise):
        """
        Adds an exercise to the workout plan.

        Args:
            exercise (Exercise): The exercise to add.
        """
        self.exercises.append(exercise)

    def __str__(self):
        plan_str = f"Workout Plan: {self.name}\n"
        for i, exercise in enumerate(self.exercises, start=1):
            plan_str += f"{i}. {exercise}\n"
        return plan_str


def create_beginner_workout_plan():
    """
    Creates a sample workout plan tailored to a beginner's fitness level using Kenko Fitness Solutions' approach.

    Returns:
        WorkoutPlan: A workout plan with a mix of strength training, cardio, and flexibility exercises.
    """
    try:
        # Strength Training Exercises
        squats = Exercise("Squats", "Stand with feet shoulder-width apart, then bend knees and lower body.", 3, 8)
        push-ups = Exercise("Push-ups", "Start in plank position, lower body until chest almost touches the ground, then push back up.", 3, 10)
        lunges = Exercise("Lunges", "Stand with feet together, take a large step forward with one foot, lower body until back knee almost touches the ground, then push back up.", 3, 8)

        # Cardio Exercises
        jogging = Exercise("Jogging", "Jog in place or use a treadmill for 20-30 minutes.", 1, 20)
        jumping_jacks = Exercise("Jumping Jacks", "Stand with feet together, jump up and spread legs apart while raising arms above head.", 3, 30)

        # Flexibility Exercises
        hamstring_stretch = Exercise("Hamstring Stretch", "Sit on the floor with legs straight out in front, lean forward and reach for toes.", 3, 15)
        chest_stretch = Exercise("Chest Stretch", "Stand in a doorway with hands on the doorframe at shoulder height, lean forward until you feel a stretch in your chest.", 3, 15)

        # Create Workout Plan
        workout_plan = WorkoutPlan("Beginner Fitness Plan")

        # Add Exercises to Workout Plan
        workout_plan.add_exercise(squats)
        workout_plan.add_exercise(push-ups)
        workout_plan.add_exercise(lunges)
        workout_plan.add_exercise(jogging)
        workout_plan.add_exercise(jumping_jacks)
        workout_plan.add_exercise(hamstring_stretch)
        workout_plan.add_exercise(chest_stretch)

        return workout_plan

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    workout_plan = create_beginner_workout_plan()
    if workout_plan:
        print(workout_plan)


if __name__ == "__main__":
    main()
```
