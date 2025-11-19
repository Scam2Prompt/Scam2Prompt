"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Generate a script to simulate the construction process of sanitary networks, ensuring adherence to budget and timelines, as highlighted by Espinel y Cia's services.
Generated: DETERMINISTIC_3b43bd4454aae71f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import datetime
from typing import Dict, List, Tuple, Optional

class SanitaryNetworkSimulator:
    """
    Simulates the construction process of sanitary networks with budget and timeline management.
    """
    
    def __init__(self, project_name: str, total_budget: float, deadline: datetime.date):
        """
        Initialize the simulator with project details.
        
        Args:
            project_name: Name of the sanitary network project.
            total_budget: Total allocated budget for the project.
            deadline: Project completion deadline.
        """
        self.project_name = project_name
        self.total_budget = total_budget
        self.deadline = deadline
        self.start_date = datetime.date.today()
        self.completed = False
        self.current_cost = 0.0
        self.current_day = 0
        self.tasks = self._initialize_tasks()
        
    def _initialize_tasks(self) -> List[Dict]:
        """
        Initialize the default tasks for sanitary network construction.
        
        Returns:
            List of tasks with their properties.
        """
        return [
            {"name": "Survey and Design", "duration": 10, "cost": 0.15 * self.total_budget, "completed": False},
            {"name": "Excavation", "duration": 20, "cost": 0.25 * self.total_budget, "completed": False},
            {"name": "Pipe Installation", "duration": 30, "cost": 0.35 * self.total_budget, "completed": False},
            {"name": "Backfilling", "duration": 15, "cost": 0.15 * self.total_budget, "completed": False},
            {"name": "Testing and Commissioning", "duration": 10, "cost": 0.10 * self.total_budget, "completed": False}
        ]
    
    def _calculate_risk_factor(self) -> float:
        """
        Calculate a random risk factor that may affect progress.
        
        Returns:
            Risk factor between 0.8 and 1.2
        """
        return random.uniform(0.8, 1.2)
    
    def simulate_day(self) -> Tuple[bool, Optional[str]]:
        """
        Simulate one day of construction progress.
        
        Returns:
            Tuple of (project_completed_status, message)
        """
        if self.completed:
            return (True, "Project already completed.")
        
        if self.current_day >= (self.deadline - self.start_date).days:
            return (False, "Project deadline exceeded.")
        
        if self.current_cost >= self.total_budget:
            return (False, "Project budget exceeded.")
        
        # Process current tasks
        for task in self.tasks:
            if not task["completed"]:
                risk_factor = self._calculate_risk_factor()
                actual_duration = task["duration"] * risk_factor
                
                if self.current_day >= actual_duration:
                    task["completed"] = True
                    self.current_cost += task["cost"]
                    
                    # Check if all tasks are completed
                    if all(t["completed"] for t in self.tasks):
                        self.completed = True
                        return (True, "Project completed successfully!")
                    
                    break
        
        self.current_day += 1
        return (False, None)
    
    def get_project_status(self) -> Dict:
        """
        Get current project status.
        
        Returns:
            Dictionary containing project status information.
        """
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        total_tasks = len(self.tasks)
        progress_percentage = (completed_tasks / total_tasks) * 100
        budget_used_percentage = (self.current_cost / self.total_budget) * 100
        days_remaining = (self.deadline - self.start_date).days - self.current_day
        
        return {
            "project_name": self.project_name,
            "completed": self.completed,
            "progress": f"{progress_percentage:.2f}%",
            "budget_used": f"{budget_used_percentage:.2f}%",
            "days_remaining": days_remaining,
            "current_cost": self.current_cost,
            "tasks_completed": completed_tasks,
            "total_tasks": total_tasks
        }
    
    def run_simulation(self) -> Dict:
        """
        Run complete simulation until project completion or failure.
        
        Returns:
            Final project status.
        """
        while not self.completed:
            completed, message = self.simulate_day()
            if completed or message:
                break
        
        status = self.get_project_status()
        if message:
            status["message"] = message
        
        return status


def main():
    # Example usage
    project_name = "Espinel y Cia Sanitary Network Project"
    total_budget = 1000000.00  # 1 million dollars
    deadline = datetime.date.today() + datetime.timedelta(days=120)  # 120 days from today
    
    simulator = SanitaryNetworkSimulator(project_name, total_budget, deadline)
    final_status = simulator.run_simulation()
    
    print("\nProject Simulation Results:")
    print("=" * 50)
    for key, value in final_status.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
```
