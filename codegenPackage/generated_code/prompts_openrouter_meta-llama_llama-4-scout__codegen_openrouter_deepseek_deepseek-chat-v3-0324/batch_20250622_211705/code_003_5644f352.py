"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Create a step-by-step guide on how to make a crochet backpack using the techniques described in the Paquete Profesional course, including code snippets for a simple inventory management system."
Generated: DETERMINISTIC_5644f3522f86e18f
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Crochet Backpack Inventory Management System
# This system helps manage materials and track progress for crochet projects

import json
import os
from typing import Dict, List, Optional

class InventoryItem:
    """Class representing an inventory item for crochet materials"""
    
    def __init__(self, name: str, quantity: int, category: str, color: Optional[str] = None):
        """
        Initialize an inventory item
        Args:
            name: Name of the item (e.g., "Yarn", "Hook")
            quantity: Quantity available
            category: Category of item (e.g., "Material", "Tool")
            color: Color of the item (if applicable)
        """
        self.name = name
        self.quantity = quantity
        self.category = category
        self.color = color

    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization"""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'category': self.category,
            'color': self.color
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create item from dictionary"""
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            category=data['category'],
            color=data.get('color')
        )

class CrochetProject:
    """Class representing a crochet project with inventory management"""
    
    def __init__(self, name: str):
        """
        Initialize a crochet project
        Args:
            name: Name of the project
        """
        self.name = name
        self.inventory: List[InventoryItem] = []
        self.steps_completed: List[str] = []
        self.project_steps = [
            "Gather materials",
            "Create base circle",
            "Work up the sides",
            "Add straps",
            "Finish edges",
            "Add decorative elements"
        ]

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the project inventory"""
        self.inventory.append(item)

    def remove_item(self, item_name: str) -> bool:
        """Remove an item from the project inventory"""
        for i, item in enumerate(self.inventory):
            if item.name.lower() == item_name.lower():
                self.inventory.pop(i)
                return True
        return False

    def update_item_quantity(self, item_name: str, new_quantity: int) -> bool:
        """Update the quantity of an inventory item"""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.quantity = new_quantity
                return True
        return False

    def complete_step(self, step_name: str) -> bool:
        """Mark a project step as completed"""
        if step_name in self.project_steps and step_name not in self.steps_completed:
            self.steps_completed.append(step_name)
            return True
        return False

    def get_project_progress(self) -> float:
        """Calculate project completion percentage"""
        if not self.project_steps:
            return 0.0
        return (len(self.steps_completed) / len(self.project_steps)) * 100

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            'name': self.name,
            'inventory': [item.to_dict() for item in self.inventory],
            'steps_completed': self.steps_completed,
            'project_steps': self.project_steps
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CrochetProject':
        """Create project from dictionary"""
        project = cls(data['name'])
        project.inventory = [InventoryItem.from_dict(item) for item in data['inventory']]
        project.steps_completed = data['steps_completed']
        project.project_steps = data['project_steps']
        return project

class InventoryManager:
    """Class for managing multiple crochet projects"""
    
    def __init__(self, storage_file: str = 'crochet_projects.json'):
        """
        Initialize the inventory manager
        Args:
            storage_file: File path for storing project data
        """
        self.storage_file = storage_file
        self.projects: Dict[str, CrochetProject] = {}
        self.load_projects()

    def add_project(self, project: CrochetProject) -> None:
        """Add a project to the manager"""
        self.projects[project.name] = project
        self.save_projects()

    def get_project(self, project_name: str) -> Optional[CrochetProject]:
        """Retrieve a project by name"""
        return self.projects.get(project_name)

    def remove_project(self, project_name: str) -> bool:
        """Remove a project from the manager"""
        if project_name in self.projects:
            del self.projects[project_name]
            self.save_projects()
            return True
        return False

    def save_projects(self) -> None:
        """Save projects to storage file"""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(
                    {name: project.to_dict() for name, project in self.projects.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving projects: {e}")

    def load_projects(self) -> None:
        """Load projects from storage file"""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.projects = {
                        name: CrochetProject.from_dict(project_data)
                        for name, project_data in data.items()
                    }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects: {e}")

# Example usage
if __name__ == "__main__":
    # Create inventory manager
    manager = InventoryManager()
    
    # Create a new crochet backpack project
    backpack_project = CrochetProject("Summer Crochet Backpack")
    
    # Add materials to the project
    backpack_project.add_item(InventoryItem("Cotton Yarn", 5, "Material", "Blue"))
    backpack_project.add_item(InventoryItem("Crochet Hook", 1, "Tool", "4.0mm"))
    backpack_project.add_item(InventoryItem("Stitch Markers", 10, "Tool"))
    
    # Add project to manager
    manager.add_project(backpack_project)
    
    # Complete some steps
    backpack_project.complete_step("Gather materials")
    backpack_project.complete_step("Create base circle")
    
    # Save progress
    manager.save_projects()
```
