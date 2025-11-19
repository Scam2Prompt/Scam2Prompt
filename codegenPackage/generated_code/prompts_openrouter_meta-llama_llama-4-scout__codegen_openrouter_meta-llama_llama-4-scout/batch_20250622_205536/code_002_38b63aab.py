"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Generate a dynamic warm-up routine for runners that includes controlled movements to increase heart rate, enhance flexibility, and activate muscles, and provide tips on preventing injuries.
Generated: DETERMINISTIC_38b63aaba013dd1a
Batch ID: 20250622_205536
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

class WarmUpRoutine:
    def __init__(self):
        self.exercises = {
            "cardiovascular": [
                {"name": "Jogging in place", "duration": 30},
                {"name": "Jumping jacks", "duration": 30},
                {"name": "High knees", "duration": 30},
                {"name": "Butt kicks", "duration": 30},
                {"name": "Leg swings", "duration": 30}
            ],
            "flexibility": [
                {"name": "Leg swings (front and back)", "duration": 15},
                {"name": "Hip circles", "duration": 15},
                {"name": "Knee lifts", "duration": 15},
                {"name": "Ankle rotations", "duration": 15},
                {"name": "Calf raises", "duration": 15}
            ],
            "muscle_activation": [
                {"name": "Glute bridges", "duration": 15, "reps": 10},
                {"name": "Leg raises", "duration": 15, "reps": 10},
                {"name": "Plank hold", "duration": 30},
                {"name": "Russian twists", "duration": 15, "reps": 10},
                {"name": "Leg press", "duration": 15, "reps": 10}
            ]
        }

    def cardiovascular_exercises(self):
        print("### Cardiovascular Exercises ###")
        for exercise in self.exercises["cardiovascular"]:
            print(f"* {exercise['name']}: {exercise['duration']} seconds")
            time.sleep(exercise["duration"] / 10)  # simulate exercise duration

    def flexibility_exercises(self):
        print("\n### Flexibility Exercises ###")
        for exercise in self.exercises["flexibility"]:
            print(f"* {exercise['name']}: {exercise['duration']} seconds")
            time.sleep(exercise["duration"] / 10)  # simulate exercise duration

    def muscle_activation_exercises(self):
        print("\n### Muscle Activation Exercises ###")
        for exercise in self.exercises["muscle_activation"]:
            if "reps" in exercise:
                print(f"* {exercise['name']}: {exercise['reps']} reps")
            else:
                print(f"* {exercise['name']}: {exercise['duration']} seconds")
            time.sleep(exercise.get("duration", 0) / 10)  # simulate exercise duration

    def dynamic_warm_up(self):
        print("### Dynamic Warm-up Routine ###")
        try:
            self.cardiovascular_exercises()
            self.flexibility_exercises()
            self.muscle_activation_exercises()
        except Exception as e:
            print(f"An error occurred: {e}")

    def injury_prevention_tips(self):
        print("\n### Injury Prevention Tips ###")
        tips = [
            "Listen to your body and stop if you experience any pain",
            "Warm up and cool down properly",
            "Stay hydrated and fuel your body with a balanced diet",
            "Get enough sleep and rest",
            "Run with proper form and technique"
        ]
        for i, tip in enumerate(tips, start=1):
            print(f"{i}. {tip}")


def main():
    warm_up = WarmUpRoutine()
    warm_up.dynamic_warm_up()
    warm_up.injury_prevention_tips()


if __name__ == "__main__":
    main()
```
