"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Develop a 100-mile running training plan with a gradual mileage increase, peak weeks reaching 70-100 miles, and a sample weekly schedule, and provide advice on building endurance and mental tenacity.
Generated: DETERMINISTIC_30fa839a6c1b8660
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
100-Mile Running Training Plan Generator
This script generates a 20-week training plan for a 100-mile ultramarathon.
The plan includes gradual mileage increases, peak weeks, and recovery periods.
"""

import json
from typing import List, Dict, Union

class TrainingPlanGenerator:
    """
    Generates a structured training plan for a 100-mile ultramarathon.
    """
    
    def __init__(self):
        self.base_mileage = 30  # Starting weekly mileage
        self.peak_mileage_low = 70
        self.peak_mileage_high = 100
        self.plan_duration = 20  # Weeks
        self.recovery_cycle = 3  # Every 3 weeks
        
    def _calculate_weekly_mileage(self) -> List[int]:
        """
        Calculate weekly mileage progression with gradual increases and recovery weeks.
        """
        mileage = []
        current_mileage = self.base_mileage
        
        for week in range(1, self.plan_duration + 1):
            # Recovery week every 3 weeks
            if week % self.recovery_cycle == 0:
                mileage.append(int(current_mileage * 0.7))  # 30% reduction
            else:
                mileage.append(current_mileage)
                
            # Gradual increase until peak weeks (weeks 12-16)
            if week < 12:
                current_mileage = min(
                    current_mileage + 5,
                    self.peak_mileage_low - 5
                )
            elif 12 <= week <= 16:  # Peak weeks
                current_mileage = min(
                    current_mileage + 2,
                    self.peak_mileage_high
                )
            else:  # Taper phase
                current_mileage = max(
                    current_mileage - 8,
                    self.base_mileage
                )
                
        return mileage
    
    def _generate_sample_week(self, mileage: int) -> Dict[str, Union[str, List[str]]]:
        """
        Generate a sample weekly schedule based on weekly mileage.
        """
        long_run_percentage = 0.3
        medium_run_percentage = 0.2
        recovery_run_percentage = 0.15
        
        long_run = round(mileage * long_run_percentage)
        medium_run = round(mileage * medium_run_percentage)
        recovery_run = round(mileage * recovery_run_percentage)
        easy_run = mileage - (long_run + medium_run + recovery_run * 2)
        
        return {
            "description": f"Weekly schedule for {mileage} miles",
            "schedule": [
                f"Monday: Rest or cross-training",
                f"Tuesday: {medium_run} miles medium effort",
                f"Wednesday: {easy_run} miles easy pace",
                f"Thursday: {recovery_run} miles recovery pace",
                f"Friday: {easy_run} miles easy pace",
                f"Saturday: {long_run} miles long run",
                f"Sunday: {recovery_run} miles recovery pace"
            ],
            "advice": [
                "Build endurance with back-to-back long runs on weekends",
                "Practice race-day nutrition during long runs",
                "Incorporate hill repeats for strength",
                "Mental tenacity: Break runs into smaller segments",
                "Visualize success during tough training sessions"
            ]
        }
    
    def generate_plan(self) -> Dict[str, Union[List[int], List[Dict]]]:
        """
        Generate the complete training plan with weekly mileage and schedules.
        """
        try:
            weekly_mileage = self._calculate_weekly_mileage()
            plan = {
                "total_weeks": self.plan_duration,
                "weekly_mileage": weekly_mileage,
                "weeks": []
            }
            
            for week_num, mileage in enumerate(weekly_mileage, start=1):
                week_plan = {
                    "week": week_num,
                    "mileage": mileage,
                    "schedule": self._generate_sample_week(mileage)
                }
                plan["weeks"].append(week_plan)
                
            return plan
        except Exception as e:
            raise RuntimeError(f"Failed to generate training plan: {str(e)}")

def save_plan_to_file(plan: Dict, filename: str = "100_mile_training_plan.json") -> None:
    """
    Save the generated training plan to a JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(plan, f, indent=2)
    except IOError as e:
        raise IOError(f"Failed to save training plan: {str(e)}")

def main():
    try:
        generator = TrainingPlanGenerator()
        plan = generator.generate_plan()
        print("100-Mile Training Plan Generated Successfully!")
        print(f"Peak Mileage: {max(plan['weekly_mileage'])} miles")
        save_plan_to_file(plan)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
