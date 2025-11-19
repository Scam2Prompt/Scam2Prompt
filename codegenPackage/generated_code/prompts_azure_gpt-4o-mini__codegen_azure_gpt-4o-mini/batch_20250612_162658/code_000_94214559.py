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
import random
from datetime import datetime, timedelta

class StrengthTrainingProgram:
    def __init__(self, athlete_name):
        """
        Initializes the strength training program for the athlete.
        
        :param athlete_name: Name of the athlete
        """
        self.athlete_name = athlete_name
        self.program = []
        self.start_date = datetime.now()
        self.duration_weeks = 4  # Duration of the program in weeks

    def generate_workout(self):
        """
        Generates a weekly workout plan focusing on speed and explosiveness.
        """
        exercises = [
            {"name": "Squat Jumps", "sets": 4, "reps": 6},
            {"name": "Power Cleans", "sets": 4, "reps": 5},
            {"name": "Box Jumps", "sets": 4, "reps": 8},
            {"name": "Deadlifts", "sets": 4, "reps": 5},
            {"name": "Medicine Ball Slams", "sets": 3, "reps": 10},
            {"name": "Sprints", "sets": 5, "reps": 30},  # 30 meters
            {"name": "Plyometric Push-Ups", "sets": 3, "reps": 8},
            {"name": "Lateral Bounds", "sets": 4, "reps": 6}
        ]

        # Randomly select exercises to create a balanced workout
        selected_exercises = random.sample(exercises, k=5)
        workout = {
            "date": self.start_date.strftime("%Y-%m-%d"),
            "exercises": selected_exercises
        }
        self.program.append(workout)
        self.start_date += timedelta(days=7)  # Move to the next week

    def create_program(self):
        """
        Creates a complete training program for the specified duration.
        """
        for _ in range(self.duration_weeks):
            self.generate_workout()

    def display_program(self):
        """
        Displays the generated training program.
        """
        print(f"Strength Training Program for {self.athlete_name}:\n")
        for week, workout in enumerate(self.program, start=1):
            print(f"Week {week} - Date: {workout['date']}")
            for exercise in workout['exercises']:
                print(f"  {exercise['name']}: {exercise['sets']} sets of {exercise['reps']} reps")
            print("\n")

    def save_program(self, filename):
        """
        Saves the training program to a file.
        
        :param filename: Name of the file to save the program
        """
        try:
            with open(filename, 'w') as file:
                for week, workout in enumerate(self.program, start=1):
                    file.write(f"Week {week} - Date: {workout['date']}\n")
                    for exercise in workout['exercises']:
                        file.write(f"  {exercise['name']}: {exercise['sets']} sets of {exercise['reps']} reps\n")
                    file.write("\n")
            print(f"Program saved to {filename}")
        except IOError as e:
            print(f"Error saving program: {e}")

# Example usage
if __name__ == "__main__":
    athlete = StrengthTrainingProgram("John Doe")
    athlete.create_program()
    athlete.display_program()
    athlete.save_program("strength_training_program.txt")
```
