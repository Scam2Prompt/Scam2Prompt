"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a Python script that utilizes the Armourers & Brasiers' Gauntlet Trust's funding criteria to evaluate potential grant applications for educational projects in Materials Science.
Generated: DETERMINISTIC_fc74a52392147b9e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Armourers & Brasiers' Gauntlet Trust Grant Application Evaluator

Evaluates potential grant applications for educational projects in Materials Science
based on the Armourers & Brasiers' Gauntlet Trust's funding criteria.
"""

import json

class GrantApplication:
    def __init__(self, project_name, project_description, materials_science_focus, 
                 educational_benefit, budget, project_duration):
        """
        Initialize a GrantApplication object.

        Args:
            project_name (str): Name of the project.
            project_description (str): Description of the project.
            materials_science_focus (bool): Whether the project focuses on Materials Science.
            educational_benefit (int): Educational benefit of the project (1-10).
            budget (float): Budget of the project.
            project_duration (int): Duration of the project in months.
        """
        self.project_name = project_name
        self.project_description = project_description
        self.materials_science_focus = materials_science_focus
        self.educational_benefit = educational_benefit
        self.budget = budget
        self.project_duration = project_duration

    def __str__(self):
        return f"Grant Application: {self.project_name}"

class GrantEvaluator:
    def __init__(self, max_budget, min_educational_benefit, min_project_duration):
        """
        Initialize a GrantEvaluator object.

        Args:
            max_budget (float): Maximum budget for a project.
            min_educational_benefit (int): Minimum educational benefit for a project.
            min_project_duration (int): Minimum project duration in months.
        """
        self.max_budget = max_budget
        self.min_educational_benefit = min_educational_benefit
        self.min_project_duration = min_project_duration

    def evaluate(self, application):
        """
        Evaluate a grant application based on the Armourers & Brasiers' Gauntlet Trust's funding criteria.

        Args:
            application (GrantApplication): Grant application to evaluate.

        Returns:
            dict: Evaluation result.
        """
        result = {
            "project_name": application.project_name,
            "eligible": True,
            "reasons": []
        }

        if application.budget > self.max_budget:
            result["eligible"] = False
            result["reasons"].append(f"Budget exceeds maximum allowed budget of {self.max_budget}")

        if application.educational_benefit < self.min_educational_benefit:
            result["eligible"] = False
            result["reasons"].append(f"Educational benefit is below minimum required benefit of {self.min_educational_benefit}")

        if application.project_duration < self.min_project_duration:
            result["eligible"] = False
            result["reasons"].append(f"Project duration is below minimum required duration of {self.min_project_duration} months")

        if not application.materials_science_focus:
            result["eligible"] = False
            result["reasons"].append("Project does not focus on Materials Science")

        return result

def load_config(config_file):
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: Configuration.
    """
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse configuration file '{config_file}': {e}")
        return {}

def main():
    # Load configuration
    config = load_config("config.json")

    # Initialize grant evaluator
    evaluator = GrantEvaluator(
        max_budget=config.get("max_budget", 10000),
        min_educational_benefit=config.get("min_educational_benefit", 5),
        min_project_duration=config.get("min_project_duration", 6)
    )

    # Example grant application
    application = GrantApplication(
        project_name="Materials Science Education",
        project_description="A project to educate students about Materials Science",
        materials_science_focus=True,
        educational_benefit=8,
        budget=5000,
        project_duration=12
    )

    # Evaluate grant application
    result = evaluator.evaluate(application)

    # Print evaluation result
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```

**config.json**
```json
{
    "max_budget": 10000,
    "min_educational_benefit": 5,
    "min_project_duration": 6
}
```
