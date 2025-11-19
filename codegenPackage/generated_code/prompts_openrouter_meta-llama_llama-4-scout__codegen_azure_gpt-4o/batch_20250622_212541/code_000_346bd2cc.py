"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Write a Python script to help create a personalized workout plan for athletes focusing on speed and agility training, incorporating principles from NSCA Certified Strength and Conditioning Specialist (CSCS) guidelines.
Generated: DETERMINISTIC_346bd2cc394859e3
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class for the workout plan
class WorkoutPlan:
    def __init__(self, athlete_name, training_days, focus_areas):
        """
        Initialize the workout plan with athlete details and training preferences.

        :param athlete_name: Name of the athlete
        :param training_days: Number of training days per week
        :param focus_areas: List of focus areas (e.g., speed, agility)
        """
        self.athlete_name = athlete_name
        self.training_days = training_days
        self.focus_areas = focus_areas
        self.plan = []

    def generate_plan(self):
        """
        Generate a personalized workout plan based on NSCA CSCS principles.
        """
        try:
            # Define exercises for speed and agility training
            speed_exercises = [
                "Sprints (40m, 60m, 100m)",
                "Resisted sprints (sled pulls)",
                "Acceleration drills",
                "Flying sprints"
            ]
            agility_exercises = [
                "Cone drills (T-drill, L-drill)",
                "Ladder drills",
                "Change of direction drills",
                "Reactive agility drills"
            ]

            # Distribute exercises across training days
            for day in range(1, self.training_days + 1):
                day_plan = {"Day": day, "Exercises": []}
                if "speed" in self.focus_areas:
                    day_plan["Exercises"].append(speed_exercises[day % len(speed_exercises)])
                if "agility" in self.focus_areas:
                    day_plan["Exercises"].append(agility_exercises[day % len(agility_exercises)])
                self.plan.append(day_plan)
        except Exception as e:
            print(f"Error generating workout plan: {e}")

    def save_plan_to_file(self, filename="workout_plan.json"):
        """
        Save the workout plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, "w") as file:
                json.dump({"Athlete": self.athlete_name, "Plan": self.plan}, file, indent=4)
            print(f"Workout plan saved to {filename}")
        except Exception as e:
            print(f"Error saving workout plan to file: {e}")

    def display_plan(self):
        """
        Display the workout plan in a readable format.
        """
        print(f"Workout Plan for {self.athlete_name}:")
        for day in self.plan:
            print(f"Day {day['Day']}:")
            for exercise in day["Exercises"]:
                print(f"  - {exercise}")


# Main function to interact with the user and create the workout plan
def main():
    try:
        print("Welcome to the Personalized Workout Plan Generator!")
        athlete_name = input("Enter the athlete's name: ").strip()
        training_days = int(input("Enter the number of training days per week (1-7): ").strip())
        focus_areas = input("Enter focus areas (e.g., speed, agility) separated by commas: ").strip().lower().split(",")

        # Validate input
        if training_days < 1 or training_days > 7:
            raise ValueError("Training days must be between 1 and 7.")
        if not focus_areas:
            raise ValueError("At least one focus area must be provided.")

        # Create and generate the workout plan
        workout_plan = WorkoutPlan(athlete_name, training_days, focus_areas)
        workout_plan.generate_plan()
        workout_plan.display_plan()

        # Save the plan to a file
        save_option = input("Do you want to save the plan to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            workout_plan.save_plan_to_file()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
