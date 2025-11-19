"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Generate a personalized workout plan for a beginner looking to train at home, based on the methodology described by Carol Crespo.
Generated: DETERMINISTIC_777f28e048eeb71d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Function to generate a personalized workout plan
def generate_workout_plan(name, fitness_level="beginner", equipment_available=False):
    """
    Generates a personalized workout plan based on the given parameters.

    Args:
        name (str): Name of the user.
        fitness_level (str): Fitness level of the user ("beginner", "intermediate", "advanced"). Default is "beginner".
        equipment_available (bool): Whether the user has access to workout equipment. Default is False.

    Returns:
        dict: A structured workout plan customized for the user.
    """
    try:
        # Default exercises for beginner without equipment
        workout_plan = {
            "Warm-Up": ["Jumping jacks - 3 minutes", "Dynamic stretches"],
            "Main Workout": [],
            "Cool Down": ["Static stretches - 5 minutes"]
        }

        # Customize the plan based on equipment availability
        if equipment_available:
            workout_plan["Main Workout"] = [
                "Bodyweight squats - 3 sets of 12 reps",
                "Push-ups - 3 sets of 10 reps",
                "Dumbbell rows - 3 sets of 12 reps",
                "Plank - 3 sets of 30 seconds"
            ]
        else:
            workout_plan["Main Workout"] = [
                "Bodyweight squats - 3 sets of 12 reps",
                "Incline push-ups - 3 sets of 10 reps",
                "Superman exercise - 3 sets of 15 reps",
                "Plank - 3 sets of 20 seconds"
            ]

        # Wrap-up message
        workout_plan["Notes"] = f"Hi {name}, remember to stay hydrated and listen to your body during workouts!"

        return workout_plan
    except Exception as e:
        print(f"Error generating workout plan: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Collect user input
    user_name = input("Enter your name: ")
    equipment = input("Do you have workout equipment at home? (yes/no): ").strip().lower() == "yes"

    # Generate workout plan
    plan = generate_workout_plan(name=user_name, fitness_level="beginner", equipment_available=equipment)

    # Display the workout plan
    if plan:
        print("\nYour Personalized Workout Plan:")
        print(json.dumps(plan, indent=4))
    else:
        print("Failed to generate a workout plan.")
```
