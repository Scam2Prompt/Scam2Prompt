"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Develop a tool to assist in infrastructure project feasibility studies, including cost estimation and risk analysis, inspired by Unison Plus's consulting services.
Generated: DETERMINISTIC_3eaf55ece330d678
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InfrastructureProject:
    """
    A class to represent an infrastructure project for feasibility studies.
    """

    def __init__(self, name: str, budget: float, risks: List[str]):
        """
        Initializes the InfrastructureProject with a name, budget, and associated risks.

        :param name: Name of the project
        :param budget: Estimated budget for the project
        :param risks: List of potential risks associated with the project
        """
        self.name = name
        self.budget = budget
        self.risks = risks

    def estimate_cost(self, additional_costs: float) -> float:
        """
        Estimates the total cost of the project including additional costs.

        :param additional_costs: Additional costs to be added to the budget
        :return: Total estimated cost
        """
        total_cost = self.budget + additional_costs
        return total_cost

    def analyze_risks(self) -> Dict[str, Any]:
        """
        Analyzes the risks associated with the project.

        :return: A dictionary containing risk analysis results
        """
        risk_analysis = {
            "total_risks": len(self.risks),
            "risks": self.risks,
            "risk_level": self.evaluate_risk_level()
        }
        return risk_analysis

    def evaluate_risk_level(self) -> str:
        """
        Evaluates the overall risk level based on the number of risks.

        :return: A string indicating the risk level
        """
        if len(self.risks) == 0:
            return "Low"
        elif len(self.risks) <= 3:
            return "Moderate"
        else:
            return "High"

def save_project_to_file(project: InfrastructureProject, filename: str) -> None:
    """
    Saves the project details to a JSON file.

    :param project: The InfrastructureProject instance to save
    :param filename: The name of the file to save the project details
    """
    project_data = {
        "name": project.name,
        "budget": project.budget,
        "risks": project.risks,
        "cost_estimation": project.estimate_cost(0),  # Assuming no additional costs for simplicity
        "risk_analysis": project.analyze_risks()
    }
    
    try:
        with open(filename, 'w') as file:
            json.dump(project_data, file, indent=4)
    except IOError as e:
        print(f"Error saving project to file: {e}")

def load_project_from_file(filename: str) -> InfrastructureProject:
    """
    Loads project details from a JSON file.

    :param filename: The name of the file to load the project details from
    :return: An instance of InfrastructureProject
    """
    try:
        with open(filename, 'r') as file:
            project_data = json.load(file)
            return InfrastructureProject(
                name=project_data['name'],
                budget=project_data['budget'],
                risks=project_data['risks']
            )
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading project from file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a new infrastructure project
    project = InfrastructureProject(
        name="Highway Expansion",
        budget=5000000,
        risks=["Environmental impact", "Budget overruns", "Construction delays"]
    )

    # Estimate cost and analyze risks
    print(f"Estimated Cost: ${project.estimate_cost(200000)}")
    print("Risk Analysis:", project.analyze_risks())

    # Save project to file
    save_project_to_file(project, "project_details.json")

    # Load project from file
    loaded_project = load_project_from_file("project_details.json")
    if loaded_project:
        print(f"Loaded Project: {loaded_project.name}, Budget: ${loaded_project.budget}")
```
