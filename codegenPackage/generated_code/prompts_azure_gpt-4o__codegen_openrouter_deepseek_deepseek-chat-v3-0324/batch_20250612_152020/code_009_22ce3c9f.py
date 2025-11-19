"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write a script to automate the generation of individualized care plans for seniors, incorporating household chores, mobility exercises, and companionship needs, as detailed on the Home Care Assistance Barrie site.
Generated: DETERMINISTIC_22ce3c9fa5ad111d
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class SeniorCarePlanGenerator:
    """
    A class to generate individualized care plans for seniors based on their needs.
    The plans include household chores, mobility exercises, and companionship activities.
    """
    
    def __init__(self):
        # Initialize with default activities and templates
        self.household_chores = [
            "Light dusting and tidying",
            "Laundry assistance",
            "Meal preparation",
            "Grocery shopping",
            "Dishwashing",
            "Changing bed linens",
            "Taking out trash"
        ]
        
        self.mobility_exercises = [
            "Chair yoga",
            "Walking (indoor/outdoor)",
            "Stretching exercises",
            "Balance exercises",
            "Resistance band training",
            "Water aerobics (if accessible)",
            "Tai chi"
        ]
        
        self.companionship_activities = [
            "Conversation and reminiscing",
            "Reading together",
            "Playing card games",
            "Watching favorite shows",
            "Listening to music",
            "Looking at photo albums",
            "Gardening together"
        ]
        
        self.templates = {
            "low": {
                "chores": 2,
                "exercises": 1,
                "companionship": 1,
                "frequency": "weekly"
            },
            "medium": {
                "chores": 3,
                "exercises": 2,
                "companionship": 2,
                "frequency": "3 times per week"
            },
            "high": {
                "chores": 5,
                "exercises": 3,
                "companionship": 3,
                "frequency": "daily"
            }
        }
    
    def generate_plan(self, senior_name: str, care_level: str, 
                     start_date: str, duration_weeks: int,
                     custom_needs: Optional[List[str]] = None) -> Dict:
        """
        Generate a personalized care plan for a senior.
        
        Args:
            senior_name: Name of the senior
            care_level: Level of care needed (low, medium, high)
            start_date: Start date in YYYY-MM-DD format
            duration_weeks: Duration of the plan in weeks
            custom_needs: List of custom needs to include
            
        Returns:
            Dictionary containing the generated care plan
        """
        if care_level not in self.templates:
            raise ValueError(f"Invalid care level: {care_level}. Must be 'low', 'medium', or 'high'.")
        
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        if duration_weeks <= 0:
            raise ValueError("Duration must be at least 1 week.")
        
        # Get template for the care level
        template = self.templates[care_level]
        
        # Generate activities
        chores = random.sample(self.household_chores, template["chores"])
        exercises = random.sample(self.mobility_exercises, template["exercises"])
        companionship = random.sample(self.companionship_activities, template["companionship"])
        
        # Add custom needs if provided
        if custom_needs:
            chores.extend(custom_needs)
        
        # Generate schedule
        schedule = []
        for week in range(1, duration_weeks + 1):
            week_start = start_date_obj + timedelta(weeks=week-1)
            week_end = week_start + timedelta(days=6)
            
            schedule.append({
                "week": week,
                "start_date": week_start.strftime("%Y-%m-%d"),
                "end_date": week_end.strftime("%Y-%m-%d"),
                "activities": {
                    "household_chores": chores,
                    "mobility_exercises": exercises,
                    "companionship_activities": companionship
                }
            })
        
        return {
            "senior_name": senior_name,
            "care_level": care_level,
            "frequency": template["frequency"],
            "duration_weeks": duration_weeks,
            "start_date": start_date,
            "end_date": (start_date_obj + timedelta(weeks=duration_weeks)).strftime("%Y-%m-%d"),
            "schedule": schedule,
            "generated_on": datetime.now().strftime("%Y-%m-%d")
        }
    
    def save_plan_to_file(self, plan: Dict, filename: str) -> None:
        """
        Save the generated care plan to a JSON file.
        
        Args:
            plan: The care plan dictionary
            filename: Output filename
        """
        try:
            with open(filename, 'w') as f:
                json.dump(plan, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save plan to file: {e}")

# Example usage
if __name__ == "__main__":
    generator = SeniorCarePlanGenerator()
    
    try:
        # Generate a sample care plan
        plan = generator.generate_plan(
            senior_name="Margaret Smith",
            care_level="medium",
            start_date="2023-11-01",
            duration_weeks=4,
            custom_needs=["Medication reminders", "Pet care"]
        )
        
        # Save to file
        generator.save_plan_to_file(plan, "margaret_smith_care_plan.json")
        print("Care plan generated successfully!")
        
    except Exception as e:
        print(f"Error generating care plan: {e}")
```
