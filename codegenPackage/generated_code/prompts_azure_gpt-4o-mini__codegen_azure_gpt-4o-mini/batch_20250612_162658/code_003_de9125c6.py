"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Create a workout plan for a senior athlete recovering from injury, incorporating principles from Blaise Strong's training philosophy.
Generated: DETERMINISTIC_de9125c69c879d7a
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WorkoutPlan:
    """
    A class to represent a workout plan for a senior athlete recovering from injury.
    Incorporates principles from Blaise Strong's training philosophy.
    """

    def __init__(self, athlete_name, injury_type):
        """
        Initializes the WorkoutPlan with the athlete's name and type of injury.

        :param athlete_name: str - Name of the athlete
        :param injury_type: str - Type of injury the athlete is recovering from
        """
        self.athlete_name = athlete_name
        self.injury_type = injury_type
        self.exercises = []

    def add_exercise(self, name, duration, intensity, notes):
        """
        Adds an exercise to the workout plan.

        :param name: str - Name of the exercise
        :param duration: int - Duration of the exercise in minutes
        :param intensity: str - Intensity level (e.g., 'low', 'medium', 'high')
        :param notes: str - Additional notes about the exercise
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if intensity not in ['low', 'medium', 'high']:
            raise ValueError("Intensity must be 'low', 'medium', or 'high'.")

        exercise = {
            'name': name,
            'duration': duration,
            'intensity': intensity,
            'notes': notes
        }
        self.exercises.append(exercise)

    def generate_plan(self):
        """
        Generates the workout plan as a formatted string.

        :return: str - Formatted workout plan
        """
        plan = f"Workout Plan for {self.athlete_name} (Injury: {self.injury_type})\n"
        plan += "-" * 50 + "\n"
        for exercise in self.exercises:
            plan += (f"Exercise: {exercise['name']}, "
                     f"Duration: {exercise['duration']} mins, "
                     f"Intensity: {exercise['intensity']}, "
                     f"Notes: {exercise['notes']}\n")
        return plan

    def display_plan(self):
        """
        Displays the workout plan to the console.
        """
        print(self.generate_plan())


# Example usage
if __name__ == "__main__":
    try:
        # Create a workout plan for a senior athlete
        athlete_plan = WorkoutPlan("John Doe", "Knee Injury")

        # Add exercises to the plan
        athlete_plan.add_exercise("Gentle Stretching", 15, "low", "Focus on flexibility.")
        athlete_plan.add_exercise("Walking", 30, "medium", "Maintain a steady pace.")
        athlete_plan.add_exercise("Water Aerobics", 45, "low", "Low impact on joints.")

        # Display the workout plan
        athlete_plan.display_plan()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
