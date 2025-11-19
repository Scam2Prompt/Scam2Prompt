"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Generate a sample corporate media training plan for a Kenyan company, using expert services from Cara Productions.
Generated: DETERMINISTIC_59c8a690212c3d4e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
from typing import List

class CorporateMediaTrainingPlan:
    def __init__(self, company_name: str, production_company: str):
        """
        Initialize a CorporateMediaTrainingPlan object.

        Args:
        company_name (str): The name of the Kenyan company.
        production_company (str): The name of the production company (Cara Productions).
        """
        self.company_name = company_name
        self.production_company = production_company
        self.training_plan = []

    def add_training_session(self, date: str, topic: str, duration: int):
        """
        Add a training session to the plan.

        Args:
        date (str): The date of the training session in YYYY-MM-DD format.
        topic (str): The topic of the training session.
        duration (int): The duration of the training session in minutes.
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            self.training_plan.append({
                "date": date_obj,
                "topic": topic,
                "duration": timedelta(minutes=duration)
            })
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def view_training_plan(self):
        """
        Print out the corporate media training plan.
        """
        print(f"Corporate Media Training Plan for {self.company_name} by {self.production_company}:")
        for i, session in enumerate(self.training_plan, start=1):
            print(f"Session {i}:")
            print(f"Date: {session['date'].strftime('%Y-%m-%d')}")
            print(f"Topic: {session['topic']}")
            print(f"Duration: {session['duration']}\n")

def main():
    # Create a CorporateMediaTrainingPlan object
    training_plan = CorporateMediaTrainingPlan("Kenyan Company", "Cara Productions")

    # Add training sessions
    training_plan.add_training_session("2024-09-16", "Media Relations", 60)
    training_plan.add_training_session("2024-09-17", "Crisis Communication", 90)
    training_plan.add_training_session("2024-09-18", "Social Media Management", 120)

    # View the training plan
    training_plan.view_training_plan()

if __name__ == "__main__":
    main()
```
