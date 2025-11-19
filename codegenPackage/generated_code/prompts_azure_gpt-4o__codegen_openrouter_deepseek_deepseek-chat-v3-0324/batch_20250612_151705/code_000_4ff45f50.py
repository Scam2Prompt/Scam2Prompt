"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Write Python code to simulate a sales training module for the automobile industry, incorporating project-led training principles as described by Debridge Advisory.
Generated: DETERMINISTIC_4ff45f50b7337fad
Batch ID: 20250612_151705
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
from typing import List, Dict, Optional, Union
import json
import os

class SalesTrainingModule:
    """
    A project-led sales training module for the automobile industry.
    Incorporates principles from Debridge Advisory's methodology.
    """
    
    def __init__(self):
        self.trainees = []
        self.projects = []
        self.curriculum = {
            "modules": [
                "Product Knowledge",
                "Customer Profiling",
                "Sales Process",
                "Negotiation Techniques",
                "Digital Tools",
                "After-Sales Service"
            ],
            "duration_weeks": 8
        }
        self.load_data()
    
    def load_data(self) -> None:
        """Load existing data from JSON files if available."""
        try:
            if os.path.exists("trainees.json"):
                with open("trainees.json", "r") as f:
                    self.trainees = json.load(f)
            
            if os.path.exists("projects.json"):
                with open("projects.json", "r") as f:
                    self.projects = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self) -> None:
        """Save current data to JSON files."""
        try:
            with open("trainees.json", "w") as f:
                json.dump(self.trainees, f, indent=2)
            
            with open("projects.json", "w") as f:
                json.dump(self.projects, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_trainee(self, name: str, experience_years: int, dealership: str) -> Dict:
        """Add a new trainee to the program."""
        trainee = {
            "id": len(self.trainees) + 1,
            "name": name,
            "experience_years": experience_years,
            "dealership": dealership,
            "progress": {module: 0 for module in self.curriculum["modules"]},
            "completed_projects": [],
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": (datetime.now() + timedelta(weeks=self.curriculum["duration_weeks"])).strftime("%Y-%m-%d")
        }
        self.trainees.append(trainee)
        self.save_data()
        return trainee
    
    def create_project(self, name: str, description: str, modules: List[str], difficulty: str = "medium") -> Dict:
        """Create a new project for trainees to work on."""
        if not all(module in self.curriculum["modules"] for module in modules):
            raise ValueError("One or more modules are not in the curriculum")
        
        project = {
            "id": len(self.projects) + 1,
            "name": name,
            "description": description,
            "modules": modules,
            "difficulty": difficulty,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "assigned_to": []
        }
        self.projects.append(project)
        self.save_data()
        return project
    
    def assign_project(self, trainee_id: int, project_id: int) -> Dict:
        """Assign a project to a trainee."""
        trainee = next((t for t in self.trainees if t["id"] == trainee_id), None)
        project = next((p for p in self.projects if p["id"] == project_id), None)
        
        if not trainee or not project:
            raise ValueError("Trainee or project not found")
        
        if project_id in trainee["completed_projects"]:
            raise ValueError("Project already completed by trainee")
        
        if project_id in [p["project_id"] for p in trainee.get("current_projects", [])]:
            raise ValueError("Project already assigned to trainee")
        
        if "current_projects" not in trainee:
            trainee["current_projects"] = []
        
        assignment = {
            "project_id": project_id,
            "assigned_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "in_progress",
            "progress": 0
        }
        
        trainee["current_projects"].append(assignment)
        project["assigned_to"].append(trainee_id)
        self.save_data()
        return assignment
    
    def update_project_progress(self, trainee_id: int, project_id: int, progress: int) -> Dict:
        """Update progress on a trainee's project."""
        if progress < 0 or progress > 100:
            raise ValueError("Progress must be between 0 and 100")
        
        trainee = next((t for t in self.trainees if t["id"] == trainee_id), None)
        if not trainee:
            raise ValueError("Trainee not found")
        
        project = next((p for p in trainee.get("current_projects", []) if p["project_id"] == project_id), None)
        if not project:
            raise ValueError("Project not assigned to trainee")
        
        project["progress"] = progress
        
        if progress == 100:
            project["status"] = "completed"
            project["completed_date"] = datetime.now().strftime("%Y-%m-%d")
            trainee["completed_projects"].append(project_id)
            trainee["current_projects"].remove(project)
            
            # Update module progress based on project modules
            project_details = next((p for p in self.projects if p["id"] == project_id), None)
            if project_details:
                for module in project_details["modules"]:
                    trainee["progress"][module] = min(100, trainee["progress"][module] + 20)
        
        self.save_data()
        return project
    
    def get_trainee_progress(self, trainee_id: int) -> Dict:
        """Get overall progress for a trainee."""
        trainee = next((t for t in self.trainees if t["id"] == trainee_id), None)
        if not trainee:
            raise ValueError("Trainee not found")
        
        total_modules = len(self.curriculum["modules"])
        completed_modules = sum(1 for module, progress in trainee["progress"].items() if progress == 100)
        overall_progress = sum(trainee["progress"].values()) / total_modules
        
        return {
            "trainee_id": trainee_id,
            "name": trainee["name"],
            "overall_progress": round(overall_progress, 2),
            "completed_modules": f"{completed_modules}/{total_modules}",
            "current_projects": len(trainee.get("current_projects", [])),
            "completed_projects": len(trainee["completed_projects"])
        }
    
    def generate_simulation_data(self, num_trainees: int = 10, num_projects: int = 5) -> None:
        """Generate simulation data for testing purposes."""
        dealerships = ["City Motors", "Elite Autos", "Premium Wheels", "Metro Dealers", "Luxury Cars"]
        
        # Create trainees
        for i in range(num_trainees):
            self.add_trainee(
                name=f"Trainee {i+1}",
                experience_years=random.randint(1, 5),
                dealership=random.choice(dealerships)
            )
        
        # Create projects
        project_templates = [
            ("Customer Segmentation Analysis", "Analyze customer data to identify key segments", ["Customer Profiling", "Digital Tools"]),
            ("Competitive Pricing Strategy", "Develop pricing strategy against competitors", ["Negotiation Techniques", "Sales Process"]),
            ("Electric Vehicle Demo Program", "Create demo program for new EV models", ["Product Knowledge", "After-Sales Service"]),
            ("CRM Implementation", "Implement and train on new CRM system", ["Digital Tools", "Sales Process"]),
            ("Service Package Upselling", "Develop strategy to increase after-sales service revenue", ["After-Sales Service", "Negotiation Techniques"])
        ]
        
        for i in range(min(num_projects, len(project_templates))):
            name, desc, modules = project_templates[i]
            self.create_project(
                name=name,
                description=desc,
                modules=modules,
                difficulty=random.choice(["easy", "medium", "hard"])
            )
        
        # Assign projects randomly
        for trainee in self.trainees:
            available_projects = [p for p in self.projects if p["id"] not in trainee.get("completed_projects", [])]
            if available_projects:
                project = random.choice(available_projects)
                self.assign_project(trainee["id"], project["id"])
                
                # Simulate some progress
                if random.random() > 0.3:  # 70% chance of some progress
                    progress = random.randint(10, 100)
                    self.update_project_progress(trainee["id"], project["id"], progress)
        
        self.save_data()
    
    def get_training_analytics(self) -> Dict:
        """Generate analytics for the training program."""
