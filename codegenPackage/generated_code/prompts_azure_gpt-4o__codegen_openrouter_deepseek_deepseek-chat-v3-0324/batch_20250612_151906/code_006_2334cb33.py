"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Develop a Python script to analyze running endurance factors (e.g., aerobic capacity, lactate threshold, muscular strength) and suggest training improvements based on Boost Running's guide.
Generated: DETERMINISTIC_2334cb3348f2dcc9
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
from typing import Dict, List, Optional, Union
from enum import Enum

class EnduranceFactor(Enum):
    AEROBIC_CAPACITY = "Aerobic Capacity"
    LACTATE_THRESHOLD = "Lactate Threshold"
    MUSCULAR_STRENGTH = "Muscular Strength"

class TrainingImprovement:
    def __init__(self, factor: EnduranceFactor, current_level: str, recommended_training: List[str]):
        self.factor = factor
        self.current_level = current_level
        self.recommended_training = recommended_training

    def to_dict(self) -> Dict:
        return {
            "factor": self.factor.value,
            "current_level": self.current_level,
            "recommended_training": self.recommended_training
        }

class EnduranceAnalyzer:
    TRAINING_RECOMMENDATIONS = {
        EnduranceFactor.AEROBIC_CAPACITY: {
            "low": [
                "Increase weekly mileage by 10-15%",
                "Include 1-2 long runs per week",
                "Maintain easy pace (able to hold conversation)"
            ],
            "medium": [
                "Include tempo runs at 85-90% max HR",
                "Add weekly interval training",
                "Maintain consistent mileage"
            ],
            "high": [
                "Focus on race-specific workouts",
                "Include VO2 max intervals",
                "Optimize recovery periods"
            ]
        },
        EnduranceFactor.LACTATE_THRESHOLD: {
            "low": [
                "Start with 20-30 min tempo runs",
                "Gradually increase tempo duration",
                "Maintain proper form"
            ],
            "medium": [
                "Increase tempo run duration to 40-60 min",
                "Add cruise intervals",
                "Focus on pacing consistency"
            ],
            "high": [
                "Race-pace specific workouts",
                "Extended tempo runs (60+ min)",
                "Optimize nutrition during runs"
            ]
        },
        EnduranceFactor.MUSCULAR_STRENGTH: {
            "low": [
                "Incorporate 2-3 strength sessions per week",
                "Focus on bodyweight exercises",
                "Include hill repeats"
            ],
            "medium": [
                "Add weighted strength training",
                "Include plyometrics",
                "Focus on running-specific strength"
            ],
            "high": [
                "Advanced strength routines",
                "Explosive power exercises",
                "Sport-specific mobility work"
            ]
        }
    }

    def __init__(self, user_data: Dict[str, str]):
        self.user_data = user_data
        self._validate_input()

    def _validate_input(self) -> None:
        required_fields = [factor.value for factor in EnduranceFactor]
        for field in required_fields:
            if field not in self.user_data:
                raise ValueError(f"Missing required field: {field}")
            
            level = self.user_data[field].lower()
            if level not in ["low", "medium", "high"]:
                raise ValueError(f"Invalid level '{level}' for {field}. Must be 'low', 'medium', or 'high'.")

    def analyze(self) -> List[TrainingImprovement]:
        improvements = []
        for factor in EnduranceFactor:
            level = self.user_data[factor.value].lower()
            recommendations = self.TRAINING_RECOMMENDATIONS[factor][level]
            improvements.append(
                TrainingImprovement(factor, level.capitalize(), recommendations)
            )
        return improvements

    def generate_report(self, improvements: List[TrainingImprovement]) -> Dict:
        return {
            "analysis": [imp.to_dict() for imp in improvements],
            "summary": self._generate_summary(improvements)
        }

    def _generate_summary(self, improvements: List[TrainingImprovement]) -> str:
        priority_areas = [
            imp.factor.value for imp in improvements 
            if imp.current_level.lower() == "low"
        ]
        
        if priority_areas:
            return (
                f"Priority areas to focus on: {', '.join(priority_areas)}. "
                "Consider addressing these first for maximum improvement."
            )
        return (
            "All endurance factors are at medium or high levels. "
            "Focus on maintaining strengths while optimizing race-specific performance."
        )

def main():
    try:
        # Example user data (in production, this would come from user input)
        user_data = {
            "Aerobic Capacity": "medium",
            "Lactate Threshold": "low",
            "Muscular Strength": "high"
        }

        analyzer = EnduranceAnalyzer(user_data)
        improvements = analyzer.analyze()
        report = analyzer.generate_report(improvements)

        print(json.dumps(report, indent=2))

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
