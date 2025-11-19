"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Write a program to simulate leadership training exercises, inspired by the methodologies shared by Dr. Lalit Arora.
Generated: DETERMINISTIC_b3d7567dfb6948b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class LeadershipExercise:
    """
    A class to represent a leadership training exercise.
    """

    def __init__(self, name, description, duration):
        """
        Initializes a new leadership exercise.

        :param name: str - The name of the exercise.
        :param description: str - A brief description of the exercise.
        :param duration: int - Duration of the exercise in seconds.
        """
        self.name = name
        self.description = description
        self.duration = duration

    def start_exercise(self):
        """
        Starts the leadership exercise, simulating its duration.
        """
        print(f"Starting exercise: {self.name}")
        print(f"Description: {self.description}")
        print(f"Duration: {self.duration} seconds")
        time.sleep(self.duration)
        print(f"Exercise '{self.name}' completed!\n")


class LeadershipTraining:
    """
    A class to manage a series of leadership exercises.
    """

    def __init__(self):
        """
        Initializes the leadership training with an empty list of exercises.
        """
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Adds a new exercise to the training program.

        :param exercise: LeadershipExercise - The exercise to add.
        """
        if not isinstance(exercise, LeadershipExercise):
            raise ValueError("exercise must be an instance of LeadershipExercise")
        self.exercises.append(exercise)
        print(f"Added exercise: {exercise.name}")

    def run_training(self):
        """
        Runs all exercises in the training program.
        """
        if not self.exercises:
            print("No exercises to run.")
            return

        print("Starting leadership training...\n")
        for exercise in self.exercises:
            exercise.start_exercise()
        print("All exercises completed!")


def main():
    """
    Main function to set up and run the leadership training program.
    """
    try:
        # Create a leadership training instance
        training = LeadershipTraining()

        # Define some exercises
        exercise1 = LeadershipExercise("Team Building", "Build trust and collaboration within the team.", 5)
        exercise2 = LeadershipExercise("Conflict Resolution", "Learn to manage and resolve conflicts effectively.", 7)
        exercise3 = LeadershipExercise("Decision Making", "Enhance decision-making skills under pressure.", 6)

        # Add exercises to the training program
        training.add_exercise(exercise1)
        training.add_exercise(exercise2)
        training.add_exercise(exercise3)

        # Run the training program
        training.run_training()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
