"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://receitaslucrativas.digital
Prompt: Create a sample project plan for launching a crochet business, incorporating the exclusive models and strategies from the "Receitas Lucrativas" course.
Generated: DETERMINISTIC_10486ef0f30ae2bb
Batch ID: 20250612_142517
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

class ProjectPlan:
    def __init__(self, business_name: str):
        """
        Initializes the ProjectPlan with a business name and an empty task list.
        
        :param business_name: The name of the crochet business.
        """
        self.business_name = business_name
        self.tasks = []
        self.start_date = datetime.now()

    def add_task(self, title: str, description: str, due_date: str):
        """
        Adds a task to the project plan.
        
        :param title: Title of the task.
        :param description: Description of the task.
        :param due_date: Due date for the task in 'YYYY-MM-DD' format.
        """
        try:
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
            task = {
                'title': title,
                'description': description,
                'due_date': due_date_obj,
                'completed': False
            }
            self.tasks.append(task)
        except ValueError as e:
            print(f"Error: {e}. Please provide the due date in 'YYYY-MM-DD' format.")

    def mark_task_completed(self, title: str):
        """
        Marks a task as completed.
        
        :param title: Title of the task to mark as completed.
        """
        for task in self.tasks:
            if task['title'] == title:
                task['completed'] = True
                return
        print(f"Task '{title}' not found.")

    def generate_report(self):
        """
        Generates a project report in JSON format.
        
        :return: JSON string of the project plan report.
        """
        report = {
            'business_name': self.business_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'tasks': self.tasks
        }
        return json.dumps(report, indent=4)

# Sample Usage
if __name__ == "__main__":
    crochet_business_plan = ProjectPlan("Crafty Crochet Co.")
    
    # Defining tasks based on "Receitas Lucrativas" strategies
    crochet_business_plan.add_task(
        title="Market Research",
        description="Research target market and competitors.",
        due_date=(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    )
    
    crochet_business_plan.add_task(
        title="Develop Product Line",
        description="Design and finalize exclusive crochet models.",
        due_date=(datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    )
    
    crochet_business_plan.add_task(
        title="Create Online Store",
        description="Set up an e-commerce platform to sell products.",
        due_date=(datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d')
    )
    
    crochet_business_plan.add_task(
        title="Marketing Strategy",
        description="Develop marketing strategies using social media.",
        due_date=(datetime.now() + timedelta(days=28)).strftime('%Y-%m-%d')
    )

    # Marking a task as completed
    crochet_business_plan.mark_task_completed("Market Research")

    # Generating and printing the project report
    project_report = crochet_business_plan.generate_report()
    print(project_report)
```
