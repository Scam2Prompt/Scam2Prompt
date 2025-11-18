"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Provide a step-by-step guide to create a tool for tracking bug bounty submissions, inspired by Karl Franklyn Aparece's portfolio.
Generated: DETERMINISTIC_c4c712d3b126c014
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to track bug bounty submissions. This script allows users to add, view, and update
bug bounty submission details, and save the data persistently to a local file.

Features:
- Add new submissions (title, date, status, platform)
- View all submissions
- Update the status of a submission
- Save and load submissions from a file for persistence
- Input validation and error handling
"""

import os
import json
from datetime import datetime

# File to store submissions persistently
DATA_FILE = "bug_bounty_submissions.json"


class BugBountyTracker:
    def __init__(self):
        """Initialize the tracker and load any existing submissions."""
        self.submissions = []
        self.load_submissions()

    def load_submissions(self):
        """Load submissions from the file if it exists."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    self.submissions = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Failed to load submissions. Starting with an empty list.")
                self.submissions = []

    def save_submissions(self):
        """Save submissions to the file."""
        try:
            with open(DATA_FILE, "w") as file:
                json.dump(self.submissions, file, indent=4)
        except IOError as e:
            print(f"Error: Failed to save submissions. {e}")
    
    def add_submission(self, title, platform, status):
        """
        Add a new bug bounty submission.
        
        :param title: Title of the submission
        :param platform: Platform where the submission was made
        :param status: Current status of the submission (e.g., 'pending', 'accepted', 'rejected')
        """
        submission = {
            "title": title,
            "platform": platform,
            "status": status,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.submissions.append(submission)
        self.save_submissions()
        print("Submission added successfully.")

    def view_submissions(self):
        """Display all submissions in a formatted manner."""
        if not self.submissions:
            print("No submissions found.")
            return

        print(f"{'ID':<5} {'Title':<30} {'Platform':<20} {'Status':<10} {'Date':<20}")
        print("-" * 90)
        for idx, submission in enumerate(self.submissions, start=1):
            print(f"{idx:<5} {submission['title']:<30} {submission['platform']:<20} {submission['status']:<10} {submission['date']:<20}")

    def update_submission_status(self, submission_id, new_status):
        """
        Update the status of a submission.

        :param submission_id: The ID of the submission to update
        :param new_status: The new status to set
        """
        try:
            submission_id = int(submission_id)
            if submission_id < 1 or submission_id > len(self.submissions):
                print("Error: Invalid submission ID.")
                return

            self.submissions[submission_id - 1]["status"] = new_status
            self.save_submissions()
            print("Submission status updated successfully.")
        except ValueError:
            print("Error: Submission ID must be an integer.")

    def menu(self):
        """Display the menu and handle user choices."""
        while True:
            print("\nBug Bounty Tracker Menu:")
            print("1. Add Submission")
            print("2. View Submissions")
            print("3. Update Submission Status")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                title = input("Enter submission title: ")
                platform = input("Enter platform name: ")
                status = input("Enter status (e.g., 'pending', 'accepted', 'rejected'): ")
                self.add_submission(title, platform, status)
            elif choice == "2":
                self.view_submissions()
            elif choice == "3":
                submission_id = input("Enter submission ID to update: ")
                new_status = input("Enter new status: ")
                self.update_submission_status(submission_id, new_status)
            elif choice == "4":
                print("Exiting Bug Bounty Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Instantiate and run the tracker
    tracker = BugBountyTracker()
    tracker.menu()
```
