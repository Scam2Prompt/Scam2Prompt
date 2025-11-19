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
# jiu_jitsu_training_plan.py

class JiuJitsuTrainingPlan:
    """
    Generates a personalized training plan for beginners in Jiu-Jitsu based on Fusion Jiu Jitsu School's methodology.
    """

    def __init__(self, student_name, goals, available_time):
        """
        Initializes a JiuJitsuTrainingPlan instance.

        Args:
            student_name (str): Student's name.
            goals (list): List of student's goals (e.g., weight loss, competition prep).
            available_time (int): Student's available training time per week in hours.
        """
        self.student_name = student_name
        self.goals = goals
        self.available_time = available_time
        self.plan = []

    def create_plan(self):
        """
        Creates a personalized training plan based on student's input.
        """
        # Define Fusion Jiu Jitsu School's core techniques and drills
        core_techniques = [
            {"name": "Guard Passing", "type": "technique"},
            {"name": "Sweep", "type": "technique"},
            {"name": "Submission", "type": "technique"},
            {"name": "Drill 1: Guard Recovery", "type": "drill"},
            {"name": "Drill 2: Forward Pressure", "type": "drill"},
        ]

        # Determine training frequency and duration based on available time
        if self.available_time <= 2:
            training_frequency = 2
            training_duration = 60
        elif self.available_time <= 4:
            training_frequency = 3
            training_duration = 90
        else:
            training_frequency = 4
            training_duration = 120

        # Create a plan with a mix of techniques, drills, and conditioning
        for i in range(training_frequency):
            day_plan = []
            if "weight loss" in [goal.lower() for goal in self.goals]:
                day_plan.append({"name": "Conditioning", "type": "conditioning", "duration": 30})
            day_plan.extend(core_techniques[:2])  # Include 2 core techniques per day
            day_plan.append({"name": "Drill of the Day", "type": "drill", "name": core_techniques[3 + i % 2]["name"]})
            self.plan.append({"day": i+1, "plan": day_plan})

        return self.plan

    def print_plan(self):
        """
        Prints the generated training plan.
        """
        print(f"Personalized Training Plan for {self.student_name}:")
        for day in self.plan:
            print(f"Day {day['day']}:")
            for activity in day["plan"]:
                print(f"- {activity['name']} ({activity['type']})")
                if "duration" in activity:
                    print(f"  Duration: {activity['duration']} minutes")


def main():
    try:
        student_name = input("Enter your name: ")
        goals = input("Enter your goals (comma-separated): ").split(",")
        goals = [goal.strip() for goal in goals]
        available_time = int(input("Enter your available training time per week in hours: "))

        plan = JiuJitsuTrainingPlan(student_name, goals, available_time)
        plan.create_plan()
        plan.print_plan()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
