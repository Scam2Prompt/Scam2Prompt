"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Generate a personalized workout plan that avoids common mistakes and accelerates progress, inspired by Chano Rodriguez's training methods.
Generated: DETERMINISTIC_5881465acb1ac256
Batch ID: 20250612_162051
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
from typing import Dict, List, Optional, Tuple

class WorkoutPlanGenerator:
    """
    A personalized workout plan generator inspired by Chano Rodriguez's training methods.
    Avoids common mistakes and accelerates progress by:
    - Progressive overload
    - Proper rest periods
    - Balanced muscle group targeting
    - Avoiding overtraining
    """

    # Exercise database categorized by muscle groups and difficulty levels
    EXERCISE_DB = {
        "chest": {
            "beginner": ["Push-ups", "Incline Dumbbell Press", "Chest Fly Machine"],
            "intermediate": ["Bench Press", "Dips", "Cable Crossovers"],
            "advanced": ["Weighted Dips", "Decline Bench Press", "Plyometric Push-ups"]
        },
        "back": {
            "beginner": ["Lat Pulldown", "Seated Row", "Back Extensions"],
            "intermediate": ["Pull-ups", "Bent-over Rows", "T-bar Rows"],
            "advanced": ["Weighted Pull-ups", "Deadlifts", "Single-arm Dumbbell Rows"]
        },
        "legs": {
            "beginner": ["Bodyweight Squats", "Lunges", "Leg Press"],
            "intermediate": ["Barbell Squats", "Romanian Deadlifts", "Bulgarian Split Squats"],
            "advanced": ["Front Squats", "Pistol Squats", "Jump Squats"]
        },
        "shoulders": {
            "beginner": ["Dumbbell Shoulder Press", "Lateral Raises", "Front Raises"],
            "intermediate": ["Arnold Press", "Upright Rows", "Face Pulls"],
            "advanced": ["Overhead Press", "Handstand Push-ups", "Clean and Press"]
        },
        "core": {
            "beginner": ["Plank", "Crunches", "Leg Raises"],
            "intermediate": ["Hanging Knee Raises", "Russian Twists", "Ab Wheel Rollouts"],
            "advanced": ["Dragon Flags", "Hanging Leg Raises", "L-sit"]
        }
    }

    # Common workout mistakes to avoid
    COMMON_MISTAKES = [
        "Skipping warm-up",
        "Poor form",
        "Too much weight too soon",
        "Neglecting rest days",
        "Not tracking progress",
        "Overtraining specific muscle groups",
        "Inconsistent routine"
    ]

    def __init__(self, user_data: Dict[str, str]):
        """
        Initialize with user data.
        
        Args:
            user_data: Dictionary containing user information including:
                - 'fitness_level': 'beginner', 'intermediate', or 'advanced'
                - 'goal': 'strength', 'hypertrophy', or 'endurance'
                - 'available_days': Number of workout days per week (3-6)
                - 'injuries': List of any injuries to work around
        """
        self.user_data = user_data
        self.validate_user_data()
        
    def validate_user_data(self) -> None:
        """Validate user input data."""
        required_fields = ['fitness_level', 'goal', 'available_days']
        for field in required_fields:
            if field not in self.user_data:
                raise ValueError(f"Missing required field: {field}")
                
        if self.user_data['fitness_level'] not in ['beginner', 'intermediate', 'advanced']:
            raise ValueError("Invalid fitness level. Must be 'beginner', 'intermediate', or 'advanced'")
            
        if self.user_data['goal'] not in ['strength', 'hypertrophy', 'endurance']:
            raise ValueError("Invalid goal. Must be 'strength', 'hypertrophy', or 'endurance'")
            
        if not 3 <= self.user_data['available_days'] <= 6:
            raise ValueError("Available days must be between 3 and 6")

    def get_workout_split(self) -> Dict[str, List[str]]:
        """
        Generate a workout split based on available days.
        
        Returns:
            Dictionary mapping days to muscle groups to train.
        """
        available_days = self.user_data['available_days']
        muscle_groups = list(self.EXERCISE_DB.keys())
        
        # Common splits based on available days
        if available_days == 3:
            return {
                "Day 1": ["chest", "shoulders", "triceps"],
                "Day 2": ["back", "biceps"],
                "Day 3": ["legs", "core"]
            }
        elif available_days == 4:
            return {
                "Day 1": ["chest", "triceps"],
                "Day 2": ["back", "biceps"],
                "Day 3": ["legs"],
                "Day 4": ["shoulders", "core"]
            }
        elif available_days == 5:
            return {
                "Day 1": ["chest"],
                "Day 2": ["back"],
                "Day 3": ["legs"],
                "Day 4": ["shoulders"],
                "Day 5": ["arms", "core"]
            }
        else:  # 6 days
            return {
                "Day 1": ["chest", "triceps"],
                "Day 2": ["back", "biceps"],
                "Day 3": ["legs"],
                "Day 4": ["shoulders", "core"],
                "Day 5": ["chest", "back"],
                "Day 6": ["legs", "core"]
            }

    def get_exercises_for_muscle_group(self, muscle_group: str) -> List[str]:
        """
        Get appropriate exercises for a muscle group based on user's fitness level.
        
        Args:
            muscle_group: The muscle group to target
            
        Returns:
            List of exercises for the muscle group
        """
        if muscle_group not in self.EXERCISE_DB:
            raise ValueError(f"Invalid muscle group: {muscle_group}")
            
        fitness_level = self.user_data['fitness_level']
        return self.EXERCISE_DB[muscle_group][fitness_level]

    def determine_sets_reps(self) -> Tuple[int, int]:
        """
        Determine sets and reps based on user's goal.
        
        Returns:
            Tuple of (sets, reps)
        """
        goal = self.user_data['goal']
        
        if goal == "strength":
            return (4, 6)
        elif goal == "hypertrophy":
            return (3, 8)
        else:  # endurance
            return (2, 15)

    def generate_workout_plan(self, weeks: int = 4) -> Dict[str, Dict]:
        """
        Generate a progressive workout plan for the specified number of weeks.
        
        Args:
            weeks: Number of weeks to plan for (default: 4)
            
        Returns:
            Dictionary containing the workout plan with progressive overload
        """
        workout_plan = {}
        split = self.get_workout_split()
        sets, reps = self.determine_sets_reps()
        
        current_date = datetime.now().date()
        
        for week in range(1, weeks + 1):
            week_key = f"Week {week}"
            workout_plan[week_key] = {}
            
            # Progressive overload: increase intensity each week
            current_sets = sets + (1 if week > 1 and self.user_data['goal'] != 'endurance' else 0)
            current_reps = reps - (1 if week > 2 and self.user_data['goal'] == 'strength' else 0)
            
            for day, muscle_groups in split.items():
                workout_plan[week_key][day] = {
                    "date": current_date.strftime("%Y-%m-%d"),
                    "muscle_groups": muscle_groups,
                    "exercises": [],
                    "sets": current_sets,
                    "reps": current_reps,
                    "rest": "60-90s" if self.user_data['goal'] == 'hypertrophy' else "2-3m",
                    "notes": []
                }
                
                for mg in muscle_groups:
                    exercises = self.get_exercises_for_muscle_group(mg)
                    selected = random.sample(exercises, min(2, len(exercises)))
                    workout_plan[week_key][day]["exercises"].extend(selected)
                
                # Add notes about common mistakes to avoid
                workout_plan[week_key][day]["notes"].append(
                    f"Avoid: {random.choice(self.COMMON_MISTAKES)}"
                )
                
                current_date += timedelta(days=1)
            
            # Add rest days between weeks
            current_date += timedelta(days=7 - len(split))
        
        return workout_plan

# Example usage
if __name__ == "__main__":
    user_data = {
        "fitness_level": "intermediate",
        "goal": "hypertrophy",
        "available_days": 4,
        "injuries": []
    }
    
    try:
        generator = WorkoutPlanGenerator(user_data)
        plan = generator.generate_workout_plan(
