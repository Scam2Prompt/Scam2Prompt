"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate a sample training program for a 64-year-old individual recovering from a broken hand and knee surgery, focusing on strength maintenance and improvement.
Generated: DETERMINISTIC_670583aedb06c154
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class Exercise:
    """Represents an exercise with a name, description, and sets/reps."""
    def __init__(self, name, description, sets, reps):
        self.name = name
        self.description = description
        self.sets = sets
        self.reps = reps

class TrainingProgram:
    """Represents a training program with a list of exercises."""
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        """Add an exercise to the program."""
        self.exercises.append(exercise)

    def display_program(self):
        """Display the training program."""
        print(f"Training Program: {self.name}")
        for i, exercise in enumerate(self.exercises, start=1):
            print(f"Exercise {i}: {exercise.name}")
            print(f"Description: {exercise.description}")
            print(f"Sets: {exercise.sets}, Reps: {exercise.reps}")
            print()

def generate_training_program(age, injury_hand, injury_knee):
    """Generate a sample training program for a 64-year-old individual recovering from a broken hand and knee surgery."""
    program = TrainingProgram("Sample Training Program")

    # Upper body exercises (modifications for broken hand)
    if injury_hand:
        program.add_exercise(Exercise("Seated Arm Raises", "Lift arms out to sides without lifting weights", 3, 10))
        program.add_exercise(Exercise("Wall Push-Ups", "Perform push-ups against a wall", 3, 10))
    else:
        program.add_exercise(Exercise("Dumbbell Shoulder Press", "Press dumbbells overhead", 3, 10))
        program.add_exercise(Exercise("Bicep Curls", "Curl dumbbells with palms facing forward", 3, 10))

    # Lower body exercises (modifications for knee surgery)
    if injury_knee:
        program.add_exercise(Exercise("Seated Leg Lifts", "Lift one leg off the floor while seated", 3, 10))
        program.add_exercise(Exercise("Wall Squats", "Perform squats against a wall", 3, 10))
    else:
        program.add_exercise(Exercise("Squats", "Perform squats with proper form", 3, 10))
        program.add_exercise(Exercise("Lunges", "Perform walking lunges with proper form", 3, 10))

    # Core exercises
    program.add_exercise(Exercise("Seated Marching", "March in place while seated", 3, 10))
    program.add_exercise(Exercise("Bridging", "Lift hips off the floor while lying on your back", 3, 10))

    return program

def main():
    try:
        age = 64
        injury_hand = True
        injury_knee = True

        program = generate_training_program(age, injury_hand, injury_knee)
        program.display_program()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
