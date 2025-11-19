"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a dynamic warm-up routine for runners that aligns with the guidelines provided in the Ultimate Guide to Dynamic Warm-Up for Runners on Boost Running.
Generated: DETERMINISTIC_2fc21aec5f58380a
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class DynamicWarmUpRoutine:
    """
    A dynamic warm-up routine generator for runners based on Boost Running's guidelines.
    Provides randomized warm-up exercises targeting different muscle groups.
    """
    
    def __init__(self):
        self.exercises = {
            'leg_swings': {
                'name': 'Leg Swings',
                'description': 'Stand on one leg and swing the other leg forward and backward. Repeat for both legs.',
                'duration': '30 seconds per leg',
                'muscles': ['hamstrings', 'hip flexors']
            },
            'high_knees': {
                'name': 'High Knees',
                'description': 'Run in place while lifting knees as high as possible.',
                'duration': '30 seconds',
                'muscles': ['quadriceps', 'hip flexors', 'calves']
            },
            'butt_kicks': {
                'name': 'Butt Kicks',
                'description': 'Run in place while kicking heels up towards glutes.',
                'duration': '30 seconds',
                'muscles': ['hamstrings', 'calves']
            },
            'lunge_with_twist': {
                'name': 'Lunge with Twist',
                'description': 'Step forward into lunge, then twist torso toward front leg. Alternate sides.',
                'duration': '10 reps per side',
                'muscles': ['quadriceps', 'glutes', 'core']
            },
            'side_lunges': {
                'name': 'Side Lunges',
                'description': 'Step to the side into a lunge, keeping other leg straight. Alternate sides.',
                'duration': '10 reps per side',
                'muscles': ['adductors', 'glutes']
            },
            'arm_circles': {
                'name': 'Arm Circles',
                'description': 'Extend arms out to sides and make small circles, then reverse direction.',
                'duration': '30 seconds forward, 30 seconds backward',
                'muscles': ['shoulders', 'upper back']
            },
            'walking_quad_stretch': {
                'name': 'Walking Quad Stretch',
                'description': 'While walking, grab one ankle and pull heel toward glutes. Alternate legs.',
                'duration': '10 reps per leg',
                'muscles': ['quadriceps']
            },
            'inchworms': {
                'name': 'Inchworms',
                'description': 'From standing, bend forward to touch toes, then walk hands out to plank position and back.',
                'duration': '8-10 reps',
                'muscles': ['hamstrings', 'shoulders', 'core']
            }
        }
    
    def generate_routine(self, duration_minutes: int = 10) -> List[Dict]:
        """
        Generate a randomized warm-up routine based on desired duration.
        
        Args:
            duration_minutes: Target duration for warm-up in minutes (default: 10)
            
        Returns:
            List of exercises with details
        """
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer")
            
        available_exercises = list(self.exercises.keys())
        routine = []
        time_remaining = duration_minutes * 60  # Convert to seconds
        
        while time_remaining > 0 and available_exercises:
            # Select random exercise
            exercise_key = random.choice(available_exercises)
            exercise = self.exercises[exercise_key]
            
            # Add to routine
            routine.append(exercise)
            
            # Estimate time (30 sec for time-based, 45 sec for rep-based)
            if 'seconds' in exercise['duration']:
                time_remaining -= 30
            else:
                time_remaining -= 45
                
            # Remove from available to avoid duplicates
            available_exercises.remove(exercise_key)
            
            # If we're running low on time, prioritize shorter exercises
            if time_remaining < 60 and len(available_exercises) > 2:
                available_exercises = [e for e in available_exercises 
                                     if 'seconds' in self.exercises[e]['duration']]
        
        return routine
    
    def print_routine(self, routine: List[Dict]):
        """Print the warm-up routine in a user-friendly format."""
        if not routine:
            print("No exercises in the routine.")
            return
            
        print("\n=== Dynamic Warm-Up Routine ===\n")
        for i, exercise in enumerate(routine, 1):
            print(f"{i}. {exercise['name']}")
            print(f"   - Description: {exercise['description']}")
            print(f"   - Duration: {exercise['duration']}")
            print(f"   - Targets: {', '.join(exercise['muscles'])}\n")
        print("=== Complete your warm-up and enjoy your run! ===\n")


# Example usage
if __name__ == "__main__":
    try:
        warm_up = DynamicWarmUpRoutine()
        routine = warm_up.generate_routine(duration_minutes=10)
        warm_up.print_routine(routine)
    except Exception as e:
        print(f"Error generating warm-up routine: {e}")
```
