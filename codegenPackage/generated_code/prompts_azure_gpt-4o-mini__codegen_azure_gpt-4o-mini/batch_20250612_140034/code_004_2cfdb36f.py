"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Provide an example of a geotechnical project that requires engineering-geological surveys, referencing the services of the Geotechnical Center.
Generated: DETERMINISTIC_2cfdb36f9d7f373e
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GeotechnicalProject:
    """
    A class to represent a geotechnical project that requires engineering-geological surveys.
    """

    def __init__(self, project_name, location):
        """
        Initializes a new geotechnical project.

        :param project_name: Name of the geotechnical project
        :param location: Location of the project
        """
        self.project_name = project_name
        self.location = location
        self.surveys = []

    def add_survey(self, survey):
        """
        Adds an engineering-geological survey to the project.

        :param survey: An instance of EngineeringGeologicalSurvey
        """
        if not isinstance(survey, EngineeringGeologicalSurvey):
            raise ValueError("Expected an instance of EngineeringGeologicalSurvey")
        self.surveys.append(survey)

    def get_project_details(self):
        """
        Returns the details of the geotechnical project.

        :return: A dictionary containing project details
        """
        return {
            "project_name": self.project_name,
            "location": self.location,
            "surveys": [survey.get_survey_details() for survey in self.surveys]
        }


class EngineeringGeologicalSurvey:
    """
    A class to represent an engineering-geological survey.
    """

    def __init__(self, survey_type, date, results):
        """
        Initializes a new engineering-geological survey.

        :param survey_type: Type of the survey (e.g., soil analysis, rock stability)
        :param date: Date of the survey
        :param results: Results of the survey
        """
        self.survey_type = survey_type
        self.date = date
        self.results = results

    def get_survey_details(self):
        """
        Returns the details of the engineering-geological survey.

        :return: A dictionary containing survey details
        """
        return {
            "survey_type": self.survey_type,
            "date": self.date,
            "results": self.results
        }


def main():
    """
    Main function to demonstrate the usage of the GeotechnicalProject and EngineeringGeologicalSurvey classes.
    """
    try:
        # Create a geotechnical project
        project = GeotechnicalProject("Foundation for High-Rise Building", "Downtown City")

        # Create engineering-geological surveys
        survey1 = EngineeringGeologicalSurvey("Soil Analysis", "2023-10-01", "Soil is stable with good load-bearing capacity.")
        survey2 = EngineeringGeologicalSurvey("Rock Stability", "2023-10-05", "Rock formations are stable with minor fractures.")

        # Add surveys to the project
        project.add_survey(survey1)
        project.add_survey(survey2)

        # Print project details
        project_details = project.get_project_details()
        print(project_details)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
