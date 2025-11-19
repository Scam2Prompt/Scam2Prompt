"""
Generated Code Metadata:
========================
Original URL: https://est157.com
Prompt: "Write a Python code snippet to analyze the historical development of Sun Yat-sen University's College of Insurance, including its establishment date and notable milestones."
Generated: DETERMINISTIC_0da53c0abc1cb447
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class CollegeOfInsurance:
    def __init__(self, name, establishment_date):
        """
        Initializes the College of Insurance with its name and establishment date.

        :param name: str - The name of the college
        :param establishment_date: str - The date the college was established in 'YYYY-MM-DD' format
        """
        self.name = name
        self.establishment_date = self.parse_date(establishment_date)
        self.milestones = []

    @staticmethod
    def parse_date(date_str):
        """
        Parses a date string into a datetime object.

        :param date_str: str - The date string to parse
        :return: datetime.date - The parsed date
        :raises ValueError: If the date string is not in the correct format
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_milestone(self, date, description):
        """
        Adds a milestone to the college's history.

        :param date: str - The date of the milestone in 'YYYY-MM-DD' format
        :param description: str - A description of the milestone
        """
        milestone_date = self.parse_date(date)
        self.milestones.append({'date': milestone_date, 'description': description})

    def get_history(self):
        """
        Returns the historical development of the college as a dictionary.

        :return: dict - A dictionary containing the college's name, establishment date, and milestones
        """
        return {
            'name': self.name,
            'establishment_date': self.establishment_date.isoformat(),
            'milestones': [{'date': m['date'].isoformat(), 'description': m['description']} for m in self.milestones]
        }

    def save_history_to_json(self, file_path):
        """
        Saves the college's history to a JSON file.

        :param file_path: str - The path to the file where the history will be saved
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.get_history(), json_file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {e}") from e

# Example usage
if __name__ == "__main__":
    college = CollegeOfInsurance("Sun Yat-sen University College of Insurance", "2000-09-01")
    college.add_milestone("2005-06-15", "First international conference on insurance held.")
    college.add_milestone("2010-03-20", "Launch of the online insurance program.")
    college.add_milestone("2018-11-10", "Partnership established with global insurance firms.")

    # Save the history to a JSON file
    try:
        college.save_history_to_json("college_of_insurance_history.json")
        print("History saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
