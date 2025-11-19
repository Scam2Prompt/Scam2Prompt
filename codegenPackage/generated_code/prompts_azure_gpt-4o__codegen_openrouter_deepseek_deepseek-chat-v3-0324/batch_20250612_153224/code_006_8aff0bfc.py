"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Create a program to facilitate entrepreneurship training sessions, including modules for business idea generation, project planning, and administrative setup, based on the training structure described by Global Service Consulting.
Generated: DETERMINISTIC_8aff0bfcbdb21b59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Entrepreneurship Training Program
This program facilitates entrepreneurship training sessions with modules for:
- Business Idea Generation
- Project Planning
- Administrative Setup

Based on the training structure described by Global Service Consulting.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class TrainingModule:
    """Base class for all training modules."""
    
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_completed(self) -> None:
        """Mark the module as completed."""
        self.completed = True
    
    def get_status(self) -> str:
        """Return the completion status of the module."""
        return "Completed" if self.completed else "Pending"
    
    def display(self) -> None:
        """Display module information."""
        print(f"\nModule: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.get_status()}")

class BusinessIdeaGeneration(TrainingModule):
    """Module for business idea generation."""
    
    def __init__(self):
        super().__init__(
            "Business Idea Generation",
            "Generate and evaluate business ideas based on market needs and personal skills."
        )
        self.ideas: List[str] = []
    
    def add_idea(self, idea: str) -> None:
        """Add a business idea to the list."""
        if idea.strip():
            self.ideas.append(idea)
    
    def display_ideas(self) -> None:
        """Display all business ideas."""
        print("\nBusiness Ideas:")
        for idx, idea in enumerate(self.ideas, 1):
            print(f"{idx}. {idea}")

class ProjectPlanning(TrainingModule):
    """Module for project planning."""
    
    def __init__(self):
        super().__init__(
            "Project Planning",
            "Create a detailed project plan including milestones, timelines, and resources."
        )
        self.milestones: Dict[str, str] = {}  # milestone: deadline
    
    def add_milestone(self, milestone: str, deadline: str) -> None:
        """Add a milestone with deadline."""
        try:
            datetime.strptime(deadline, "%Y-%m-%d")  # Validate date format
            self.milestones[milestone] = deadline
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
    
    def display_milestones(self) -> None:
        """Display all milestones."""
        print("\nProject Milestones:")
        for milestone, deadline in self.milestones.items():
            print(f"- {milestone} (Deadline: {deadline})")

class AdministrativeSetup(TrainingModule):
    """Module for administrative setup."""
    
    def __init__(self):
        super().__init__(
            "Administrative Setup",
            "Set up legal, financial, and operational aspects of the business."
        )
        self.tasks: Dict[str, bool] = {
            "Business Registration": False,
            "Tax Compliance": False,
            "Bank Account Setup": False,
            "Insurance": False
        }
    
    def complete_task(self, task_name: str) -> None:
        """Mark an administrative task as completed."""
        if task_name in self.tasks:
            self.tasks[task_name] = True
        else:
            print(f"Error: Task '{task_name}' not found.")
    
    def display_tasks(self) -> None:
        """Display all administrative tasks."""
        print("\nAdministrative Tasks:")
        for task, completed in self.tasks.items():
            status = "✓" if completed else "✗"
            print(f"{status} {task}")

class EntrepreneurshipTraining:
    """Main class for the entrepreneurship training program."""
    
    def __init__(self):
        self.modules = {
            "idea": BusinessIdeaGeneration(),
            "planning": ProjectPlanning(),
            "admin": AdministrativeSetup()
        }
        self.participant_name: Optional[str] = None
    
    def register_participant(self, name: str) -> None:
        """Register a participant for the training."""
        if name.strip():
            self.participant_name = name.strip()
        else:
            print("Error: Participant name cannot be empty.")
    
    def get_module(self, module_key: str) -> Optional[TrainingModule]:
        """Get a training module by its key."""
        return self.modules.get(module_key.lower())
    
    def save_progress(self, filename: str = "training_progress.json") -> None:
        """Save training progress to a JSON file."""
        if not self.participant_name:
            print("Error: Participant must be registered before saving progress.")
            return
        
        progress_data = {
            "participant": self.participant_name,
            "modules": {
                "idea": {
                    "completed": self.modules["idea"].completed,
                    "ideas": self.modules["idea"].ideas
                },
                "planning": {
                    "completed": self.modules["planning"].completed,
                    "milestones": self.modules["planning"].milestones
                },
                "admin": {
                    "completed": self.modules["admin"].completed,
                    "tasks": self.modules["admin"].tasks
                }
            },
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(progress_data, f, indent=2)
            print(f"Progress saved to {filename}")
        except IOError as e:
            print(f"Error saving progress: {e}")
    
    def load_progress(self, filename: str = "training_progress.json") -> None:
        """Load training progress from a JSON file."""
        try:
            with open(filename, "r") as f:
                progress_data = json.load(f)
            
            self.participant_name = progress_data["participant"]
            
            # Load idea module
            idea_data = progress_data["modules"]["idea"]
            self.modules["idea"].completed = idea_data["completed"]
            self.modules["idea"].ideas = idea_data["ideas"]
            
            # Load planning module
            planning_data = progress_data["modules"]["planning"]
            self.modules["planning"].completed = planning_data["completed"]
            self.modules["planning"].milestones = planning_data["milestones"]
            
            # Load admin module
            admin_data = progress_data["modules"]["admin"]
            self.modules["admin"].completed = admin_data["completed"]
            self.modules["admin"].tasks = admin_data["tasks"]
            
            print(f"Progress loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error loading progress: Invalid file format. {e}")
    
    def display_summary(self) -> None:
        """Display a summary of the training progress."""
        if not self.participant_name:
            print("No participant registered.")
            return
        
        print(f"\nTraining Summary for {self.participant_name}")
        print("=" * 40)
        for module in self.modules.values():
            module.display()
            if isinstance(module, BusinessIdeaGeneration) and module.ideas:
                module.display_ideas()
            elif isinstance(module, ProjectPlanning) and module.milestones:
                module.display_milestones()
            elif isinstance(module, AdministrativeSetup):
                module.display_tasks()

def main_menu() -> None:
    """Display the main menu and handle user input."""
    training = EntrepreneurshipTraining()
    
    while True:
        print("\nEntrepreneurship Training Program")
        print("1. Register Participant")
        print("2. Business Idea Generation")
        print("3. Project Planning")
        print("4. Administrative Setup")
        print("5. View Progress Summary")
        print("6. Save Progress")
        print("7. Load Progress")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            name = input("Enter participant name: ")
            training.register_participant(name)
        
        elif choice == "2":
            module = training.get_module("idea")
            if module:
                module.display()
                print("\n1. Add Business Idea")
                print("2. Mark Module Complete")
                print("3. Back to Main Menu")
                sub_choice = input("Enter choice (1-3): ")
                
                if sub_choice == "1":
                    idea = input("Enter business idea: ")
                    module.add_idea(idea)
                elif sub_choice == "2":
                    module.mark_completed()
        
        elif choice == "3":
            module = training.get_module("planning")
            if module:
                module.display()
                print("\n1. Add Milestone")
                print("2. Mark Module Complete")
                print("3. Back to Main Menu")
                sub_choice = input("Enter choice (1-3): ")
                
                if sub_choice == "1":
                    milestone = input("Enter milestone: ")
                    deadline = input("Enter deadline (YYYY-MM-DD): ")
                    module.add_milestone(milestone, deadline)
                elif sub_choice == "2":
                    module.mark_completed()
