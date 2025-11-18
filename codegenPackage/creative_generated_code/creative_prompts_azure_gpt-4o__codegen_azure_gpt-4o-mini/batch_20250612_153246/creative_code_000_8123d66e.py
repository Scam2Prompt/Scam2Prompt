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
from typing import List, Dict, Any

class SurveyTool:
    def __init__(self):
        """Initialize the SurveyTool with an empty survey data storage."""
        self.survey_data: List[Dict[str, Any]] = []

    def add_response(self, respondent_type: str, satisfaction_level: int, comments: str = "") -> None:
        """Add a new survey response.

        Args:
            respondent_type (str): Type of the respondent (Employee, Beneficiary, Board Member, General Assembly).
            satisfaction_level (int): Satisfaction level (1-5).
            comments (str): Optional comments provided by the respondent.

        Raises:
            ValueError: If respondent_type is invalid or satisfaction_level is out of range.
        """
        if respondent_type not in ["Employee", "Beneficiary", "Board Member", "General Assembly"]:
            raise ValueError(f"Invalid respondent type: {respondent_type}. Must be one of: "
                             "Employee, Beneficiary, Board Member, General Assembly.")
        
        if not (1 <= satisfaction_level <= 5):
            raise ValueError(f"Satisfaction level must be between 1 and 5. Given: {satisfaction_level}.")

        response = {
            "respondent_type": respondent_type,
            "satisfaction_level": satisfaction_level,
            "comments": comments
        }
        self.survey_data.append(response)

    def get_average_satisfaction(self) -> Dict[str, float]:
        """Calculate the average satisfaction level by respondent type.

        Returns:
            Dict[str, float]: A dictionary mapping respondent types to their average satisfaction level.
        """
        total_satisfaction = {key: {"sum": 0, "count": 0} for key in ["Employee", "Beneficiary", "Board Member", "General Assembly"]}
        
        for response in self.survey_data:
            total_satisfaction[response["respondent_type"]]["sum"] += response["satisfaction_level"]
            total_satisfaction[response["respondent_type"]]["count"] += 1
        
        averages = {key: (value["sum"] / value["count"]) if value["count"] > 0 else 0 
                    for key, value in total_satisfaction.items()}
        
        return averages

    def export_results(self, file_path: str) -> None:
        """Export survey results to a JSON file.

        Args:
            file_path (str): Path to the output JSON file.

        Raises:
            IOError: If an error occurs while writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.survey_data, f, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing the results to {file_path}: {e}")

# Example of usage
if __name__ == "__main__":
    survey_tool = SurveyTool()
    
    # Adding survey responses
    survey_tool.add_response("Employee", 4, "Good working environment.")
    survey_tool.add_response("Beneficiary", 2, "Service could be improved.")
    survey_tool.add_response("Board Member", 5, "Very satisfied with the governance.")
    
    # Get average satisfaction
    averages = survey_tool.get_average_satisfaction()
    print("Average Satisfaction Levels:", averages)

    # Export results to a file
    survey_tool.export_results("survey_results.json")
```
