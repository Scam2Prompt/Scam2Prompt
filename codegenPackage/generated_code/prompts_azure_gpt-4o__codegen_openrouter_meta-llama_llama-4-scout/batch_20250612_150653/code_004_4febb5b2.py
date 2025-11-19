"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: Write code to generate a detailed report on building reconstruction projects, including structural reinforcement, facade restoration, and engineering network upgrades, as described on the ExpertStroy website.
Generated: DETERMINISTIC_4febb5b207900ee8
Batch ID: 20250612_150653
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

# Define Enum for project status
class ProjectStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

# Define data class for structural reinforcement
@dataclass
class StructuralReinforcement:
    """Class to represent structural reinforcement details"""
    material: str
    quantity: int
    cost: float

# Define data class for facade restoration
@dataclass
class FacadeRestoration:
    """Class to represent facade restoration details"""
    material: str
    area: float
    cost: float

# Define data class for engineering network upgrades
@dataclass
class EngineeringNetworkUpgrades:
    """Class to represent engineering network upgrades details"""
    network_type: str
    length: float
    cost: float

# Define data class for building reconstruction project
@dataclass
class BuildingReconstructionProject:
    """Class to represent building reconstruction project details"""
    project_id: int
    project_name: str
    status: ProjectStatus
    structural_reinforcement: List[StructuralReinforcement]
    facade_restoration: List[FacadeRestoration]
    engineering_network_upgrades: List[EngineeringNetworkUpgrades]

# Define function to generate report
def generate_report(project: BuildingReconstructionProject) -> str:
    """
    Generate a detailed report on building reconstruction project.

    Args:
        project (BuildingReconstructionProject): The project details.

    Returns:
        str: A detailed report on the project.
    """
    report = f"Project ID: {project.project_id}\n"
    report += f"Project Name: {project.project_name}\n"
    report += f"Status: {project.status.value.capitalize()}\n\n"

    report += "Structural Reinforcement:\n"
    for i, reinforcement in enumerate(project.structural_reinforcement, start=1):
        report += f"  {i}. Material: {reinforcement.material}, Quantity: {reinforcement.quantity}, Cost: ${reinforcement.cost:.2f}\n"

    report += "\nFacade Restoration:\n"
    for i, restoration in enumerate(project.facade_restoration, start=1):
        report += f"  {i}. Material: {restoration.material}, Area: {restoration.area:.2f} sq.m, Cost: ${restoration.cost:.2f}\n"

    report += "\nEngineering Network Upgrades:\n"
    for i, upgrade in enumerate(project.engineering_network_upgrades, start=1):
        report += f"  {i}. Network Type: {upgrade.network_type}, Length: {upgrade.length:.2f} m, Cost: ${upgrade.cost:.2f}\n"

    return report

# Define function to load project data from JSON
def load_project_data(file_path: str) -> BuildingReconstructionProject:
    """
    Load project data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        BuildingReconstructionProject: The project details.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the JSON is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            project = BuildingReconstructionProject(
                project_id=data['project_id'],
                project_name=data['project_name'],
                status=ProjectStatus(data['status']),
                structural_reinforcement=[StructuralReinforcement(**item) for item in data['structural_reinforcement']],
                facade_restoration=[FacadeRestoration(**item) for item in data['facade_restoration']],
                engineering_network_upgrades=[EngineeringNetworkUpgrades(**item) for item in data['engineering_network_upgrades']]
            )
            return project
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None

# Main function
def main():
    file_path = 'project_data.json'
    project = load_project_data(file_path)
    if project:
        report = generate_report(project)
        print(report)

        # Save report to file
        with open('project_report.txt', 'w') as file:
            file.write(report)
        print("Report saved to project_report.txt")

if __name__ == "__main__":
    main()
```

Example JSON file (`project_data.json`):
```json
{
    "project_id": 1,
    "project_name": "Building Reconstruction Project",
    "status": "in_progress",
    "structural_reinforcement": [
        {"material": "Steel", "quantity": 100, "cost": 10000.0},
        {"material": "Concrete", "quantity": 50, "cost": 5000.0}
    ],
    "facade_restoration": [
        {"material": "Glass", "area": 1000.0, "cost": 20000.0},
        {"material": "Stone", "area": 500.0, "cost": 10000.0}
    ],
    "engineering_network_upgrades": [
        {"network_type": "Water Supply", "length": 1000.0, "cost": 30000.0},
        {"network_type": "Electrical", "length": 500.0, "cost": 15000.0}
    ]
}
```
