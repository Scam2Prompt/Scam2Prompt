"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selffeeling.com
Prompt: Generate a Python script that incorporates mindfulness exercises for emotional well-being, as described in the Self-Feeling Program.
Generated: DETERMINISTIC_8833db82be735a23
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class MindfulnessExercise:
    def __init__(self, exercise_name, description, duration_minutes):
        """
        Initializes a mindfulness exercise.

        Args:
            exercise_name (str): The name of the exercise.
            description (str): A description of the exercise.
            duration_minutes (int): Estimated duration of the exercise in minutes.
        """
        self.exercise_name = exercise_name
        self.description = description
        self.duration_minutes = duration_minutes

    def perform_exercise(self):
        """
        Simulate performing the mindfulness exercise.
        """
        print(f"Starting '{self.exercise_name}' for {self.duration_minutes} minutes.")
        print(self.description)
        print("Take a deep breath and begin...")
        try:
            self.countdown(self.duration_minutes)
        except Exception as e:
            print(f"An error occurred while performing the exercise: {e}")

    @staticmethod
    def countdown(minutes):
        """
        Countdown timer to simulate exercise duration.

        Args:
            minutes (int): The duration in minutes for the countdown.
        """
        import time
        for remaining in range(minutes * 60, 0, -1):
            time.sleep(1)  # Simulate the passage of time.
            if remaining % 60 == 0:  # Print message every minute.
                print(f"{remaining // 60} minute(s) remaining...")
        print("Exercise complete! Great job!")

class SelfFeelingProgram:
    def __init__(self):
        """
        Initializes the Self-Feeling Program with a list of mindfulness exercises.
        """
        self.exercises = [
            MindfulnessExercise(
                "Guided Breathing",
                "Focus on your breath. Inhale deeply through your nose, hold for a moment, then exhale slowly.",
                5
            ),
            MindfulnessExercise(
                "Body Scan",
                "Bring your attention to each part of your body, relaxing it as you go.",
                10
            ),
            MindfulnessExercise(
                "Gratitude Reflection",
                "Think about three things you are grateful for today. Reflect on why they are important to you.",
                15
            ),
            MindfulnessExercise(
                "Nature Visualization",
                "Imagine a peaceful place in nature. Engage your senses to visualize this environment.",
                10
            )
        ]

    def run_program(self):
        """
        Run the Self-Feeling Program and allow the user to choose an exercise.
        """
        print("Welcome to the Self-Feeling Program!")
        print("Here are some mindfulness exercises you can choose from:")
        
        for index, exercise in enumerate(self.exercises, start=1):
            print(f"{index}. {exercise.exercise_name} - {exercise.duration_minutes} minutes")

        try:
            choice = int(input("Please select an exercise by number (1-4): "))
            if choice < 1 or choice > len(self.exercises):
                raise ValueError("Invalid selection! Please choose a number from the list.")
            selected_exercise = self.exercises[choice - 1]
            selected_exercise.perform_exercise()
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Thank you for participating in the Self-Feeling Program!")

if __name__ == "__main__":
    program = SelfFeelingProgram()
    program.run_program()
```
