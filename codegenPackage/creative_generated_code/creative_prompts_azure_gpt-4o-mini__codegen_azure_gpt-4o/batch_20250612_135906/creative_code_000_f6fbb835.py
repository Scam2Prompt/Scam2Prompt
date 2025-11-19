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
# Construction Project Management Application
# This application handles features for architectural, structural, electrical, and mechanical designs.

import json

class ConstructionProject:
    """
    Represents a construction project with various design components.
    """

    def __init__(self, project_name):
        """
        Initialize the construction project with a name and empty design components.
        """
        self.project_name = project_name
        self.designs = {
            "architectural": {},
            "structural": {},
            "electrical": {},
            "mechanical": {}
        }

    def add_design(self, design_type, design_name, details):
        """
        Add a design component to the project.

        :param design_type: Type of design (architectural, structural, electrical, mechanical)
        :param design_name: Name of the design
        :param details: Details of the design as a dictionary
        """
        if design_type not in self.designs:
            raise ValueError(f"Invalid design type: {design_type}. Must be one of {list(self.designs.keys())}.")
        
        # Ensure design_name is unique within the design type
        if design_name in self.designs[design_type]:
            raise ValueError(f"Design name '{design_name}' already exists in {design_type} designs.")
        
        self.designs[design_type][design_name] = details

    def get_design(self, design_type, design_name):
        """
        Retrieve details of a specific design.

        :param design_type: Type of design (architectural, structural, electrical, mechanical)
        :param design_name: Name of the design
        :returns: Details of the design or None if not found
        """
        return self.designs.get(design_type, {}).get(design_name)

    def list_designs(self, design_type):
        """
        List all designs of a specific type.

        :param design_type: Type of design (architectural, structural, electrical, mechanical)
        :returns: List of design names
        """
        if design_type not in self.designs:
            raise ValueError(f"Invalid design type: {design_type}. Must be one of {list(self.designs.keys())}.")
        
        return list(self.designs[design_type].keys())

    def export_project(self, filepath):
        """
        Export the project details to a JSON file.

        :param filepath: Filepath to save the project data
        """
        try:
            with open(filepath, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "designs": self.designs
                }, file, indent=4)
            print(f"Project exported successfully to {filepath}")
        except Exception as e:
            print(f"Error exporting project: {e}")

    def import_project(self, filepath):
        """
        Import project details from a JSON file.

        :param filepath: Filepath to load the project data
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                self.project_name = data.get("project_name", self.project_name)
                self.designs = data.get("designs", self.designs)
            print(f"Project imported successfully from {filepath}")
        except Exception as e:
            print(f"Error importing project: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = ConstructionProject("Clickmart Office Building")

        # Add designs
        project.add_design("architectural", "Floor Plan", {"description": "Main office floor plan", "version": "1.0"})
        project.add_design("structural", "Foundation Design", {"description": "Concrete foundation", "version": "2.0"})
        project.add_design("electrical", "Wiring Diagram", {"description": "Office wiring diagram", "version": "1.0"})
        project.add_design("mechanical", "HVAC System", {"description": "Heating and cooling system", "version": "3.1"})

        # List designs
        print("Architectural Designs:", project.list_designs("architectural"))
        print("Structural Designs:", project.list_designs("structural"))

        # Get specific design
        wiring_details = project.get_design("electrical", "Wiring Diagram")
        print("Electrical Design (Wiring Diagram):", wiring_details)

        # Export and import project data
        export_path = "project_data.json"
        project.export_project(export_path)  # Exports data to JSON file

        imported_project = ConstructionProject("Imported Project")
        imported_project.import_project(export_path)  # Imports data from JSON file
        print("Imported Project Name:", imported_project.project_name)

    except Exception as e:
        print(f"Error encountered: {e}")
```
