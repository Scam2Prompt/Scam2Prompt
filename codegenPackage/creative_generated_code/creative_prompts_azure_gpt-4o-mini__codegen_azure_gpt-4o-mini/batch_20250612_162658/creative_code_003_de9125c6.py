"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Create a workout plan for a senior athlete recovering from injury, incorporating principles from Blaise Strong's training philosophy.
Generated: DETERMINISTIC_de9125c69c879d7a
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WorkoutPlan:
    def __init__(self, athlete_name, injury_type):
        """
        Initialize a workout plan for a senior athlete.

        :param athlete_name: str, the name of the athlete
        :param injury_type: str, the type of injury the athlete is recovering from
        """
        self.athlete_name = athlete_name
        self.injury_type = injury_type
        self.exercises = []
        self.schedule = []

    def add_exercise(self, name, repetitions, sets, duration, intensity):
        """
        Add an exercise to the workout plan.

        :param name: str, the name of the exercise
        :param repetitions: int, number of repetitions for the exercise
        :param sets: int, number of sets for the exercise
        :param duration: int, duration of the exercise in minutes
        :param intensity: str, intensity level ('low', 'moderate', 'high')
        """
        exercise = {
            'name': name,
            'repetitions': repetitions,
            'sets': sets,
            'duration': duration,
            'intensity': intensity
        }
        self.exercises.append(exercise)

    def create_schedule(self):
        """
        Create a weekly workout schedule based on the exercises added.
        The schedule is designed to avoid overexertion and allow recovery.

        :return: list of dict, the workout schedule for the week
        """
        schedule_template = [
            {"day": "Monday", "focus": "strength training"},
            {"day": "Tuesday", "focus": "cardio"},
            {"day": "Wednesday", "focus": "flexibility and balance"},
            {"day": "Thursday", "focus": "strength training"},
            {"day": "Friday", "focus": "rest"},
            {"day": "Saturday", "focus": "light activity"},
            {"day": "Sunday", "focus": "rest"}
        ]

        for day in schedule_template:
            day['exercises'] = self.exercises if day['focus'] != "rest" else []

        self.schedule = schedule_template
        return self.schedule

    def display_plan(self):
        """
        Display the workout plan including exercises and weekly schedule.
        """
        print(f"Workout Plan for {self.athlete_name} (Injury: {self.injury_type})")
        print("\nExercises:")
        for exercise in self.exercises:
            print(f"- {exercise['name']} | Reps: {exercise['repetitions']}, Sets: {exercise['sets']}, "
                  f"Duration: {exercise['duration']} mins, Intensity: {exercise['intensity']}")

        print("\nWeekly Schedule:")
        for day in self.schedule:
            print(f"{day['day']}: {day['focus']}")
            for exercise in day['exercises']:
                print(f"  - {exercise['name']} | Reps: {exercise['repetitions']}, Sets: {exercise['sets']}")

# Example usage
if __name__ == "__main__":
    try:
        athlete = WorkoutPlan("John Doe", "Knee Injury")
        athlete.add_exercise("Bodyweight Squats", repetitions=10, sets=3, duration=15, intensity="low")
        athlete.add_exercise("Walking", repetitions=0, sets=0, duration=30, intensity="moderate")
        athlete.add_exercise("Stretching", repetitions=0, sets=0, duration=20, intensity="low")

        athlete.create_schedule()
        athlete.display_plan()
    except Exception as e:
        print(f"An error occurred: {e}")
```
