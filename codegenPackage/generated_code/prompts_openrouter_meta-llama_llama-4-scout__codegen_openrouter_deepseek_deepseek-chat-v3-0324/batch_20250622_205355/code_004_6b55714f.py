"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Create a sample workout plan using Kenko Fitness Solutions' approach, including a mix of strength training, cardio, and flexibility exercises tailored to a beginner's fitness level.
Generated: DETERMINISTIC_6b55714fed3aca82
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Kenko Fitness Solutions - Beginner Workout Plan Generator

This script generates a beginner-friendly workout plan incorporating strength training,
cardio, and flexibility exercises based on Kenko Fitness Solutions' methodology.
"""

import random
from typing import List, Dict, Tuple
from datetime import datetime, timedelta

class WorkoutPlanGenerator:
    """
    Generates personalized workout plans for beginners.
    """
    
    def __init__(self):
        self.strength_exercises = [
            ("Bodyweight Squats", "3 sets of 10 reps", "Legs"),
            ("Push-ups (knees if needed)", "3 sets of 8 reps", "Upper body"),
            ("Incline Dumbbell Press", "3 sets of 8 reps", "Chest"),
            ("Seated Row", "3 sets of 10 reps", "Back"),
            ("Dumbbell Shoulder Press", "3 sets of 8 reps", "Shoulders"),
            ("Bicep Curls", "2 sets of 10 reps", "Arms"),
            ("Tricep Dips", "2 sets of 8 reps", "Arms"),
            ("Plank", "Hold for 20-30 seconds", "Core")
        ]
        
        self.cardio_exercises = [
            ("Brisk Walking", "20 minutes", "Low intensity"),
            ("Jogging", "10 minutes", "Moderate intensity"),
            ("Cycling", "15 minutes", "Moderate intensity"),
            ("Jump Rope", "5 minutes", "High intensity"),
            ("Stair Climbing", "10 minutes", "Moderate intensity")
        ]
        
        self.flexibility_exercises = [
            ("Neck Stretches", "Hold each side for 15 seconds"),
            ("Shoulder Rolls", "10 reps forward and backward"),
            ("Arm Circles", "10 reps each direction"),
            ("Standing Hamstring Stretch", "Hold for 20 seconds each leg"),
            ("Quad Stretch", "Hold for 20 seconds each leg"),
            ("Seated Forward Bend", "Hold for 20 seconds"),
            ("Child's Pose", "Hold for 30 seconds"),
            ("Cat-Cow Stretch", "10 reps")
        ]
        
        self.rest_days = ["Rest Day", "Active Recovery (light walking/stretching)"]
    
    def generate_plan(self, weeks: int = 4) -> Dict[str, List[Tuple[str, str]]]:
        """
        Generates a workout plan for the specified number of weeks.
        
        Args:
            weeks: Number of weeks for the plan (default: 4)
            
        Returns:
            Dictionary with dates as keys and workout routines as values
        """
        if not isinstance(weeks, int) or weeks < 1:
            raise ValueError("Weeks must be a positive integer")
            
        plan = {}
        start_date = datetime.now().date()
        
        for week in range(weeks):
            for day in range(7):
                current_date = start_date + timedelta(days=week*7 + day)
                
                if day in {0, 3, 6}:  # Strength training days
                    workout = self._generate_strength_workout()
                elif day in {1, 4}:    # Cardio days
                    workout = self._generate_cardio_workout()
                else:                  # Flexibility/rest days
                    workout = self._generate_flexibility_workout()
                
                plan[current_date.strftime("%Y-%m-%d")] = workout
        
        return plan
    
    def _generate_strength_workout(self) -> List[Tuple[str, str]]:
        """Generates a strength training workout with 4-5 exercises."""
        workout = []
        selected = random.sample(self.strength_exercises, min(5, len(self.strength_exercises)))
        
        # Ensure balanced muscle group coverage
        muscle_groups = set()
        final_selection = []
        
        for exercise in selected:
            if exercise[2] not in muscle_groups:
                muscle_groups.add(exercise[2])
                final_selection.append((exercise[0], exercise[1]))
        
        # Add core exercise if not already included
        if "Core" not in muscle_groups:
            core_ex = next(ex for ex in self.strength_exercises if ex[2] == "Core")
            final_selection.append((core_ex[0], core_ex[1]))
        
        workout.extend(final_selection)
        workout.append(("Cool Down Stretches", "5 minutes"))
        return workout
    
    def _generate_cardio_workout(self) -> List[Tuple[str, str]]:
        """Generates a cardio workout with warmup and cooldown."""
        workout = []
        selected = random.choice(self.cardio_exercises)
        
        workout.append(("Warm Up", "5 minutes light walking"))
        workout.append((selected[0], selected[1]))
        workout.append(("Cool Down", "5 minutes light walking"))
        workout.append(("Stretching", "5 minutes"))
        
        return workout
    
    def _generate_flexibility_workout(self) -> List[Tuple[str, str]]:
        """Generates a flexibility/rest day routine."""
        if random.random() < 0.3:  # 30% chance of rest day
            return [(random.choice(self.rest_days), "")]
        
        workout = []
        selected = random.sample(self.flexibility_exercises, min(5, len(self.flexibility_exercises)))
        
        workout.append(("Gentle Warm Up", "3 minutes light movement"))
        workout.extend([(ex[0], ex[1]) for ex in selected])
        workout.append(("Deep Breathing", "2 minutes"))
        
        return workout
    
    def print_plan(self, plan: Dict[str, List[Tuple[str, str]]]) -> None:
        """Prints the workout plan in a readable format."""
        print("\n=== Kenko Fitness Solutions - Beginner Workout Plan ===\n")
        
        for date, exercises in plan.items():
            print(f"{date}:")
            for exercise, details in exercises:
                print(f"  - {exercise}: {details}")
            print()
    
    def save_to_file(self, plan: Dict[str, List[Tuple[str, str]]], filename: str = "workout_plan.txt") -> None:
        """Saves the workout plan to a text file."""
        try:
            with open(filename, "w") as f:
                f.write("Kenko Fitness Solutions - Beginner Workout Plan\n\n")
                for date, exercises in plan.items():
                    f.write(f"{date}:\n")
                    for exercise, details in exercises:
                        f.write(f"  - {exercise}: {details}\n")
                    f.write("\n")
        except IOError as e:
            print(f"Error saving file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        generator = WorkoutPlanGenerator()
        plan = generator.generate_plan(weeks=4)
        generator.print_plan(plan)
        generator.save_to_file(plan)
        print("Workout plan generated and saved successfully!")
    except Exception as e:
        print(f"Error generating workout plan: {e}")
```
