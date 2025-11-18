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
"""
Automates the creation of engineering-geological survey programs
by referencing geotechnical services provided by Научно-образовательный центр «Геотехника».

This script is production-ready, well-documented, and includes error handling.
"""

import json
import datetime


class SurveyProgramGenerator:
    """
    A class to generate engineering-geological survey programs.
    """

    def __init__(self, organization_name):
        """
        Initializes the SurveyProgramGenerator with the given organization name.
        
        Args:
            organization_name (str): The name of the geotechnical services provider.
        """
        self.organization_name = organization_name

    def get_service_catalog(self):
        """
        Retrieves the geotechnical services catalog from the organization.
        This simulates fetching services from an external source.
        
        Returns:
            list: A list of geotechnical services.
        Raises:
            Exception: If the service catalog cannot be retrieved.
        """
        try:
            # Simulated service catalog. It could be fetched from a database or API in production.
            service_catalog = [
                {"id": 1, "name": "Soil Composition Analysis"},
                {"id": 2, "name": "Rock Stability Testing"},
                {"id": 3, "name": "Groundwater Assessment"},
                {"id": 4, "name": "Seismic Hazard Evaluation"},
                {"id": 5, "name": "Environmental Impact Study"}
            ]
            return service_catalog
        except Exception as e:
            raise Exception(f"Error retrieving service catalog: {str(e)}")

    def create_survey_program(self, project_name, selected_services):
        """
        Creates an engineering-geological survey program based on selected services.
        
        Args:
            project_name (str): The name of the project.
            selected_services (list): List of service IDs selected for the survey.
        
        Returns:
            dict: The generated survey program.
        Raises:
            ValueError: If selected_services contains invalid IDs.
        """
        try:
            # Validate selected services
            service_catalog = self.get_service_catalog()
            valid_service_ids = {service["id"] for service in service_catalog}
            invalid_ids = [service_id for service_id in selected_services if service_id not in valid_service_ids]

            if invalid_ids:
                raise ValueError(f"Invalid service IDs: {invalid_ids}")

            # Build the survey program
            program_details = {
                "project_name": project_name,
                "organization_name": self.organization_name,
                "creation_date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "services": [
                    service for service in service_catalog if service["id"] in selected_services
                ]
            }
            return program_details
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Error creating survey program: {str(e)}")

    def export_program_to_file(self, program_details, file_path):
        """
        Exports the survey program details to a JSON file.
        
        Args:
            program_details (dict): The survey program details.
            file_path (str): The file path where the program will be saved.
        
        Raises:
            Exception: If the file cannot be written.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(program_details, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Error exporting program to file: {str(e)}")


# Script Usage Example
if __name__ == "__main__":
    try:
        # Initialize the generator with the organization name
        generator = SurveyProgramGenerator("Научно-образовательный центр «Геотехника»")

        # Specify the project name and chosen services
        project_name = "Urban Development Project"
        selected_services = [1, 3, 5]  # Service IDs to include in the survey

        # Create the survey program
        survey_program = generator.create_survey_program(project_name, selected_services)

        # Export the survey program to a JSON file
        output_file = "survey_program.json"
        generator.export_program_to_file(survey_program, output_file)

        print(f"Survey program successfully generated and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
