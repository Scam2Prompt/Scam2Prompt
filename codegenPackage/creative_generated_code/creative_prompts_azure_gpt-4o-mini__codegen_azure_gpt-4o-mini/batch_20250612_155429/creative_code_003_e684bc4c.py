"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Create a function that allows users to submit their interior design project ideas, inspired by the client collaboration process at Zirciulit.
Generated: DETERMINISTIC_e684bc4ccd0625dc
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class DesignProjectSubmissionError(Exception):
    """Custom exception for design project submission errors."""
    pass

class DesignProject:
    """Class to represent a user's interior design project idea."""

    def __init__(self, project_name: str, client_name: str, description: str):
        self.project_name = project_name
        self.client_name = client_name
        self.description = description

    def to_dict(self) -> Dict[str, str]:
        """Convert the design project to a dictionary."""
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "description": self.description
        }

class DesignProjectPortal:
    """Class for handling design project submissions."""

    def __init__(self):
        # Storage for submitted projects
        self.projects: List[DesignProject] = []

    def submit_project(self, project_name: str, client_name: str, description: str) -> None:
        """Submits a new design project idea.

        Args:
            project_name (str): The name of the project.
            client_name (str): The name of the client.
            description (str): A brief description of the project.

        Raises:
            DesignProjectSubmissionError: If any of the input fields are invalid or empty.
        """
        # Validate inputs
        if not project_name or not client_name or not description:
            raise DesignProjectSubmissionError("All fields are required.")

        # Create a new project instance
        new_project = DesignProject(project_name, client_name, description)
        
        # Append to the project list
        self.projects.append(new_project)

        # Log the submission
        self.log_submission(new_project)

    def log_submission(self, project: DesignProject) -> None:
        """Logs the project submission to a JSON file.

        Args:
            project (DesignProject): The project to log.
        """
        try:
            # Save to a JSON file
            with open("submitted_projects.json", "a") as file:
                file.write(json.dumps(project.to_dict()) + "\n")
        except IOError as e:
            raise DesignProjectSubmissionError(f"Failed to log submission: {e}")

# Example usage
if __name__ == "__main__":
    portal = DesignProjectPortal()
    try:
        portal.submit_project("Modern Living Room", "Alice Smith", "A cozy and modern living room with neutral colors.")
        print("Project submitted successfully.")
    except DesignProjectSubmissionError as e:
        print(f"Error submitting project: {e}")
```
