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
class RunningPlan:
    def __init__(self, distance, duration):
        """
        Initialize a running plan.

        Args:
            distance (int): The target distance in miles.
            duration (int): The target duration in weeks.
        """
        self.distance = distance
        self.duration = duration
        self.workouts = []

    def add_workout(self, workout):
        """
        Add a workout to the plan.

        Args:
            workout (Workout): The workout to add.
        """
        self.workouts.append(workout)


class Workout:
    def __init__(self, name, purpose, description):
        """
        Initialize a workout.

        Args:
            name (str): The name of the workout.
            purpose (str): The purpose of the workout.
            description (str): A description of the workout.
        """
        self.name = name
        self.purpose = purpose
        self.description = description


class TenMileRunningPlan(RunningPlan):
    def __init__(self):
        """
        Initialize a 10-mile running plan.
        """
        super().__init__(10, 8)
        self.create_plan()

    def create_plan(self):
        """
        Create a sample 10-mile running plan.
        """
        # Week 1-2: Base building
        self.add_workout(Workout("Easy Run", "Endurance", "30 minutes at a conversational pace"))
        self.add_workout(Workout("Brisk Walk", "Endurance", "30 minutes at a brisk pace"))

        # Week 3-4: Building endurance
        self.add_workout(Workout("Interval Training", "Speed and Endurance", "Alternate between 2 minutes of fast running and 2 minutes of walking"))
        self.add_workout(Workout("Hill Repeats", "Strength and Endurance", "Repeat 3-5 times: run up a hill at a high intensity, then walk or jog back down"))

        # Week 5-6: Building speed and endurance
        self.add_workout(Workout("Tempo Run", "Endurance and Speed", "20-30 minutes at a moderate to fast pace"))
        self.add_workout(Workout("Long Run", "Endurance", "Gradually increase the distance to build endurance"))

        # Week 7-8: Taper and rest
        self.add_workout(Workout("Easy Run", "Maintenance", "30 minutes at a conversational pace"))
        self.add_workout(Workout("Rest Day", "Recovery", "Take a day off to rest and recover"))


def print_plan(plan):
    """
    Print a running plan.

    Args:
        plan (RunningPlan): The plan to print.
    """
    print(f"Target Distance: {plan.distance} miles")
    print(f"Target Duration: {plan.duration} weeks")
    print("Workouts:")
    for i, workout in enumerate(plan.workouts):
        print(f"Week {i+1}: {workout.name} - {workout.purpose}")
        print(f"  Description: {workout.description}")


def main():
    try:
        plan = TenMileRunningPlan()
        print_plan(plan)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
