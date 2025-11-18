"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://procreaition.pages.dev
Prompt: Generate a roadmap template for an AI-powered blockchain project, incorporating Procreation AI's phased development approach.
Generated: DETERMINISTIC_f958ab856add981e
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict


class Roadmap:
    """
    A class to represent a roadmap for an AI-powered blockchain project.
    """

    def __init__(self, project_name: str):
        """
        Initializes the Roadmap with a project name and an empty list of phases.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.phases: List[Dict[str, str]] = []

    def add_phase(self, phase_name: str, start_date: str, end_date: str, description: str):
        """
        Adds a phase to the roadmap.

        Args:
            phase_name (str): The name of the phase.
            start_date (str): The start date of the phase in 'YYYY-MM-DD' format.
            end_date (str): The end date of the phase in 'YYYY-MM-DD' format.
            description (str): A description of the phase.
        """
        try:
            # Validate date format
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            if start >= end:
                raise ValueError("Start date must be before end date.")

            # Append phase to the list
            self.phases.append({
                "phase_name": phase_name,
                "start_date": start_date,
                "end_date": end_date,
                "description": description
            })
        except ValueError as e:
            print(f"Error adding phase: {e}")

    def save_to_file(self, file_name: str):
        """
        Saves the roadmap to a JSON file.

        Args:
            file_name (str): The name of the file to save the roadmap.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "phases": self.phases
                }, file, indent=4)
            print(f"Roadmap saved to {file_name}.")
        except IOError as e:
            print(f"Error saving roadmap to file: {e}")

    def load_from_file(self, file_name: str):
        """
        Loads a roadmap from a JSON file.

        Args:
            file_name (str): The name of the file to load the roadmap from.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.project_name = data.get("project_name", "")
                self.phases = data.get("phases", [])
            print(f"Roadmap loaded from {file_name}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading roadmap from file: {e}")

    def display_roadmap(self):
        """
        Displays the roadmap in a readable format.
        """
        print(f"Project: {self.project_name}\nRoadmap:")
        for phase in self.phases:
            print(f"- {phase['phase_name']} ({phase['start_date']} to {phase['end_date']}): {phase['description']}")


# Example usage
if __name__ == "__main__":
    # Create a new roadmap for an AI-powered blockchain project
    roadmap = Roadmap("AI-Powered Blockchain Project")
    
    # Add phases to the roadmap
    roadmap.add_phase("Phase 1: Research", "2024-01-01", "2024-03-01", "Conduct research on blockchain technology and AI integration.")
    roadmap.add_phase("Phase 2: Development", "2024-03-02", "2024-06-01", "Develop the initial version of the AI-powered blockchain system.")
    roadmap.add_phase("Phase 3: Testing", "2024-06-02", "2024-09-01", "Test the system thoroughly for bugs and performance issues.")
    
    # Display the roadmap
    roadmap.display_roadmap()
    
    # Save the roadmap to a file
    roadmap.save_to_file("roadmap.json")
    
    # Load the roadmap from a file
    new_roadmap = Roadmap("")
    new_roadmap.load_from_file("roadmap.json")
    new_roadmap.display_roadmap()
```
