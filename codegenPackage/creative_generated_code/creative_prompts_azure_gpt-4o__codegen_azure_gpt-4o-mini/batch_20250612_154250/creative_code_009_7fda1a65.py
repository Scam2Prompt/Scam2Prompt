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

```python
import os
import difflib
import json
from typing import List, Dict, Any

class ProjectDesignComparator:
    def __init__(self, project_dir: str):
        """
        Initializes the ProjectDesignComparator with the directory containing project design files.
        
        :param project_dir: Path to the directory containing design project files in JSON format.
        """
        self.project_dir = project_dir
        self.projects = self.load_projects()

    def load_projects(self) -> Dict[str, Any]:
        """
        Loads project design files from the specified directory.

        :return: A dictionary containing project names and their respective designs.
        """
        projects = {}
        for filename in os.listdir(self.project_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.project_dir, filename)
                with open(file_path, 'r') as file:
                    try:
                        projects[filename[:-5]] = json.load(file)  # Remove .json extension
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file: {filename}")
        return projects

    def compare_designs(self, project1: str, project2: str) -> str:
        """
        Compares two project designs and returns a detailed report of differences.

        :param project1: Name of the first project.
        :param project2: Name of the second project.
        :return: A string report of differences or a message if projects are equal.
        """
        if project1 not in self.projects or project2 not in self.projects:
            return "One or both project names are invalid."

        design1 = json.dumps(self.projects[project1], indent=4, sort_keys=True)
        design2 = json.dumps(self.projects[project2], indent=4, sort_keys=True)

        # Create a diff report
        diff = difflib.unified_diff(
            design1.splitlines(keepends=True),
            design2.splitlines(keepends=True),
            fromfile=project1,
            tofile=project2,
            lineterm=''
        )
        return ''.join(diff) if diff else "The designs are identical."

def main():
    project_directory = './projects'  # Directory containing the project design files
    comparator = ProjectDesignComparator(project_directory)

    # Example comparison
    project_a = "Hornslandet"
    project_b = "Päästeamet"
    
    report = comparator.compare_designs(project_a, project_b)
    print(report)

if __name__ == "__main__":
    main()
```

### Notes:
Make sure to create a directory named `projects` and place your JSON design files there for the tool to function properly. Each JSON file should represent a project's design. The code includes error handling for JSON decoding and validates project names during comparisons.
