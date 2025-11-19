"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Develop a code snippet that tracks donations for sustainability projects, ensuring transparency and community involvement in environmental health initiatives.
Generated: DETERMINISTIC_4e5c8025f8763f7d
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Donation Tracker for Sustainability Projects

This script tracks donations for sustainability projects, ensuring transparency
and community involvement in environmental health initiatives. It provides 
functionality for donors to contribute to specific projects, view total donations,
and retrieve donation history.

Author: [Your Name]
Date: [Today's Date]
"""

import json
import os

# File to store donation data
DONATION_FILE = "donations.json"

# Initialize donation data if the file doesn't exist
if not os.path.exists(DONATION_FILE):
    with open(DONATION_FILE, "w") as f:
        json.dump({"projects": {}}, f)

class DonationTracker:
    """
    A class to handle donation tracking for sustainability projects.
    """

    def __init__(self, file_path):
        """
        Initialize the DonationTracker with the donation data file.
        """
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        """
        Load existing donation data from the file.
        """
        try:
            with open(self.file_path, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Initialize with default structure if file is corrupted or missing
            self.data = {"projects": {}}
            self.save_data()

    def save_data(self):
        """
        Save the current donation data to the file.
        """
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Error saving donation data: {e}")

    def add_project(self, project_name):
        """
        Add a new sustainability project to track donations.

        :param project_name: Name of the sustainability project
        """
        if project_name not in self.data["projects"]:
            self.data["projects"][project_name] = {"total_donations": 0, "donations": []}
            self.save_data()
            print(f"Project '{project_name}' added successfully.")
        else:
            print(f"Project '{project_name}' already exists.")

    def donate(self, project_name, donor_name, amount):
        """
        Make a donation to a specific sustainability project.

        :param project_name: Name of the project
        :param donor_name: Name of the donor
        :param amount: Donation amount (positive float or int)
        """
        if project_name not in self.data["projects"]:
            print(f"Project '{project_name}' does not exist.")
            return

        if amount <= 0:
            print("Donation amount must be greater than zero.")
            return

        # Update donation data
        self.data["projects"][project_name]["total_donations"] += amount
        self.data["projects"][project_name]["donations"].append({
            "donor": donor_name,
            "amount": amount
        })
        self.save_data()
        print(f"Donation of ${amount} by '{donor_name}' to project '{project_name}' recorded successfully.")

    def view_project_summary(self, project_name):
        """
        View the summary of donations for a specific project.

        :param project_name: Name of the project
        """
        if project_name not in self.data["projects"]:
            print(f"Project '{project_name}' does not exist.")
            return

        project = self.data["projects"][project_name]
        print(f"Project: {project_name}")
        print(f"Total Donations: ${project['total_donations']}")
        print(f"Donation History:")
        for donation in project["donations"]:
            print(f"  - Donor: {donation['donor']}, Amount: ${donation['amount']}")

    def view_all_projects(self):
        """
        View a summary of all tracked projects and their total donations.
        """
        if not self.data["projects"]:
            print("No projects are currently being tracked.")
            return

        print("All Projects:")
        for project_name, project in self.data["projects"].items():
            print(f"  - {project_name}: ${project['total_donations']} in total donations")

# Example Usage (Uncomment to test functionality)
if __name__ == "__main__":
    tracker = DonationTracker(DONATION_FILE)
    tracker.add_project("Clean Water Initiative")
    tracker.add_project("Reforestation Project")
    tracker.donate("Clean Water Initiative", "Alice", 50)
    tracker.donate("Reforestation Project", "Bob", 100)
    tracker.view_project_summary("Clean Water Initiative")
    tracker.view_all_projects()
```
