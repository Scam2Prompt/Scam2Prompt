"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write Python code to design a survey tool for measuring satisfaction levels among employees, beneficiaries, board members, and general assembly members, as described in the governance section of the Tabuk Community Development Association.
Generated: DETERMINISTIC_8123d66e767ffa8e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class SurveyTool:
    def __init__(self):
        """Initialize the SurveyTool with an empty survey data structure."""
        self.surveys: List[Dict[str, Any]] = []

    def add_survey(self, respondent_type: str, satisfaction_level: int, comments: str = "") -> None:
        """
        Add a survey response to the survey data.

        Args:
            respondent_type (str): Type of the respondent (e.g., 'employee', 'beneficiary', 'board member', 'general assembly member').
            satisfaction_level (int): Satisfaction level on a scale of 1 to 5.
            comments (str): Optional comments from the respondent.
        
        Raises:
            ValueError: If satisfaction_level is not between 1 and 5.
        """
        if satisfaction_level < 1 or satisfaction_level > 5:
            raise ValueError("Satisfaction level must be between 1 and 5.")

        survey_response = {
            "respondent_type": respondent_type,
            "satisfaction_level": satisfaction_level,
            "comments": comments
        }
        self.surveys.append(survey_response)

    def get_average_satisfaction(self) -> Dict[str, float]:
        """
        Calculate the average satisfaction level for each respondent type.

        Returns:
            Dict[str, float]: A dictionary with respondent types as keys and their average satisfaction levels as values.
        """
        satisfaction_totals = {}
        counts = {}

        for survey in self.surveys:
            respondent_type = survey["respondent_type"]
            satisfaction_level = survey["satisfaction_level"]

            if respondent_type not in satisfaction_totals:
                satisfaction_totals[respondent_type] = 0
                counts[respondent_type] = 0

            satisfaction_totals[respondent_type] += satisfaction_level
            counts[respondent_type] += 1

        averages = {respondent_type: total / counts[respondent_type] for respondent_type, total in satisfaction_totals.items()}
        return averages

    def save_surveys_to_file(self, filename: str) -> None:
        """
        Save the survey data to a JSON file.

        Args:
            filename (str): The name of the file to save the survey data.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.surveys, file, indent=4)
        except IOError as e:
            print(f"Error saving surveys to file: {e}")

    def load_surveys_from_file(self, filename: str) -> None:
        """
        Load survey data from a JSON file.

        Args:
            filename (str): The name of the file to load the survey data from.
        
        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.surveys = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading surveys from file: {e}")

# Example usage
if __name__ == "__main__":
    survey_tool = SurveyTool()
    
    # Adding survey responses
    survey_tool.add_survey('employee', 4, 'Great work environment!')
    survey_tool.add_survey('beneficiary', 5, 'Very satisfied with the services.')
    survey_tool.add_survey('board member', 3, 'Could improve communication.')
    
    # Calculate average satisfaction
    averages = survey_tool.get_average_satisfaction()
    print("Average Satisfaction Levels:", averages)
    
    # Save surveys to a file
    survey_tool.save_surveys_to_file('surveys.json')
    
    # Load surveys from a file
    survey_tool.load_surveys_from_file('surveys.json')
```
