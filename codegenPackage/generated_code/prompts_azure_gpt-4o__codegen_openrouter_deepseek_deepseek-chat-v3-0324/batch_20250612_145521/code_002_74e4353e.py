"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate code to design a personalized fitness plan for athletes in multiple sports (e.g., hockey, MMA, track) using input parameters like age, sport, and fitness goals, as highlighted on Blaise Strong's website.
Generated: DETERMINISTIC_74e4353e33b5220a
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class Sport(Enum):
    """Enum representing different sports."""
    HOCKEY = "hockey"
    MMA = "mma"
    TRACK = "track"
    BASKETBALL = "basketball"
    SOCCER = "soccer"

class Goal(Enum):
    """Enum representing different fitness goals."""
    STRENGTH = "strength"
    ENDURANCE = "endurance"
    SPEED = "speed"
    AGILITY = "agility"
    POWER = "power"

class FitnessPlan:
    """Class representing a personalized fitness plan."""
    
    def __init__(self, age: int, sport: Sport, goal: Goal, days_per_week: int):
        """
        Initialize a fitness plan.
        
        Args:
            age: Athlete's age
            sport: Athlete's sport
            goal: Fitness goal
            days_per_week: Number of training days per week
        """
        self.age = age
        self.sport = sport
        self.goal = goal
        self.days_per_week = days_per_week
        self.workouts = self._generate_workouts()
    
    def _generate_workouts(self) -> List[Dict]:
        """Generate workouts based on athlete's parameters."""
        workouts = []
        
        # Base workout template
        base_workout = {
            "warmup": "10-15 minutes dynamic stretching",
            "cooldown": "5-10 minutes static stretching"
        }
        
        # Sport-specific adjustments
        if self.sport == Sport.HOCKEY:
            base_workout.update({
                "sport_specific": "Plyometrics and explosive leg exercises"
            })
        elif self.sport == Sport.MMA:
            base_workout.update({
                "sport_specific": "Core strengthening and grappling drills"
            })
        elif self.sport == Sport.TRACK:
            base_workout.update({
                "sport_specific": "Sprint intervals and form drills"
            })
        
        # Goal-specific adjustments
        if self.goal == Goal.STRENGTH:
            base_workout.update({
                "primary_focus": "Heavy compound lifts (3-5 reps)",
                "secondary_focus": "Accessory movements (8-12 reps)"
            })
        elif self.goal == Goal.ENDURANCE:
            base_workout.update({
                "primary_focus": "High-rep circuits (15-20 reps)",
                "secondary_focus": "Cardio intervals"
            })
        elif self.goal == Goal.SPEED:
            base_workout.update({
                "primary_focus": "Explosive movements",
                "secondary_focus": "Reaction drills"
            })
        
        # Age adjustments
        if self.age < 18:
            base_workout.update({
                "age_note": "Focus on technique and gradual progression",
                "volume": "Moderate"
            })
        elif self.age > 40:
            base_workout.update({
                "age_note": "Emphasize recovery and joint health",
                "volume": "Lower intensity, higher frequency"
            })
        else:
            base_workout.update({
                "age_note": "Standard programming",
                "volume": "High intensity"
            })
        
        # Generate workout days
        for day in range(1, self.days_per_week + 1):
            workout = base_workout.copy()
            workout["day"] = day
            workout["focus"] = self._get_day_focus(day)
            workouts.append(workout)
        
        return workouts
    
    def _get_day_focus(self, day: int) -> str:
        """Determine the focus for a specific training day."""
        if self.goal == Goal.STRENGTH:
            focuses = ["Upper Body", "Lower Body", "Full Body"]
        elif self.goal == Goal.ENDURANCE:
            focuses = ["Cardio", "Circuit Training", "Active Recovery"]
        else:
            focuses = ["Power", "Speed", "Agility"]
        
        return focuses[(day - 1) % len(focuses)]
    
    def to_json(self) -> str:
        """Convert the fitness plan to JSON format."""
        return json.dumps({
            "age": self.age,
            "sport": self.sport.value,
            "goal": self.goal.value,
            "days_per_week": self.days_per_week,
            "workouts": self.workouts
        }, indent=2)

class FitnessPlanGenerator:
    """Class to generate and manage fitness plans."""
    
    @staticmethod
    def create_plan(age: int, sport: str, goal: str, days_per_week: int) -> Optional[FitnessPlan]:
        """
        Create a fitness plan with validation.
        
        Args:
            age: Athlete's age
            sport: Athlete's sport
            goal: Fitness goal
            days_per_week: Number of training days per week
            
        Returns:
            FitnessPlan if valid, None otherwise
        """
        try:
            # Validate inputs
            if not (12 <= age <= 80):
                raise ValueError("Age must be between 12 and 80")
            if not (1 <= days_per_week <= 7):
                raise ValueError("Days per week must be between 1 and 7")
            
            sport_enum = Sport(sport.lower())
            goal_enum = Goal(goal.lower())
            
            return FitnessPlan(age, sport_enum, goal_enum, days_per_week)
        
        except ValueError as e:
            print(f"Error creating fitness plan: {e}")
            return None

# Example usage
if __name__ == "__main__":
    plan = FitnessPlanGenerator.create_plan(
        age=25,
        sport="hockey",
        goal="strength",
        days_per_week=4
    )
    
    if plan:
        print(plan.to_json())
```
