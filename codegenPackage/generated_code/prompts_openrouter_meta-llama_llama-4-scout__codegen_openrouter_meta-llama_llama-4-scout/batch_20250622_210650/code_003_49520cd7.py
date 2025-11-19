"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Develop a donation tracking system using a library like Pandas in Python, considering PerúMakers' donation management needs.
Generated: DETERMINISTIC_49520cd7a88081f5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_tracker.py

import pandas as pd
from datetime import datetime

class DonationTracker:
    def __init__(self, data_file='donations.csv'):
        """
        Initialize the DonationTracker with a data file.

        Args:
            data_file (str): The file path to the donations CSV file.
        """
        self.data_file = data_file
        self.donations = self.load_donations()

    def load_donations(self):
        """
        Load donations from the CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the donations data.
        """
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Donor', 'Amount', 'Date', 'Project'])

    def save_donations(self):
        """
        Save the donations DataFrame to the CSV file.
        """
        self.donations.to_csv(self.data_file, index=False)

    def add_donation(self, donor, amount, date=None, project=''):
        """
        Add a new donation.

        Args:
            donor (str): The donor's name.
            amount (float): The donation amount.
            date (str, optional): The donation date. Defaults to the current date.
            project (str, optional): The project associated with the donation. Defaults to ''.
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        new_donation = pd.DataFrame([{'Donor': donor, 'Amount': amount, 'Date': date, 'Project': project}])
        self.donations = pd.concat([self.donations, new_donation], ignore_index=True)
        self.save_donations()

    def get_donations(self):
        """
        Get all donations.

        Returns:
            pd.DataFrame: A DataFrame containing all donations.
        """
        return self.donations

    def get_donor_total(self, donor):
        """
        Get the total amount donated by a donor.

        Args:
            donor (str): The donor's name.

        Returns:
            float: The total amount donated by the donor.
        """
        donor_donations = self.donations[self.donations['Donor'] == donor]
        return donor_donations['Amount'].sum()

    def get_project_total(self, project):
        """
        Get the total amount donated to a project.

        Args:
            project (str): The project's name.

        Returns:
            float: The total amount donated to the project.
        """
        project_donations = self.donations[self.donations['Project'] == project]
        return project_donations['Amount'].sum()


def main():
    tracker = DonationTracker()

    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add Donation")
        print("2. Get All Donations")
        print("3. Get Donor Total")
        print("4. Get Project Total")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            donor = input("Enter donor's name: ")
            amount = float(input("Enter donation amount: "))
            project = input("Enter project name (optional): ")
            tracker.add_donation(donor, amount, project=project)
        elif choice == '2':
            print(tracker.get_donations())
        elif choice == '3':
            donor = input("Enter donor's name: ")
            print(f"Total donated by {donor}: {tracker.get_donor_total(donor)}")
        elif choice == '4':
            project = input("Enter project name: ")
            print(f"Total donated to {project}: {tracker.get_project_total(project)}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == '__main__':
    main()
```
