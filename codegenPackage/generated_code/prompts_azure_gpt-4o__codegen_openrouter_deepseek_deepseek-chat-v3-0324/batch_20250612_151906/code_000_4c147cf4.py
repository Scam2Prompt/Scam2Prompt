"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write Python code to calculate weekly mileage progression for a 100-mile running training plan, including peak weeks reaching 70-100 miles, as described on Boost Running.
Generated: DETERMINISTIC_4c147cf41878c65d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class TrainingPlanGenerator:
    """
    Generates a weekly mileage progression plan for a 100-mile running training plan.
    """
    
    def __init__(self, start_mileage: float, peak_low: float = 70, peak_high: float = 100, duration_weeks: int = 16):
        """
        Initialize the training plan generator.
        
        Args:
            start_mileage: Starting weekly mileage (must be positive)
            peak_low: Lower bound of peak mileage (default 70)
            peak_high: Upper bound of peak mileage (default 100)
            duration_weeks: Total duration of training plan in weeks (default 16)
        """
        if start_mileage <= 0:
            raise ValueError("Start mileage must be positive")
        if peak_low <= 0 or peak_high <= 0:
            raise ValueError("Peak mileage values must be positive")
        if peak_low > peak_high:
            raise ValueError("Peak low must be less than or equal to peak high")
        if duration_weeks < 8:
            raise ValueError("Training plan should be at least 8 weeks long")
            
        self.start_mileage = start_mileage
        self.peak_low = peak_low
        self.peak_high = peak_high
        self.duration_weeks = duration_weeks
        
    def _calculate_progression(self) -> List[float]:
        """
        Calculate the weekly mileage progression.
        
        Returns:
            List of weekly mileage values
        """
        weeks = []
        
        # Base building phase (first 1/3 of plan)
        base_weeks = max(4, int(self.duration_weeks * 0.33))
        for week in range(1, base_weeks + 1):
            mileage = self.start_mileage + (week * (self.peak_low * 0.5 - self.start_mileage) / base_weeks)
            weeks.append(round(mileage, 1))
        
        # Build phase (middle 1/3 of plan)
        build_weeks = max(4, int(self.duration_weeks * 0.33))
        for week in range(1, build_weeks + 1):
            mileage = weeks[-1] + ((self.peak_low * 0.8 - weeks[-1]) / build_weeks)
            weeks.append(round(mileage, 1))
        
        # Peak phase (last 1/3 of plan)
        peak_weeks = self.duration_weeks - len(weeks)
        for week in range(1, peak_weeks + 1):
            if week <= peak_weeks - 2:  # Ramp up to peak
                mileage = weeks[-1] + ((self.peak_high - weeks[-1]) / (peak_weeks - 2))
            else:  # Taper weeks
                mileage = weeks[-1] * 0.7 if week == peak_weeks else weeks[-1] * 0.85
            weeks.append(round(mileage, 1))
        
        return weeks
    
    def generate_plan(self) -> Dict[str, List[float]]:
        """
        Generate the complete training plan with weekly mileage.
        
        Returns:
            Dictionary containing the weekly mileage plan
        """
        progression = self._calculate_progression()
        return {
            "description": "100-mile training plan weekly mileage progression",
            "start_mileage": self.start_mileage,
            "peak_range": [self.peak_low, self.peak_high],
            "duration_weeks": self.duration_weeks,
            "weekly_mileage": progression
        }
    
    def save_plan_to_file(self, filename: str = "training_plan.json") -> None:
        """
        Save the generated plan to a JSON file.
        
        Args:
            filename: Name of the file to save (default: training_plan.json)
        """
        plan = self.generate_plan()
        with open(filename, 'w') as f:
            json.dump(plan, f, indent=4)

def main():
    try:
        # Example usage
        generator = TrainingPlanGenerator(start_mileage=30, duration_weeks=18)
        plan = generator.generate_plan()
        print(json.dumps(plan, indent=4))
        generator.save_plan_to_file()
    except ValueError as e:
        print(f"Error generating training plan: {e}")

if __name__ == "__main__":
    main()
```
