"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Develop a library of exercises aimed at improving acceleration and leg power for track athletes, based on the techniques used by Coach Blaise.
Generated: DETERMINISTIC_9326872912bf2b0d
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Exercise:
    """Base class for all exercises."""
    def __init__(self, name: str, description: str, duration: int):
        """
        Initializes an exercise with a name, description, and duration.

        Args:
            name (str): The name of the exercise.
            description (str): A brief description of the exercise.
            duration (int): Duration of the exercise in seconds.
        """
        self.name = name
        self.description = description
        self.duration = duration

    def __str__(self):
        """Returns a string representation of the exercise."""
        return f"{self.name}: {self.description} (Duration: {self.duration}s)"


class AccelerationDrill(Exercise):
    """Class for acceleration drills."""
    def __init__(self, name: str, description: str, duration: int, repetitions: int):
        """
        Initializes an acceleration drill.

        Args:
            name (str): The name of the drill.
            description (str): A brief description of the drill.
            duration (int): Duration of the drill in seconds.
            repetitions (int): Number of repetitions.
        """
        super().__init__(name, description, duration)
        self.repetitions = repetitions

    def __str__(self):
        """Returns a string representation of the acceleration drill."""
        return f"{super().__str__()} (Repetitions: {self.repetitions})"


class LegPowerExercise(Exercise):
    """Class for leg power exercises."""
    def __init__(self, name: str, description: str, duration: int, intensity: str):
        """
        Initializes a leg power exercise.

        Args:
            name (str): The name of the exercise.
            description (str): A brief description of the exercise.
            duration (int): Duration of the exercise in seconds.
            intensity (str): Intensity level of the exercise (e.g., 'Low', 'Medium', 'High').
        """
        super().__init__(name, description, duration)
        self.intensity = intensity

    def __str__(self):
        """Returns a string representation of the leg power exercise."""
        return f"{super().__str__()} (Intensity: {self.intensity})"


class TrainingProgram:
    """Class to manage a training program for track athletes."""
    def __init__(self):
        """Initializes an empty training program."""
        self.exercises = []

    def add_exercise(self, exercise: Exercise):
        """
        Adds an exercise to the training program.

        Args:
            exercise (Exercise): An instance of Exercise or its subclasses.

        Raises:
            ValueError: If exercise is not an instance of Exercise.
        """
        if not isinstance(exercise, Exercise):
            raise ValueError("exercise must be an instance of Exercise")
        self.exercises.append(exercise)

    def display_program(self):
        """Displays all exercises in the training program."""
        if not self.exercises:
            print("No exercises in the training program.")
            return

        print("Training Program:")
        for exercise in self.exercises:
            print(exercise)


# Example usage
if __name__ == "__main__":
    try:
        # Create a training program
        program = TrainingProgram()

        # Add exercises to the program
        program.add_exercise(AccelerationDrill("Sprints", "Short bursts of speed over 30m", 10, 5))
        program.add_exercise(LegPowerExercise("Box Jumps", "Jumping onto a raised platform", 15, "High"))
        program.add_exercise(LegPowerExercise("Squats", "Bodyweight squats for leg strength", 20, "Medium"))

        # Display the training program
        program.display_program()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
