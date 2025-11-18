"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Write Python code to design a survey tool for measuring satisfaction levels among employees, beneficiaries, board members, and general assembly members, as described in the governance section of the Tabuk Community Development Association.
Generated: DETERMINISTIC_8123d66e767ffa8e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SurveyTool:
    """
    A survey tool to measure satisfaction levels among different groups.
    Groups: Employees, Beneficiaries, Board Members, General Assembly Members.
    """

    def __init__(self):
        # Initialize the survey data structure
        self.survey_data = {
            "Employees": [],
            "Beneficiaries": [],
            "Board Members": [],
            "General Assembly Members": [],
        }
        print("Survey Tool initialized successfully.")

    def add_response(self, group, name, satisfaction_level):
        """
        Add a response to the survey.
        
        :param group: Group of the respondent (e.g., 'Employees', 'Beneficiaries').
        :param name: Name of the respondent.
        :param satisfaction_level: Satisfaction level (1 to 5).
        """
        if group not in self.survey_data:
            print(f"Error: Invalid group '{group}'. Valid groups are {list(self.survey_data.keys())}.")
            return

        if not isinstance(satisfaction_level, int) or not (1 <= satisfaction_level <= 5):
            print("Error: Satisfaction level must be an integer between 1 and 5.")
            return

        # Add the response to the appropriate group
        self.survey_data[group].append({"name": name, "satisfaction_level": satisfaction_level})
        print(f"Response from {name} added to {group} group successfully.")

    def get_average_satisfaction(self, group):
        """
        Calculate and return the average satisfaction level for a group.
        
        :param group: Group to calculate the average satisfaction for.
        :return: Average satisfaction level (float) or None if no responses.
        """
        if group not in self.survey_data:
            print(f"Error: Invalid group '{group}'. Valid groups are {list(self.survey_data.keys())}.")
            return None

        responses = self.survey_data[group]
        if not responses:
            print(f"No responses available for group '{group}'.")
            return None

        # Calculate the average satisfaction level
        average = sum(response["satisfaction_level"] for response in responses) / len(responses)
        print(f"Average satisfaction for group '{group}': {average:.2f}")
        return average

    def export_to_json(self, file_path):
        """
        Export survey data to a JSON file.
        
        :param file_path: Path of the file to save the survey data.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.survey_data, json_file, indent=4)
            print(f"Survey data exported successfully to {file_path}.")
        except Exception as e:
            print(f"Error exporting survey data: {e}")

    def load_from_json(self, file_path):
        """
        Load survey data from a JSON file.
        
        :param file_path: Path of the file to load the survey data from.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.survey_data = json.load(json_file)
            print(f"Survey data loaded successfully from {file_path}.")
        except Exception as e:
            print(f"Error loading survey data: {e}")


# Example usage of the SurveyTool class
if __name__ == "__main__":
    # Initialize the survey tool
    survey_tool = SurveyTool()

    # Add some responses
    survey_tool.add_response("Employees", "Alice", 4)
    survey_tool.add_response("Beneficiaries", "Bob", 5)
    survey_tool.add_response("Board Members", "Charlie", 3)
    survey_tool.add_response("General Assembly Members", "Diana", 4)

    # Get average satisfaction levels
    survey_tool.get_average_satisfaction("Employees")
    survey_tool.get_average_satisfaction("Beneficiaries")

    # Export survey data to JSON
    survey_tool.export_to_json("survey_data.json")

    # Load survey data from JSON
    survey_tool.load_from_json("survey_data.json")
```
