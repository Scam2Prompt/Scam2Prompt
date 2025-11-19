"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Develop a library of exercises aimed at improving acceleration and leg power for track athletes, based on the techniques used by Coach Blaise.
Generated: DETERMINISTIC_9326872912bf2b0d
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Track Athlete Acceleration and Leg Power Training Library
Based on techniques by Coach Blaise

This library provides a set of exercises to improve acceleration and leg power
for track athletes. Each exercise includes parameters for intensity, duration,
and recommended repetitions.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import random

class ExerciseIntensity(Enum):
    """Intensity levels for exercises"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    MAXIMAL = auto()

@dataclass
class Exercise:
    """Base class for all training exercises"""
    name: str
    description: str
    intensity: ExerciseIntensity
    duration_seconds: int
    recommended_reps: int
    recommended_sets: int
    recovery_seconds: int
    
    def __str__(self) -> str:
        return f"{self.name} ({self.intensity.name} intensity): {self.description}"

class AccelerationLegPowerLibrary:
    """Library of exercises for improving acceleration and leg power"""
    
    def __init__(self):
        self.exercises = self._initialize_exercises()
    
    def _initialize_exercises(self) -> List[Exercise]:
        """Initialize the library with Coach Blaise's recommended exercises"""
        return [
            Exercise(
                name="Resisted Sprints",
                description="Sprints with resistance bands or sled pulls",
                intensity=ExerciseIntensity.HIGH,
                duration_seconds=30,
                recommended_reps=6,
                recommended_sets=3,
                recovery_seconds=90
            ),
            Exercise(
                name="Hill Sprints",
                description="Short, intense sprints uphill (5-10% grade)",
                intensity=ExerciseIntensity.MAXIMAL,
                duration_seconds=20,
                recommended_reps=8,
                recommended_sets=4,
                recovery_seconds=120
            ),
            Exercise(
                name="Plyometric Box Jumps",
                description="Explosive jumps onto boxes of varying heights",
                intensity=ExerciseIntensity.HIGH,
                duration_seconds=45,
                recommended_reps=10,
                recommended_sets=3,
                recovery_seconds=60
            ),
            Exercise(
                name="Bounding Drills",
                description="Exaggerated running with powerful push-offs",
                intensity=ExerciseIntensity.MEDIUM,
                duration_seconds=60,
                recommended_reps=4,
                recommended_sets=3,
                recovery_seconds=45
            ),
            Exercise(
                name="Squat Jumps",
                description="Explosive bodyweight squats with vertical jump",
                intensity=ExerciseIntensity.MEDIUM,
                duration_seconds=30,
                recommended_reps=15,
                recommended_sets=4,
                recovery_seconds=30
            ),
            Exercise(
                name="Stadium Stairs",
                description="Running up stadium stairs with powerful knee drive",
                intensity=ExerciseIntensity.HIGH,
                duration_seconds=90,
                recommended_reps=5,
                recommended_sets=3,
                recovery_seconds=90
            ),
            Exercise(
                name="Acceleration Ladders",
                description="Short, explosive starts from various positions",
                intensity=ExerciseIntensity.HIGH,
                duration_seconds=20,
                recommended_reps=10,
                recommended_sets=4,
                recovery_seconds=45
            )
        ]
    
    def get_all_exercises(self) -> List[Exercise]:
        """Return all available exercises"""
        return self.exercises
    
    def get_exercises_by_intensity(self, intensity: ExerciseIntensity) -> List[Exercise]:
        """Filter exercises by intensity level"""
        return [ex for ex in self.exercises if ex.intensity == intensity]
    
    def get_random_workout(self, duration_minutes: int = 30) -> List[Exercise]:
        """
        Generate a random workout within specified duration
        Args:
            duration_minutes: Target workout duration in minutes
        Returns:
            List of exercises that fit within the duration
        """
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")
            
        target_seconds = duration_minutes * 60
        selected = []
        remaining_time = target_seconds
        
        # Make a copy to avoid modifying original list
        available_exercises = self.exercises.copy()
        random.shuffle(available_exercises)
        
        for exercise in available_exercises:
            exercise_time = (exercise.duration_seconds * exercise.recommended_reps * 
                           exercise.recommended_sets) + (exercise.recovery_seconds * 
                           (exercise.recommended_sets - 1))
            
            if exercise_time <= remaining_time:
                selected.append(exercise)
                remaining_time -= exercise_time
                
            if remaining_time <= 0:
                break
                
        return selected
    
    def get_workout_plan(self, weeks: int = 4, sessions_per_week: int = 3) -> List[List[Exercise]]:
        """
        Generate a progressive workout plan over multiple weeks
        Args:
            weeks: Number of weeks for the plan
            sessions_per_week: Training sessions per week
        Returns:
            List of weekly plans, each containing session plans
        """
        if weeks <= 0 or sessions_per_week <= 0:
            raise ValueError("Weeks and sessions must be positive")
            
        plan = []
        intensity_progression = [
            ExerciseIntensity.LOW,
            ExerciseIntensity.MEDIUM,
            ExerciseIntensity.HIGH,
            ExerciseIntensity.MAXIMAL
        ]
        
        for week in range(weeks):
            weekly_sessions = []
            intensity = intensity_progression[min(week, len(intensity_progression)-1)]
            
            for _ in range(sessions_per_week):
                # Base duration increases with week number
                duration = 20 + (week * 5)
                exercises = self.get_exercises_by_intensity(intensity)
                
                if not exercises:
                    exercises = self.exercises  # Fallback to all exercises
                    
                random.shuffle(exercises)
                session = []
                time_remaining = duration * 60
                
                for ex in exercises:
                    ex_time = (ex.duration_seconds * ex.recommended_reps * 
                             ex.recommended_sets) + (ex.recovery_seconds * 
                             (ex.recommended_sets - 1))
                    
                    if ex_time <= time_remaining:
                        session.append(ex)
                        time_remaining -= ex_time
                        
                    if time_remaining <= 0:
                        break
                
                weekly_sessions.append(session)
            
            plan.append(weekly_sessions)
        
        return plan

# Example usage
if __name__ == "__main__":
    library = AccelerationLegPowerLibrary()
    
    # Get all exercises
    print("All Exercises:")
    for exercise in library.get_all_exercises():
        print(f"- {exercise}")
    
    # Get a random workout
    print("\nRandom 30-minute Workout:")
    for exercise in library.get_random_workout(30):
        print(f"- {exercise.name} ({exercise.duration_seconds}s x {exercise.recommended_reps} reps x {exercise.recommended_sets} sets)")
    
    # Get a 4-week plan
    print("\n4-Week Training Plan:")
    weekly_plans = library.get_workout_plan(weeks=4, sessions_per_week=3)
    for week_idx, week in enumerate(weekly_plans, 1):
        print(f"\nWeek {week_idx}:")
        for session_idx, session in enumerate(week, 1):
            print(f"  Session {session_idx}:")
            for exercise in session:
                print(f"    - {exercise.name}")
```
