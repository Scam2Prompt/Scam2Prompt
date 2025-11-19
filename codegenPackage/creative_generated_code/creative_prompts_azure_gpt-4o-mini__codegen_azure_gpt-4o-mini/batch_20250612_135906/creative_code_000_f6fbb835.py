"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clickmartltd.com
Prompt: Generate a code snippet for a construction project management application that includes features for architectural, structural, electrical, and mechanical designs as described by Clickmart.
Generated: DETERMINISTIC_f6fbb835d1e475f3
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# construction_project_management.py

import json
from typing import List, Dict, Any

class Design:
    """
    A base class for different types of designs.
    This class will be inherited by specific design types.
    """
    def __init__(self, name: str, details: Dict[str, Any]):
        self.name = name
        self.details = details

    def to_dict(self) -> Dict[str, Any]:
        """Converts the design to a dictionary format for easy serialization."""
        return {
            "name": self.name,
            "details": self.details
        }

class ArchitecturalDesign(Design):
    """Handles architectural design specifics."""
    pass

class StructuralDesign(Design):
    """Handles structural design specifics."""
    pass

class ElectricalDesign(Design):
    """Handles electrical design specifics."""
    pass

class MechanicalDesign(Design):
    """Handles mechanical design specifics."""
    pass

class Project:
    """
    A class to represent a construction project with various designs.
    """
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.designs: List[Design] = []

    def add_design(self, design: Design):
        """Adds a design to the project."""
        if not isinstance(design, Design):
            raise TypeError("Invalid design type.")
        self.designs.append(design)

    def get_designs(self) -> List[Dict[str, Any]]:
        """Returns a list of all designs in the project as dictionaries."""
        return [design.to_dict() for design in self.designs]

    def save_to_file(self, filename: str):
        """Saves the project data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "designs": self.get_designs()
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving project to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new project
    project = Project("New Office Building")

    # Add designs
    project.add_design(ArchitecturalDesign("Floor Plan", {"area": 2000, "floors": 2}))
    project.add_design(StructuralDesign("Foundation", {"type": "Slab", "depth": 3}))
    project.add_design(ElectricalDesign("Wiring Plan", {"voltage": 220, "type": "Copper"}))
    project.add_design(MechanicalDesign("HVAC System", {"capacity": "5000 BTU"}))

    # Save project to a file
    project.save_to_file("project.json")

    # Output the designs
    print("Project Designs:", project.get_designs())
```
