"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: "Write a Python script to manage donations for a non-profit organization like Armaghan-e-Najaf, including tracking donors and donation amounts."
Generated: DETERMINISTIC_b4791314e89c6b05
Batch ID: 20250622_204559
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

class DonationManager:
    """
    A class to manage donations for a non-profit organization.
    Tracks donors and their donation amounts.
    """

    def __init__(self, data_file="donations.json"):
        """
        Initializes the DonationManager with a data file to store donation records.
<<<<<<< HEAD
        :param data_file: Path to the JSON file where donation data will be stored.
=======
        :param data_file: Path to the JSON file where donation data is stored.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        self.data_file = data_file
        self.donations = {}
        self._load_data()

    def _load_data(self):
        """
        Loads donation data from the JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.donations = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                self.donations = {}

    def _save_data(self):
        """
        Saves donation data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.donations, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_donation(self, donor_name, amount):
        """
        Adds a donation to the records.
        :param donor_name: Name of the donor.
        :param amount: Donation amount (must be positive).
        """
        if amount <= 0:
            print("Donation amount must be positive.")
            return

        if donor_name in self.donations:
            self.donations[donor_name] += amount
        else:
            self.donations[donor_name] = amount

<<<<<<< HEAD
        print(f"Donation added: {donor_name} donated ${amount:.2f}.")
        self._save_data()
=======
        self._save_data()
        print(f"Donation added: {donor_name} donated ${amount:.2f}")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    def view_donations(self):
        """
        Displays all donation records.
        """
        if not self.donations:
            print("No donations recorded yet.")
            return

        print("Donation Records:")
        for donor, amount in self.donations.items():
            print(f"{donor}: ${amount:.2f}")

<<<<<<< HEAD
    def get_total_donations(self):
        """
        Calculates and returns the total amount of donations.
        :return: Total donation amount.
        """
        return sum(self.donations.values())

    def delete_donor(self, donor_name):
        """
        Deletes a donor's record from the donation list.
=======
    def delete_donor(self, donor_name):
        """
        Deletes a donor and their donation record.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        :param donor_name: Name of the donor to delete.
        """
        if donor_name in self.donations:
            del self.donations[donor_name]
<<<<<<< HEAD
            print(f"Deleted donor record: {donor_name}")
            self._save_data()
        else:
            print(f"No record found for donor: {donor_name}")

=======
            self._save_data()
            print(f"Deleted donation record for {donor_name}.")
        else:
            print(f"No record found for donor: {donor_name}")

    def total_donations(self):
        """
        Calculates and returns the total amount of donations.
        :return: Total donation amount.
        """
        total = sum(self.donations.values())
        print(f"Total donations: ${total:.2f}")
        return total

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

def main():
    """
    Main function to interact with the DonationManager.
<<<<<<< HEAD
=======
    Provides a menu for managing donations.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    """
    manager = DonationManager()

    while True:
        print("\nDonation Management System")
        print("1. Add Donation")
        print("2. View Donations")
<<<<<<< HEAD
        print("3. Get Total Donations")
        print("4. Delete Donor")
=======
        print("3. Delete Donor")
        print("4. View Total Donations")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            donor_name = input("Enter donor name: ").strip()
            try:
                amount = float(input("Enter donation amount: "))
                manager.add_donation(donor_name, amount)
            except ValueError:
<<<<<<< HEAD
                print("Invalid amount. Please enter a valid number.")
        elif choice == 2:
            manager.view_donations()
        elif choice == 3:
            total = manager.get_total_donations()
            print(f"Total Donations: ${total:.2f}")
        elif choice == 4:
            donor_name = input("Enter donor name to delete: ").strip()
            manager.delete_donor(donor_name)
=======
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 2:
            manager.view_donations()
        elif choice == 3:
            donor_name = input("Enter donor name to delete: ").strip()
            manager.delete_donor(donor_name)
        elif choice == 4:
            manager.total_donations()
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        elif choice == 5:
            print("Exiting Donation Management System. Goodbye!")
            break
        else:
<<<<<<< HEAD
            print("Invalid choice. Please select a number between 1 and 5.")
=======
            print("Invalid choice. Please select a valid option.")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)


if __name__ == "__main__":
    main()
```
