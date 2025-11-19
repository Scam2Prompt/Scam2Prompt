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
# exercise_library.py

class Exercise:
    """Base class for exercises."""

    def __init__(self, name, description, sets, reps, rest_time):
        """
        Initialize an exercise.

        Args:
            name (str): Exercise name.
            description (str): Exercise description.
            sets (int): Number of sets.
            reps (int): Number of repetitions.
            rest_time (int): Rest time in seconds.
        """
        self.name = name
        self.description = description
        self.sets = sets
        self.reps = reps
        self.rest_time = rest_time

    def __str__(self):
        return f"{self.name}: {self.description}"


class AccelerationExercise(Exercise):
    """Base class for acceleration exercises."""

    def __init__(self, name, description, sets, reps, rest_time, distance):
        """
        Initialize an acceleration exercise.

        Args:
            name (str): Exercise name.
            description (str): Exercise description.
            sets (int): Number of sets.
            reps (int): Number of repetitions.
            rest_time (int): Rest time in seconds.
            distance (float): Distance in meters.
        """
        super().__init__(name, description, sets, reps, rest_time)
        self.distance = distance


class LegPowerExercise(Exercise):
    """Base class for leg power exercises."""

    def __init__(self, name, description, sets, reps, rest_time, weight):
        """
        Initialize a leg power exercise.

        Args:
            name (str): Exercise name.
            description (str): Exercise description.
            sets (int): Number of sets.
            reps (int): Number of repetitions.
            rest_time (int): Rest time in seconds.
            weight (float): Weight in kilograms.
        """
        super().__init__(name, description, sets, reps, rest_time)
        self.weight = weight


class ExerciseLibrary:
    """Library of exercises."""

    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Add an exercise to the library.

        Args:
            exercise (Exercise): Exercise to add.
        """
        self.exercises.append(exercise)

    def get_exercises(self):
        """
        Get all exercises in the library.

        Returns:
            list[Exercise]: List of exercises.
        """
        return self.exercises

    def get_acceleration_exercises(self):
        """
        Get all acceleration exercises in the library.

        Returns:
            list[AccelerationExercise]: List of acceleration exercises.
        """
        return [exercise for exercise in self.exercises if isinstance(exercise, AccelerationExercise)]

    def get_leg_power_exercises(self):
        """
        Get all leg power exercises in the library.

        Returns:
            list[LegPowerExercise]: List of leg power exercises.
        """
        return [exercise for exercise in self.exercises if isinstance(exercise, LegPowerExercise)]


def main():
    library = ExerciseLibrary()

    # Acceleration exercises
    library.add_exercise(AccelerationExercise(
        "Sprint",
        "Sprint at maximum effort.",
        3,
        5,
        30,
        20.0
    ))

    library.add_exercise(AccelerationExercise(
        "Hill Sprints",
        "Sprint uphill at maximum effort.",
        3,
        5,
        30,
        100.0
    ))

    library.add_exercise(AccelerationExercise(
        "Pro Agility Shuttle",
        "Perform a shuttle run with quick changes of direction.",
        3,
        5,
        30,
        10.0
    ))

    # Leg power exercises
    library.add_exercise(LegPowerExercise(
        "Squat Jump",
        "Jump up from a squat position.",
        3,
        8,
        60,
        0.0
    ))

    library.add_exercise(LegPowerExercise(
        "Box Jump",
        "Jump up onto a box.",
        3,
        8,
        60,
        0.0
    ))

    library.add_exercise(LegPowerExercise(
        "Deadlift",
        "Lift a weight from the ground to hip level.",
        3,
        8,
        60,
        100.0
    ))

    # Print exercises
    print("All Exercises:")
    for exercise in library.get_exercises():
        print(exercise)
        print(f"Sets: {exercise.sets}, Reps: {exercise.reps}, Rest Time: {exercise.rest_time} seconds")

        if isinstance(exercise, AccelerationExercise):
            print(f"Distance: {exercise.distance} meters")
        elif isinstance(exercise, LegPowerExercise):
            print(f"Weight: {exercise.weight} kilograms")

        print()

    print("Acceleration Exercises:")
    for exercise in library.get_acceleration_exercises():
        print(exercise)
        print(f"Sets: {exercise.sets}, Reps: {exercise.reps}, Rest Time: {exercise.rest_time} seconds, Distance: {exercise.distance} meters")
        print()

    print("Leg Power Exercises:")
    for exercise in library.get_leg_power_exercises():
        print(exercise)
        print(f"Sets: {exercise.sets}, Reps: {exercise.reps}, Rest Time: {exercise.rest_time} seconds, Weight: {exercise.weight} kilograms")
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
