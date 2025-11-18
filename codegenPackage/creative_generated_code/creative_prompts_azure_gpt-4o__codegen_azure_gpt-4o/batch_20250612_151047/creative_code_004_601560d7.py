"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write a function to calculate the total material requirements for tile and marble installation projects, considering AKNAN's technical capabilities.
Generated: DETERMINISTIC_601560d7e8e7b647
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: material_calculator.py
Description: Contains a function to calculate total material requirements for tile and marble installation projects.
Author: Expert Programmer
"""

def calculate_material_requirements(projects):
    """
    Calculate the total material requirements for tile and marble installation projects.
    
    Parameters:
        projects (list of dict): A list of projects. Each project is represented as a dictionary
                                 with the following structure:
                                 {
                                     "type": "tile" or "marble",
                                     "area_sq_m": float,  # Area in square meters
                                     "wastage_percentage": float  # Percentage of wastage to consider
                                 }
                                 
    Returns:
        dict: A dictionary containing the total material requirements for each type:
              {
                  "tile": float,  # Total tile material required in square meters
                  "marble": float  # Total marble material required in square meters
              }
              
    Raises:
        ValueError: If a project's area_sq_m is negative or if wastage_percentage is not in the range [0, 100].
    """
    
    # Initialize totals for tile and marble
    totals = {"tile": 0.0, "marble": 0.0}
    
    for project in projects:
        try:
            # Validate input
            if project["area_sq_m"] < 0:
                raise ValueError(f"Project area cannot be negative: {project['area_sq_m']}")
            if not (0 <= project["wastage_percentage"] <= 100):
                raise ValueError(f"Wastage percentage must be between 0 and 100: {project['wastage_percentage']}")
            
            # Calculate total material required for the current project
            material_required = project["area_sq_m"] * (1 + project["wastage_percentage"] / 100)
            
            # Add to the appropriate total based on project type
            if project["type"] == "tile":
                totals["tile"] += material_required
            elif project["type"] == "marble":
                totals["marble"] += material_required
            else:
                raise ValueError(f"Invalid project type: {project['type']}")
        
        except KeyError as e:
            raise ValueError(f"Missing required project key: {e}")
    
    return totals

# Example usage:
if __name__ == "__main__":
    try:
        projects = [
            {"type": "tile", "area_sq_m": 50.5, "wastage_percentage": 5.0},
            {"type": "marble", "area_sq_m": 75.0, "wastage_percentage": 8.0},
            {"type": "tile", "area_sq_m": 100.0, "wastage_percentage": 10.0},
        ]
        
        total_requirements = calculate_material_requirements(projects)
        print("Total material requirements:", total_requirements)
    except ValueError as e:
        print(f"Error: {e}")
```
