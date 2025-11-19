"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Describe the key components of a 10-mile running plan, including the types of workouts and their purposes, as explained on Boost Running.
Generated: DETERMINISTIC_a2dd5a0c0a07b067
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A 10-mile running plan generator based on Boost Running principles.
This script outlines the key components of a training plan including workout types and their purposes.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class WorkoutType(Enum):
    """Enum representing different types of running workouts."""
    LONG_RUN = auto()
    TEMPO_RUN = auto()
    INTERVAL_TRAINING = auto()
    RECOVERY_RUN = auto()
    STRENGTH_TRAINING = auto()
    REST_DAY = auto()

@dataclass
class Workout:
    """Data class representing a single workout in the training plan."""
    workout_type: WorkoutType
    description: str
    purpose: str
    typical_duration: str  # Could be miles or minutes
    intensity: str  # Low, Medium, High

def generate_10_mile_plan() -> List[Workout]:
    """
    Generates a 10-mile running training plan based on Boost Running principles.
    
    Returns:
        List[Workout]: A list of workout objects representing the training plan components.
    """
    return [
        Workout(
            workout_type=WorkoutType.LONG_RUN,
            description="Extended duration run at comfortable pace",
            purpose="Build endurance and mental toughness",
            typical_duration="6-10 miles",
            intensity="Medium"
        ),
        Workout(
            workout_type=WorkoutType.TEMPO_RUN,
            description="Sustained effort at slightly faster than race pace",
            purpose="Improve lactate threshold and race pace efficiency",
            typical_duration="4-6 miles (including warmup/cooldown)",
            intensity="High"
        ),
        Workout(
            workout_type=WorkoutType.INTERVAL_TRAINING,
            description="Short, fast repeats with recovery periods",
            purpose="Increase speed and VO2 max",
            typical_duration="5-8 x 400m-800m repeats",
            intensity="High"
        ),
        Workout(
            workout_type=WorkoutType.RECOVERY_RUN,
            description="Easy, relaxed pace run",
            purpose="Promote recovery while maintaining mileage",
            typical_duration="3-5 miles",
            intensity="Low"
        ),
        Workout(
            workout_type=WorkoutType.STRENGTH_TRAINING,
            description="Core and leg strengthening exercises",
            purpose="Improve running economy and prevent injuries",
            typical_duration="30-45 minutes",
            intensity="Medium"
        ),
        Workout(
            workout_type=WorkoutType.REST_DAY,
            description="Complete rest or active recovery",
            purpose="Allow body to recover and adapt",
            typical_duration="1 day",
            intensity="None"
        )
    ]

def display_plan(plan: List[Workout]) -> None:
    """Prints the training plan in a readable format."""
    print("10-Mile Running Training Plan Components:")
    print("=" * 50)
    for workout in plan:
        print(f"\nWorkout Type: {workout.workout_type.name.replace('_', ' ').title()}")
        print(f"Description: {workout.description}")
        print(f"Purpose: {workout.purpose}")
        print(f"Typical Duration: {workout.typical_duration}")
        print(f"Intensity: {workout.intensity}")

if __name__ == "__main__":
    try:
        plan = generate_10_mile_plan()
        display_plan(plan)
    except Exception as e:
        print(f"Error generating training plan: {e}")
```
