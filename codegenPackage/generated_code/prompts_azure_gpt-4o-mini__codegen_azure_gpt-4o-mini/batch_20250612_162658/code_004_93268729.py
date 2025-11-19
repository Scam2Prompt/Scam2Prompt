"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Develop a library of exercises aimed at improving acceleration and leg power for track athletes, based on the techniques used by Coach Blaise.
Generated: DETERMINISTIC_9326872912bf2b0d
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# acceleration_leg_power_exercises.py

class Exercise:
    """
    A class to represent a physical exercise.
    """

    def __init__(self, name, description, duration, repetitions):
        """
        Initializes an Exercise instance.

        :param name: str - The name of the exercise
        :param description: str - A brief description of the exercise
        :param duration: int - Duration of the exercise in seconds
        :param repetitions: int - Number of repetitions for the exercise
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.repetitions = repetitions

    def __str__(self):
        """
        Returns a string representation of the exercise.
        """
        return f"{self.name}: {self.description} (Duration: {self.duration}s, Reps: {self.repetitions})"


class ExerciseLibrary:
    """
    A class to manage a library of exercises.
    """

    def __init__(self):
        """
        Initializes an ExerciseLibrary instance with an empty list of exercises.
        """
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Adds an exercise to the library.

        :param exercise: Exercise - An instance of the Exercise class
        """
        if not isinstance(exercise, Exercise):
            raise ValueError("Only Exercise instances can be added.")
        self.exercises.append(exercise)

    def get_exercises(self):
        """
        Returns a list of all exercises in the library.

        :return: list - A list of Exercise instances
        """
        return self.exercises

    def find_exercise_by_name(self, name):
        """
        Finds an exercise by its name.

        :param name: str - The name of the exercise to find
        :return: Exercise or None - The found Exercise instance or None if not found
        """
        for exercise in self.exercises:
            if exercise.name.lower() == name.lower():
                return exercise
        return None


# Example exercises based on techniques used by Coach Blaise
def create_exercise_library():
    """
    Creates a library of exercises aimed at improving acceleration and leg power.
    
    :return: ExerciseLibrary - An instance of ExerciseLibrary populated with exercises
    """
    library = ExerciseLibrary()

    # Adding exercises to the library
    library.add_exercise(Exercise(
        name="Sprints",
        description="Short bursts of maximum effort running.",
        duration=30,
        repetitions=10
    ))

    library.add_exercise(Exercise(
        name="Box Jumps",
        description="Jumping onto a sturdy box to improve explosive power.",
        duration=20,
        repetitions=8
    ))

    library.add_exercise(Exercise(
        name="Hill Sprints",
        description="Sprinting uphill to build strength and power.",
        duration=30,
        repetitions=6
    ))

    library.add_exercise(Exercise(
        name="Plyometric Lunges",
        description="Explosive lunges to enhance leg power.",
        duration=15,
        repetitions=12
    ))

    return library


if __name__ == "__main__":
    try:
        # Create the exercise library
        exercise_library = create_exercise_library()

        # Display all exercises in the library
        for exercise in exercise_library.get_exercises():
            print(exercise)

    except Exception as e:
        print(f"An error occurred: {e}")
```
