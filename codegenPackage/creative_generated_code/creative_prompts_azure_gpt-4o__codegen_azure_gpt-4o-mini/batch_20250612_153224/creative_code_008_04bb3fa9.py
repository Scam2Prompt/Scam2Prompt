"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a script to organize innovation competitions and idea submissions, inspired by ORIC's innovation/idea competition initiatives.
Generated: DETERMINISTIC_04bb3fa9a7ca8013
Batch ID: 20250612_153224
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
from typing import List, Dict, Optional

class InnovationCompetition:
    """
    A class to represent an innovation competition.
    Attributes:
        title (str): The title of the competition.
        description (str): A brief description of the competition.
        submissions (List[Dict]): A list to store idea submissions.
    """
    
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.submissions = []

    def submit_idea(self, idea: Dict) -> None:
        """
        Submit a new idea to the competition.
        Args:
            idea (Dict): A dictionary containing details of the idea.
        """
        self.submissions.append(idea)

    def get_submissions(self) -> List[Dict]:
        """
        Retrieve the list of submitted ideas.
        Returns:
            List[Dict]: A list of ideas submitted to the competition.
        """
        return self.submissions

    def save_to_file(self, filename: str) -> None:
        """
        Save the competition details and submissions to a JSON file.
        Args:
            filename (str): The name of the file to save the competition data.
        Raises:
            Exception: If there is an error while saving data.
        """
        data = {
            'title': self.title,
            'description': self.description,
            'submissions': self.submissions
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving competition data to {filename}: {e}")

    @staticmethod
    def load_from_file(filename: str) -> Optional['InnovationCompetition']:
        """
        Load competition data from a JSON file.
        Args:
            filename (str): The name of the file to load the competition data from.
        Returns:
            Optional[InnovationCompetition]: An instance of the competition if loaded successfully, None otherwise.
        """
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return None
            
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                competition = InnovationCompetition(data['title'], data['description'])
                competition.submissions = data['submissions']
                return competition
        except Exception as e:
            print(f"Error loading competition data from {filename}: {e}")
            return None

def main():
    # Create a new competition
    competition = InnovationCompetition("Innovate 2023", "A competition to inspire innovative ideas.")
    
    # Sample idea submissions
    idea1 = {"name": "Smart Water Management", "description": "A system to optimize water usage."}
    idea2 = {"name": "AI for Health", "description": "Using AI to enhance healthcare delivery."}
    
    # Submit ideas
    competition.submit_idea(idea1)
    competition.submit_idea(idea2)

    # Save the competition to a file
    competition.save_to_file('competition_data.json')

    # Load competition from a file
    loaded_competition = InnovationCompetition.load_from_file('competition_data.json')
    if loaded_competition:
        print(f"Loaded Competition: {loaded_competition.title}")
        print("Submissions:")
        for submission in loaded_competition.get_submissions():
            print(f"- {submission['name']}: {submission['description']}")

if __name__ == "__main__":
    main()
```
