"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate a strength training program for an ice hockey athlete focusing on speed and explosiveness, inspired by Blaise Strong's coaching methods.
Generated: DETERMINISTIC_94214559c6d11cd8
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Exercise:
    """Represents a strength training exercise with relevant details."""
    
    def __init__(self, name: str, sets: int, reps: int, rest: int, notes: str = ""):
        """
        Initialize an Exercise.
        
        Args:
            name: Name of the exercise
            sets: Number of sets
            reps: Number of repetitions per set
            rest: Rest time in seconds between sets
            notes: Additional notes about the exercise
        """
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rest = rest
        self.notes = notes
    
    def to_dict(self) -> Dict:
        """Convert Exercise to dictionary for serialization."""
        return {
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "rest": self.rest,
            "notes": self.notes
        }

class TrainingDay:
    """Represents a single day of training with multiple exercises."""
    
    def __init__(self, day_name: str, focus: str, exercises: List[Exercise]):
        """
        Initialize a TrainingDay.
        
        Args:
            day_name: Name of the day (e.g., "Monday")
            focus: Primary focus of the training day
            exercises: List of exercises for the day
        """
        self.day_name = day_name
        self.focus = focus
        self.exercises = exercises
    
    def to_dict(self) -> Dict:
        """Convert TrainingDay to dictionary for serialization."""
        return {
            "day_name": self.day_name,
            "focus": self.focus,
            "exercises": [ex.to_dict() for ex in self.exercises]
        }

class TrainingProgram:
    """Represents a complete training program over multiple weeks."""
    
    def __init__(self, name: str, duration_weeks: int, athlete_level: str):
        """
        Initialize a TrainingProgram.
        
        Args:
            name: Name of the program
            duration_weeks: Duration in weeks
            athlete_level: Level of the athlete (e.g., "Intermediate")
        """
        self.name = name
        self.duration_weeks = duration_weeks
        self.athlete_level = athlete_level
        self.weekly_schedule = []
    
    def add_week(self, training_days: List[TrainingDay]) -> None:
        """Add a week of training days to the program."""
        if len(training_days) > 7:
            raise ValueError("A week cannot have more than 7 training days")
        self.weekly_schedule.append(training_days)
    
    def to_dict(self) -> Dict:
        """Convert TrainingProgram to dictionary for serialization."""
        return {
            "name": self.name,
            "duration_weeks": self.duration_weeks,
            "athlete_level": self.athlete_level,
            "weekly_schedule": [
                [day.to_dict() for day in week] 
                for week in self.weekly_schedule
            ]
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save the training program to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TrainingProgram':
        """Load a training program from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        program = cls(data['name'], data['duration_weeks'], data['athlete_level'])
        
        for week in data['weekly_schedule']:
            training_days = []
            for day in week:
                exercises = [
                    Exercise(
                        ex['name'], ex['sets'], ex['reps'], ex['rest'], ex.get('notes', '')
                    ) for ex in day['exercises']
                ]
                training_days.append(
                    TrainingDay(day['day_name'], day['focus'], exercises)
                )
            program.add_week(training_days)
        
        return program

def create_hockey_training_program() -> TrainingProgram:
    """Create a hockey-specific strength training program focused on speed and explosiveness."""
    program = TrainingProgram(
        name="Hockey Speed & Explosiveness Program",
        duration_weeks=8,
        athlete_level="Intermediate"
    )
    
    # Week 1-2: Foundation Phase
    week1_2 = [
        # Monday: Lower Body Power
        TrainingDay(
            "Monday",
            "Lower Body Power",
            [
                Exercise("Barbell Back Squat", 4, 5, 120, "70-75% 1RM"),
                Exercise("Romanian Deadlift", 3, 6, 90),
                Exercise("Box Jumps", 3, 5, 90),
                Exercise("Single-Leg Calf Raises", 3, 10, 60)
            ]
        ),
        # Wednesday: Upper Body & Core
        TrainingDay(
            "Wednesday",
            "Upper Body & Core",
            [
                Exercise("Bench Press", 4, 5, 120, "70-75% 1RM"),
                Exercise("Pull-Ups", 3, 6, 90),
                Exercise("Medicine Ball Slams", 3, 8, 60),
                Exercise("Plank", 3, 30, 60, "30 sec hold")
            ]
        ),
        # Friday: Explosive Power
        TrainingDay(
            "Friday",
            "Explosive Power",
            [
                Exercise("Power Cleans", 4, 3, 120, "60-65% 1RM"),
                Exercise("Bulgarian Split Squats", 3, 6, 90),
                Exercise("Broad Jumps", 3, 5, 90),
                Exercise("Russian Twists", 3, 12, 60)
            ]
        )
    ]
    
    # Week 3-4: Strength Phase
    week3_4 = [
        # Monday: Lower Body Strength
        TrainingDay(
            "Monday",
            "Lower Body Strength",
            [
                Exercise("Barbell Back Squat", 5, 3, 150, "80-85% 1RM"),
                Exercise("Deadlift", 4, 4, 120),
                Exercise("Depth Jumps", 3, 5, 120),
                Exercise("Seated Calf Raises", 3, 12, 60)
            ]
        ),
        # Wednesday: Upper Body & Core
        TrainingDay(
            "Wednesday",
            "Upper Body & Core",
            [
                Exercise("Bench Press", 5, 3, 150, "80-85% 1RM"),
                Exercise("Bent Over Rows", 4, 5, 90),
                Exercise("Medicine Ball Chest Pass", 3, 8, 60),
                Exercise("Hanging Leg Raises", 3, 10, 60)
            ]
        ),
        # Friday: Explosive Power
        TrainingDay(
            "Friday",
            "Explosive Power",
            [
                Exercise("Power Cleans", 5, 3, 150, "70-75% 1RM"),
                Exercise("Front Squats", 4, 4, 120),
                Exercise("Single-Leg Hops", 3, 5, 90),
                Exercise("Anti-Rotation Press", 3, 8, 60)
            ]
        )
    ]
    
    # Week 5-6: Power Phase
    week5_6 = [
        # Monday: Lower Body Power
        TrainingDay(
            "Monday",
            "Lower Body Power",
            [
                Exercise("Barbell Back Squat", 4, 3, 180, "85-90% 1RM"),
                Exercise("Trap Bar Deadlift", 4, 3, 150),
                Exercise("Plyometric Box Jumps", 3, 5, 120),
                Exercise("Standing Calf Raises", 3, 10, 60)
            ]
        ),
        # Wednesday: Upper Body & Core
        TrainingDay(
            "Wednesday",
            "Upper Body & Core",
            [
                Exercise("Bench Press", 4, 3, 180, "85-90% 1RM"),
                Exercise("Weighted Pull-Ups", 3, 4, 120),
                Exercise("Overhead Medicine Ball Throws", 3, 6, 90),
                Exercise("Ab Wheel Rollouts", 3, 8, 60)
            ]
        ),
        # Friday: Explosive Power
        TrainingDay(
            "Friday",
            "Explosive Power",
            [
                Exercise("Hang Cleans", 4, 3, 180, "75-80% 1RM"),
                Exercise("Jump Squats", 3, 5, 120),
                Exercise("Lateral Bounds", 3, 5, 90),
                Exercise("Pallof Press", 3, 8, 60)
            ]
        )
    ]
    
    #
