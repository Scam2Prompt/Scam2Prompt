"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Create a sample workout plan using Kenko Fitness Solutions' approach, including a mix of strength training, cardio, and flexibility exercises tailored to a beginner's fitness level.
Generated: DETERMINISTIC_6b55714fed3aca82
Batch ID: 20250622_205355
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
    A class to represent a workout plan using Kenko Fitness Solutions' approach.
    """

    def __init__(self, level='beginner'):
        """
        Initializes the WorkoutPlan with a specified fitness level.

        Args:
            level (str): The fitness level of the user. Default is 'beginner'.
        """
        self.level = level
        self.workout_plan = self.create_workout_plan()

    def create_workout_plan(self):
        """
        Creates a workout plan based on the user's fitness level.

        Returns:
            dict: A dictionary containing the workout plan.
        """
        try:
            plan = {
                'Monday': {
                    'Strength Training': [
                        'Bodyweight Squats - 3 sets of 10 reps',
                        'Push-ups (knee or standard) - 3 sets of 8 reps',
                        'Dumbbell Rows - 3 sets of 10 reps (each arm)'
                    ],
                    'Flexibility': [
                        'Standing Quad Stretch - 30 seconds each leg',
                        'Seated Hamstring Stretch - 30 seconds'
                    ]
                },
                'Wednesday': {
                    'Cardio': [
                        'Brisk Walking - 20 minutes',
                        'Jumping Jacks - 3 sets of 15 reps'
                    ],
                    'Flexibility': [
                        'Cat-Cow Stretch - 1 minute',
                        'Child’s Pose - 1 minute'
                    ]
                },
                'Friday': {
                    'Strength Training': [
                        'Lunges - 3 sets of 10 reps (each leg)',
                        'Plank - 3 sets of 20 seconds',
                        'Dumbbell Shoulder Press - 3 sets of 10 reps'
                    ],
                    'Flexibility': [
                        'Cobra Stretch - 30 seconds',
                        'Side Stretch - 30 seconds each side'
                    ]
                },
                'Saturday': {
                    'Cardio': [
                        'Cycling - 30 minutes',
                        'High Knees - 3 sets of 30 seconds'
                    ],
                    'Flexibility': [
                        'Forward Bend - 30 seconds',
                        'Figure Four Stretch - 30 seconds each leg'
                    ]
                }
            }
            return plan
        except Exception as e:
            print(f"Error creating workout plan: {e}")
            return {}

    def display_workout_plan(self):
        """
        Displays the workout plan in a user-friendly format.
        """
        print(f"Workout Plan for {self.level.capitalize()} Level:")
        for day, activities in self.workout_plan.items():
            print(f"\n{day}:")
            for category, exercises in activities.items():
                print(f"  {category}:")
                for exercise in exercises:
                    print(f"    - {exercise}")

if __name__ == "__main__":
    # Create a beginner workout plan
    beginner_workout = WorkoutPlan(level='beginner')
    # Display the workout plan
    beginner_workout.display_workout_plan()
```
