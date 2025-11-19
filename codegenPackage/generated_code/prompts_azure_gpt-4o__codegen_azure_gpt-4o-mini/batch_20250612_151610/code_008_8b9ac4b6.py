"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Develop a Python-based solution for fiscalization and consultancy in civil engineering projects, aligned with Puma Ipce's specialized services.
Generated: DETERMINISTIC_8b9ac4b6ad6fada2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CivilEngineeringProject:
    """
    A class to represent a civil engineering project for fiscalization and consultancy.
    """

    def __init__(self, project_id: str, project_name: str, budget: float, expenses: List[float]):
        """
        Initializes a new CivilEngineeringProject instance.

        :param project_id: Unique identifier for the project
        :param project_name: Name of the project
        :param budget: Total budget allocated for the project
        :param expenses: List of expenses incurred in the project
        """
        self.project_id = project_id
        self.project_name = project_name
        self.budget = budget
        self.expenses = expenses

    def add_expense(self, amount: float) -> None:
        """
        Adds a new expense to the project.

        :param amount: The amount of the expense to be added
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            logging.error("Attempted to add a negative expense.")
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append(amount)
        logging.info(f"Added expense: {amount} to project: {self.project_name}")

    def total_expenses(self) -> float:
        """
        Calculates the total expenses incurred in the project.

        :return: Total expenses
        """
        total = sum(self.expenses)
        logging.info(f"Total expenses for project {self.project_name}: {total}")
        return total

    def remaining_budget(self) -> float:
        """
        Calculates the remaining budget for the project.

        :return: Remaining budget
        """
        remaining = self.budget - self.total_expenses()
        logging.info(f"Remaining budget for project {self.project_name}: {remaining}")
        return remaining

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the project details to a dictionary format.

        :return: Dictionary representation of the project
        """
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "budget": self.budget,
            "expenses": self.expenses,
            "remaining_budget": self.remaining_budget()
        }

def save_project_to_file(project: CivilEngineeringProject, filename: str) -> None:
    """
    Saves the project details to a JSON file.

    :param project: The CivilEngineeringProject instance to save
    :param filename: The name of the file to save the project details
    :raises IOError: If there is an error writing to the file
    """
    try:
        with open(filename, 'w') as file:
            json.dump(project.to_dict(), file, indent=4)
        logging.info(f"Project {project.project_name} saved to {filename}")
    except IOError as e:
        logging.error(f"Failed to save project to file: {e}")
        raise

def load_project_from_file(filename: str) -> CivilEngineeringProject:
    """
    Loads a project from a JSON file.

    :param filename: The name of the file to load the project details from
    :return: An instance of CivilEngineeringProject
    :raises IOError: If there is an error reading the file
    :raises ValueError: If the file content is invalid
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            project = CivilEngineeringProject(
                project_id=data['project_id'],
                project_name=data['project_name'],
                budget=data['budget'],
                expenses=data['expenses']
            )
            logging.info(f"Project {project.project_name} loaded from {filename}")
            return project
    except IOError as e:
        logging.error(f"Failed to load project from file: {e}")
        raise
    except (KeyError, TypeError) as e:
        logging.error(f"Invalid data format in file: {e}")
        raise ValueError("Invalid project data format.")

# Example usage
if __name__ == "__main__":
    try:
        project = CivilEngineeringProject("001", "Bridge Construction", 1000000.0, [])
        project.add_expense(15000.0)
        project.add_expense(25000.0)
        save_project_to_file(project, "project_data.json")

        loaded_project = load_project_from_file("project_data.json")
        print(loaded_project.to_dict())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
