"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Develop a Python-based solution for fiscalization and consultancy in civil engineering projects, aligned with Puma Ipce's specialized services.
Generated: DETERMINISTIC_8b9ac4b6ad6fada2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CivilEngineeringProject:
    """
    A class to represent a civil engineering project with fiscalization and consultancy services.
    """

    def __init__(self, project_id: str, project_name: str, budget: float, consultants: List[str]):
        """
        Initializes a new CivilEngineeringProject instance.

        Args:
            project_id (str): Unique identifier for the project.
            project_name (str): Name of the project.
            budget (float): Budget allocated for the project.
            consultants (List[str]): List of consultants assigned to the project.
        """
        self.project_id = project_id
        self.project_name = project_name
        self.budget = budget
        self.consultants = consultants
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        """
        Adds an expense to the project.

        Args:
            description (str): Description of the expense.
            amount (float): Amount of the expense.

        Raises:
            ValueError: If the expense amount is negative or exceeds the available budget.
        """
        if amount < 0:
            logging.error("Attempted to add a negative expense amount.")
            raise ValueError("Expense amount cannot be negative.")
        if (self.get_total_expenses() + amount) > self.budget:
            logging.error("Expense exceeds the available budget.")
            raise ValueError("Expense exceeds the available budget.")

        self.expenses.append({"description": description, "amount": amount})
        logging.info(f"Added expense: {description} of amount: {amount}")

    def get_total_expenses(self) -> float:
        """
        Calculates the total expenses for the project.

        Returns:
            float: Total amount of all expenses.
        """
        return sum(expense["amount"] for expense in self.expenses)

    def serialize(self) -> Dict[str, Any]:
        """
        Serializes the project data to a dictionary format.

        Returns:
            Dict[str, Any]: Serialized project data.
        """
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "budget": self.budget,
            "consultants": self.consultants,
            "expenses": self.expenses,
            "total_expenses": self.get_total_expenses()
        }

def save_project_to_file(project: CivilEngineeringProject, file_path: str):
    """
    Saves the project data to a JSON file.

    Args:
        project (CivilEngineeringProject): The project to save.
        file_path (str): Path where the project data will be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(project.serialize(), file, indent=4)
            logging.info(f"Project data saved to {file_path}")
    except IOError as e:
        logging.error(f"Failed to write to file {file_path}: {e}")
        raise

def main():
    """
    Main function to demonstrate the CivilEngineeringProject functionality.
    """
    # Example usage
    try:
        project = CivilEngineeringProject(project_id="CE-001", project_name="Urban Development", budget=1000000, consultants=["Alice", "Bob"])
        
        project.add_expense("Initial Survey", 20000)
        project.add_expense("Material Costs", 150000)
        
        # Save project data to file
        save_project_to_file(project, "project_data.json")
        
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
