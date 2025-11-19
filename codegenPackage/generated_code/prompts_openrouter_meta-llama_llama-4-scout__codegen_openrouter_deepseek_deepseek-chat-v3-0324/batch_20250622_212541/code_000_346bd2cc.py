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
from typing import Dict, List, Optional

class WorkoutPlanGenerator:
    """
    A class to generate personalized workout plans for speed and agility training
    based on NSCA CSCS guidelines.
    """
    
    def __init__(self):
        self.exercises = {
            'speed': [
                {'name': 'Sprints', 'sets': 4, 'reps': '20-40m', 'rest': '2-3 min'},
                {'name': 'Hill Sprints', 'sets': 4, 'reps': '20-30m', 'rest': '2-3 min'},
                {'name': 'Resisted Sprints', 'sets': 3, 'reps': '20-30m', 'rest': '2-3 min'},
                {'name': 'Flying Sprints', 'sets': 3, 'reps': '20-30m', 'rest': '2-3 min'}
            ],
            'agility': [
                {'name': 'Ladder Drills', 'sets': 3, 'reps': '30-60 sec', 'rest': '1 min'},
                {'name': 'Cone Drills', 'sets': 3, 'reps': '5-8 reps', 'rest': '1 min'},
                {'name': 'Shuttle Runs', 'sets': 3, 'reps': '5-8 reps', 'rest': '1 min'},
                {'name': 'Plyometric Box Drills', 'sets': 3, 'reps': '8-12 reps', 'rest': '1 min'}
            ],
            'strength': [
                {'name': 'Squats', 'sets': 3, 'reps': '6-8', 'rest': '2-3 min'},
                {'name': 'Deadlifts', 'sets': 3, 'reps': '6-8', 'rest': '2-3 min'},
                {'name': 'Lunges', 'sets': 3, 'reps': '8-10 per leg', 'rest': '1-2 min'},
                {'name': 'Plyometric Jumps', 'sets': 3, 'reps': '8-10', 'rest': '1-2 min'}
            ]
        }
        
        self.workout_days = ['Monday', 'Wednesday', 'Friday']
        self.current_week = 1
        
    def generate_workout_plan(self, weeks: int = 4, focus: str = 'balanced') -> Dict[str, List[Dict]]:
        """
        Generate a workout plan for the specified number of weeks.
        
        Args:
            weeks: Number of weeks for the plan (default: 4)
            focus: Training focus ('speed', 'agility', 'balanced')
            
        Returns:
            Dictionary containing weekly workout plans
        """
        if weeks < 1 or weeks > 12:
            raise ValueError("Weeks must be between 1 and 12")
            
        if focus not in ['speed', 'agility', 'balanced']:
            raise ValueError("Focus must be 'speed', 'agility', or 'balanced'")
            
        plan = {}
        
        for week in range(1, weeks + 1):
            weekly_plan = []
            for day in self.workout_days:
                workout = self._generate_daily_workout(focus)
                weekly_plan.append({'day': day, 'workout': workout})
            plan[f'Week {week}'] = weekly_plan
            
        return plan
    
    def _generate_daily_workout(self, focus: str) -> List[Dict]:
        """
        Generate a single day's workout based on focus.
        
        Args:
            focus: Training focus ('speed', 'agility', 'balanced')
            
        Returns:
            List of exercises for the day
        """
        workout = []
        
        # Always include strength exercises
        strength_exercises = random.sample(self.exercises['strength'], 2)
        workout.extend(strength_exercises)
        
        # Add focus-specific exercises
        if focus == 'speed':
            speed_exercises = random.sample(self.exercises['speed'], 2)
            workout.extend(speed_exercises)
        elif focus == 'agility':
            agility_exercises = random.sample(self.exercises['agility'], 2)
            workout.extend(agility_exercises)
        else:  # balanced
            speed_exercise = random.choice(self.exercises['speed'])
            agility_exercise = random.choice(self.exercises['agility'])
            workout.extend([speed_exercise, agility_exercise])
            
        return workout
    
    def print_workout_plan(self, plan: Dict[str, List[Dict]]) -> None:
        """
        Print the workout plan in a readable format.
        
        Args:
            plan: The workout plan dictionary
        """
        for week, days in plan.items():
            print(f"\n{week}:")
            for day in days:
                print(f"\n{day['day']}:")
                for exercise in day['workout']:
                    print(f"- {exercise['name']}: {exercise['sets']} sets x {exercise['reps']} (rest {exercise['rest']})")


def main():
    """
    Main function to demonstrate the workout plan generator.
    """
    try:
        generator = WorkoutPlanGenerator()
        
        print("Speed and Agility Workout Plan Generator")
        print("----------------------------------------")
        
        # Get user input
        weeks = int(input("Enter number of weeks for the plan (1-12): "))
        focus = input("Enter training focus (speed/agility/balanced): ").lower()
        
        # Generate and display plan
        plan = generator.generate_workout_plan(weeks=weeks, focus=focus)
        generator.print_workout_plan(plan)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
