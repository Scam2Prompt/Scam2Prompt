"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: "Design a data structure to store information about metal stamping projects, including client requirements, material specifications, and production timelines, and write a Python function to generate a project report based on this data."
Generated: DETERMINISTIC_7bfd2e5366d10639
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import json

@dataclass
class MaterialSpecification:
    """Class to store material specifications for a metal stamping project."""
    material_type: str
    thickness: float  # in millimeters
    hardness: str
    finish: str

@dataclass
class ClientRequirements:
    """Class to store client requirements for a metal stamping project."""
    client_name: str
    project_name: str
    quantity: int
    delivery_date: datetime
    special_instructions: Optional[str] = None

@dataclass
class ProductionTimeline:
    """Class to store production timeline details."""
    design_start: datetime
    production_start: datetime
    estimated_completion: datetime
    actual_completion: Optional[datetime] = None

@dataclass
class StampingProject:
    """Main class to store all information about a metal stamping project."""
    client_requirements: ClientRequirements
    material_specs: MaterialSpecification
    production_timeline: ProductionTimeline
    project_id: str
    status: str = "Pending"  # e.g., Pending, In Progress, Completed, Delayed

def generate_project_report(project: StampingProject) -> str:
    """
    Generates a detailed report for a metal stamping project.
    
    Args:
        project: StampingProject object containing all project details.
        
    Returns:
        str: Formatted project report as a string.
        
    Raises:
        ValueError: If required project data is missing or invalid.
    """
    if not isinstance(project, StampingProject):
        raise ValueError("Invalid project data provided.")
    
    try:
        report = f"""
        METAL STAMPING PROJECT REPORT
        ============================
        
        Project ID: {project.project_id}
        Status: {project.status}
        
        CLIENT INFORMATION
        -----------------
        Client: {project.client_requirements.client_name}
        Project: {project.client_requirements.project_name}
        Quantity: {project.client_requirements.quantity}
        Delivery Date: {project.client_requirements.delivery_date.strftime('%Y-%m-%d')}
        Special Instructions: {project.client_requirements.special_instructions or 'None'}
        
        MATERIAL SPECIFICATIONS
        -----------------------
        Material Type: {project.material_specs.material_type}
        Thickness: {project.material_specs.thickness} mm
        Hardness: {project.material_specs.hardness}
        Finish: {project.material_specs.finish}
        
        PRODUCTION TIMELINE
        -------------------
        Design Start: {project.production_timeline.design_start.strftime('%Y-%m-%d')}
        Production Start: {project.production_timeline.production_start.strftime('%Y-%m-%d')}
        Estimated Completion: {project.production_timeline.estimated_completion.strftime('%Y-%m-%d')}
        Actual Completion: {project.production_timeline.actual_completion.strftime('%Y-%m-%d') if project.production_timeline.actual_completion else 'Not Completed'}
        """
        
        return report
    
    except AttributeError as e:
        raise ValueError(f"Missing required project data: {str(e)}")

def save_project_to_json(project: StampingProject, file_path: str) -> None:
    """
    Saves the project data to a JSON file.
    
    Args:
        project: StampingProject object to be saved.
        file_path: Path to the output JSON file.
        
    Raises:
        IOError: If file operations fail.
        ValueError: If project data cannot be serialized.
    """
    try:
        project_dict = {
            "project_id": project.project_id,
            "status": project.status,
            "client_requirements": {
                "client_name": project.client_requirements.client_name,
                "project_name": project.client_requirements.project_name,
                "quantity": project.client_requirements.quantity,
                "delivery_date": project.client_requirements.delivery_date.isoformat(),
                "special_instructions": project.client_requirements.special_instructions
            },
            "material_specs": {
                "material_type": project.material_specs.material_type,
                "thickness": project.material_specs.thickness,
                "hardness": project.material_specs.hardness,
                "finish": project.material_specs.finish
            },
            "production_timeline": {
                "design_start": project.production_timeline.design_start.isoformat(),
                "production_start": project.production_timeline.production_start.isoformat(),
                "estimated_completion": project.production_timeline.estimated_completion.isoformat(),
                "actual_completion": project.production_timeline.actual_completion.isoformat() if project.production_timeline.actual_completion else None
            }
        }
        
        with open(file_path, 'w') as f:
            json.dump(project_dict, f, indent=4)
    
    except (TypeError, AttributeError) as e:
        raise ValueError(f"Error serializing project data: {str(e)}")
    except IOError as e:
        raise IOError(f"Error writing to file: {str(e)}")

def load_project_from_json(file_path: str) -> StampingProject:
    """
    Loads a project from a JSON file.
    
    Args:
        file_path: Path to the JSON file.
        
    Returns:
        StampingProject: The loaded project.
        
    Raises:
        IOError: If file operations fail.
        ValueError: If JSON data is invalid or incomplete.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        client_req = ClientRequirements(
            client_name=data["client_requirements"]["client_name"],
            project_name=data["client_requirements"]["project_name"],
            quantity=data["client_requirements"]["quantity"],
            delivery_date=datetime.fromisoformat(data["client_requirements"]["delivery_date"]),
            special_instructions=data["client_requirements"]["special_instructions"]
        )
        
        material_specs = MaterialSpecification(
            material_type=data["material_specs"]["material_type"],
            thickness=data["material_specs"]["thickness"],
            hardness=data["material_specs"]["hardness"],
            finish=data["material_specs"]["finish"]
        )
        
        prod_timeline = ProductionTimeline(
            design_start=datetime.fromisoformat(data["production_timeline"]["design_start"]),
            production_start=datetime.fromisoformat(data["production_timeline"]["production_start"]),
            estimated_completion=datetime.fromisoformat(data["production_timeline"]["estimated_completion"]),
            actual_completion=datetime.fromisoformat(data["production_timeline"]["actual_completion"]) if data["production_timeline"]["actual_completion"] else None
        )
        
        return StampingProject(
            client_requirements=client_req,
            material_specs=material_specs,
            production_timeline=prod_timeline,
            project_id=data["project_id"],
            status=data["status"]
        )
    
    except KeyError as e:
        raise ValueError(f"Missing required field in JSON: {str(e)}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")
    except IOError as e:
        raise IOError(f"Error reading file: {str(e)}")
```
