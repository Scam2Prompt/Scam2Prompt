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

Here's a Python implementation that generates a 16-week half marathon training plan:

```python
from enum import Enum
from dataclasses import dataclass
from typing import List
import datetime

class RunType(Enum):
    """Types of training runs in the plan"""
    LONG_RUN = "Long Run"
    INTERVAL = "Interval Run"
    TEMPO = "Tempo Run"
    RECOVERY = "Recovery Run"
    REST = "Rest Day"
    CROSS_TRAIN = "Cross Training"

@dataclass
class TrainingDay:
    """Represents a single day in the training plan"""
    date: datetime.date
    run_type: RunType
    description: str
    distance_km: float = None
    notes: str = None

class HalfMarathonPlan:
    """16-week half marathon training plan generator"""
    
    def __init__(self, start_date: datetime.date):
        self.start_date = start_date
        self.plan_duration_weeks = 16
        self.plan = []
        
    def generate_plan(self) -> List[TrainingDay]:
        """Generate the complete training plan"""
        current_date = self.start_date
        
        for week in range(1, self.plan_duration_weeks + 1):
            self._add_week(current_date, week)
            current_date += datetime.timedelta(days=7)
            
        return self.plan
    
    def _add_week(self, start_date: datetime.date, week_num: int) -> None:
        """Add a week of training to the plan"""
        week_days = []
        
        # Week structure alternates between hard and easy weeks
        is_hard_week = week_num % 2 == 1
        
        # Monday
        week_days.append(TrainingDay(
            date=start_date,
            run_type=RunType.REST if week_num == 1 else RunType.RECOVERY,
            description="Rest day" if week_num == 1 else "Easy recovery run",
            distance_km=0 if week_num == 1 else 5
        ))
        
        # Tuesday
        if week_num < 3:
            week_days.append(TrainingDay(
                date=start_date + datetime.timedelta(days=1),
                run_type=RunType.RECOVERY,
                description="Easy run",
                distance_km=5 + (week_num * 0.5)
            ))
        else:
            week_days.append(TrainingDay(
                date=start_date + datetime.timedelta(days=1),
                run_type=RunType.INTERVAL,
                description=f"{'4-5' if is_hard_week else '3-4'} x 800m at 5K pace with 400m recovery",
                distance_km=8 if is_hard_week else 6
            ))
        
        # Wednesday
        week_days.append(TrainingDay(
            date=start_date + datetime.timedelta(days=2),
            run_type=RunType.CROSS_TRAIN,
            description="Cross training (cycling, swimming, etc.)",
            notes="30-45 minutes moderate effort"
        ))
        
        # Thursday
        if week_num < 4:
            week_days.append(TrainingDay(
                date=start_date + datetime.timedelta(days=3),
                run_type=RunType.RECOVERY,
                description="Easy run",
                distance_km=5 + (week_num * 0.5)
            ))
        else:
            week_days.append(TrainingDay(
                date=start_date + datetime.timedelta(days=3),
                run_type=RunType.TEMPO,
                description=f"{'5-6' if is_hard_week else '4-5'} km at half marathon pace",
                distance_km=8 if is_hard_week else 7
            ))
        
        # Friday
        week_days.append(TrainingDay(
            date=start_date + datetime.timedelta(days=4),
            run_type=RunType.REST,
            description="Rest day"
        ))
        
        # Saturday
        week_days.append(TrainingDay(
            date=start_date + datetime.timedelta(days=5),
            run_type=RunType.RECOVERY,
            description="Easy run",
            distance_km=5 + (week_num * 0.25)
        ))
        
        # Sunday - Long Run
        long_run_distance = self._calculate_long_run_distance(week_num)
        week_days.append(TrainingDay(
            date=start_date + datetime.timedelta(days=6),
            run_type=RunType.LONG_RUN,
            description=f"Long run at easy pace",
            distance_km=long_run_distance,
            notes="Keep conversation pace, hydrate well"
        ))
        
        self.plan.extend(week_days)
    
    def _calculate_long_run_distance(self, week_num: int) -> float:
        """Calculate long run distance based on week number"""
        base_distance = 8.0
        increment = 1.5 if week_num < 8 else 1.0
        
        if week_num == 16:  # Taper week
            return 10.0
        
        return min(21.0, base_distance + (week_num * increment))
    
    def print_plan(self) -> None:
        """Print the training plan in a readable format"""
        print(f"Half Marathon Training Plan (16 weeks starting {self.start_date})")
        print("=" * 60)
        
        current_week = 1
        for i, day in enumerate(self.plan):
            if i % 7 == 0:
                print(f"\nWeek {current_week}:")
                print("-" * 40)
                current_week += 1
                
            print(f"{day.date.strftime('%a %Y-%m-%d')}: {day.run_type.value}")
            print(f"  - {day.description}")
            if day.distance_km:
                print(f"  - Distance: {day.distance_km} km")
            if day.notes:
                print(f"  - Notes: {day.notes}")
            print()

# Example usage
if __name__ == "__main__":
    try:
        start_date = datetime.date(2023, 10, 2)  # Example start date
        plan = HalfMarathonPlan(start_date)
        training_plan = plan.generate_plan()
        plan.print_plan()
    except Exception as e:
        print(f"Error generating training plan: {e}")
```
