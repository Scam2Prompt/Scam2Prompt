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
# geotechnical_project.py

class GeotechnicalCenter:
    """Represents a geotechnical center providing survey services."""

    def __init__(self, name, location):
        """
        Initializes a GeotechnicalCenter instance.

        Args:
            name (str): Name of the geotechnical center.
            location (str): Location of the geotechnical center.
        """
        self.name = name
        self.location = location
        self.surveys = []

    def add_survey(self, survey):
        """
        Adds an engineering-geological survey to the center's records.

        Args:
            survey (EngineeringGeologicalSurvey): Survey to add.
        """
        self.surveys.append(survey)

    def get_surveys(self):
        """
        Retrieves a list of all engineering-geological surveys conducted.

        Returns:
            list[EngineeringGeologicalSurvey]: List of surveys.
        """
        return self.surveys


class EngineeringGeologicalSurvey:
    """Represents an engineering-geological survey."""

    def __init__(self, project_name, location, survey_type):
        """
        Initializes an EngineeringGeologicalSurvey instance.

        Args:
            project_name (str): Name of the geotechnical project.
            location (str): Location of the survey.
            survey_type (str): Type of engineering-geological survey.
        """
        self.project_name = project_name
        self.location = location
        self.survey_type = survey_type
        self.results = None

    def conduct_survey(self):
        """
        Conducts the engineering-geological survey.

        Raises:
            Exception: If survey conduction fails.
        """
        try:
            # Simulate survey conduction
            self.results = f"Survey results for {self.project_name} at {self.location}"
        except Exception as e:
            raise Exception(f"Failed to conduct survey: {str(e)}")

    def get_results(self):
        """
        Retrieves the results of the survey.

        Returns:
            str: Survey results.

        Raises:
            Exception: If survey results are not available.
        """
        if self.results is None:
            raise Exception("Survey results are not available")
        return self.results


class GeotechnicalProject:
    """Represents a geotechnical project requiring engineering-geological surveys."""

    def __init__(self, name, location):
        """
        Initializes a GeotechnicalProject instance.

        Args:
            name (str): Name of the geotechnical project.
            location (str): Location of the geotechnical project.
        """
        self.name = name
        self.location = location
        self.surveys = []

    def add_survey(self, survey):
        """
        Adds an engineering-geological survey to the project's records.

        Args:
            survey (EngineeringGeologicalSurvey): Survey to add.
        """
        self.surveys.append(survey)

    def reference_geotechnical_center(self, center):
        """
        References the services of a geotechnical center for the project.

        Args:
            center (GeotechnicalCenter): Geotechnical center to reference.

        Raises:
            Exception: If referencing the center fails.
        """
        try:
            for survey in self.surveys:
                center.add_survey(survey)
        except Exception as e:
            raise Exception(f"Failed to reference geotechnical center: {str(e)}")


def main():
    # Create a geotechnical center
    center = GeotechnicalCenter("Geotechnical Center", "123 Main St")

    # Create a geotechnical project
    project = GeotechnicalProject("Example Project", "456 Elm St")

    # Create engineering-geological surveys
    survey1 = EngineeringGeologicalSurvey(project.name, project.location, "Soil Investigation")
    survey2 = EngineeringGeologicalSurvey(project.name, project.location, "Rock Mechanics")

    # Conduct surveys
    survey1.conduct_survey()
    survey2.conduct_survey()

    # Add surveys to project
    project.add_survey(survey1)
    project.add_survey(survey2)

    # Reference geotechnical center
    project.reference_geotechnical_center(center)

    # Print survey results
    for survey in center.get_surveys():
        print(survey.get_results())


if __name__ == "__main__":
    main()
```
