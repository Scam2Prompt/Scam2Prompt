"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Develop a program that evaluates the impact of social and educational projects, incorporating the monitoring and evaluation techniques outlined by Matter.
Generated: DETERMINISTIC_866b4b3299dda49a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code that evaluates the impact of social and educational projects using monitoring and evaluation techniques:

```python
import pandas as pd
import numpy as np
import json

class ProjectEvaluator:
    """
    A class to evaluate the impact of social and educational projects
    based on monitoring and evaluation techniques.
    """
    
    def __init__(self, project_data_file):
        """
        Initialize the evaluator with project data.

        :param project_data_file: Path to a JSON file containing project data.
        """
        self.project_data_file = project_data_file
        self.project_data = self.load_project_data()
    
    def load_project_data(self):
        """
        Load project data from the JSON file.

        :return: A list of projects with relevant attributes.
        """
        try:
            with open(self.project_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.project_data_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File {self.project_data_file} contains invalid JSON.")
    
    def calculate_impact_score(self, project):
        """
        Calculate the impact score for a single project.

        :param project: Dictionary containing project attributes.
                        Must include 'beneficiaries', 'budget', and 'outcomes'.
        :return: Impact score as a float.
        """
        try:
            beneficiaries = project['beneficiaries']
            budget = project['budget']
            outcomes = project['outcomes']

            # Normalize beneficiaries and budget
            beneficiaries_score = np.log1p(beneficiaries)  # Logarithmic scaling
            budget_score = np.sqrt(budget)  # Square root scaling
            
            # Weight outcomes more heavily
            outcome_score = np.mean(outcomes) * 2
            
            # Combine scores
            impact_score = beneficiaries_score + budget_score + outcome_score
            return round(impact_score, 2)
        except KeyError:
            raise KeyError("Project data must contain 'beneficiaries', 'budget', and 'outcomes' fields.")
        except TypeError:
            raise TypeError("Ensure 'beneficiaries', 'budget', and 'outcomes' are numeric.")
    
    def evaluate_projects(self):
        """
        Evaluate all projects and calculate their impact scores.

        :return: A DataFrame containing project names and their impact scores.
        """
        evaluated_projects = []

        for project in self.project_data:
            try:
                impact_score = self.calculate_impact_score(project)
                evaluated_projects.append({
                    'Project Name': project.get('name', 'Unnamed Project'),
                    'Impact Score': impact_score
                })
            except Exception as e:
                print(f"Error evaluating project '{project.get('name', 'Unnamed Project')}': {e}")
        
        # Convert results to DataFrame for easy analysis
        return pd.DataFrame(evaluated_projects)
    
    def export_evaluation_results(self, output_file):
        """
        Export evaluation results to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        results = self.evaluate_projects()
        try:
            results.to_csv(output_file, index=False)
            print(f"Results successfully exported to {output_file}")
        except Exception as e:
            print(f"Error exporting results: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize evaluator with sample project data file
    evaluator = ProjectEvaluator("sample_project_data.json")
    
    # Perform evaluation
    results = evaluator.evaluate_projects()
    print("Evaluation Results:")
    print(results)
    
    # Export results to CSV
    evaluator.export_evaluation_results("evaluation_results.csv")
```

### Example of `sample_project_data.json` (project data input file):
```json
[
    {
        "name": "Literacy Program",
        "beneficiaries": 500,
        "budget": 20000,
        "outcomes": [4, 5, 4.5]  // Average outcome ratings
    },
    {
        "name": "Health Awareness Campaign",
        "beneficiaries": 1200,
        "budget": 50000,
        "outcomes": [4.8, 5, 4.9]
    }
]
```

To test the program, create a JSON file named `sample_project_data.json` with the above example data, run the Python script, and it will generate a CSV file with the evaluation results.
