"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Create a dynamic warm-up routine for runners that aligns with the guidelines provided in the Ultimate Guide to Dynamic Warm-Up for Runners on Boost Running.
Generated: DETERMINISTIC_2fc21aec5f58380a
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class DynamicWarmUp:
    def __init__(self):
        """Initialize the warm-up routine with predefined exercises."""
        self.exercises = [
            {"name": "Leg Swings", "duration": 30},
            {"name": "Arm Circles", "duration": 30},
            {"name": "Lunges with a Twist", "duration": 30},
            {"name": "High Knees", "duration": 30},
            {"name": "Butt Kicks", "duration": 30},
            {"name": "Walking Toe Touches", "duration": 30},
            {"name": "Frankenstein Walks", "duration": 30},
            {"name": "Knee Hugs", "duration": 30},
        ]

    def display_exercise(self, exercise):
        """Display the current exercise name and duration."""
        print(f"Next exercise: {exercise['name']} for {exercise['duration']} seconds.")

    def perform_exercise(self, exercise):
        """Simulate performing the exercise for the specified duration."""
        self.display_exercise(exercise)
        time.sleep(exercise['duration'])  # Simulate time spent on the exercise

    def run_warm_up(self):
        """Run the dynamic warm-up routine."""
        print("Starting dynamic warm-up routine...")
        print("Total exercises:", len(self.exercises))

        # Shuffle exercises for randomness
        random.shuffle(self.exercises)

        try:
            for exercise in self.exercises:
                self.perform_exercise(exercise)
            print("Dynamic warm-up routine completed successfully!")
        except Exception as e:
            print(f"An error occurred while performing the warm-up: {e}")

if __name__ == "__main__":
    warm_up_routine = DynamicWarmUp()
    warm_up_routine.run_warm_up()
```
