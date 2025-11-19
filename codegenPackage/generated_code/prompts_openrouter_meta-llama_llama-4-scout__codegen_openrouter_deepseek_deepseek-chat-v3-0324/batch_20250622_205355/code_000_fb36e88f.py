"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: "Generate a sales training program for a real estate company using project-led training methods."
Generated: DETERMINISTIC_fb36e88fda85da14
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sales Training Program for Real Estate Company
Project-Led Training Implementation
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Trainee:
    """Represents a sales trainee in the program."""
    
    def __init__(self, name: str, experience_level: str):
        self.name = name
        self.experience_level = experience_level
        self.completed_projects = []
        self.current_project = None
        self.skill_scores = {
            "prospecting": 0,
            "presentation": 0,
            "negotiation": 0,
            "closing": 0
        }
    
    def start_project(self, project: 'Project') -> None:
        """Assign a project to the trainee."""
        if self.current_project is not None:
            raise ValueError("Trainee is already working on a project")
        self.current_project = project
    
    def complete_project(self, performance_score: float) -> None:
        """Mark the current project as completed with performance score."""
        if self.current_project is None:
            raise ValueError("No active project to complete")
        
        self.completed_projects.append({
            "project": self.current_project,
            "completion_date": datetime.now(),
            "performance_score": performance_score
        })
        
        # Update skills based on project type
        for skill in self.current_project.skills_developed:
            self.skill_scores[skill] = min(100, self.skill_scores[skill] + 10)
        
        self.current_project = None
    
    def get_skill_level(self, skill: str) -> int:
        """Get the trainee's current skill level."""
        return self.skill_scores.get(skill, 0)
    
    def __str__(self) -> str:
        return f"Trainee: {self.name} ({self.experience_level})"

class Project:
    """Represents a training project for sales trainees."""
    
    def __init__(self, name: str, description: str, duration_days: int, skills_developed: List[str]):
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.skills_developed = skills_developed
        self.start_date = None
        self.completion_date = None
    
    def start(self) -> None:
        """Mark the project as started."""
        self.start_date = datetime.now()
    
    def complete(self) -> None:
        """Mark the project as completed."""
        if self.start_date is None:
            raise ValueError("Project must be started before completion")
        self.completion_date = datetime.now()
    
    def is_completed(self) -> bool:
        """Check if project is completed."""
        return self.completion_date is not None
    
    def __str__(self) -> str:
        return f"Project: {self.name}"

class TrainingProgram:
    """Manages the sales training program with project-led approach."""
    
    def __init__(self):
        self.trainees = []
        self.projects = []
        self.project_templates = [
            {
                "name": "Cold Calling Mastery",
                "description": "Practice cold calling techniques with real leads",
                "duration": 7,
                "skills": ["prospecting"]
            },
            {
                "name": "Listing Presentation",
                "description": "Develop and deliver compelling listing presentations",
                "duration": 10,
                "skills": ["presentation"]
            },
            {
                "name": "Price Negotiation",
                "description": "Simulate price negotiations with various client types",
                "duration": 14,
                "skills": ["negotiation"]
            },
            {
                "name": "Closing Techniques",
                "description": "Practice different closing techniques in simulated scenarios",
                "duration": 10,
                "skills": ["closing"]
            },
            {
                "name": "Full Sales Cycle",
                "description": "Complete a full sales cycle from prospecting to closing",
                "duration": 21,
                "skills": ["prospecting", "presentation", "negotiation", "closing"]
            }
        ]
    
    def add_trainee(self, trainee: Trainee) -> None:
        """Add a new trainee to the program."""
        self.trainees.append(trainee)
    
    def create_project(self, template_name: str) -> Project:
        """Create a new project based on a template."""
        template = next((t for t in self.project_templates if t["name"] == template_name), None)
        if template is None:
            raise ValueError(f"Project template '{template_name}' not found")
        
        project = Project(
            name=template["name"],
            description=template["description"],
            duration_days=template["duration"],
            skills_developed=template["skills"]
        )
        self.projects.append(project)
        return project
    
    def assign_project(self, trainee: Trainee, project: Project) -> None:
        """Assign a project to a trainee."""
        if trainee not in self.trainees:
            raise ValueError("Trainee not in program")
        if project not in self.projects:
            raise ValueError("Project not in program")
        
        trainee.start_project(project)
        project.start()
    
    def evaluate_trainee(self, trainee: Trainee, performance_score: float) -> None:
        """Evaluate a trainee's performance on their current project."""
        if trainee.current_project is None:
            raise ValueError("Trainee has no active project")
        
        trainee.complete_project(performance_score)
        trainee.current_project.complete()
    
    def get_trainee_progress(self, trainee: Trainee) -> Dict:
        """Get progress report for a trainee."""
        return {
            "name": trainee.name,
            "experience_level": trainee.experience_level,
            "completed_projects": len(trainee.completed_projects),
            "current_project": str(trainee.current_project) if trainee.current_project else None,
            "skill_scores": trainee.skill_scores
        }
    
    def recommend_next_project(self, trainee: Trainee) -> Optional[Project]:
        """Recommend the next project based on trainee's skill levels."""
        if trainee.current_project is not None:
            return None
        
        # Find the skill with lowest score
        weakest_skill = min(trainee.skill_scores.items(), key=lambda x: x[1])[0]
        
        # Find projects that develop this skill
        suitable_projects = [
            t for t in self.project_templates 
            if weakest_skill in t["skills"] and 
            not any(p["project"].name == t["name"] for p in trainee.completed_projects)
        ]
        
        if not suitable_projects:
            # If all projects for this skill are completed, recommend full cycle
            full_cycle = next(t for t in self.project_templates if t["name"] == "Full Sales Cycle")
            return self.create_project(full_cycle["name"])
        
        # Choose randomly from suitable projects
        chosen_template = random.choice(suitable_projects)
        return self.create_project(chosen_template["name"])

# Example usage
if __name__ == "__main__":
    # Initialize training program
    program = TrainingProgram()
    
    # Add trainees
    trainee1 = Trainee("John Doe", "Beginner")
    trainee2 = Trainee("Jane Smith", "Intermediate")
    program.add_trainee(trainee1)
    program.add_trainee(trainee2)
    
    # Create and assign initial projects
    cold_calling = program.create_project("Cold Calling Mastery")
    program.assign_project(trainee1, cold_calling)
    
    listing_presentation = program.create_project("Listing Presentation")
    program.assign_project(trainee2, listing_presentation)
    
    # Simulate project completion
    program.evaluate_trainee(trainee1, 85.5)
    program.evaluate_trainee(trainee2, 92.0)
    
    # Get progress reports
    print("Trainee Progress Reports:")
    print(program.get_trainee_progress(trainee1))
    print(program.get_trainee_progress(trainee2))
    
    # Recommend next projects
    print("\nRecommended Next Projects:")
    next_project1 = program.recommend_next_project(trainee1)
    next_project2 = program.recommend_next_project(trainee2)
    print(f"For {trainee1.name}: {next_project1}")
    print(f"For {trainee2.name}: {next_project2}")
```
