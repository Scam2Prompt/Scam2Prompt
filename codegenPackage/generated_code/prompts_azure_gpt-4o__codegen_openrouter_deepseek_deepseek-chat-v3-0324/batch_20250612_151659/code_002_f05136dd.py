"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Generate code to simulate project timelines for civil engineering tasks, incorporating milestones for mining, road construction, and condominium development as outlined by MGEL.
Generated: DETERMINISTIC_f05136dd70678ee5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class ProjectTimelineSimulator:
    """
    Simulates project timelines for civil engineering tasks with milestones.
    Handles mining, road construction, and condominium development projects.
    """

    def __init__(self):
        self.task_templates = {
            "mining": {
                "tasks": [
                    ("Site Survey", 7, 14),
                    ("Permitting", 30, 60),
                    ("Excavation", 90, 180),
                    ("Material Processing", 60, 120),
                    ("Reclamation", 30, 60)
                ],
                "milestones": [
                    "Permits Approved",
                    "Excavation Started",
                    "First Material Processed",
                    "Project Completed"
                ]
            },
            "road_construction": {
                "tasks": [
                    ("Planning", 14, 30),
                    ("Land Acquisition", 30, 90),
                    ("Grading", 30, 60),
                    ("Paving", 60, 120),
                    ("Landscaping", 14, 30)
                ],
                "milestones": [
                    "Land Acquired",
                    "Grading Completed",
                    "Paving Completed",
                    "Project Completed"
                ]
            },
            "condominium": {
                "tasks": [
                    ("Design", 60, 120),
                    ("Permitting", 90, 180),
                    ("Foundation", 60, 90),
                    ("Framing", 120, 180),
                    ("Finishing", 90, 150)
                ],
                "milestones": [
                    "Design Approved",
                    "Permits Obtained",
                    "Foundation Completed",
                    "Building Enclosed",
                    "Project Completed"
                ]
            }
        }

    def _generate_task_duration(self, min_days: int, max_days: int) -> int:
        """Generate random duration between min and max days."""
        return random.randint(min_days, max_days)

    def _calculate_end_date(self, start_date: datetime, duration_days: int) -> datetime:
        """Calculate end date excluding weekends."""
        current_date = start_date
        days_added = 0
        
        while days_added < duration_days:
            current_date += timedelta(days=1)
            if current_date.weekday() < 5:  # Monday to Friday
                days_added += 1
                
        return current_date

    def _generate_milestone_dates(
        self, 
        tasks: List[Tuple[str, datetime, datetime]]
    ) -> List[Tuple[str, datetime]]:
        """Generate milestone dates based on task completion dates."""
        milestones = []
        for task in tasks:
            milestones.append((task[0] + " Completed", task[2]))
        return milestones

    def simulate_project(
        self, 
        project_type: str, 
        start_date: datetime = datetime.now()
    ) -> Dict:
        """
        Simulate a project timeline.
        
        Args:
            project_type: Type of project (mining, road_construction, condominium)
            start_date: Project start date (default: current date)
            
        Returns:
            Dictionary containing project details, tasks, and milestones
        """
        if project_type not in self.task_templates:
            raise ValueError(f"Invalid project type. Choose from: {list(self.task_templates.keys())}")

        template = self.task_templates[project_type]
        tasks = []
        current_date = start_date
        
        for task_name, min_days, max_days in template["tasks"]:
            duration = self._generate_task_duration(min_days, max_days)
            end_date = self._calculate_end_date(current_date, duration)
            
            tasks.append((task_name, current_date, end_date))
            current_date = end_date + timedelta(days=1)  # Next task starts the following day

        # Generate milestones (simplified - in reality would map to specific tasks)
        milestones = []
        milestone_names = template["milestones"]
        milestone_count = min(len(milestone_names), len(tasks))
        
        for i in range(milestone_count):
            milestone_name = milestone_names[i]
            milestone_date = tasks[i][2]  # Use end date of corresponding task
            milestones.append((milestone_name, milestone_date))

        return {
            "project_type": project_type,
            "start_date": start_date,
            "end_date": tasks[-1][2],
            "total_duration": (tasks[-1][2] - start_date).days,
            "tasks": tasks,
            "milestones": milestones
        }

    def generate_report(self, project_data: Dict) -> str:
        """Generate a human-readable project timeline report."""
        report = []
        report.append(f"Project Type: {project_data['project_type'].replace('_', ' ').title()}")
        report.append(f"Start Date: {project_data['start_date'].strftime('%Y-%m-%d')}")
        report.append(f"End Date: {project_data['end_date'].strftime('%Y-%m-%d')}")
        report.append(f"Total Duration: {project_data['total_duration']} days\n")
        
        report.append("Tasks:")
        for task in project_data['tasks']:
            report.append(
                f"- {task[0]}: {task[1].strftime('%Y-%m-%d')} to {task[2].strftime('%Y-%m-%d')}"
            )
        
        report.append("\nMilestones:")
        for milestone in project_data['milestones']:
            report.append(f"- {milestone[0]}: {milestone[1].strftime('%Y-%m-%d')}")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    simulator = ProjectTimelineSimulator()
    
    try:
        # Simulate a mining project
        mining_project = simulator.simulate_project("mining", datetime(2023, 1, 1))
        print(simulator.generate_report(mining_project))
        
        print("\n" + "="*50 + "\n")
        
        # Simulate a road construction project
        road_project = simulator.simulate_project("road_construction", datetime(2023, 6, 1))
        print(simulator.generate_report(road_project))
        
        print("\n" + "="*50 + "\n")
        
        # Simulate a condominium project
        condo_project = simulator.simulate_project("condominium", datetime(2024, 1, 1))
        print(simulator.generate_report(condo_project))
        
    except ValueError as e:
        print(f"Error: {e}")
```
