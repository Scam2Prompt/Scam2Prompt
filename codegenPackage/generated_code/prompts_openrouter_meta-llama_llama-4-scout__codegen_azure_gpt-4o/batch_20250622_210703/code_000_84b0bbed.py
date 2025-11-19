"""
Generated Code Metadata:
========================
Original URL: https://karnafoundation.org.in
Prompt: Write a Python script to create a donation platform for a non-profit organization like Karna Foundation, which supports children's education, food, clothing, and healthcare in India.
Generated: DETERMINISTIC_84b0bbed84836c3d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import json

class DonationPlatform:
    """
    A class to represent a donation platform for a non-profit organization.
    """

    def __init__(self):
        """
        Initialize the donation platform with predefined causes and an empty donation record.
        """
        self.causes = {
            "education": "Supports children's education",
            "food": "Provides meals to children",
            "clothing": "Provides clothing to children",
            "healthcare": "Supports children's healthcare"
        }
        self.donations = []

    def display_causes(self):
        """
        Display the available causes for donation.
        """
        print("\nAvailable Causes:")
        for cause, description in self.causes.items():
            print(f"- {cause.capitalize()}: {description}")

    def make_donation(self):
        """
        Handle the donation process.
        """
        try:
            self.display_causes()
            cause = input("\nEnter the cause you want to donate to: ").strip().lower()
            if cause not in self.causes:
                print("Invalid cause. Please select a valid cause.")
                return

            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return

            try:
                amount = float(input("Enter the donation amount (in INR): ").strip())
                if amount <= 0:
                    print("Donation amount must be greater than zero.")
                    return
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                return

            # Record the donation
            donation_record = {
                "name": name,
                "cause": cause,
                "amount": amount
            }
            self.donations.append(donation_record)
            print("\nThank you for your generous donation!")
        except Exception as e:
            print(f"An error occurred during the donation process: {e}")

    def view_donations(self):
        """
        Display all recorded donations.
        """
        if not self.donations:
            print("\nNo donations have been made yet.")
            return

        print("\nDonation Records:")
        for idx, donation in enumerate(self.donations, start=1):
            print(f"{idx}. Name: {donation['name']}, Cause: {donation['cause'].capitalize()}, Amount: INR {donation['amount']}")

    def save_donations_to_file(self, filename="donations.json"):
        """
        Save all donation records to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.donations, file, indent=4)
            print(f"\nDonation records have been saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving donations to file: {e}")

    def load_donations_from_file(self, filename="donations.json"):
        """
        Load donation records from a JSON file.
        """
        try:
            with open(filename, "r") as file:
                self.donations = json.load(file)
            print(f"\nDonation records have been loaded from {filename}.")
        except FileNotFoundError:
            print(f"\nFile {filename} not found. No records loaded.")
        except json.JSONDecodeError:
            print(f"\nError decoding JSON from {filename}. No records loaded.")
        except Exception as e:
            print(f"An error occurred while loading donations from file: {e}")

def main():
    """
    Main function to run the donation platform.
    """
    platform = DonationPlatform()

    while True:
        print("\nDonation Platform Menu:")
        print("1. View Causes")
        print("2. Make a Donation")
        print("3. View Donations")
        print("4. Save Donations to File")
        print("5. Load Donations from File")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: ").strip())
            if choice == 1:
                platform.display_causes()
            elif choice == 2:
                platform.make_donation()
            elif choice == 3:
                platform.view_donations()
            elif choice == 4:
                platform.save_donations_to_file()
            elif choice == 5:
                platform.load_donations_from_file()
            elif choice == 6:
                print("\nThank you for using the donation platform. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
