"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
Generated: DETERMINISTIC_94214559c6d11cd8
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Strength training program generator for ice hockey athletes
def generate_training_program():
    """
    Generates a strength training program aimed at improving speed and explosiveness 
    for ice hockey athletes. Inspired by Blaise Strong's coaching methods.
    
    Returns:
        dict: A structured training program with warm-up, main workout, and cool-down components.
    """
    try:
        # Define exercises categorized by type
        warm_up_exercises = [
            "Dynamic stretches (leg swings, arm circles)",
            "Foam rolling (quads, hamstrings, glutes)",
            "Bodyweight squats (10 reps)",
            "High knees (30 seconds)"
        ]

        speed_and_explosiveness_exercises = [
            "Box jumps (3 sets of 8 reps)",
            "Broad jumps (4 sets of 6 reps)",
            "Sprint intervals (5x 40 meters at max effort)",
            "Explosive push-ups (3 sets of 12 reps)",
            "Medicine ball slams (3 sets of 15 reps)"
        ]

        strength_exercises = [
            "Trap bar deadlifts (4 sets of 5 reps)",
            "Bulgarian split squats (3 sets of 8 reps per leg)",
            "Pull-ups (4 sets of 10 reps or max effort)",
            "Barbell bench press (3 sets of 8 reps)",
            "Kettlebell swings (4 sets of 12 reps)"
        ]

        cool_down_exercises = [
            "Static stretches (hamstrings, quads, shoulders)",
            "Foam rolling (lower back, calves)",
            "Breathing exercises for recovery (5 minutes)"
        ]

        # Randomly select exercises to keep the program dynamic
        warm_up = random.sample(warm_up_exercises, 3)
        main_workout = random.sample(speed_and_explosiveness_exercises, 3) + random.sample(strength_exercises, 2)
        cool_down = random.sample(cool_down_exercises, 2)

        # Structure the training program
        training_program = {
            "Warm-Up": warm_up,
            "Main Workout": main_workout,
            "Cool-Down": cool_down
        }

        return training_program
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while generating the training program: {str(e)}")
        return None

def display_program(training_program):
    """
    Displays the generated training program in a structured format.

    Args:
        training_program (dict): The training program to display.
    """
    if not training_program:
        print("No program to display.")
        return

    print("Ice Hockey Athlete Strength Training Program\n")
    for section, exercises in training_program.items():
        print(f"{section}:")
        for exercise in exercises:
            print(f"  - {exercise}")
        print()

# Main execution
if __name__ == "__main__":
    # Generate and display the training program
    program = generate_training_program()
    display_program(program)
```
