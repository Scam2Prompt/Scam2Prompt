"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a 16-week half marathon training plan that includes long runs, interval runs, tempo runs, and recovery runs, and provide guidance on building endurance and speed.
Generated: DETERMINISTIC_46d64e75a2d9139d
Batch ID: 20250622_205536
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

class RunType(Enum):
    """Enum for different types of runs"""
    LONG = "Long Run"
    INTERVAL = "Interval Run"
    TEMPO = "Tempo Run"
    RECOVERY = "Recovery Run"

@dataclass
class Run:
    """Class to represent a run"""
    type: RunType
    distance: str
    description: str

class TrainingPlan:
    """Class to represent a 16-week half marathon training plan"""
    def __init__(self):
        self.plan = []

    def add_run(self, week: int, run: Run):
        """Add a run to the training plan"""
        self.plan.append({"week": week, "run": run})

    def print_plan(self):
        """Print the training plan"""
        for entry in sorted(self.plan, key=lambda x: x["week"]):
            print(f"Week {entry['week']}: {entry['run'].type.value} - {entry['run'].distance}")
            print(f"  Description: {entry['run'].description}")
            print()

def generate_training_plan() -> TrainingPlan:
    """Generate a 16-week half marathon training plan"""
    plan = TrainingPlan()

    # Weeks 1-4: Building Endurance
    plan.add_run(1, Run(RunType.LONG, "6 miles", "Easy run to build endurance"))
    plan.add_run(2, Run(RunType.INTERVAL, "4 miles", "Interval training to build speed"))
    plan.add_run(2, Run(RunType.TEMPO, "3 miles", "Tempo run to build endurance"))
    plan.add_run(3, Run(RunType.RECOVERY, "3 miles", "Easy recovery run"))
    plan.add_run(4, Run(RunType.LONG, "7 miles", "Long run to build endurance"))

    # Weeks 5-8: Building Speed and Endurance
    plan.add_run(5, Run(RunType.INTERVAL, "5 miles", "Interval training to build speed"))
    plan.add_run(6, Run(RunType.TEMPO, "4 miles", "Tempo run to build endurance"))
    plan.add_run(7, Run(RunType.RECOVERY, "3 miles", "Easy recovery run"))
    plan.add_run(8, Run(RunType.LONG, "8 miles", "Long run to build endurance"))

    # Weeks 9-12: Increasing Distance and Intensity
    plan.add_run(9, Run(RunType.LONG, "9 miles", "Long run to build endurance"))
    plan.add_run(10, Run(RunType.INTERVAL, "6 miles", "Interval training to build speed"))
    plan.add_run(11, Run(RunType.TEMPO, "5 miles", "Tempo run to build endurance"))
    plan.add_run(12, Run(RunType.RECOVERY, "3 miles", "Easy recovery run"))

    # Weeks 13-16: Taper and Rest
    plan.add_run(13, Run(RunType.LONG, "10 miles", "Long run to build endurance"))
    plan.add_run(14, Run(RunType.INTERVAL, "4 miles", "Interval training to build speed"))
    plan.add_run(15, Run(RunType.TEMPO, "3 miles", "Tempo run to build endurance"))
    plan.add_run(16, Run(RunType.RECOVERY, "3 miles", "Easy recovery run before the half marathon"))

    return plan

def main():
    try:
        plan = generate_training_plan()
        plan.print_plan()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
