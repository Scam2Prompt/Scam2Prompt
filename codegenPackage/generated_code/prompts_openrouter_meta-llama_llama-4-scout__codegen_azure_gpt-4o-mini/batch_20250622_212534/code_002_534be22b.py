"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Generate a case study on the application of ultrasonic cleaning for removing grease and scale from industrial equipment, using examples from Sonic Solutions Ltd."
Generated: DETERMINISTIC_534be22bd13e82ed
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UltrasonicCleaningCaseStudy:
    """
    A class to represent a case study on ultrasonic cleaning applications.
    """

    def __init__(self, company_name: str):
        """
        Initializes the case study with the company name.

        :param company_name: Name of the company conducting the case study.
        """
        self.company_name = company_name
        self.case_studies: List[Dict] = []

    def add_case_study(self, equipment: str, cleaning_method: str, results: str):
        """
        Adds a case study to the list.

        :param equipment: The type of industrial equipment cleaned.
        :param cleaning_method: Description of the ultrasonic cleaning method used.
        :param results: The results of the cleaning process.
        """
        case_study = {
            "equipment": equipment,
            "cleaning_method": cleaning_method,
            "results": results
        }
        self.case_studies.append(case_study)
        logging.info(f"Added case study for {equipment}.")

    def export_case_studies(self, file_path: str):
        """
        Exports the case studies to a JSON file.

        :param file_path: The path where the JSON file will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.case_studies, json_file, indent=4)
            logging.info(f"Case studies exported successfully to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")

    def display_case_studies(self):
        """
        Displays the case studies in a readable format.
        """
        for index, study in enumerate(self.case_studies, start=1):
            print(f"Case Study {index}:")
            print(f"  Equipment: {study['equipment']}")
            print(f"  Cleaning Method: {study['cleaning_method']}")
            print(f"  Results: {study['results']}\n")


# Example usage
if __name__ == "__main__":
    # Create an instance of the case study for Sonic Solutions Ltd.
    case_study = UltrasonicCleaningCaseStudy("Sonic Solutions Ltd.")

    # Add case studies
    case_study.add_case_study(
        equipment="Industrial Heat Exchanger",
        cleaning_method="Ultrasonic cleaning with biodegradable detergents",
        results="Successfully removed grease and scale, improving efficiency by 20%."
    )

    case_study.add_case_study(
        equipment="Manufacturing Equipment",
        cleaning_method="High-frequency ultrasonic cleaning",
        results="Eliminated all contaminants, reducing downtime by 30%."
    )

    # Display the case studies
    case_study.display_case_studies()

    # Export the case studies to a JSON file
    case_study.export_case_studies("ultrasonic_cleaning_case_studies.json")
```
