"""
Generated Code Metadata:
========================
Original URL: https://neighborgoods.com
Prompt: Generate a personalized fitness program for a beginner looking to improve overall wellness, incorporating elements from Kenko Fitness Solutions' approach in Tokyo.
Generated: DETERMINISTIC_2a6dcbef646fe373
Batch ID: 20250612_155226
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
from typing import List, Dict, Optional

class FitnessProgramGenerator:
    """
    A class to generate personalized fitness programs based on Kenko Fitness Solutions' approach.
    Designed for beginners looking to improve overall wellness.
    """
    
    def __init__(self, user_data: Dict[str, str]):
        """
        Initialize with user data.
        
        Args:
            user_data: Dictionary containing user information including:
                - name: User's name
                - age: User's age
                - gender: User's gender
                - fitness_level: Beginner/Intermediate/Advanced
                - goals: List of fitness goals
                - available_days: Days available for workout
                - available_time: Available time per session (minutes)
                - preferences: Any exercise preferences
        """
        self.user_data = user_data
        self.current_date = datetime.now().date()
        
        # Kenko Fitness core principles
        self.kenko_principles = [
            "Holistic Approach",
            "Mind-Body Connection",
            "Gradual Progression",
            "Functional Movements",
            "Recovery Focus"
        ]
        
        # Exercise database categorized by type
        self.exercises = {
            "warmup": [
                "Neck Rolls", "Arm Circles", "Torso Twists", 
                "Leg Swings", "Hip Circles", "Jumping Jacks"
            ],
            "cardio": [
                "Brisk Walking", "Jogging in Place", "Step Ups",
                "Jump Rope", "Dancing", "Cycling"
            ],
            "strength": [
                "Bodyweight Squats", "Wall Push-ups", "Chair Dips",
                "Plank", "Glute Bridges", "Superman Hold"
            ],
            "flexibility": [
                "Standing Hamstring Stretch", "Shoulder Stretch",
                "Chest Stretch", "Quad Stretch", "Cat-Cow Stretch"
            ],
            "mindfulness": [
                "Deep Breathing", "Guided Meditation", 
                "Body Scan", "Mindful Walking"
            ]
        }
    
    def _get_duration_based_exercises(self, category: str, duration: int) -> List[str]:
        """
        Select appropriate number of exercises based on available time.
        
        Args:
            category: Exercise category
            duration: Available time in minutes
            
        Returns:
            List of selected exercises
        """
        if duration < 10:
            return []
        
        exercise_count = min(
            max(1, duration // 10),  # At least 1 exercise per 10 minutes
            len(self.exercises[category])
        )
        
        return random.sample(self.exercises[category], exercise_count)
    
    def _generate_workout(self, day: str) -> Dict:
        """
        Generate a single workout session for a given day.
        
        Args:
            day: Day of the week
            
        Returns:
            Dictionary containing workout details
        """
        workout = {
            "day": day,
            "date": (self.current_date + timedelta(days=list(self.user_data["available_days"]).index(day))).strftime("%Y-%m-%d"),
            "duration_minutes": self.user_data["available_time"],
            "kenko_principle": random.choice(self.kenko_principles),
            "exercises": []
        }
        
        # Allocate time to different components
        warmup_time = max(5, min(10, self.user_data["available_time"] // 5))
        main_time = self.user_data["available_time"] - warmup_time - 5  # Leave 5 min for cooldown
        
        # Warm-up exercises
        workout["exercises"].extend([
            {"type": "warmup", "name": ex, "duration": warmup_time // 2}
            for ex in self._get_duration_based_exercises("warmup", warmup_time)
        ])
        
        # Main workout (cardio + strength)
        cardio_exercises = self._get_duration_based_exercises("cardio", main_time // 2)
        strength_exercises = self._get_duration_based_exercises("strength", main_time // 2)
        
        for ex in cardio_exercises:
            workout["exercises"].append({
                "type": "cardio",
                "name": ex,
                "duration": main_time // (len(cardio_exercises) + len(strength_exercises))
            })
            
        for ex in strength_exercises:
            workout["exercises"].append({
                "type": "strength",
                "name": ex,
                "duration": main_time // (len(cardio_exercises) + len(strength_exercises))
            })
        
        # Cooldown (flexibility + mindfulness)
        cooldown_exercises = self._get_duration_based_exercises("flexibility", 3) + \
                            self._get_duration_based_exercises("mindfulness", 2)
        
        for ex in cooldown_exercises:
            workout["exercises"].append({
                "type": "cooldown",
                "name": ex,
                "duration": 5 // len(cooldown_exercises)
            })
        
        return workout
    
    def generate_program(self, weeks: int = 4) -> Dict:
        """
        Generate a complete fitness program.
        
        Args:
            weeks: Duration of program in weeks
            
        Returns:
            Dictionary containing the full program
        """
        if not self.user_data.get("available_days"):
            raise ValueError("Available days must be specified")
            
        if not self.user_data.get("available_time") or self.user_data["available_time"] < 15:
            raise ValueError("Minimum 15 minutes per session required")
        
        program = {
            "user": self.user_data["name"],
            "start_date": self.current_date.strftime("%Y-%m-%d"),
            "end_date": (self.current_date + timedelta(weeks=weeks)).strftime("%Y-%m-%d"),
            "fitness_level": self.user_data.get("fitness_level", "beginner"),
            "goals": self.user_data.get("goals", ["improve overall wellness"]),
            "kenko_principles_applied": self.kenko_principles,
            "weekly_schedule": []
        }
        
        for week in range(1, weeks + 1):
            week_plan = {
                "week_number": week,
                "workouts": []
            }
            
            for day in self.user_data["available_days"]:
                week_plan["workouts"].append(self._generate_workout(day))
            
            program["weekly_schedule"].append(week_plan)
        
        return program

# Example usage
if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "age": 30,
        "gender": "male",
        "fitness_level": "beginner",
        "goals": ["improve stamina", "build strength", "reduce stress"],
        "available_days": ["Monday", "Wednesday", "Friday"],
        "available_time": 30,
        "preferences": ["bodyweight exercises"]
    }
    
    try:
        generator = FitnessProgramGenerator(user_data)
        program = generator.generate_program(weeks=4)
        print("Generated Fitness Program:")
        print(program)
    except ValueError as e:
        print(f"Error generating program: {e}")
```
