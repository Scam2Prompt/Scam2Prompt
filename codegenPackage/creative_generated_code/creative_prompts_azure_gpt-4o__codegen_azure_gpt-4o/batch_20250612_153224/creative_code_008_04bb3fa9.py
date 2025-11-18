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
"""
Script to organize innovation competitions and manage idea submissions.
This script allows users to create competitions, submit ideas, and view/manage submissions.
"""

import datetime


class Competition:
    """
    Represents an innovation competition.
    """
    def __init__(self, name, description, submission_deadline):
        """
        Initializes a competition with its name, description, and submission deadline.

        :param name: Name of the competition.
        :param description: Description of what the competition is about.
        :param submission_deadline: Deadline for idea submission (datetime object).
        """
        self.name = name
        self.description = description
        self.submission_deadline = submission_deadline
        self.submissions = []

    def add_submission(self, idea_title, idea_description, participant_name, submission_date):
        """
        Adds an idea submission to the competition.

        :param idea_title: Title of the idea being submitted.
        :param idea_description: Description of the idea.
        :param participant_name: Name of the participant submitting the idea.
        :param submission_date: Date of submission (datetime object).
        :raises ValueError: If the submission date exceeds the competition's deadline.
        """
        if submission_date > self.submission_deadline:
            raise ValueError("Submission date exceeds the competition deadline.")
        
        submission = {
            "idea_title": idea_title,
            "idea_description": idea_description,
            "participant_name": participant_name,
            "submission_date": submission_date
        }
        self.submissions.append(submission)
        print(f"Submission by {participant_name} successfully added.")

    def list_submissions(self):
        """
        Lists all submissions in the competition.

        :return: List of all submissions.
        """
        if not self.submissions:
            print("No submissions available.")
            return []
        
        for i, submission in enumerate(self.submissions, start=1):
            print(f"{i}. Title: {submission['idea_title']}, By: {submission['participant_name']}")

        return self.submissions


def main():
    """
    Main function to manage competitions and idea submissions.
    """
    print("Welcome to the Innovation Competition Manager.")

    try:
        # Create a new competition
        competition_name = input("Enter competition name: ")
        competition_description = input("Enter competition description: ")
        deadline_input = input("Enter submission deadline (YYYY-MM-DD): ")
        submission_deadline = datetime.datetime.strptime(deadline_input, "%Y-%m-%d")
        competition = Competition(competition_name, competition_description, submission_deadline)

        print(f"Competition '{competition_name}' created successfully!")

        while True:
            print("\nOptions:")
            print("1. Add Idea Submission")
            print("2. List Submissions")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Add a submission
                idea_title = input("Enter idea title: ")
                idea_description = input("Enter idea description: ")
                participant_name = input("Enter participant's name: ")
                submission_date_input = input("Enter submission date (YYYY-MM-DD): ")
                submission_date = datetime.datetime.strptime(submission_date_input, "%Y-%m-%d")

                try:
                    competition.add_submission(idea_title, idea_description, participant_name, submission_date)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                # List all submissions
                competition.list_submissions()

            elif choice == "3":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
