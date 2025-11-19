"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write Python code to generate a personalized 10-mile running plan, incorporating easy runs, long runs, hill repeats, and strides, as outlined on Boost Running.
Generated: DETERMINISTIC_98182d7e442cd4da
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class WorkoutType(Enum):
    EASY_RUN = "Easy Run"
    LONG_RUN = "Long Run"
    HILL_REPEATS = "Hill Repeats"
    STRIDES = "Strides"

@dataclass
class Workout:
    type: WorkoutType
    distance: float  # in miles
    intensity: str

class RunningPlan:
    def __init__(self, goal_distance: float, easy_run_percentage: float, long_run_percentage: float, 
                 hill_repeats_percentage: float, strides_percentage: float):
        """
        Initialize a 10-mile running plan.

        Args:
        goal_distance (float): The goal distance of the plan (10 miles).
        easy_run_percentage (float): The percentage of easy runs.
        long_run_percentage (float): The percentage of long runs.
        hill_repeats_percentage (float): The percentage of hill repeats.
        strides_percentage (float): The percentage of strides.
        """
        self.goal_distance = goal_distance
        self.easy_run_percentage = easy_run_percentage
        self.long_run_percentage = long_run_percentage
        self.hill_repeats_percentage = hill_repeats_percentage
        self.strides_percentage = strides_percentage

    def generate_plan(self) -> List[Workout]:
        """
        Generate a personalized 10-mile running plan.

        Returns:
        List[Workout]: A list of workouts for the plan.
        """
        plan = []
        total_distance = 0

        # Calculate distances for each type of workout
        easy_run_distance = self.goal_distance * self.easy_run_percentage / 100
        long_run_distance = self.goal_distance * self.long_run_percentage / 100
        hill_repeats_distance = self.goal_distance * self.hill_repeats_percentage / 100
        strides_distance = self.goal_distance * self.strides_percentage / 100

        # Add easy run
        if easy_run_distance > 0:
            plan.append(Workout(WorkoutType.EASY_RUN, easy_run_distance, "Conversational pace"))
            total_distance += easy_run_distance

        # Add long run
        if long_run_distance > 0:
            plan.append(Workout(WorkoutType.LONG_RUN, long_run_distance, "Moderate to fast pace"))
            total_distance += long_run_distance

        # Add hill repeats
        if hill_repeats_distance > 0:
            plan.append(Workout(WorkoutType.HILL_REPEATS, hill_repeats_distance, "High intensity"))
            total_distance += hill_repeats_distance

        # Add strides
        if strides_distance > 0:
            plan.append(Workout(WorkoutType.STRIDES, strides_distance, "Fast pace"))
            total_distance += strides_distance

        # Check if total distance meets goal distance
        if total_distance < self.goal_distance:
            plan[-1] = Workout(plan[-1].type, plan[-1].distance + (self.goal_distance - total_distance), plan[-1].intensity)

        return plan

def main():
    try:
        plan = RunningPlan(10, 40, 20, 20, 20)
        workouts = plan.generate_plan()
        for i, workout in enumerate(workouts):
            print(f"Day {i+1}: {workout.type.value} - Distance: {workout.distance} miles, Intensity: {workout.intensity}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
