"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartenoir.org
Prompt: Design a project management tool that incorporates health and safety training modules, based on the customized training approaches described by Carte Noir Consulting.
Generated: DETERMINISTIC_e77715c10b62f899
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's a Python implementation of a project management tool with health and safety training modules based on customized training approaches. The code includes error handling, is well-documented, and follows best practices.

```python
import json
import datetime


class HealthAndSafetyTrainingModule:
    """
    Represents a health and safety training module.
    Includes detailed training content based on customized approaches.
    """

    def __init__(self, title, description, duration_minutes, required):
        """
        Initializes a training module.
        :param title: Title of the training module
        :param description: Detailed description of the module
        :param duration_minutes: Duration of the training in minutes
        :param required: Boolean indicating if the module is mandatory
        """
        self.title = title
        self.description = description
        self.duration_minutes = duration_minutes
        self.required = required

    def to_dict(self):
        """
        Converts the module details to a dictionary for serialization.
        """
        return {
            "title": self.title,
            "description": self.description,
            "duration_minutes": self.duration_minutes,
            "required": self.required
        }


class Project:
    """
    Represents a project with associated health and safety training modules.
    """

    def __init__(self, name, start_date, end_date):
        """
        Initializes a project.
        :param name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.name = name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.training_modules = []

        if self.start_date >= self.end_date:
            raise ValueError("Start date must be earlier than end date.")

    def add_training_module(self, module):
        """
        Adds a training module to the project.
        :param module: Instance of HealthAndSafetyTrainingModule
        """
        if not isinstance(module, HealthAndSafetyTrainingModule):
            raise TypeError("Expected a HealthAndSafetyTrainingModule instance.")
        self.training_modules.append(module)

    def list_training_modules(self):
        """
        Lists all the training modules associated with the project.
        """
        return [module.to_dict() for module in self.training_modules]

    def save_project(self, file_name):
        """
        Saves project details to a JSON file.
        :param file_name: Name of the file to save the project details
        """
        try:
            project_data = {
                "name": self.name,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "training_modules": self.list_training_modules()
            }
            with open(file_name, 'w') as file:
                json.dump(project_data, file, indent=4)
        except IOError as e:
            print(f"Error saving project to file: {e}")

    @staticmethod
    def _validate_date(date_str):
        """
        Validates and parses a date string.
        :param date_str: Date string in format YYYY-MM-DD
        :return: Parsed date string
        """
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")


# Example Usage
if __name__ == "__main__":
    try:
        # Create a project
        project = Project(name="Construction Project A", start_date="2023-11-01", end_date="2024-01-31")

        # Add health and safety training modules
        module1 = HealthAndSafetyTrainingModule(
            title="Fire Safety",
            description="Comprehensive fire safety procedures and evacuation training.",
            duration_minutes=60,
            required=True
        )

        module2 = HealthAndSafetyTrainingModule(
            title="First Aid",
            description="Basic first aid training, including CPR and wound care.",
            duration_minutes=90,
            required=True
        )

        project.add_training_module(module1)
        project.add_training_module(module2)

        # List modules and save project to file
        print("Training Modules:")
        for module in project.list_training_modules():
            print(module)

        project.save_project("project_details.json")
        print("Project details saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code defines a `HealthAndSafetyTrainingModule` class for training modules and a `Project` class to manage these modules. It includes error handling, validation, and ensures that the project details can be saved to a JSON file. You can run the script as provided, and it will produce a sample project with associated training modules while saving the data to a file.
