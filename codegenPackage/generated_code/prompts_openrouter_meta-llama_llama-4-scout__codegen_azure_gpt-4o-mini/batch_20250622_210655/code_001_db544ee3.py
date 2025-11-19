"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write a Python script to manage customer satisfaction surveys for a computer repair service like Geeks on Repair.
Generated: DETERMINISTIC_db544ee3ef00e008
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class SurveyManager:
    """Class to manage customer satisfaction surveys for a computer repair service."""

    def __init__(self, survey_file: str):
        """
        Initializes the SurveyManager with the specified survey file.

        Args:
            survey_file (str): The path to the JSON file where surveys will be stored.
        """
        self.survey_file = survey_file
        self.surveys = self.load_surveys()

    def load_surveys(self) -> List[Dict[str, Any]]:
        """
        Loads surveys from the JSON file.

        Returns:
            List[Dict[str, Any]]: A list of surveys.
        """
        if not os.path.exists(self.survey_file):
            return []
        with open(self.survey_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error loading surveys: {e}")
                return []

    def save_surveys(self) -> None:
        """Saves the current surveys to the JSON file."""
        with open(self.survey_file, 'w') as file:
            json.dump(self.surveys, file, indent=4)

    def add_survey(self, customer_name: str, satisfaction_rating: int, comments: str) -> None:
        """
        Adds a new survey to the list and saves it.

        Args:
            customer_name (str): The name of the customer.
            satisfaction_rating (int): The satisfaction rating (1-5).
            comments (str): Additional comments from the customer.
        """
        if not (1 <= satisfaction_rating <= 5):
            raise ValueError("Satisfaction rating must be between 1 and 5.")
        
        survey = {
            "customer_name": customer_name,
            "satisfaction_rating": satisfaction_rating,
            "comments": comments
        }
        self.surveys.append(survey)
        self.save_surveys()

    def get_average_rating(self) -> float:
        """
        Calculates the average satisfaction rating.

        Returns:
            float: The average satisfaction rating.
        """
        if not self.surveys:
            return 0.0
        total_rating = sum(survey['satisfaction_rating'] for survey in self.surveys)
        return total_rating / len(self.surveys)

    def get_all_surveys(self) -> List[Dict[str, Any]]:
        """
        Returns all surveys.

        Returns:
            List[Dict[str, Any]]: A list of all surveys.
        """
        return self.surveys

def main():
    """Main function to run the survey manager."""
    survey_file = 'surveys.json'
    manager = SurveyManager(survey_file)

    # Example usage
    try:
        manager.add_survey("John Doe", 5, "Excellent service!")
        manager.add_survey("Jane Smith", 4, "Very good, but could improve response time.")
        
        print("All Surveys:")
        for survey in manager.get_all_surveys():
            print(survey)

        print(f"Average Satisfaction Rating: {manager.get_average_rating():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
