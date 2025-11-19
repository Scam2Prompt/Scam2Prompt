"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Develop a data analysis tool to evaluate the impact of social projects like Casa Abrigo and Projeto Vida, using metrics such as the number of beneficiaries and program outcomes.
Generated: DETERMINISTIC_ce2a8ddba0106087
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_analysis_tool.py

import pandas as pd
import numpy as np

class SocialProject:
    """Represents a social project with its metrics."""

    def __init__(self, name, beneficiaries, outcomes):
        """
        Initializes a SocialProject instance.

        Args:
            name (str): The name of the social project.
            beneficiaries (int): The number of beneficiaries.
            outcomes (dict): A dictionary of program outcomes.
        """
        self.name = name
        self.beneficiaries = beneficiaries
        self.outcomes = outcomes

    def __str__(self):
        return f"Social Project: {self.name}"

    def get_outcome(self, outcome_name):
        """
        Retrieves a specific program outcome.

        Args:
            outcome_name (str): The name of the outcome.

        Returns:
            The value of the outcome if it exists, otherwise None.
        """
        return self.outcomes.get(outcome_name)


class DataAnalysisTool:
    """Evaluates the impact of social projects."""

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """
        Adds a social project to the analysis tool.

        Args:
            project (SocialProject): The social project to add.
        """
        self.projects.append(project)

    def get_project(self, project_name):
        """
        Retrieves a social project by its name.

        Args:
            project_name (str): The name of the project.

        Returns:
            The social project if it exists, otherwise None.
        """
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def analyze_projects(self):
        """
        Analyzes the social projects and prints their metrics.

        Returns:
            A dictionary with the analysis results.
        """
        analysis_results = {}
        for project in self.projects:
            print(f"Project: {project.name}")
            print(f"Beneficiaries: {project.beneficiaries}")
            print("Outcomes:")
            for outcome, value in project.outcomes.items():
                print(f"  - {outcome}: {value}")
            analysis_results[project.name] = {
                "beneficiaries": project.beneficiaries,
                "outcomes": project.outcomes,
            }
        return analysis_results

    def compare_projects(self, project_name1, project_name2):
        """
        Compares two social projects based on their metrics.

        Args:
            project_name1 (str): The name of the first project.
            project_name2 (str): The name of the second project.

        Returns:
            A dictionary with the comparison results.
        """
        project1 = self.get_project(project_name1)
        project2 = self.get_project(project_name2)

        if project1 is None or project2 is None:
            raise ValueError("One or both projects do not exist.")

        comparison_results = {
            "project1": project_name1,
            "project2": project_name2,
            "beneficiaries_diff": project1.beneficiaries - project2.beneficiaries,
        }

        for outcome in project1.outcomes:
            if outcome in project2.outcomes:
                comparison_results[outcome] = {
                    "project1_value": project1.outcomes[outcome],
                    "project2_value": project2.outcomes[outcome],
                    "diff": project1.outcomes[outcome] - project2.outcomes[outcome],
                }

        return comparison_results


def load_data(file_path):
    """
    Loads social project data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        A list of SocialProject instances.
    """
    try:
        data = pd.read_csv(file_path)
        projects = []
        for index, row in data.iterrows():
            project = SocialProject(
                row["name"],
                row["beneficiaries"],
                {
                    "education": row["education"],
                    "employment": row["employment"],
                    "health": row["health"],
                },
            )
            projects.append(project)
        return projects
    except FileNotFoundError:
        print("The file does not exist.")
        return []
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return []
    except pd.errors.ParserError:
        print("Error parsing the file.")
        return []


def main():
    # Load data from CSV file
    file_path = "social_projects.csv"
    projects = load_data(file_path)

    # Create a data analysis tool
    analysis_tool = DataAnalysisTool()

    # Add projects to the analysis tool
    for project in projects:
        analysis_tool.add_project(project)

    # Analyze projects
    analysis_results = analysis_tool.analyze_projects()
    print("\nAnalysis Results:")
    print(analysis_results)

    # Compare projects
    comparison_results = analysis_tool.compare_projects("Casa Abrigo", "Projeto Vida")
    print("\nComparison Results:")
    print(comparison_results)


if __name__ == "__main__":
    main()
```

Example use case:

`social_projects.csv` file:
```csv
name,beneficiaries,education,employment,health
Casa Abrigo,1000,80,70,90
Projeto Vida,500,70,60,80
```

Running the `data_analysis_tool.py` script will load the data from the CSV file, analyze the social projects, and compare the metrics of "Casa Abrigo" and "Projeto Vida". The analysis and comparison results will be printed to the console.
