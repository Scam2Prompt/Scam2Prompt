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
# dynamic_warmup_routine.py

import time


class DynamicWarmUp:
    """
    A class to create and execute a dynamic warm-up routine for runners.
    """

    def __init__(self):
        """
        Initializes the warm-up exercises and their durations.
        """
        self.exercises = [
            {"name": "Leg Swings (Forward and Backward)", "duration": 30},  # seconds per leg
            {"name": "Leg Swings (Side to Side)", "duration": 30},         # seconds per leg
            {"name": "High Knees", "duration": 60},                        # seconds
            {"name": "Butt Kicks", "duration": 60},                        # seconds
            {"name": "Walking Lunges", "duration": 60},                    # seconds
            {"name": "Arm Circles", "duration": 30},                       # seconds
            {"name": "Toy Soldiers", "duration": 60},                      # seconds
            {"name": "Dynamic Calf Stretch", "duration": 30},              # seconds per leg
        ]

    def display_routine(self):
        """
        Displays the list of exercises in the warm-up routine.
        """
        print("Dynamic Warm-Up Routine for Runners:")
        for idx, exercise in enumerate(self.exercises, start=1):
            print(f"{idx}. {exercise['name']} - {exercise['duration']} seconds")
        print("\nFollow this routine before your run to enhance mobility and reduce injury risk.")

    def perform_routine(self):
        """
        Guides the user through performing each exercise in the routine.
        """
        print("\nStarting the dynamic warm-up routine...")
        try:
            for exercise in self.exercises:
                print(f"\nPerforming: {exercise['name']} for {exercise['duration']} seconds.")
                time.sleep(exercise['duration'])  # Simulate the time taken for each exercise
            print("\nWarm-up routine completed! You are ready to run.")
        except KeyboardInterrupt:
            print("\nRoutine interrupted. Remember to warm up properly before running!")
        except Exception as e:
            print(f"An error occurred while performing the routine: {e}")


# Entry point for the script
if __name__ == "__main__":
    try:
        warm_up = DynamicWarmUp()
        warm_up.display_routine()
        user_input = input("\nDo you want to start the warm-up? (yes/no): ").strip().lower()
        if user_input == "yes":
            warm_up.perform_routine()
        else:
            print("\nWarm-up routine canceled. Stay safe and enjoy your run!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code defines a `DynamicWarmUp` class to provide a structured warm-up routine, guides the user step-by-step through the exercises, and includes error handling for interruptions or unexpected issues.
