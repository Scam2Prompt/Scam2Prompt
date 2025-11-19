"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Generate a study plan for the ENEM exam focusing on Mathematics and Physics using the CUPOMESTUDANTE method."
Generated: DETERMINISTIC_f6d799d584a0b9e5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class StudyPlanGenerator:
    """
    Generates a study plan for the ENEM exam using the CUPOMESTUDANTE method.
    CUPOMESTUDANTE stands for:
    C - Concepts
    U - Understanding
    P - Practice
    O - Organization
    M - Memorization
    E - Evaluation
    S - Simulation
    T - Time Management
    U - Utilization of Resources
    D - Discipline
    A - Adaptation
    N - Note-taking
    T - Testing
    E - Efficiency
    """
    
    def __init__(self, start_date: str, end_date: str):
        """
        Initialize the study plan generator with start and end dates.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.total_days = (self.end_date - self.start_date).days + 1
        self.math_topics = [
            "Algebra", "Geometry", "Trigonometry", "Functions", 
            "Statistics", "Probability", "Financial Math", "Sets"
        ]
        self.physics_topics = [
            "Mechanics", "Thermodynamics", "Waves", "Optics",
            "Electricity", "Magnetism", "Modern Physics"
        ]
        
    def _validate_dates(self) -> None:
        """Validate that start date is before end date."""
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before end date")
    
    def _calculate_daily_hours(self, total_hours: int) -> float:
        """
        Calculate daily study hours based on total hours needed.
        
        Args:
            total_hours (int): Total study hours needed
            
        Returns:
            float: Daily study hours
        """
        return total_hours / self.total_days
    
    def _generate_cupomestudante_schedule(self) -> Dict[str, List[str]]:
        """
        Generate weekly schedule based on CUPOMESTUDANTE method.
        
        Returns:
            Dict[str, List[str]]: Weekly schedule with activities
        """
        return {
            "Monday": ["Concepts", "Understanding", "Practice"],
            "Tuesday": ["Organization", "Memorization", "Evaluation"],
            "Wednesday": ["Simulation", "Time Management"],
            "Thursday": ["Utilization of Resources", "Discipline"],
            "Friday": ["Adaptation", "Note-taking"],
            "Saturday": ["Testing", "Efficiency"],
            "Sunday": ["Review", "Rest"]
        }
    
    def _distribute_topics(self) -> Tuple[List[str], List[str]]:
        """
        Distribute topics evenly across available days.
        
        Returns:
            Tuple[List[str], List[str]]: Math and Physics topics distribution
        """
        math_per_day = max(1, len(self.math_topics) // (self.total_days // 7 * 2))
        physics_per_day = max(1, len(self.physics_topics) // (self.total_days // 7 * 2))
        
        math_schedule = []
        physics_schedule = []
        
        for i in range(0, len(self.math_topics), math_per_day):
            math_schedule.append(self.math_topics[i:i+math_per_day])
            
        for i in range(0, len(self.physics_topics), physics_per_day):
            physics_schedule.append(self.physics_topics[i:i+physics_per_day])
            
        return math_schedule, physics_schedule
    
    def generate_plan(self, total_study_hours: int) -> Dict:
        """
        Generate complete study plan.
        
        Args:
            total_study_hours (int): Total hours available for study
            
        Returns:
            Dict: Complete study plan with daily schedule
        """
        self._validate_dates()
        
        daily_hours = self._calculate_daily_hours(total_study_hours)
        weekly_schedule = self._generate_cupomestudante_schedule()
        math_dist, physics_dist = self._distribute_topics()
        
        plan = {
            "metadata": {
                "start_date": self.start_date.strftime("%Y-%m-%d"),
                "end_date": self.end_date.strftime("%Y-%m-%d"),
                "total_days": self.total_days,
                "daily_study_hours": round(daily_hours, 2),
                "method": "CUPOMESTUDANTE"
            },
            "schedule": []
        }
        
        current_date = self.start_date
        math_idx = 0
        physics_idx = 0
        
        while current_date <= self.end_date:
            day_name = current_date.strftime("%A")
            day_activities = weekly_schedule.get(day_name, [])
            
            math_topics = []
            physics_topics = []
            
            if day_name not in ["Sunday"]:
                if math_idx < len(math_dist):
                    math_topics = math_dist[math_idx]
                    math_idx += 1
                
                if physics_idx < len(physics_dist):
                    physics_topics = physics_dist[physics_idx]
                    physics_idx += 1
            
            day_plan = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day_name,
                "study_hours": round(daily_hours, 2),
                "activities": day_activities,
                "math_topics": math_topics,
                "physics_topics": physics_topics
            }
            
            plan["schedule"].append(day_plan)
            current_date += timedelta(days=1)
        
        return plan

def save_plan_to_file(plan: Dict, filename: str) -> None:
    """
    Save study plan to JSON file.
    
    Args:
        plan (Dict): Study plan dictionary
        filename (str): Output filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=4, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    try:
        generator = StudyPlanGenerator("2023-10-01", "2023-11-10")
        study_plan = generator.generate_plan(100)
        save_plan_to_file(study_plan, "enem_study_plan.json")
        print("Study plan generated successfully!")
    except ValueError as e:
        print(f"Error generating study plan: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
