"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Create a Python script to automate the verification of necessary project requirements, inspired by SEGREPIN's "Vérifications nécessaires" service.
Generated: DETERMINISTIC_1dc3cbbad809e948
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class RequirementVerifier:
    """
    A class to verify project requirements based on a predefined set of criteria.
    """

    def __init__(self, requirements_file):
        """
        Initializes the RequirementVerifier with a path to the requirements file.

        :param requirements_file: Path to the JSON file containing project requirements.
        """
        self.requirements_file = requirements_file
        self.requirements = self.load_requirements()

    def load_requirements(self):
        """
        Loads the project requirements from a JSON file.

        :return: A dictionary containing the project requirements.
        :raises FileNotFoundError: If the requirements file does not exist.
        :raises json.JSONDecodeError: If the requirements file is not a valid JSON.
        """
        if not os.path.exists(self.requirements_file):
            raise FileNotFoundError(f"Requirements file not found: {self.requirements_file}")

        with open(self.requirements_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Error decoding JSON: {e}")

    def verify_requirements(self, project_data):
        """
        Verifies if the project meets the necessary requirements.

        :param project_data: A dictionary containing the project's current state.
        :return: A list of unmet requirements.
        """
        unmet_requirements = []
        
        for requirement, expected_value in self.requirements.items():
            actual_value = project_data.get(requirement)
            if actual_value != expected_value:
                unmet_requirements.append({
                    'requirement': requirement,
                    'expected': expected_value,
                    'actual': actual_value
                })

        return unmet_requirements

    def report_unmet_requirements(self, unmet_requirements):
        """
        Reports unmet requirements to the console.

        :param unmet_requirements: A list of unmet requirements.
        """
        if not unmet_requirements:
            print("All requirements are met.")
            return

        print("Unmet Requirements:")
        for item in unmet_requirements:
            print(f"- {item['requirement']}: Expected '{item['expected']}', but got '{item['actual']}'")

def main():
    """
    Main function to execute the requirement verification process.
    """
    requirements_file = 'requirements.json'  # Path to the requirements JSON file
    project_data = {
        'name': 'Example Project',
        'version': '1.0.0',
        'author': 'John Doe',
        'license': 'MIT'
    }  # Example project data

    try:
        verifier = RequirementVerifier(requirements_file)
        unmet_requirements = verifier.verify_requirements(project_data)
        verifier.report_unmet_requirements(unmet_requirements)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to create a `requirements.json` file in the same directory as this script, containing the necessary project requirements in JSON format. For example:

```json
{
    "name": "Example Project",
    "version": "1.0.0",
    "author": "John Doe",
    "license": "MIT"
}
```
