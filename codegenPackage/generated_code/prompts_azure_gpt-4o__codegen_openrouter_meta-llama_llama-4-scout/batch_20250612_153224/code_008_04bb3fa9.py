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
# innovation_competition.py

import datetime
import json

class InnovationCompetition:
    def __init__(self, name, start_date, end_date):
        """
        Initialize an innovation competition.

        Args:
            name (str): The name of the competition.
            start_date (str): The start date of the competition in YYYY-MM-DD format.
            end_date (str): The end date of the competition in YYYY-MM-DD format.
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.ideas = []

    def is_open(self):
        """
        Check if the competition is currently open.

        Returns:
            bool: True if the competition is open, False otherwise.
        """
        return self.start_date <= datetime.datetime.now() <= self.end_date

    def submit_idea(self, idea):
        """
        Submit an idea to the competition.

        Args:
            idea (dict): The idea to submit, with 'title', 'description', and 'submitter' keys.

        Raises:
            ValueError: If the competition is not open or the idea is invalid.
        """
        if not self.is_open():
            raise ValueError("Competition is not currently open")

        required_fields = ['title', 'description', 'submitter']
        if not all(field in idea for field in required_fields):
            raise ValueError("Idea is missing required fields")

        self.ideas.append(idea)

    def get_ideas(self):
        """
        Get all submitted ideas.

        Returns:
            list: A list of submitted ideas.
        """
        return self.ideas


class InnovationCompetitionManager:
    def __init__(self):
        """
        Initialize the innovation competition manager.
        """
        self.competitions = {}

    def create_competition(self, name, start_date, end_date):
        """
        Create a new innovation competition.

        Args:
            name (str): The name of the competition.
            start_date (str): The start date of the competition in YYYY-MM-DD format.
            end_date (str): The end date of the competition in YYYY-MM-DD format.

        Raises:
            ValueError: If a competition with the same name already exists.
        """
        if name in self.competitions:
            raise ValueError("Competition with this name already exists")

        self.competitions[name] = InnovationCompetition(name, start_date, end_date)

    def get_competition(self, name):
        """
        Get an innovation competition by name.

        Args:
            name (str): The name of the competition.

        Returns:
            InnovationCompetition: The innovation competition, or None if not found.
        """
        return self.competitions.get(name)

    def submit_idea(self, competition_name, idea):
        """
        Submit an idea to a competition.

        Args:
            competition_name (str): The name of the competition.
            idea (dict): The idea to submit.

        Raises:
            ValueError: If the competition does not exist or the idea is invalid.
        """
        competition = self.get_competition(competition_name)
        if competition is None:
            raise ValueError("Competition does not exist")

        competition.submit_idea(idea)


def main():
    # Example usage:
    manager = InnovationCompetitionManager()
    manager.create_competition("ORIC Innovation Challenge", "2024-01-01", "2024-06-30")

    competition = manager.get_competition("ORIC Innovation Challenge")
    idea = {
        'title': 'Example Idea',
        'description': 'This is an example idea.',
        'submitter': 'John Doe'
    }
    manager.submit_idea("ORIC Innovation Challenge", idea)

    print(json.dumps(competition.get_ideas(), indent=4))


if __name__ == "__main__":
    main()
```
