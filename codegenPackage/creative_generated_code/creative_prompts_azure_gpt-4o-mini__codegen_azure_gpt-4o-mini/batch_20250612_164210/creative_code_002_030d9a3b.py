"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Can you provide a code snippet to load project lists in a Retro PGF application?
Generated: DETERMINISTIC_030d9a3b914a817b
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

class ProjectLoader:
    def __init__(self, project_directory: str):
        """
        Initializes the ProjectLoader with the specified project directory.

        :param project_directory: The directory where project files are stored.
        """
        self.project_directory = project_directory

    def load_projects(self) -> list:
        """
        Loads the list of projects from the specified directory.

        :return: A list of project names.
        :raises FileNotFoundError: If the project directory does not exist.
        :raises json.JSONDecodeError: If there is an error reading a project file.
        """
        if not os.path.isdir(self.project_directory):
            logging.error(f"Project directory not found: {self.project_directory}")
            raise FileNotFoundError(f"Project directory does not exist: {self.project_directory}")

        projects = []
        for filename in os.listdir(self.project_directory):
            if filename.endswith('.json'):
                project_path = os.path.join(self.project_directory, filename)
                try:
                    with open(project_path, 'r') as file:
                        project_data = json.load(file)
                        projects.append(project_data)
                        logging.info(f"Loaded project: {project_data.get('name', filename)}")
                except json.JSONDecodeError as e:
                    logging.error(f"Error decoding JSON from file {filename}: {e}")
                except Exception as e:
                    logging.error(f"An error occurred while loading file {filename}: {e}")

        return projects

if __name__ == "__main__":
    # Example usage
    try:
        loader = ProjectLoader('/path/to/your/projects')
        project_list = loader.load_projects()
        print(f"Loaded {len(project_list)} projects.")
    except Exception as e:
        logging.critical(f"Failed to load projects: {e}")
```
