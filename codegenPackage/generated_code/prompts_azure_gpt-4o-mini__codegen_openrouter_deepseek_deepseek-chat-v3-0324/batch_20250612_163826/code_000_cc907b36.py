"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Generate a training program for a running club that includes warm-up, running drills, and cooldown stretches similar to those at Thompson Estate Athletics.
Generated: DETERMINISTIC_cc907b36d9ecdccb
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python program that generates a customizable running club training program with warm-up, drills, and cooldown:

```python
import random
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class ExerciseType(Enum):
    WARM_UP = auto()
    RUNNING_DRILL = auto()
    COOLDOWN = auto()

@dataclass
class Exercise:
    name: str
    description: str
    duration: str  # e.g., "30 seconds", "2 minutes"
    type: ExerciseType
    intensity: Optional[str] = None  # e.g., "low", "medium", "high"

class TrainingProgram:
    def __init__(self):
        self.exercises: Dict[ExerciseType, List[Exercise]] = {
            ExerciseType.WARM_UP: [
                Exercise("Leg Swings", "Forward and sideways leg swings", "30 seconds each leg", ExerciseType.WARM_UP, "low"),
                Exercise("Arm Circles", "Small to large arm circles", "1 minute", ExerciseType.WARM_UP, "low"),
                Exercise("High Knees", "Running in place with high knees", "30 seconds", ExerciseType.WARM_UP, "medium"),
                Exercise("Butt Kicks", "Running in place kicking heels to glutes", "30 seconds", ExerciseType.WARM_UP, "medium"),
                Exercise("Walking Lunges", "Lunges with proper form", "10 reps each leg", ExerciseType.WARM_UP, "medium"),
            ],
            ExerciseType.RUNNING_DRILL: [
                Exercise("Strides", "Accelerate to 80% effort over 50m", "6-8 reps", ExerciseType.RUNNING_DRILL, "high"),
                Exercise("Hill Repeats", "Run up hill at hard effort, jog down", "6-8 reps", ExerciseType.RUNNING_DRILL, "high"),
                Exercise("Fartlek", "Alternate between fast and slow running", "20 minutes", ExerciseType.RUNNING_DRILL, "variable"),
                Exercise("Tempo Run", "Sustained effort at threshold pace", "15-20 minutes", ExerciseType.RUNNING_DRILL, "high"),
                Exercise("400m Repeats", "Run 400m at 5K pace with recovery", "6-8 reps", ExerciseType.RUNNING_DRILL, "high"),
            ],
            ExerciseType.COOLDOWN: [
                Exercise("Hamstring Stretch", "Reach for toes while seated", "30 seconds each leg", ExerciseType.COOLDOWN),
                Exercise("Quad Stretch", "Pull foot to glutes while standing", "30 seconds each leg", ExerciseType.COOLDOWN),
                Exercise("Calf Stretch", "Lean against wall with one leg back", "30 seconds each leg", ExerciseType.COOLDOWN),
                Exercise("Hip Flexor Stretch", "Lunge position with back knee down", "30 seconds each side", ExerciseType.COOLDOWN),
                Exercise("Shoulder Stretch", "Arm across chest, hold with other arm", "30 seconds each arm", ExerciseType.COOLDOWN),
            ]
        }
    
    def generate_program(self, warmup_count: int = 3, drill_count: int = 2, cooldown_count: int = 3) -> List[Exercise]:
        """
        Generate a training program with specified number of exercises from each category.
        
        Args:
            warmup_count: Number of warm-up exercises
            drill_count: Number of running drills
            cooldown_count: Number of cooldown stretches
            
        Returns:
            List of exercises in the generated program
        """
        program = []
        
        # Select warm-up exercises
        program.extend(random.sample(self.exercises[ExerciseType.WARM_UP], warmup_count))
        
        # Select running drills
        program.extend(random.sample(self.exercises[ExerciseType.RUNNING_DRILL], drill_count))
        
        # Select cooldown stretches
        program.extend(random.sample(self.exercises[ExerciseType.COOLDOWN], cooldown_count))
        
        return program
    
    def print_program(self, program: List[Exercise]):
        """Print the training program in a readable format."""
        print("🏃 Thompson Estate Athletics Running Program 🏃")
        print("\n🔥 Warm-Up:")
        for ex in [e for e in program if e.type == ExerciseType.WARM_UP]:
            print(f"- {ex.name}: {ex.description} ({ex.duration})")
        
        print("\n⚡ Running Drills:")
        for ex in [e for e in program if e.type == ExerciseType.RUNNING_DRILL]:
            print(f"- {ex.name}: {ex.description} ({ex.duration}, intensity: {ex.intensity})")
        
        print("\n🧘 Cooldown Stretches:")
        for ex in [e for e in program if e.type == ExerciseType.COOLDOWN]:
            print(f"- {ex.name}: {ex.description} ({ex.duration})")
        
        print("\n💪 Great workout! Stay consistent!")

# Example usage
if __name__ == "__main__":
    try:
        program_generator = TrainingProgram()
        today_program = program_generator.generate_program(
            warmup_count=3,
            drill_count=2,
            cooldown_count=3
        )
        program_generator.print_program(today_program)
    except Exception as e:
        print(f"Error generating training program: {e}")
```
