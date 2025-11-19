"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
Generated: DETERMINISTIC_94214559c6d11cd8
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# strength_training_program.py

class Athlete:
    def __init__(self, name, experience_level):
        """
        Initialize an Athlete object.

        Args:
            name (str): The athlete's name.
            experience_level (str): The athlete's experience level (e.g., 'beginner', 'intermediate', 'advanced').
        """
        self.name = name
        self.experience_level = experience_level

class Exercise:
    def __init__(self, name, sets, reps, weight, rest_time):
        """
        Initialize an Exercise object.

        Args:
            name (str): The exercise name.
            sets (int): The number of sets.
            reps (int): The number of repetitions.
            weight (float): The weight to lift.
            rest_time (int): The rest time between sets in seconds.
        """
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.rest_time = rest_time

class StrengthTrainingProgram:
    def __init__(self, athlete):
        """
        Initialize a StrengthTrainingProgram object.

        Args:
            athlete (Athlete): The athlete object.
        """
        self.athlete = athlete
        self.exercises = []

    def add_exercise(self, exercise):
        """
        Add an exercise to the program.

        Args:
            exercise (Exercise): The exercise object.
        """
        self.exercises.append(exercise)

    def generate_program(self):
        """
        Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness.

        Returns:
            list: A list of exercises.
        """
        # Day 1: Lower Body
        self.add_exercise(Exercise("Box Squats", 3, 8, 100.0, 60))
        self.add_exercise(Exercise("Depth Jumps", 3, 10, 0.0, 30))
        self.add_exercise(Exercise("Bulgarian Split Squats", 3, 10, 80.0, 60))

        # Day 2: Upper Body
        self.add_exercise(Exercise("Incline Dumbbell Press", 3, 8, 40.0, 60))
        self.add_exercise(Exercise("Medicine Ball Throws", 3, 10, 10.0, 30))
        self.add_exercise(Exercise("Bent-Over Rows", 3, 8, 60.0, 60))

        # Day 3: Rest day

        # Day 4: Lower Body
        self.add_exercise(Exercise("Trap Bar Deadlifts", 3, 8, 120.0, 60))
        self.add_exercise(Exercise("Box Jumps", 3, 10, 0.0, 30))
        self.add_exercise(Exercise("Glute-Ham Raises", 3, 10, 0.0, 30))

        # Day 5: Upper Body
        self.add_exercise(Exercise("Push-Ups", 3, 10, 0.0, 30))
        self.add_exercise(Exercise("Dumbbell Snatches", 3, 10, 20.0, 30))
        self.add_exercise(Exercise("Pull-Ups", 3, 8, 0.0, 60))

        return self.exercises

def main():
    try:
        athlete = Athlete("John Doe", "intermediate")
        program = StrengthTrainingProgram(athlete)
        exercises = program.generate_program()

        print("Strength Training Program for", athlete.name)
        print("-----------------------------------------------")

        for i, exercise in enumerate(exercises):
            print(f"Day {((i // 6) % 5) + 1}: {exercise.name}")
            print(f"Sets: {exercise.sets}, Reps: {exercise.reps}, Weight: {exercise.weight} lbs, Rest Time: {exercise.rest_time} seconds")
            print()

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
```
