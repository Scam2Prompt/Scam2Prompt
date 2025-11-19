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
class TrainingProgram:
    def __init__(self, age, injury_type):
        """
        Initializes the training program for an individual.

        :param age: Age of the individual
        :param injury_type: Type of injury (e.g., 'broken hand', 'knee surgery')
        """
        self.age = age
        self.injury_type = injury_type
        self.exercises = []

    def add_exercise(self, name, description, repetitions, sets):
        """
        Adds an exercise to the training program.

        :param name: Name of the exercise
        :param description: Description of the exercise
        :param repetitions: Number of repetitions for the exercise
        :param sets: Number of sets for the exercise
        """
        exercise = {
            'name': name,
            'description': description,
            'repetitions': repetitions,
            'sets': sets
        }
        self.exercises.append(exercise)

    def display_program(self):
        """
        Displays the training program with all exercises.
        """
        print(f"Training Program for Age: {self.age}, Injury: {self.injury_type}\n")
        for exercise in self.exercises:
            print(f"Exercise: {exercise['name']}")
            print(f"Description: {exercise['description']}")
            print(f"Repetitions: {exercise['repetitions']}, Sets: {exercise['sets']}\n")

    def validate_program(self):
        """
        Validates the training program to ensure it is suitable for the individual.

        :raises ValueError: If the program is not suitable
        """
        if self.age < 60:
            raise ValueError("This program is designed for individuals aged 60 and above.")
        if self.injury_type not in ['broken hand', 'knee surgery']:
            raise ValueError("This program is specifically for broken hand or knee surgery recovery.")

def main():
    try:
        # Create a training program for a 64-year-old recovering from knee surgery
        program = TrainingProgram(age=64, injury_type='knee surgery')
        
        # Validate the program
        program.validate_program()

        # Add exercises to the program
        program.add_exercise(
            name='Seated Leg Raises',
            description='Sit on a chair and lift one leg at a time, keeping it straight.',
            repetitions=10,
            sets=3
        )
        program.add_exercise(
            name='Wrist Flexion',
            description='With a light weight, flex the wrist up and down while seated.',
            repetitions=12,
            sets=3
        )
        program.add_exercise(
            name='Wall Push-Ups',
            description='Stand a few feet from a wall and push against it with your arms.',
            repetitions=8,
            sets=3
        )
        program.add_exercise(
            name='Heel Slides',
            description='While lying down, slide your heel towards your buttocks and back.',
            repetitions=10,
            sets=3
        )

        # Display the training program
        program.display_program()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
