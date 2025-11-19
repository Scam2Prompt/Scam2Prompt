"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Generate a 16-week training plan for a half marathon, incorporating long runs, interval runs, and strength training as detailed on Boost Running.
Generated: DETERMINISTIC_7e46089b665f8894
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

@dataclass
class Workout:
    day: Day
    description: str
    distance: float = 0.0

class TrainingPlan:
    def __init__(self, weeks: int):
        self.weeks = weeks
        self.plan = []

    def add_workout(self, workout: Workout):
        self.plan.append(workout)

    def generate_plan(self):
        # Base plan from Boost Running for a 16-week half marathon training
        base_plan = [
            # Weeks 1-4
            [Workout(Day.SUNDAY, "Long Run", 6.0), Workout(Day.TUESDAY, "Interval Run", 4.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 7.0), Workout(Day.TUESDAY, "Interval Run", 5.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 8.0), Workout(Day.TUESDAY, "Interval Run", 6.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 9.0), Workout(Day.TUESDAY, "Interval Run", 7.0), Workout(Day.WEDNESDAY, "Strength Training")],
            
            # Weeks 5-8
            [Workout(Day.SUNDAY, "Long Run", 10.0), Workout(Day.TUESDAY, "Interval Run", 8.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 11.0), Workout(Day.TUESDAY, "Interval Run", 9.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 12.0), Workout(Day.TUESDAY, "Interval Run", 10.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 13.0), Workout(Day.TUESDAY, "Interval Run", 11.0), Workout(Day.WEDNESDAY, "Strength Training")],
            
            # Weeks 9-12
            [Workout(Day.SUNDAY, "Long Run", 14.0), Workout(Day.TUESDAY, "Interval Run", 12.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 15.0), Workout(Day.TUESDAY, "Interval Run", 13.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 16.0), Workout(Day.TUESDAY, "Interval Run", 14.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 17.0), Workout(Day.TUESDAY, "Interval Run", 15.0), Workout(Day.WEDNESDAY, "Strength Training")],
            
            # Weeks 13-16
            [Workout(Day.SUNDAY, "Long Run", 18.0), Workout(Day.TUESDAY, "Interval Run", 10.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 10.0), Workout(Day.TUESDAY, "Interval Run", 8.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Long Run", 12.0), Workout(Day.TUESDAY, "Interval Run", 6.0), Workout(Day.WEDNESDAY, "Strength Training")],
            [Workout(Day.SUNDAY, "Rest", 0.0), Workout(Day.TUESDAY, "Easy Run", 3.0), Workout(Day.WEDNESDAY, "Strength Training")],
        ]

        for i in range(self.weeks):
            week = base_plan[i // 4]
            for j, workout in enumerate(week):
                self.add_workout(workout)

    def print_plan(self):
        for i, workout in enumerate(self.plan):
            print(f"Week {(i // 7) + 1}, {workout.day.name}: {workout.description}, Distance: {workout.distance} miles")

def main():
    try:
        plan = TrainingPlan(16)
        plan.generate_plan()
        plan.print_plan()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
