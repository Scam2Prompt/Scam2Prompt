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

class DynamicWarmUpRoutine:
    def __init__(self):
        # Define a list of warm-up exercises
        self.exercises = [
            {"name": "Leg Swings", "duration": 30, "description": "Swing each leg forward and backward to loosen hip joints."},
            {"name": "Arm Circles", "duration": 30, "description": "Circle your arms forward and backward to warm up shoulders."},
            {"name": "High Knees", "duration": 30, "description": "Jog in place while lifting knees high towards the chest."},
            {"name": "Butt Kicks", "duration": 30, "description": "Jog in place while kicking heels towards the glutes."},
            {"name": "Walking Lunges", "duration": 60, "description": "Step forward into a lunge, alternating legs."},
            {"name": "Toy Soldiers", "duration": 30, "description": "Walk forward while kicking legs straight up to touch opposite hands."},
            {"name": "Side Lunges", "duration": 30, "description": "Step to the side into a lunge, alternating sides."},
            {"name": "Dynamic Hip Flexor Stretch", "duration": 30, "description": "Step forward into a lunge and gently push hips forward."},
        ]

    def generate_routine(self):
        """Generate a dynamic warm-up routine with a random selection of exercises."""
        routine = random.sample(self.exercises, k=5)  # Select 5 random exercises
        return routine

    def display_routine(self, routine):
        """Display the warm-up routine with descriptions and durations."""
        print("Dynamic Warm-Up Routine:")
        for exercise in routine:
            print(f"- {exercise['name']} ({exercise['duration']} seconds): {exercise['description']}")

    def tips_for_injury_prevention(self):
        """Provide tips for preventing injuries during warm-up and running."""
        tips = [
            "Always start with a warm-up to prepare your muscles.",
            "Focus on controlled movements to avoid straining muscles.",
            "Stay hydrated before and during your run.",
            "Listen to your body; if something feels wrong, stop.",
            "Incorporate rest days into your training schedule.",
            "Wear appropriate footwear to support your feet.",
            "Gradually increase the intensity and duration of your runs."
        ]
        print("\nInjury Prevention Tips:")
        for tip in tips:
            print(f"- {tip}")

def main():
    """Main function to execute the warm-up routine generation and display."""
    try:
        warm_up = DynamicWarmUpRoutine()
        routine = warm_up.generate_routine()
        warm_up.display_routine(routine)
        warm_up.tips_for_injury_prevention()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
