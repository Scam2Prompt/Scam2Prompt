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
import random
from datetime import datetime, timedelta

class WorkoutPlan:
    def __init__(self, athlete_name, duration_weeks=4):
        """
        Initializes the WorkoutPlan with the athlete's name and duration.
        
        :param athlete_name: Name of the athlete
        :param duration_weeks: Duration of the workout plan in weeks
        """
        self.athlete_name = athlete_name
        self.duration_weeks = duration_weeks
        self.workouts = []
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(weeks=duration_weeks)

    def generate_workout(self):
        """
        Generates a personalized workout focusing on speed and agility.
        """
        speed_drills = [
            "Sprints (30m, 60m, 100m)",
            "Agility Ladder Drills",
            "Cone Drills (T-drill, L-drill)",
            "Plyometric Box Jumps",
            "Resistance Sprints"
        ]
        
        strength_exercises = [
            "Squats",
            "Deadlifts",
            "Lunges",
            "Power Cleans",
            "Box Squats"
        ]
        
        cooldowns = [
            "Static Stretching",
            "Foam Rolling",
            "Light Jogging"
        ]
        
        # Randomly select drills and exercises
        selected_speed_drills = random.sample(speed_drills, 3)
        selected_strength_exercises = random.sample(strength_exercises, 2)
        selected_cooldown = random.choice(cooldowns)

        workout = {
            "Speed Drills": selected_speed_drills,
            "Strength Exercises": selected_strength_exercises,
            "Cooldown": selected_cooldown
        }
        
        return workout

    def create_plan(self):
        """
        Creates a complete workout plan for the specified duration.
        """
        for week in range(self.duration_weeks):
            week_plan = {
                "Week": week + 1,
                "Date": (self.start_date + timedelta(weeks=week)).date(),
                "Workout": self.generate_workout()
            }
            self.workouts.append(week_plan)

    def display_plan(self):
        """
        Displays the complete workout plan.
        """
        print(f"Personalized Workout Plan for {self.athlete_name}")
        print(f"Duration: {self.duration_weeks} weeks")
        print("-------------------------------------------------")
        for week in self.workouts:
            print(f"Week {week['Week']} - Date: {week['Date']}")
            for category, exercises in week['Workout'].items():
                print(f"{category}: {', '.join(exercises)}")
            print("-------------------------------------------------")

def main():
    """
    Main function to execute the workout plan generation.
    """
    try:
        athlete_name = input("Enter the athlete's name: ")
        duration_weeks = int(input("Enter the duration of the workout plan in weeks (1-12): "))
        
        if duration_weeks < 1 or duration_weeks > 12:
            raise ValueError("Duration must be between 1 and 12 weeks.")
        
        workout_plan = WorkoutPlan(athlete_name, duration_weeks)
        workout_plan.create_plan()
        workout_plan.display_plan()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
