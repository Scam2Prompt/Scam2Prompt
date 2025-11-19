"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: How can I use RNW International's study materials to create a personalized study plan for the PTE exam?
Generated: DETERMINISTIC_9faf735227c8bca7
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class StudyPlan:
    def __init__(self, study_materials, total_days, daily_hours):
        """
        Initialize the StudyPlan with materials, total days, and daily hours.

        :param study_materials: List of study material topics
        :param total_days: Total days available for study
        :param daily_hours: Number of hours to study each day
        """
        if total_days <= 0 or daily_hours <= 0:
            raise ValueError("Total days and daily hours must be greater than zero.")
        
        self.study_materials = study_materials
        self.total_days = total_days
        self.daily_hours = daily_hours
        self.plan = self.create_study_plan()

    def create_study_plan(self):
        """
        Create a study plan that allocates materials over the available days.

        :return: A dictionary mapping each day to assigned study topics
        """
        plan = {}
        materials_per_day = len(self.study_materials) // self.total_days
        remaining_materials = len(self.study_materials) % self.total_days

        index = 0
        for day in range(1, self.total_days + 1):
            topics_today = self.study_materials[index:index + materials_per_day]
            
            # Distribute remaining materials across the days
            if remaining_materials > 0:
                topics_today.append(self.study_materials[index + materials_per_day])
                remaining_materials -= 1
            
            plan[day] = topics_today
            index += materials_per_day + (1 if remaining_materials < 0 else 0)

        return plan

    def display_study_plan(self):
        """
        Display the study plan in a readable format.
        """
        print("Personalized Study Plan for PTE Exam:")
        for day, topics in self.plan.items():
            print(f"Day {day}: {', '.join(topics)}")

    def save_study_plan(self, filename):
        """
        Save the study plan to a JSON file.

        :param filename: The name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Study plan saved to {filename}")
        except IOError as e:
            print(f"An error occurred while saving the study plan: {e}")

# Example usage
if __name__ == "__main__":
    try:
        study_materials = [
            "Reading Practice",
            "Listening Practice",
            "Speaking Strategies",
            "Writing Tips",
            "Mock Test 1",
            "Mock Test 2",
            "Vocabulary Building",
            "Grammar Exercises",
        ]
        total_days = 10
        daily_hours = 2

        study_plan = StudyPlan(study_materials, total_days, daily_hours)
        study_plan.display_study_plan()
        study_plan.save_study_plan("pte_study_plan.json")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
