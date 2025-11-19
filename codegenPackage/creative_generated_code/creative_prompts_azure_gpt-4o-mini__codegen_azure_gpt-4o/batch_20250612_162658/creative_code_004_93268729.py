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
# Filename: track_training_library.py

"""
Track Training Library - Exercises for Improving Acceleration and Leg Power
Based on techniques used by Coach Blaise.

This module provides a set of exercises designed for track athletes to enhance
their acceleration and leg power. Each exercise includes details about
how it's performed, recommended sets and repetitions, and equipment needed.
"""

class ExerciseLibrary:
    """
    A library of exercises tailored for track athletes to improve acceleration
    and leg power.
    """
    def __init__(self):
        # Initialize exercise library with predefined exercises.
        self.exercises = []
        self._initialize_exercises()

    def _initialize_exercises(self):
        """Private method to preload exercises into the library."""
        self.add_exercise(
            name="Sprint Starts",
            description="Short sprints focusing on explosive starts from a low stance.",
            equipment="None",
            sets=5,
            repetitions=3,
            instructions="Start in a low crouched position, explode forward into a sprint for 20 meters."
        )
        self.add_exercise(
            name="Hill Sprints",
            description="Sprints performed on an incline to build power and endurance.",
            equipment="None",
            sets=6,
            repetitions=1,
            instructions="Sprint up a steep hill for 30 meters, walk down to recover before next sprint."
        )
        self.add_exercise(
            name="Depth Jumps",
            description="Jumping exercises to improve explosive power and fast-twitch muscle response.",
            equipment="Plyometric box or sturdy platform.",
            sets=4,
            repetitions=10,
            instructions="Step off the box and immediately jump as high as possible upon landing."
        )
        self.add_exercise(
            name="Weighted Lunges",
            description="Lunges performed while holding weights to build leg strength.",
            equipment="Dumbbells or kettlebells.",
            sets=3,
            repetitions=12,
            instructions="Step forward into a lunge position, keeping your back straight. Switch legs after each rep."
        )
        self.add_exercise(
            name="Resistance Band Acceleration Drills",
            description="Sprint drills using resistance bands to build acceleration power.",
            equipment="Resistance bands.",
            sets=4,
            repetitions=30,
            instructions="Attach a resistance band around your waist and sprint forward while a partner provides resistance."
        )

    def add_exercise(self, name, description, equipment, sets, repetitions, instructions):
        """
        Add a new exercise to the library.
        
        Parameters:
            name (str): Name of the exercise.
            description (str): Brief description of the exercise.
            equipment (str): Equipment required, if any.
            sets (int): Recommended number of sets.
            repetitions (int): Recommended number of repetitions per set.
            instructions (str): Step-by-step instructions for performing the exercise.
        """
        exercise = {
            "name": name,
            "description": description,
            "equipment": equipment,
            "sets": sets,
            "repetitions": repetitions,
            "instructions": instructions
        }
        self.exercises.append(exercise)

    def get_exercise(self, name):
        """
        Retrieve an exercise by name.
        
        Parameters:
            name (str): The name of the exercise to retrieve.
        
        Returns:
            dict: The exercise details if found, or None if not found.
        """
        for exercise in self.exercises:
            if exercise['name'].lower() == name.lower():
                return exercise
        return None

    def list_exercises(self):
        """
        List all exercises in the library.
        
        Returns:
            list: A list of exercise names.
        """
        return [exercise['name'] for exercise in self.exercises]


# Error handling example: Main block to test the library
if __name__ == "__main__":
    try:
        library = ExerciseLibrary()

        print("Available exercises:")
        for exercise in library.list_exercises():
            print(f" - {exercise}")

        # Example: Retrieve a specific exercise
        exercise_name = "Hill Sprints"
        exercise = library.get_exercise(exercise_name)

        if exercise:
            print(f"\nDetails for '{exercise_name}':")
            for key, value in exercise.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"\nError: Exercise '{exercise_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
