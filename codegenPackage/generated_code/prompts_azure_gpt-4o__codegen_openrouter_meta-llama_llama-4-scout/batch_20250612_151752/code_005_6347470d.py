"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write code to automate the creation of engineering-geological survey programs, referencing the geotechnical services provided by Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_6347470d77cf42ba
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be using Python as the programming language. Here's the code:

```python
# -*- coding: utf-8 -*-

"""
Module to automate the creation of engineering-geological survey programs.

References:
    - Geotechnical services provided by Научно-образовательный центр «Геотехника»
"""

import os
import json
from datetime import datetime

class SurveyProgram:
    def __init__(self, project_name, location, survey_type):
        """
        Initialize a SurveyProgram object.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project.
            survey_type (str): Type of survey (e.g., engineering-geological).
        """
        self.project_name = project_name
        self.location = location
        self.survey_type = survey_type
        self.tasks = []

    def add_task(self, task_name, task_description):
        """
        Add a task to the survey program.

        Args:
            task_name (str): Name of the task.
            task_description (str): Description of the task.
        """
        self.tasks.append({"name": task_name, "description": task_description})

    def generate_program(self):
        """
        Generate the survey program.

        Returns:
            dict: Survey program with tasks.
        """
        program = {
            "project_name": self.project_name,
            "location": self.location,
            "survey_type": self.survey_type,
            "tasks": self.tasks,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return program

    def save_program(self, output_file):
        """
        Save the survey program to a JSON file.

        Args:
            output_file (str): Path to the output file.

        Raises:
            Exception: If the output file cannot be written.
        """
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(self.generate_program(), f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise Exception(f"Failed to save program to {output_file}: {str(e)}")

def main():
    # Example usage
    project_name = "Example Project"
    location = "Москва, Россия"
    survey_type = "Инженерно-геологические изыскания"

    survey_program = SurveyProgram(project_name, location, survey_type)

    survey_program.add_task("Задача 1", "Описание задачи 1")
    survey_program.add_task("Задача 2", "Описание задачи 2")

    output_file = "survey_program.json"
    survey_program.save_program(output_file)

    print(f"Survey program saved to {output_file}")

if __name__ == "__main__":
    main()
```
