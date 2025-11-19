"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Create a project plan that incorporates EasyDoc's strategies for file management and digitalization in a corporate environment.
Generated: DETERMINISTIC_125cd99855084b99
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class ProjectPlan:
    """Class to represent a project plan incorporating file management and digitalization strategies."""

    def __init__(self, project_name):
        """Initialize the project plan with a name and create necessary directories."""
        self.project_name = project_name
        self.base_dir = os.path.join(os.getcwd(), project_name)
        self.strategies = []
        self.create_project_directory()

    def create_project_directory(self):
        """Create the base directory for the project if it does not exist."""
        try:
            os.makedirs(self.base_dir, exist_ok=True)
            print(f"Project directory created at: {self.base_dir}")
        except Exception as e:
            print(f"Error creating project directory: {e}")

    def add_strategy(self, strategy_name, description):
        """Add a strategy to the project plan."""
        strategy = {
            "name": strategy_name,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        self.strategies.append(strategy)
        print(f"Strategy '{strategy_name}' added to the project plan.")

    def save_plan(self):
        """Save the project plan to a JSON file."""
        plan_file = os.path.join(self.base_dir, 'project_plan.json')
        try:
            with open(plan_file, 'w') as file:
                json.dump({"project_name": self.project_name, "strategies": self.strategies}, file, indent=4)
            print(f"Project plan saved to {plan_file}")
        except Exception as e:
            print(f"Error saving project plan: {e}")

    def display_plan(self):
        """Display the details of the project plan."""
        print(f"\nProject Name: {self.project_name}")
        print("Strategies:")
        for strategy in self.strategies:
            print(f"- {strategy['name']}: {strategy['description']} (Added on: {strategy['created_at']})")

# Example usage
if __name__ == "__main__":
    # Create a new project plan
    project = ProjectPlan("EasyDoc File Management Project")
    
    # Add strategies to the project
    project.add_strategy("Centralized Document Storage", "Implement a centralized storage solution for easy access.")
    project.add_strategy("Automated Version Control", "Use version control systems to manage document changes.")
    project.add_strategy("Digitalization of Paper Records", "Convert paper records to digital formats for easy retrieval.")
    
    # Display the project plan
    project.display_plan()
    
    # Save the project plan to a JSON file
    project.save_plan()
```
