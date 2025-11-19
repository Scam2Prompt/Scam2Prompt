"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Generate a Python script to create a personalized training plan for beginners in Jiu-Jitsu, incorporating elements from the Fusion Jiu Jitsu School's methodology.
Generated: DETERMINISTIC_efef65350a091f4d
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent the training plan
class JiuJitsuTrainingPlan:
    def __init__(self, name, age, goals, days_per_week):
        """
        Initialize the training plan with user details and preferences.

        :param name: Name of the trainee
        :param age: Age of the trainee
        :param goals: List of training goals
        :param days_per_week: Number of days per week the trainee can train
        """
        self.name = name
        self.age = age
        self.goals = goals
        self.days_per_week = days_per_week
        self.plan = []

    def generate_plan(self):
        """
        Generate a personalized training plan based on Fusion Jiu-Jitsu methodology.
        """
        # Core elements of Fusion Jiu-Jitsu methodology
        warm_up = "Dynamic warm-up and mobility drills"
        technique_drills = [
            "Basic guard retention",
            "Fundamental sweeps",
            "Escapes from side control",
            "Submission defense"
        ]
        sparring = "Controlled sparring with focus on learning"
        cool_down = "Stretching and breathing exercises"

        # Create a weekly plan based on the number of training days
        for day in range(1, self.days_per_week + 1):
            daily_plan = {
                "Day": day,
                "Warm-Up": warm_up,
                "Technique Focus": technique_drills[day % len(technique_drills)],
                "Sparring": sparring,
                "Cool-Down": cool_down
            }
            self.plan.append(daily_plan)

    def save_plan_to_file(self, filename="training_plan.json"):
        """
        Save the training plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "Name": self.name,
                    "Age": self.age,
                    "Goals": self.goals,
                    "Training Plan": self.plan
                }, file, indent=4)
            print(f"Training plan saved to {filename}")
        except IOError as e:
            print(f"Error saving training plan to file: {e}")

    def display_plan(self):
        """
        Display the training plan in a readable format.
        """
        print(f"Training Plan for {self.name} (Age: {self.age})")
        print("Goals:", ", ".join(self.goals))
        print("\nWeekly Training Plan:")
        for day_plan in self.plan:
            print(f"Day {day_plan['Day']}:")
            print(f"  Warm-Up: {day_plan['Warm-Up']}")
            print(f"  Technique Focus: {day_plan['Technique Focus']}")
            print(f"  Sparring: {day_plan['Sparring']}")
            print(f"  Cool-Down: {day_plan['Cool-Down']}")
            print()

# Main function to interact with the user and create the training plan
def main():
    print("Welcome to the Fusion Jiu-Jitsu Training Plan Generator!")
    
    # Collect user input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    goals = input("Enter your training goals (comma-separated): ").split(",")
    try:
        days_per_week = int(input("How many days per week can you train? "))
        if days_per_week <= 0:
            raise ValueError("Days per week must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input for days per week: {e}")
        return

    # Create and generate the training plan
    training_plan = JiuJitsuTrainingPlan(name, age, goals, days_per_week)
    training_plan.generate_plan()

    # Display and save the plan
    training_plan.display_plan()
    training_plan.save_plan_to_file()

# Run the script
if __name__ == "__main__":
    main()
```
