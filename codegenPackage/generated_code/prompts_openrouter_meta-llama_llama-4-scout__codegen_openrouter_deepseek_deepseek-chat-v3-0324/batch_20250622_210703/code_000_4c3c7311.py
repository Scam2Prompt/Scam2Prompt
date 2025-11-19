"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Generate a project plan for an electrical engineering project using business intelligence tools and methodologies offered by Jau Consulting."
Generated: DETERMINISTIC_4c3c73114bbe9b25
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Engineering Project Plan Generator using Jau Consulting BI Tools
This script generates a comprehensive project plan for electrical engineering projects
using business intelligence methodologies from Jau Consulting.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
import json

class ProjectPhase(Enum):
    INITIATION = "Initiation"
    PLANNING = "Planning"
    EXECUTION = "Execution"
    MONITORING = "Monitoring & Control"
    CLOSURE = "Closure"

class Task:
    def __init__(self, name: str, description: str, phase: ProjectPhase, 
                 duration_days: int, dependencies: List[str] = None):
        self.name = name
        self.description = description
        self.phase = phase
        self.duration_days = duration_days
        self.dependencies = dependencies or []
        self.resources = []
        self.metrics = []

    def add_resource(self, resource: str):
        self.resources.append(resource)
    
    def add_metric(self, metric: str):
        self.metrics.append(metric)
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "phase": self.phase.value,
            "duration_days": self.duration_days,
            "dependencies": self.dependencies,
            "resources": self.resources,
            "metrics": self.metrics
        }

class ProjectPlan:
    def __init__(self, project_name: str, client: str, start_date: datetime.date):
        self.project_name = project_name
        self.client = client
        self.start_date = start_date
        self.tasks = []
        self.bi_tools = ["Jau PowerBI", "Jau Analytics Dashboard", "Jau Predictive Models"]
        self.methodologies = ["Agile BI", "Data-Driven Decision Making", "KPI Optimization"]
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def generate_gantt_data(self) -> List[Dict]:
        gantt_data = []
        current_date = self.start_date
        
        for task in self.tasks:
            end_date = current_date + datetime.timedelta(days=task.duration_days)
            gantt_data.append({
                "task": task.name,
                "start": current_date.isoformat(),
                "end": end_date.isoformat(),
                "phase": task.phase.value,
                "dependencies": ", ".join(task.dependencies) if task.dependencies else "None"
            })
            current_date = end_date
        
        return gantt_data
    
    def generate_report(self) -> Dict:
        return {
            "project_name": self.project_name,
            "client": self.client,
            "start_date": self.start_date.isoformat(),
            "bi_tools": self.bi_tools,
            "methodologies": self.methodologies,
            "tasks": [task.to_dict() for task in self.tasks],
            "gantt_chart": self.generate_gantt_data()
        }
    
    def save_to_json(self, filename: str):
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_report(), f, indent=4)
        except IOError as e:
            print(f"Error saving project plan: {e}")

def create_sample_plan() -> ProjectPlan:
    """Create a sample electrical engineering project plan"""
    plan = ProjectPlan(
        "Smart Grid Implementation",
        "City Power Utility",
        datetime.date(2023, 1, 1)
    )
    
    # Initiation Phase
    requirements = Task(
        "Requirements Gathering",
        "Collect and document all project requirements",
        ProjectPhase.INITIATION,
        10
    )
    requirements.add_resource("Business Analyst")
    requirements.add_metric("Requirements Document Completion %")
    plan.add_task(requirements)
    
    # Planning Phase
    design = Task(
        "System Design",
        "Create detailed electrical system designs",
        ProjectPhase.PLANNING,
        15,
        ["Requirements Gathering"]
    )
    design.add_resource("Electrical Engineer")
    design.add_resource("CAD Technician")
    design.add_metric("Design Approval Status")
    plan.add_task(design)
    
    # Execution Phase
    implementation = Task(
        "System Implementation",
        "Install and configure smart grid components",
        ProjectPhase.EXECUTION,
        45,
        ["System Design"]
    )
    implementation.add_resource("Field Engineers")
    implementation.add_resource("Technicians")
    implementation.add_metric("Installation Completion %")
    plan.add_task(implementation)
    
    # Monitoring Phase
    testing = Task(
        "System Testing",
        "Perform comprehensive system tests",
        ProjectPhase.MONITORING,
        20,
        ["System Implementation"]
    )
    testing.add_resource("QA Team")
    testing.add_metric("Test Pass Rate")
    plan.add_task(testing)
    
    # Closure Phase
    handover = Task(
        "Project Handover",
        "Deliver project to client and complete documentation",
        ProjectPhase.CLOSURE,
        5,
        ["System Testing"]
    )
    handover.add_resource("Project Manager")
    handover.add_metric("Client Satisfaction Score")
    plan.add_task(handover)
    
    return plan

if __name__ == "__main__":
    project_plan = create_sample_plan()
    project_plan.save_to_json("electrical_engineering_project_plan.json")
```
