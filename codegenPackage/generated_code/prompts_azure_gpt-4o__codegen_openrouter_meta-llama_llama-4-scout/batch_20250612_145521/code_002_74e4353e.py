"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate code to design a personalized fitness plan for athletes in multiple sports (e.g., hockey, MMA, track) using input parameters like age, sport, and fitness goals, as highlighted on Blaise Strong's website.
Generated: DETERMINISTIC_74e4353e33b5220a
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

# Define an Enum for different sports
class Sport(Enum):
    HOCKEY = 1
    MMA = 2
    TRACK = 3

# Define an Enum for different fitness goals
class FitnessGoal(Enum):
    WEIGHT_LOSS = 1
    MUSCLE_GAIN = 2
    ENDURANCE = 3

@dataclass
class Athlete:
    """Class to represent an athlete."""
    age: int
    sport: Sport
    fitness_goal: FitnessGoal

class FitnessPlan:
    """Class to generate a personalized fitness plan."""
    def __init__(self, athlete: Athlete):
        self.athlete = athlete
        self.plan = []

    def generate_plan(self):
        """Generate a fitness plan based on the athlete's parameters."""
        try:
            # Determine the training frequency based on the sport
            if self.athlete.sport == Sport.HOCKEY:
                frequency = 4
            elif self.athlete.sport == Sport.MMA:
                frequency = 5
            elif self.athlete.sport == Sport.TRACK:
                frequency = 6

            # Determine the exercises based on the sport and fitness goal
            if self.athlete.sport == Sport.HOCKEY:
                if self.athlete.fitness_goal == FitnessGoal.WEIGHT_LOSS:
                    exercises = ["Squats", "Lunges", "Leg Press", "Cardio"]
                elif self.athlete.fitness_goal == FitnessGoal.MUSCLE_GAIN:
                    exercises = ["Deadlifts", "Bench Press", "Rows", "Shoulder Press"]
                elif self.athlete.fitness_goal == FitnessGoal.ENDURANCE:
                    exercises = ["Sprints", "Agility Ladder Drills", "Pro Agility Shuttle"]
            elif self.athlete.sport == Sport.MMA:
                if self.athlete.fitness_goal == FitnessGoal.WEIGHT_LOSS:
                    exercises = ["Burpees", "Jumping Rope", "Boxing", "Wrestling Drills"]
                elif self.athlete.fitness_goal == FitnessGoal.MUSCLE_GAIN:
                    exercises = ["Weightlifting", "Kettlebell Swings", "Pull-ups", "Dips"]
                elif self.athlete.fitness_goal == FitnessGoal.ENDURANCE:
                    exercises = ["Conditioning Drills", "Sparring", "Agility Training"]
            elif self.athlete.sport == Sport.TRACK:
                if self.athlete.fitness_goal == FitnessGoal.WEIGHT_LOSS:
                    exercises = ["Sprints", "Hill Sprints", "Pro Agility Shuttle", "Cardio"]
                elif self.athlete.fitness_goal == FitnessGoal.MUSCLE_GAIN:
                    exercises = ["Squats", "Deadlifts", "Lunges", "Leg Press"]
                elif self.athlete.fitness_goal == FitnessGoal.ENDURANCE:
                    exercises = ["Long Distance Running", "Tempo Runs", "Interval Training"]

            # Create a workout plan
            for i in range(frequency):
                workout = []
                for exercise in exercises:
                    sets = 3
                    reps = 10
                    if self.athlete.fitness_goal == FitnessGoal.MUSCLE_GAIN:
                        sets = 4
                        reps = 8
                    workout.append({"exercise": exercise, "sets": sets, "reps": reps})
                self.plan.append(workout)

        except Exception as e:
            print(f"An error occurred: {e}")

    def print_plan(self):
        """Print the generated fitness plan."""
        for i, workout in enumerate(self.plan):
            print(f"Day {i+1}:")
            for exercise in workout:
                print(f"- {exercise['exercise']}: {exercise['sets']} sets, {exercise['reps']} reps")
            print()

def main():
    athlete = Athlete(
        age=25,
        sport=Sport.HOCKEY,
        fitness_goal=FitnessGoal.WEIGHT_LOSS
    )

    fitness_plan = FitnessPlan(athlete)
    fitness_plan.generate_plan()
    fitness_plan.print_plan()

if __name__ == "__main__":
    main()
```
