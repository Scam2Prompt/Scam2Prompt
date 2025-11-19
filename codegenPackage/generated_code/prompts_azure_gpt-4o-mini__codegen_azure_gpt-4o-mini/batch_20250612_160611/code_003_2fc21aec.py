"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a dynamic warm-up routine for runners that aligns with the guidelines provided in the Ultimate Guide to Dynamic Warm-Up for Runners on Boost Running.
Generated: DETERMINISTIC_2fc21aec5f58380a
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class DynamicWarmUp:
    def __init__(self):
        """Initialize the warm-up routine with predefined exercises."""
        self.exercises = [
            {"name": "Leg Swings", "duration": 30},  # seconds
            {"name": "Walking Lunges", "duration": 30},
            {"name": "High Knees", "duration": 30},
            {"name": "Butt Kicks", "duration": 30},
            {"name": "Arm Circles", "duration": 30},
            {"name": "Hip Circles", "duration": 30},
            {"name": "Frankenstein Walks", "duration": 30},
            {"name": "Side Lunges", "duration": 30},
        ]

    def shuffle_exercises(self):
        """Shuffle the exercises to create a dynamic routine."""
        random.shuffle(self.exercises)

    def display_exercise(self, exercise):
        """Display the current exercise and its duration."""
        print(f"Next exercise: {exercise['name']} for {exercise['duration']} seconds.")
        time.sleep(exercise['duration'])  # Simulate the duration of the exercise

    def run_warm_up(self):
        """Run the dynamic warm-up routine."""
        print("Starting dynamic warm-up routine...\n")
        self.shuffle_exercises()
        
        for exercise in self.exercises:
            try:
                self.display_exercise(exercise)
            except Exception as e:
                print(f"An error occurred while performing {exercise['name']}: {e}")

        print("\nDynamic warm-up routine completed. Ready to run!")

if __name__ == "__main__":
    warm_up_routine = DynamicWarmUp()
    warm_up_routine.run_warm_up()
```
