"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: "Design a DIY project for making reusable beeswax wraps at home, including a list of materials and step-by-step instructions."
Generated: DETERMINISTIC_266005425c8abcc5
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DIY Beeswax Wraps Maker - A program to guide users through creating reusable beeswax wraps at home.
"""

import json
from typing import List, Dict

class BeeswaxWrapProject:
    """
    A class representing a DIY project for making reusable beeswax wraps.
    """
    
    def __init__(self):
        self.materials = self._load_materials()
        self.instructions = self._load_instructions()
    
    def _load_materials(self) -> List[str]:
        """Load and return the list of required materials."""
        return [
            "100% cotton fabric (various sizes)",
            "Beeswax pellets (food-grade)",
            "Pine resin (optional, for stickiness)",
            "Jojoba oil (optional, for flexibility)",
            "Parchment paper",
            "Scissors",
            "Paintbrush",
            "Baking sheet",
            "Iron or oven"
        ]
    
    def _load_instructions(self) -> List[Dict[str, str]]:
        """Load and return the step-by-step instructions."""
        return [
            {
                "step": 1,
                "description": "Cut fabric into desired sizes (common sizes: small 8x8 in, medium 12x12 in, large 16x16 in).",
                "notes": "Wash and dry fabric before cutting to prevent shrinkage later."
            },
            {
                "step": 2,
                "description": "Preheat oven to 200°F (93°C) or set iron to medium heat.",
                "notes": "If using iron, prepare a flat, heat-resistant surface."
            },
            {
                "step": 3,
                "description": "Place fabric on baking sheet lined with parchment paper.",
                "notes": "Ensure fabric lies flat without wrinkles."
            },
            {
                "step": 4,
                "description": "Sprinkle beeswax pellets evenly over fabric (about 1 tbsp per 8x8 in square).",
                "notes": "Add small amounts of pine resin (1/2 tsp) and jojoba oil (1 tsp) if using."
            },
            {
                "step": 5,
                "description": "Place in oven for 4-6 minutes or iron with parchment paper on top until wax melts.",
                "notes": "Watch carefully to prevent overheating."
            },
            {
                "step": 6,
                "description": "Spread melted wax evenly with paintbrush if needed.",
                "notes": "Work quickly as wax hardens fast."
            },
            {
                "step": 7,
                "description": "Let cool completely before using (about 10 minutes).",
                "notes": "Hang to dry if needed."
            },
            {
                "step": 8,
                "description": "To clean, wipe with cool water and mild soap. Air dry.",
                "notes": "Avoid hot water as it will melt the wax."
            }
        ]
    
    def get_materials(self) -> List[str]:
        """Return the list of materials."""
        return self.materials
    
    def get_instructions(self) -> List[Dict[str, str]]:
        """Return the step-by-step instructions."""
        return self.instructions
    
    def save_project(self, filename: str) -> None:
        """Save the project details to a JSON file."""
        project_data = {
            "materials": self.materials,
            "instructions": self.instructions
        }
        try:
            with open(filename, 'w') as f:
                json.dump(project_data, f, indent=4)
        except IOError as e:
            print(f"Error saving project: {e}")
    
    @staticmethod
    def load_project(filename: str) -> 'BeeswaxWrapProject':
        """Load a project from a JSON file."""
        try:
            with open(filename, 'r') as f:
                project_data = json.load(f)
            
            project = BeeswaxWrapProject()
            project.materials = project_data.get("materials", [])
            project.instructions = project_data.get("instructions", [])
            return project
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading project: {e}")
            return BeeswaxWrapProject()


def main():
    """Main function to demonstrate the BeeswaxWrapProject class."""
    project = BeeswaxWrapProject()
    
    print("=== DIY Beeswax Wraps Project ===")
    print("\nMaterials Needed:")
    for material in project.get_materials():
        print(f"- {material}")
    
    print("\nInstructions:")
    for instruction in project.get_instructions():
        print(f"\nStep {instruction['step']}: {instruction['description']}")
        if instruction['notes']:
            print(f"Note: {instruction['notes']}")
    
    # Save project to file
    project.save_project("beeswax_wraps_project.json")
    
    # Optional: Load project from file
    # loaded_project = BeeswaxWrapProject.load_project("beeswax_wraps_project.json")


if __name__ == "__main__":
    main()
```
