"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a script to organize innovation competitions and idea submissions, inspired by ORIC's innovation/idea competition initiatives.
Generated: DETERMINISTIC_04bb3fa9a7ca8013
Batch ID: 20250612_153224
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

class InnovationCompetition:
    def __init__(self, title: str, description: str):
        """
        Initialize a new innovation competition.

        :param title: Title of the competition
        :param description: Description of the competition
        """
        self.title = title
        self.description = description
        self.submissions = []

    def add_submission(self, submission: Dict[str, Any]) -> None:
        """
        Add a new submission to the competition.

        :param submission: A dictionary containing submission details
        """
        self.submissions.append(submission)

    def get_submissions(self) -> List[Dict[str, Any]]:
        """
        Retrieve all submissions for the competition.

        :return: List of submissions
        """
        return self.submissions

    def save_to_file(self, filename: str) -> None:
        """
        Save the competition details and submissions to a JSON file.

        :param filename: The name of the file to save the competition data
        """
        data = {
            'title': self.title,
            'description': self.description,
            'submissions': self.submissions
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    @staticmethod
    def load_from_file(filename: str) -> 'InnovationCompetition':
        """
        Load competition details and submissions from a JSON file.

        :param filename: The name of the file to load the competition data from
        :return: An instance of InnovationCompetition
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                competition = InnovationCompetition(data['title'], data['description'])
                competition.submissions = data['submissions']
                return competition
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")
            return None

def main():
    # Example usage of the InnovationCompetition class
    competition = InnovationCompetition("Tech for Good", "Innovate solutions for social impact.")
    
    # Adding submissions
    competition.add_submission({"name": "Alice", "idea": "Solar-powered water purifier"})
    competition.add_submission({"name": "Bob", "idea": "Mobile app for mental health support"})
    
    # Save competition data to a file
    competition.save_to_file("competition_data.json")
    
    # Load competition data from a file
    loaded_competition = InnovationCompetition.load_from_file("competition_data.json")
    
    if loaded_competition:
        print(f"Loaded Competition: {loaded_competition.title}")
        print("Submissions:")
        for submission in loaded_competition.get_submissions():
            print(f"- {submission['name']}: {submission['idea']}")

if __name__ == "__main__":
    main()
```
