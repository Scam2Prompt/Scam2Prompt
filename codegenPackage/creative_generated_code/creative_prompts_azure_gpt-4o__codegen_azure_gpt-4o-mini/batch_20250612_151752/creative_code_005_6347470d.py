"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Write code to automate the creation of engineering-geological survey programs, referencing the geotechnical services provided by Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_6347470d77cf42ba
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime
from typing import List, Dict

class GeologicalSurveyProgram:
    """
    A class to represent an engineering-geological survey program.
    
    Attributes:
        title (str): The title of the survey program.
        date (datetime): The date of the survey.
        services (List[str]): A list of geotechnical services provided.
    """

    def __init__(self, title: str, date: datetime, services: List[str]):
        self.title = title
        self.date = date
        self.services = services

    def to_dict(self) -> Dict:
        """Convert the survey program to a dictionary for JSON serialization."""
        return {
            "title": self.title,
            "date": self.date.strftime('%Y-%m-%d'),
            "services": self.services
        }

class SurveyProgramManager:
    """
    A class to manage the creation and storage of survey programs.
    """

    def __init__(self, storage_directory: str):
        self.storage_directory = storage_directory
        self.ensure_storage_directory()

    def ensure_storage_directory(self):
        """Ensure that the storage directory exists."""
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)

    def save_program(self, program: GeologicalSurveyProgram) -> None:
        """
        Save a survey program to a JSON file.

        Args:
            program (GeologicalSurveyProgram): The survey program to save.
        """
        file_path = os.path.join(self.storage_directory, f"{program.title.replace(' ', '_')}.json")
        try:
            with open(file_path, 'w') as file:
                json.dump(program.to_dict(), file, indent=4)
            print(f"Survey program '{program.title}' saved successfully.")
        except IOError as e:
            print(f"Error saving survey program: {e}")

    def create_survey_program(self, title: str, services: List[str]) -> GeologicalSurveyProgram:
        """
        Create a new geological survey program.

        Args:
            title (str): The title of the survey program.
            services (List[str]): A list of geotechnical services provided.

        Returns:
            GeologicalSurveyProgram: The created survey program.
        """
        date = datetime.now()
        program = GeologicalSurveyProgram(title, date, services)
        self.save_program(program)
        return program

# Example usage
if __name__ == "__main__":
    # Define the storage directory for survey programs
    storage_dir = './survey_programs'
    
    # Initialize the manager
    manager = SurveyProgramManager(storage_dir)

    # Define the geotechnical services provided
    services_offered = [
        "Soil Testing",
        "Site Investigation",
        "Groundwater Analysis",
        "Geological Mapping"
    ]

    # Create a new survey program
    survey_title = "Geotechnical Survey for Project Alpha"
    manager.create_survey_program(survey_title, services_offered)
```

This Python code provides a class structure for managing geological survey programs based on the user's request while ensuring best practices in coding, including error handling and comments for clarity.
