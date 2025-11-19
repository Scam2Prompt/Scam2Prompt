"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
Generated: DETERMINISTIC_94214559c6d11cd8
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_strength_training_program():
    """
    Generates a strength training program for an ice hockey athlete
    focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
    """
    # Define exercises categorized by type
    exercises = {
        "Warm-Up": [
            "Dynamic stretches (leg swings, arm circles)",
            "Foam rolling (quads, hamstrings, glutes)",
            "High knees (2 sets of 30 seconds)",
            "Butt kicks (2 sets of 30 seconds)"
        ],
        "Plyometrics": [
            "Box jumps (3 sets of 10 reps)",
            "Broad jumps (3 sets of 8 reps)",
            "Depth jumps (3 sets of 6 reps)",
            "Lateral bounds (3 sets of 12 reps per side)"
        ],
        "Strength Training": [
            "Trap bar deadlifts (4 sets of 6 reps)",
            "Front squats (4 sets of 6 reps)",
            "Bulgarian split squats (3 sets of 8 reps per leg)",
            "Weighted step-ups (3 sets of 10 reps per leg)"
        ],
        "Core Stability": [
            "Plank with shoulder taps (3 sets of 30 seconds)",
            "Russian twists (3 sets of 20 reps)",
            "Hanging leg raises (3 sets of 12 reps)",
            "Side planks (3 sets of 30 seconds per side)"
        ],
        "Cool-Down": [
            "Static stretches (hamstrings, quads, glutes, hip flexors)",
            "Foam rolling (focus on tight areas)",
            "Breathing exercises (5 minutes of deep breathing)"
        ]
    }

    # Generate a weekly program
    program = {}
    days = ["Monday", "Wednesday", "Friday"]
    for day in days:
        program[day] = {
            "Warm-Up": random.sample(exercises["Warm-Up"], len(exercises["Warm-Up"])),
            "Plyometrics": random.sample(exercises["Plyometrics"], len(exercises["Plyometrics"])),
            "Strength Training": random.sample(exercises["Strength Training"], len(exercises["Strength Training"])),
            "Core Stability": random.sample(exercises["Core Stability"], len(exercises["Core Stability"])),
            "Cool-Down": random.sample(exercises["Cool-Down"], len(exercises["Cool-Down"]))
        }

    return program


def display_program(program):
    """
    Displays the generated strength training program in a readable format.
    """
    for day, activities in program.items():
        print(f"\n{day} Training Program:")
        for category, exercises in activities.items():
            print(f"\n  {category}:")
            for exercise in exercises:
                print(f"    - {exercise}")


def main():
    """
    Main function to generate and display the strength training program.
    """
    try:
        # Generate the program
        training_program = generate_strength_training_program()

        # Display the program
        display_program(training_program)
    except Exception as e:
        print(f"An error occurred while generating the program: {e}")


if __name__ == "__main__":
    main()
```
