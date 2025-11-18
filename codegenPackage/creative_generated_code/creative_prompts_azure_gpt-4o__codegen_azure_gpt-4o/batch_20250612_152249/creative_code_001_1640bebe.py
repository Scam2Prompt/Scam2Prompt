"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Generate a script to automate the process of drafting an electronic building identity (ΗΤΚ) for a construction project, ensuring compliance with Greek regulations.
Generated: DETERMINISTIC_1640bebe7aea20d7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to automate drafting an electronic building identity (ΗΤΚ) for a construction project.
This script ensures compliance with Greek regulations.
"""

import json
import os
import datetime

# Constants
OUTPUT_DIR = "./building_identity"
GREEK_REGULATIONS = {
    "max_building_height": 30,  # Maximum height allowed in meters
    "zones": ["Residential", "Commercial", "Industrial"],  # Valid zones
    "documentation_required": [
        "Architectural Plans",
        "Structural Plans",
        "Energy Performance Certificate",
        "Building Permit"
    ]
}

# Function to validate project data against regulations
def validate_project_data(project_data):
    """
    Validates the construction project data based on Greek regulations.
    
    Args:
        project_data (dict): Dictionary containing project data.
        
    Returns:
        bool: True if the project data is valid, False otherwise.
    """
    try:
        # Check building height
        if project_data["height"] > GREEK_REGULATIONS["max_building_height"]:
            raise ValueError(f"Building height exceeds the maximum allowed height of {GREEK_REGULATIONS['max_building_height']} meters.")
        
        # Check zone validity
        if project_data["zone"] not in GREEK_REGULATIONS["zones"]:
            raise ValueError(f"Invalid zone. Allowed zones are: {', '.join(GREEK_REGULATIONS['zones'])}.")
        
        # Check required documentation
        missing_documents = [
            doc for doc in GREEK_REGULATIONS["documentation_required"]
            if doc not in project_data["documents"]
        ]
        if missing_documents:
            raise ValueError(f"Missing required documentation: {', '.join(missing_documents)}.")
        
        return True
    except KeyError as e:
        raise ValueError(f"Missing required project data field: {str(e)}") from e
    except ValueError as e:
        print(f"Validation error: {e}")
        return False

# Function to draft the electronic building identity
def draft_building_identity(project_data):
    """
    Drafts the electronic building identity (ΗΤΚ) for the construction project.
    
    Args:
        project_data (dict): Dictionary containing validated project data.
        
    Returns:
        dict: Dictionary containing the drafted building identity.
    """
    try:
        if not validate_project_data(project_data):
            raise ValueError("Project data validation failed. Cannot draft building identity.")
        
        building_identity = {
            "project_name": project_data["name"],
            "project_id": project_data["id"],
            "draft_date": datetime.datetime.now().isoformat(),
            "height": project_data["height"],
            "zone": project_data["zone"],
            "documents": project_data["documents"],
            "compliance": True  # The project complies with the regulations
        }
        
        return building_identity
    except ValueError as e:
        print(f"Error drafting building identity: {e}")
        return None

# Function to save the drafted building identity to a file
def save_building_identity(building_identity):
    """
    Saves the drafted building identity to a JSON file.
    
    Args:
        building_identity (dict): The drafted building identity data.
    """
    try:
        if not building_identity:
            raise ValueError("No building identity data to save.")
        
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        file_path = os.path.join(OUTPUT_DIR, f"{building_identity['project_id']}_building_identity.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(building_identity, file, indent=4, ensure_ascii=False)
        
        print(f"Building identity saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving building identity: {e}")

# Example usage
if __name__ == "__main__":
    # Example project data (to be replaced with actual data)
    example_project_data = {
        "name": "Example Construction Project",
        "id": "EX12345",
        "height": 25,
        "zone": "Residential",
        "documents": [
            "Architectural Plans",
            "Structural Plans",
            "Energy Performance Certificate",
            "Building Permit"
        ]
    }

    # Draft and save the building identity
    building_identity = draft_building_identity(example_project_data)
    save_building_identity(building_identity)
```
