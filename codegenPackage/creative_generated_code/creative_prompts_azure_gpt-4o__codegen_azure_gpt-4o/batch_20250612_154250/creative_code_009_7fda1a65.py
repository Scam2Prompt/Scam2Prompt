"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tari.ee
Prompt: Create a tool for comparing architectural project designs, inspired by the diverse projects listed on Tari.ee, such as Hornslandet and Päästeamet.
Generated: DETERMINISTIC_7fda1a65ba48ca8a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation for comparing architectural project designs. This tool focuses on comparing attributes like dimensions, materials, and estimated costs.

```python
import json

class ArchitecturalProject:
    """
    A class representing an architectural project with attributes for comparison.
    """
    def __init__(self, name, dimensions, materials, estimated_cost):
        """
        Initialize the project with name, dimensions, materials, and estimated cost.

        :param name: Name of the project
        :param dimensions: Dimensions of the project (e.g., area in square meters)
        :param materials: List of primary materials used
        :param estimated_cost: Estimated cost of the project
        """
        self.name = name
        self.dimensions = dimensions
        self.materials = materials
        self.estimated_cost = estimated_cost

    def to_dict(self):
        """
        Convert the project details into a dictionary for comparisons.

        :return: Dictionary of project details
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "materials": self.materials,
            "estimated_cost": self.estimated_cost
        }

class ProjectComparisonTool:
    """
    A tool for comparing architectural projects based on various attributes.
    """
    def __init__(self):
        """
        Initialize the comparison tool with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a project to the tool.

        :param project: An instance of ArchitecturalProject
        """
        if not isinstance(project, ArchitecturalProject):
            raise TypeError("The project must be an instance of ArchitecturalProject.")
        self.projects.append(project)

    def compare_projects(self):
        """
        Compare all projects in the tool based on dimensions, materials, and cost.

        :return: A comparison summary as a dictionary
        """
        if len(self.projects) < 2:
            raise ValueError("At least two projects are required for comparison.")
        
        comparison_summary = {
            "size_difference": self._compare_dimensions(),
            "common_materials": self._compare_materials(),
            "cost_difference": self._compare_costs()
        }
        return comparison_summary

    def _compare_dimensions(self):
        """
        Compare the dimensions between projects.

        :return: The difference in dimensions as a dictionary
        """
        dimensions = [project.dimensions for project in self.projects]
        max_dimensions = max(dimensions)
        min_dimensions = min(dimensions)
        return {"max": max_dimensions, "min": min_dimensions, "difference": max_dimensions - min_dimensions}

    def _compare_materials(self):
        """
        Find common materials between projects.

        :return: List of common materials
        """
        material_lists = [set(project.materials) for project in self.projects]
        common_materials = set.intersection(*material_lists)
        return list(common_materials)

    def _compare_costs(self):
        """
        Compare the estimated costs between projects.

        :return: Cost difference summary as a dictionary
        """
        costs = [project.estimated_cost for project in self.projects]
        max_cost = max(costs)
        min_cost = min(costs)
        return {"max": max_cost, "min": min_cost, "difference": max_cost - min_cost}

    def export_comparison_summary(self, file_path="comparison_summary.json"):
        """
        Export the comparison summary to a JSON file.

        :param file_path: Path to the output file
        """
        summary = self.compare_projects()
        try:
            with open(file_path, "w") as file:
                json.dump(summary, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

# Example usage:
if __name__ == "__main__":
    # Create sample architectural projects
    project1 = ArchitecturalProject(
        name="Hornslandet",
        dimensions=500,
        materials=["wood", "glass", "steel"],
        estimated_cost=150000
    )
    
    project2 = ArchitecturalProject(
        name="Päästeamet",
        dimensions=300,
        materials=["concrete", "glass", "steel"],
        estimated_cost=100000
    )
    
    # Initialize the comparison tool
    tool = ProjectComparisonTool()
    
    # Add projects to the tool
    tool.add_project(project1)
    tool.add_project(project2)
    
    # Compare projects and display the summary
    comparison = tool.compare_projects()
    print("Comparison Summary:", comparison)
    
    # Export the comparison summary to a file
    tool.export_comparison_summary("comparison_summary.json")
```

This code implements a robust and reusable architecture for comparing projects based on dimensions, materials, and estimated costs. It includes error handling and adheres to best practices.
