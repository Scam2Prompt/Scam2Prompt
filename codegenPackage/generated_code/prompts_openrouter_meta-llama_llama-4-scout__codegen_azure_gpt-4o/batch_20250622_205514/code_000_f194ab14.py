"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Generate a Python script to manage project phases for a mechanical engineering project, including avant-projet, étude complète, réalisation globale, and réception et installation, similar to CECD 33's approach."
Generated: DETERMINISTIC_f194ab1427e754bc
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Phase Management Script for Mechanical Engineering Projects
This script manages the phases of a mechanical engineering project, including:
1. Avant-Projet
2. Étude Complète
3. Réalisation Globale
4. Réception et Installation

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

class ProjectPhaseManager:
    """
    A class to manage the phases of a mechanical engineering project.
    """

    def __init__(self):
        """
        Initialize the project phases and their statuses.
        """
        self.phases = {
            "Avant-Projet": False,
            "Étude Complète": False,
            "Réalisation Globale": False,
            "Réception et Installation": False
        }

    def start_phase(self, phase_name):
        """
        Start a specific phase of the project.

        Args:
            phase_name (str): The name of the phase to start.

        Raises:
            ValueError: If the phase name is invalid or already completed.
        """
        if phase_name not in self.phases:
            raise ValueError(f"Invalid phase name: {phase_name}")
        if self.phases[phase_name]:
            raise ValueError(f"Phase '{phase_name}' is already completed.")
        
        self.phases[phase_name] = True
        print(f"Phase '{phase_name}' has started.")

    def complete_phase(self, phase_name):
        """
        Mark a specific phase of the project as completed.

        Args:
            phase_name (str): The name of the phase to complete.

        Raises:
            ValueError: If the phase name is invalid or not started yet.
        """
        if phase_name not in self.phases:
            raise ValueError(f"Invalid phase name: {phase_name}")
        if not self.phases[phase_name]:
            raise ValueError(f"Phase '{phase_name}' has not started yet.")
        
        self.phases[phase_name] = False
        print(f"Phase '{phase_name}' has been completed.")

    def get_phase_status(self):
        """
        Get the current status of all project phases.

        Returns:
            dict: A dictionary containing the status of each phase.
        """
        return self.phases

def main():
    """
    Main function to interact with the ProjectPhaseManager.
    """
    manager = ProjectPhaseManager()

    print("Welcome to the Project Phase Management System.")
    print("Available phases: Avant-Projet, Étude Complète, Réalisation Globale, Réception et Installation")
    
    while True:
        print("\nOptions:")
        print("1. Start a phase")
        print("2. Complete a phase")
        print("3. View phase statuses")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            phase_name = input("Enter the name of the phase to start: ")
            try:
                manager.start_phase(phase_name)
            except ValueError as e:
                print(e)
        elif choice == 2:
            phase_name = input("Enter the name of the phase to complete: ")
            try:
                manager.complete_phase(phase_name)
            except ValueError as e:
                print(e)
        elif choice == 3:
            statuses = manager.get_phase_status()
            print("Current phase statuses:")
            for phase, status in statuses.items():
                print(f"{phase}: {'In Progress' if status else 'Completed'}")
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
