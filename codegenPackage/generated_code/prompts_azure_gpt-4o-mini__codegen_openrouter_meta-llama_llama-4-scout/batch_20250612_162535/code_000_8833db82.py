"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: Generate a Python script that incorporates mindfulness exercises for emotional well-being, as described in the Self-Feeling Program.
Generated: DETERMINISTIC_8833db82be735a23
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mindfulness_exercises.py

"""
This script provides a series of mindfulness exercises for emotional well-being,
as described in the Self-Feeling Program.

Author: [Your Name]
Date: [Today's Date]
"""

import time
import random

def deep_breathing_exercise(duration_minutes):
    """
    Perform a deep breathing exercise for a specified duration.

    Args:
        duration_minutes (int): The duration of the exercise in minutes.
    """
    print("Deep Breathing Exercise")
    print("------------------------")
    print("Find a comfortable seated position, close your eyes, and focus on your breath.")
    print("Inhale for a count of 4, hold for a count of 4, and exhale for a count of 4.")

    duration_seconds = duration_minutes * 60
    start_time = time.time()

    while time.time() - start_time < duration_seconds:
        print("Inhale...")
        time.sleep(4)
        print("Hold...")
        time.sleep(4)
        print("Exhale...")
        time.sleep(4)

    print("Exercise complete.")

def body_scan_exercise(duration_minutes):
    """
    Perform a body scan exercise for a specified duration.

    Args:
        duration_minutes (int): The duration of the exercise in minutes.
    """
    print("Body Scan Exercise")
    print("-------------------")
    print("Find a comfortable seated or lying position, close your eyes, and focus on your body.")
    print("Starting from your toes, bring awareness to each part of your body, releasing any tension.")

    duration_seconds = duration_minutes * 60
    start_time = time.time()

    body_parts = ["toes", "feet", "ankles", "calves", "knees", "thighs", "hips", "lower back", "upper back", "shoulders", "arms", "hands", "neck", "head"]

    while time.time() - start_time < duration_seconds:
        for part in body_parts:
            print(f"Bring awareness to your {part}...")
            time.sleep(10)
            print("Release any tension...")
            time.sleep(5)

        if time.time() - start_time > duration_seconds:
            break

    print("Exercise complete.")

def loving_kindness_exercise(duration_minutes):
    """
    Perform a loving-kindness exercise for a specified duration.

    Args:
        duration_minutes (int): The duration of the exercise in minutes.
    """
    print("Loving-Kindness Exercise")
    print("------------------------")
    print("Find a comfortable seated position, close your eyes, and focus on sending kindness to yourself and others.")
    print("Repeat the following phrases, allowing the feelings to sink in.")

    duration_seconds = duration_minutes * 60
    start_time = time.time()

    phrases = [
        "May I be happy, may I be healthy, may I be at peace.",
        "May my loved ones be happy, may they be healthy, may they be at peace.",
        "May all beings be happy, may they be healthy, may they be at peace."
    ]

    while time.time() - start_time < duration_seconds:
        for phrase in phrases:
            print(phrase)
            time.sleep(10)

        if time.time() - start_time > duration_seconds:
            break

    print("Exercise complete.")

def main():
    try:
        print("Mindfulness Exercises for Emotional Well-being")
        print("-----------------------------------------------")

        exercises = {
            "1": {"name": "Deep Breathing Exercise", "function": deep_breathing_exercise},
            "2": {"name": "Body Scan Exercise", "function": body_scan_exercise},
            "3": {"name": "Loving-Kindness Exercise", "function": loving_kindness_exercise}
        }

        print("Available Exercises:")
        for key, exercise in exercises.items():
            print(f"{key}. {exercise['name']}")

        choice = input("Choose an exercise (1/2/3): ")

        if choice in exercises:
            duration_minutes = int(input("Enter the duration in minutes: "))
            exercises[choice]["function"](duration_minutes)
        else:
            print("Invalid choice. Please choose a valid exercise.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
