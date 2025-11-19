"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: What are the best practices for integrating architectural design and construction management in a software tool, based on the approach taken by Bismillah Traders?
Generated: DETERMINISTIC_5ad97069022e536d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for design and construction management phases
class Phase(Enum):
    DESIGN = "design"
    CONSTRUCTION = "construction"

# Define a data class for architectural design
@dataclass
class ArchitecturalDesign:
    id: int
    name: str
    description: str
    phase: Phase

# Define a data class for construction management
@dataclass
class ConstructionManagement:
    id: int
    design_id: int
    status: str

# Define a class for integrating architectural design and construction management
class IntegratedTool:
    def __init__(self):
        self.designs = []
        self.construction_projects = []

    # Method to add architectural design
    def add_design(self, design: ArchitecturalDesign):
        """Add a new architectural design to the tool"""
        self.designs.append(design)

    # Method to add construction management project
    def add_construction_project(self, project: ConstructionManagement):
        """Add a new construction management project to the tool"""
        self.construction_projects.append(project)

    # Method to get all designs
    def get_designs(self) -> List[ArchitecturalDesign]:
        """Get all architectural designs"""
        return self.designs

    # Method to get all construction projects
    def get_construction_projects(self) -> List[ConstructionManagement]:
        """Get all construction management projects"""
        return self.construction_projects

    # Method to link design with construction project
    def link_design_with_construction(self, design_id: int, project_id: int):
        """Link a design with a construction project"""
        design = next((d for d in self.designs if d.id == design_id), None)
        project = next((p for p in self.construction_projects if p.id == project_id), None)
        
        if design and project:
            project.design_id = design_id
        else:
            raise ValueError("Design or construction project not found")

    # Method to save data to JSON file
    def save_to_json(self, filename: str):
        """Save data to a JSON file"""
        data = {
            "designs": [d.__dict__ for d in self.designs],
            "construction_projects": [p.__dict__ for p in self.construction_projects]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data to JSON file: {str(e)}")

    # Method to load data from JSON file
    def load_from_json(self, filename: str):
        """Load data from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.designs = [ArchitecturalDesign(**d) for d in data["designs"]]
                self.construction_projects = [ConstructionManagement(**p) for p in data["construction_projects"]]
        except Exception as e:
            print(f"Error loading data from JSON file: {str(e)}")

# Example usage
if __name__ == "__main__":
    tool = IntegratedTool()

    design1 = ArchitecturalDesign(1, "Design 1", "This is design 1", Phase.DESIGN)
    design2 = ArchitecturalDesign(2, "Design 2", "This is design 2", Phase.DESIGN)

    tool.add_design(design1)
    tool.add_design(design2)

    project1 = ConstructionManagement(1, 0, "In Progress")
    project2 = ConstructionManagement(2, 0, "Completed")

    tool.add_construction_project(project1)
    tool.add_construction_project(project2)

    tool.link_design_with_construction(1, 1)
    tool.link_design_with_construction(2, 2)

    tool.save_to_json("data.json")

    tool.load_from_json("data.json")

    print("Designs:")
    for design in tool.get_designs():
        print(design)

    print("\nConstruction Projects:")
    for project in tool.get_construction_projects():
        print(project)
```
